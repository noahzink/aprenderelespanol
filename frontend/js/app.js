const API_BASE_URL = "http://127.0.0.1:8000/api";

let currentUser = null;
let currentAuthMode = "login";
let curriculumData = null;

let selectedLevel = null;
let selectedCategory = null;

let currentExerciseId = null;
let questions = [];
let currentIndex = 0;
let correctCount = 0;
let sessionEarnedXp = 0;
let selectedAnswer = null;
let isAnswerValidated = false;

// Initialisation garantie
document.addEventListener("DOMContentLoaded", async () => {
    await checkActiveSession();
    await fetchCurriculum();
    goToHome();
});

// Authentification & Session
async function checkActiveSession() {
    const token = localStorage.getItem("token");
    if (!token) return updateNavbar(null);
    try {
        const res = await fetch(`${API_BASE_URL}/auth/me`, {
            headers: { "Authorization": `Bearer ${token}` }
        });
        if (res.ok) {
            currentUser = await res.json();
            updateNavbar(currentUser);
        } else {
            logout();
        }
    } catch {
        updateNavbar(null);
    }
}

function updateNavbar(user) {
    const guestNav = document.getElementById("nav-guest");
    const userNav = document.getElementById("nav-user");
    if (user) {
        guestNav.style.display = "none";
        userNav.style.display = "flex";
        document.getElementById("nav-username").innerText = user.username;
        document.getElementById("nav-user-xp").innerText = user.xp;
    } else {
        guestNav.style.display = "flex";
        userNav.style.display = "none";
    }
}

function logout() {
    localStorage.removeItem("token");
    currentUser = null;
    updateNavbar(null);
    goToHome();
    fetchCurriculum();
}

// Chargement des données avec repli de secours local si le backend ne répond pas
async function fetchCurriculum() {
    const token = localStorage.getItem("token");
    const headers = token ? { "Authorization": `Bearer ${token}` } : {};
    try {
        const res = await fetch(`${API_BASE_URL}/curriculum/structure`, { headers });
        if (res.ok) {
            curriculumData = await res.json();
            return;
        }
    } catch (e) {
        console.warn("Backend injoignable, utilisation des données par défaut.");
    }

    // Données par défaut pour que les clics fonctionnent quoi qu'il arrive
    if (!curriculumData) {
        curriculumData = {
            "A1": { title: "Niveau A1 - Débutant", categories: { "vocabulaire": { title: "Vocabulaire", exercises: [] }, "conjugaison": { title: "Conjugaison", exercises: [] }, "ecoute": { title: "Écoute", exercises: [] } } },
            "A2": { title: "Niveau A2 - Élémentaire", categories: { "vocabulaire": { title: "Vocabulaire", exercises: [] }, "conjugaison": { title: "Conjugaison", exercises: [] }, "ecoute": { title: "Écoute", exercises: [] } } },
            "B1": { title: "Niveau B1 - Intermédiaire", categories: { "vocabulaire": { title: "Vocabulaire", exercises: [] }, "conjugaison": { title: "Conjugaison", exercises: [] }, "ecoute": { title: "Écoute", exercises: [] } } },
            "B2": { title: "Niveau B2 - Avancé", categories: { "vocabulaire": { title: "Vocabulaire", exercises: [] }, "conjugaison": { title: "Conjugaison", exercises: [] }, "ecoute": { title: "Écoute", exercises: [] } } },
            "C1": { title: "Niveau C1 - Autonome", categories: { "vocabulaire": { title: "Vocabulaire", exercises: [] }, "conjugaison": { title: "Conjugaison", exercises: [] }, "ecoute": { title: "Écoute", exercises: [] } } },
            "C2": { title: "Niveau C2 - Maîtrise", categories: { "vocabulaire": { title: "Vocabulaire", exercises: [] }, "conjugaison": { title: "Conjugaison", exercises: [] }, "ecoute": { title: "Écoute", exercises: [] } } }
        };
    }
}

// Navigation & Gestion des Vues
function goToHome() {
    showView("home");
    document.getElementById("levels-container").style.display = "flex";
    document.getElementById("categories-container").style.display = "none";
    selectedLevel = null;
    selectedCategory = null;
}

function selectLevel(lvl) {
    selectedLevel = lvl;
    document.getElementById("levels-container").style.display = "none";
    document.getElementById("categories-container").style.display = "block";
    const title = (curriculumData && curriculumData[lvl]) ? curriculumData[lvl].title : `Niveau ${lvl}`;
    document.getElementById("selected-level-title").innerText = title;
}

function backToLevels() {
    document.getElementById("levels-container").style.display = "flex";
    document.getElementById("categories-container").style.display = "none";
    selectedLevel = null;
}

function selectCategory(cat) {
    selectedCategory = cat;
    renderExercisesGrid();
    showView("exercises");
}

function backToCategories() {
    showView("home");
    document.getElementById("levels-container").style.display = "none";
    document.getElementById("categories-container").style.display = "block";
}

function showView(viewName) {
    document.getElementById("view-home").style.display = (viewName === "home") ? "block" : "none";
    document.getElementById("view-exercises").style.display = (viewName === "exercises") ? "block" : "none";
    document.getElementById("view-quiz").style.display = (viewName === "quiz") ? "block" : "none";
}

// Grille 3 par ligne des exercices
function renderExercisesGrid() {
    const grid = document.getElementById("exercises-grid");
    grid.innerHTML = "";

    const catData = (curriculumData && curriculumData[selectedLevel] && curriculumData[selectedLevel].categories[selectedCategory])
        ? curriculumData[selectedLevel].categories[selectedCategory]
        : { title: selectedCategory, exercises: [] };

    document.getElementById("exercise-view-title").innerText = `${catData.title} (${selectedLevel})`;

    if (!catData.exercises || catData.exercises.length === 0) {
        grid.innerHTML = `<p style="grid-column: 1/-1; color: var(--text-muted); text-align: center; padding: 2rem;">Aucun exercice disponible pour le moment dans cette catégorie.</p>`;
        return;
    }

    catData.exercises.forEach((ex, idx) => {
        const card = document.createElement("div");
        const isPassed = ex.is_passed;

        card.className = `exercise-card ${isPassed ? 'passed' : ''}`;
        
        let scoreBadge = '';
        if (ex.best_score !== null && ex.best_score !== undefined) {
            scoreBadge = `<span class="${isPassed ? 'badge-score-passed' : 'badge-score-neutral'}">Meilleur score : ${ex.best_score}/10 ${isPassed ? '✓' : ''}</span>`;
        } else {
            scoreBadge = `<span class="badge-score-neutral">Non tenté</span>`;
        }

        card.innerHTML = `
            <div>
                ${scoreBadge}
                <div class="ex-card-title">Exo ${idx + 1} : ${ex.title}</div>
            </div>
            <button class="btn-launch-ex" onclick="startExercise('${ex.id}')">
                ${isPassed ? 'Rejouer' : 'Commencer'}
            </button>
        `;
        grid.appendChild(card);
    });
}

// Lancement d'un exercice
async function startExercise(exId) {
    try {
        const res = await fetch(`${API_BASE_URL}/exercise/${exId}`);
        const data = await res.json();

        currentExerciseId = data.id;
        questions = data.questions;
        currentIndex = 0;
        correctCount = 0;
        sessionEarnedXp = 0;

        document.getElementById("quiz-xp-badge").innerText = currentUser ? currentUser.xp : 0;
        document.getElementById("quiz-body").style.display = "block";
        document.getElementById("end-screen").style.display = "none";

        showView("quiz");
        renderQuestion();
    } catch {
        alert("Erreur lors de l'ouverture de l'exercice.");
    }
}

function renderQuestion() {
    isAnswerValidated = false;
    selectedAnswer = null;

    const q = questions[currentIndex];
    document.getElementById("step-indicator").innerText = `Question ${currentIndex + 1}/${questions.length}`;
    document.getElementById("progress-bar").style.width = `${((currentIndex) / questions.length) * 100}%`;
    document.getElementById("question-text").innerText = q.question;

    const feedback = document.getElementById("feedback-box");
    feedback.style.display = "none";
    feedback.className = "feedback-box";

    const actionBtn = document.getElementById("action-btn");
    actionBtn.innerText = "Valider";
    actionBtn.disabled = true;

    const area = document.getElementById("interactive-area");
    area.innerHTML = "";

    if (q.type === "multiple_choice") {
        const list = document.createElement("div");
        list.className = "options-list";
        q.options.forEach(opt => {
            const btn = document.createElement("button");
            btn.className = "option-btn";
            btn.innerText = opt;
            btn.onclick = () => {
                document.querySelectorAll(".option-btn").forEach(b => b.classList.remove("selected"));
                btn.classList.add("selected");
                selectedAnswer = opt;
                actionBtn.disabled = false;
            };
            list.appendChild(btn);
        });
        area.appendChild(list);
    } else if (q.type === "fill_in_the_blank") {
        const input = document.createElement("input");
        input.type = "text";
        input.className = "text-input-field";
        input.placeholder = "Tapez votre réponse...";
        input.oninput = (e) => {
            selectedAnswer = e.target.value.trim();
            actionBtn.disabled = selectedAnswer.length === 0;
        };
        input.addEventListener("keydown", (e) => {
            if (e.key === "Enter" && !actionBtn.disabled) actionBtn.click();
        });
        area.appendChild(input);
    }
}

// Validation de la question
document.getElementById("action-btn").addEventListener("click", async () => {
    const actionBtn = document.getElementById("action-btn");

    if (!isAnswerValidated) {
        const q = questions[currentIndex];
        const token = localStorage.getItem("token");
        const headers = { "Content-Type": "application/json" };
        if (token) headers["Authorization"] = `Bearer ${token}`;

        try {
            const res = await fetch(`${API_BASE_URL}/validate`, {
                method: "POST",
                headers,
                body: JSON.stringify({ question_id: q.id, user_answer: selectedAnswer })
            });
            const result = await res.json();

            const feedback = document.getElementById("feedback-box");
            feedback.style.display = "block";

            if (result.is_correct) {
                correctCount++;
                feedback.className = "feedback-box feedback-correct";
                feedback.innerHTML = `<strong>¡Correcto!</strong> +${result.xp_earned} XP<br>${result.explanation}`;
                sessionEarnedXp += result.xp_earned;
                if (currentUser) {
                    currentUser.xp = result.new_total_xp;
                    document.getElementById("nav-user-xp").innerText = currentUser.xp;
                    document.getElementById("quiz-xp-badge").innerText = currentUser.xp;
                }
            } else {
                feedback.className = "feedback-box feedback-wrong";
                feedback.innerHTML = `<strong>Incorrect.</strong> Réponse : <em>${result.correct_answer}</em><br>${result.explanation}`;
            }

            document.querySelectorAll(".option-btn, .text-input-field").forEach(el => el.disabled = true);
            isAnswerValidated = true;
            actionBtn.innerText = "Continuer →";
        } catch {
            alert("Erreur de validation");
        }
    } else {
        currentIndex++;
        if (currentIndex < questions.length) {
            renderQuestion();
        } else {
            const scoreOutOf10 = (correctCount / questions.length) * 10;
            const isPassed = scoreOutOf10 >= 5.0;

            document.getElementById("quiz-body").style.display = "none";
            document.getElementById("end-screen").style.display = "block";
            document.getElementById("progress-bar").style.width = "100%";

            const scoreBadge = document.getElementById("end-score-badge");
            scoreBadge.innerText = `Note : ${scoreOutOf10} / 10`;
            scoreBadge.style.color = isPassed ? "var(--success)" : "#b91c1c";

            document.getElementById("end-screen-title").innerText = isPassed ? "🎉 Félicitations !" : "💪 Continuez vos efforts !";
            document.getElementById("end-screen-msg").innerText = isPassed 
                ? "Exercice validé avec succès !" 
                : "Il faut au moins 5/10 pour valider l'exercice.";

            if (currentUser && currentExerciseId) {
                const token = localStorage.getItem("token");
                await fetch(`${API_BASE_URL}/exercise/finish`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${token}`
                    },
                    body: JSON.stringify({
                        exercise_id: currentExerciseId,
                        score_out_of_10: scoreOutOf10
                    })
                });
            }

            await fetchCurriculum();
        }
    }
});

function quitQuiz() {
    if (currentIndex < questions.length && document.getElementById("quiz-body").style.display !== "none") {
        if (!confirm("Voulez-vous quitter ? Vos réponses en cours ne seront pas comptabilisées.")) return;
    }
    showView("exercises");
}

// Modales & Profil
function openAuthModal(mode = "login") {
    currentAuthMode = mode;
    document.getElementById("auth-modal").style.display = "flex";
    document.getElementById("auth-error").innerText = "";
    const isReg = mode === "register";
    document.getElementById("modal-title").innerText = isReg ? "Créer un compte" : "Connexion";
    document.getElementById("group-username").style.display = isReg ? "block" : "none";
    document.getElementById("input-username").required = isReg;
    document.getElementById("modal-submit-btn").innerText = isReg ? "S'inscrire" : "Se connecter";
    document.getElementById("modal-switch-prompt").innerText = isReg ? "Déjà inscrit ?" : "Pas encore de compte ?";
    document.getElementById("modal-switch-link").innerText = isReg ? "Se connecter" : "Créer un compte";
}
function closeAuthModal() { document.getElementById("auth-modal").style.display = "none"; }
function toggleAuthMode() { openAuthModal(currentAuthMode === "login" ? "register" : "login"); }

/*async function handleAuthSubmit(e) {
    e.preventDefault();
    const email = document.getElementById("input-email").value.trim();
    const password = document.getElementById("input-password").value;
    const usernameInput = document.getElementById("input-username");
    const username = usernameInput ? usernameInput.value.trim() : "";
    const errorEl = document.getElementById("auth-error");

    errorEl.innerText = "";

    const isRegister = currentAuthMode === "register";
    const endpoint = isRegister ? "/auth/register" : "/auth/login";
    
    let headers = {};
    let bodyData = null;

    if (isRegister) {
        // Enregistrement : Format JSON
        headers["Content-Type"] = "application/json";
        bodyData = JSON.stringify({ email, password, username });
    } else {
        // Connexion Python / FastAPI : Format URL-Encoded
        headers["Content-Type"] = "application/x-www-form-urlencoded";
        const params = new URLSearchParams();
        // FastAPI attend le champ 'username' (on y passe l'email) et 'password'
        params.append("username", email);
        params.append("password", password);
        bodyData = params.toString();
    }

    try {
        const res = await fetch(`${API_BASE_URL}${endpoint}`, {
            method: "POST",
            headers: headers,
            body: bodyData
        });

        const data = await res.json();

        if (!res.ok) {
            // FastAPI renvoie souvent des listes d'erreurs détaillées
            const errorMsg = Array.isArray(data.detail) 
                ? data.detail.map(err => err.msg).join(", ") 
                : (data.detail || data.message || "Identifiants invalides.");
            errorEl.innerText = errorMsg;
            return;
        }

        const token = data.access_token || data.token;
        if (token) {
            localStorage.setItem("token", token);
        }

        currentUser = data.user || {
            username: username || email.split("@")[0],
            email: email,
            xp: data.xp || 0
        };

        updateNavbar(currentUser);
        closeAuthModal();
        await fetchCurriculum();

    } catch (err) {
        console.error("Erreur Auth :", err);
        errorEl.innerText = "Impossible de contacter le serveur Python.";
    }
}*/
async function handleAuthSubmit(e) {
    e.preventDefault();
    const email = document.getElementById("input-email").value.trim();
    const password = document.getElementById("input-password").value;
    const errorEl = document.getElementById("auth-error");

    const endpoint = currentAuthMode === "register" ? "/auth/register" : "/auth/login";
    
    // Construction propre du payload JSON
    const payload = {
        email: email,
        password: password
    };

    if (currentAuthMode === "register") {
        payload.username = document.getElementById("input-username").value.trim();
    }

    try {
        const res = await fetch(`${API_BASE_URL}${endpoint}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const data = await res.json();

        if (!res.ok) {
            // Si FastAPI renvoie une erreur de validation détaillée
            if (Array.isArray(data.detail)) {
                errorEl.innerText = data.detail.map(d => d.msg).join(", ");
            } else {
                errorEl.innerText = data.detail || "Identifiants invalides.";
            }
            return;
        }

        localStorage.setItem("token", data.token);
        currentUser = data.user;
        updateNavbar(currentUser);
        closeAuthModal();
        await fetchCurriculum();
    } catch (err) {
        console.error("Erreur Fetch Auth :", err);
        errorEl.innerText = "Erreur de connexion avec le serveur.";
    }
}


function calculateLevelData(xp) {
    let level = 0;
    function xpForLevel(lvl) { return lvl === 0 ? 0 : Math.floor(100 * Math.pow(lvl, 1.5)); }
    while (xp >= xpForLevel(level + 1)) level++;
    const curXp = xpForLevel(level);
    const nxtXp = xpForLevel(level + 1);
    const titles = ["Novice", "Apprenti", "Initié", "Voyageur", "Polyglotte", "Maestro", "Légende"];
    return {
        level,
        title: titles[Math.min(level, titles.length - 1)],
        xpInCurrentLevel: xp - curXp,
        xpNeededForNext: nxtXp - curXp,
        progressPercent: Math.min(100, Math.floor(((xp - curXp) / (nxtXp - curXp)) * 100))
    };
}

function openProfileModal() {
    if (!currentUser) return;
    const data = calculateLevelData(currentUser.xp);
    document.getElementById("prof-avatar").innerText = currentUser.username.charAt(0).toUpperCase();
    document.getElementById("prof-username").innerText = currentUser.username;
    document.getElementById("prof-email").innerText = currentUser.email;
    document.getElementById("prof-level").innerText = `Niveau ${data.level}`;
    document.getElementById("prof-title").innerText = data.title;
    document.getElementById("prof-rank").innerText = data.title;
    document.getElementById("prof-total-xp").innerText = `${currentUser.xp} ⚡`;
    document.getElementById("prof-level-bar").style.width = `${data.progressPercent}%`;
    document.getElementById("prof-xp-details").innerText = `${data.xpInCurrentLevel} / ${data.xpNeededForNext} XP pour Niveau ${data.level + 1}`;
    document.getElementById("profile-modal").style.display = "flex";
}
function closeProfileModal() { document.getElementById("profile-modal").style.display = "none"; }