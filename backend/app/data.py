CURRICULUM_DB = {
    "A1": {
        "title": "Niveau A1 - Débutant",
        "categories": {
            "vocabulaire": {
                "title": "Vocabulaire",
                "exercises": [
                    {
                        "id": "a1_voc_saludos_1",
                        "title": "Salutations et formules de politesse",
                        "questions": [
                            {"id": 1, "type": "multiple_choice", "question": "Comment dit-on 'Bonjour' (le matin) en espagnol ?", "options": ["Buenos días", "Buenas tardes", "Buenas noches", "Hasta luego"], "correct_answer": "Buenos días", "explanation": "'Buenos días' s'utilise le matin jusqu'à l'après-midi.", "xp": 10},
                            {"id": 2, "type": "fill_in_the_blank", "question": "Complétez : ¡Buenas ___! (Bonsoir / Bonne nuit)", "options": None, "correct_answer": "noches", "explanation": "'Buenas noches' sert à saluer le soir ou souhaiter une bonne nuit.", "xp": 10},
                            {"id": 3, "type": "multiple_choice", "question": "Que signifie '¿Qué tal?' ?", "options": ["Comment ça va ?", "Quel âge as-tu ?", "Où habites-tu ?", "Comment t'appelles-tu ?"], "correct_answer": "Comment ça va ?", "explanation": "'¿Qué tal?' est une formule familière pour demander des nouvelles.", "xp": 10},
                            {"id": 4, "type": "multiple_choice", "question": "Comment répond-on à 'Muchas gracias' ?", "options": ["De nada", "Por favor", "Hola", "Adiós"], "correct_answer": "De nada", "explanation": "'De nada' signifie 'De rien'.", "xp": 10},
                            {"id": 5, "type": "fill_in_the_blank", "question": "Complétez : ¡Hasta ___! (À plus tard)", "options": None, "correct_answer": "luego", "explanation": "'Hasta luego' = À plus tard / À bientôt.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_presentacion_1",
                        "title": "Se présenter et faire connaissance",
                        "questions": [
                            {"id": 6, "type": "multiple_choice", "question": "Comment dit-on 'Je m'appelle Carlos' ?", "options": ["Me llamo Carlos", "Tengo Carlos", "Soy de Carlos", "Estoy Carlos"], "correct_answer": "Me llamo Carlos", "explanation": "On utilise le verbe réflexif 'llamarse' : Me llamo.", "xp": 10},
                            {"id": 7, "type": "fill_in_the_blank", "question": "Complétez : Mucho ___ (Enchanté).", "options": None, "correct_answer": "gusto", "explanation": "'Mucho gusto' signifie 'Enchanté(e)'.", "xp": 10},
                            {"id": 8, "type": "multiple_choice", "question": "Quelle question pose-t-on pour demander le prénom à un ami ?", "options": ["¿Cómo te llamas?", "¿Cómo se llama usted?", "¿De dónde eres?", "¿Cuántos años tienes?"], "correct_answer": "¿Cómo te llamas?", "explanation": "'¿Cómo te llamas?' tutoie l'interlocuteur.", "xp": 10},
                            {"id": 9, "type": "multiple_choice", "question": "Si une femme dit 'Enchantée', elle peut dire :", "options": ["Encantada", "Encantado", "Gracias", "Bienvenida"], "correct_answer": "Encantada", "explanation": "L'adjectif s'accorde au féminin : 'Encantada'.", "xp": 10},
                            {"id": 10, "type": "fill_in_the_blank", "question": "Complétez : Mi ___ es Ana (Mon prénom/nom est Ana).", "options": None, "correct_answer": "nombre", "explanation": "'Nombre' = prénom / nom.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_paises_1",
                        "title": "Pays d'Europe et d'Amérique",
                        "questions": [
                            {"id": 11, "type": "multiple_choice", "question": "Comment dit-on 'La France' en espagnol ?", "options": ["Francia", "França", "Franca", "Francesa"], "correct_answer": "Francia", "explanation": "'Francia' = La France.", "xp": 10},
                            {"id": 12, "type": "fill_in_the_blank", "question": "Complétez : Madrid es la capital de ___ (Espagne).", "options": None, "correct_answer": "España", "explanation": "'España' = L'Espagne.", "xp": 10},
                            {"id": 13, "type": "multiple_choice", "question": "Comment traduit-on 'L'Allemagne' ?", "options": ["Alemania", "Alemana", "Almania", "Germany"], "correct_answer": "Alemania", "explanation": "'Alemania' = Allemagne.", "xp": 10},
                            {"id": 14, "type": "multiple_choice", "question": "Quel pays hispanophone se trouve en Amérique du Nord ?", "options": ["México", "Brasil", "Portugal", "Canadá"], "correct_answer": "México", "explanation": "Le Mexique (México) est en Amérique du Nord.", "xp": 10},
                            {"id": 15, "type": "fill_in_the_blank", "question": "Complétez : Roma está en ___ (Italie).", "options": None, "correct_answer": "Italia", "explanation": "'Italia' = Italie.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_nacionalidades_1",
                        "title": "Nationalités (Masculin / Féminin)",
                        "questions": [
                            {"id": 16, "type": "multiple_choice", "question": "Quel est le féminin de 'español' ?", "options": ["española", "españole", "españolas", "español"], "correct_answer": "española", "explanation": "Les adjectifs de nationalité en consonne prennent un -a au féminin.", "xp": 10},
                            {"id": 17, "type": "fill_in_the_blank", "question": "Complétez : Pierre es de Francia, es ___ (français).", "options": None, "correct_answer": "francés", "explanation": "'Francés' = français.", "xp": 10},
                            {"id": 18, "type": "multiple_choice", "question": "Une femme venant d'Italie est :", "options": ["italiana", "italiano", "italiene", "italias"], "correct_answer": "italiana", "explanation": "'Italiana' est la forme féminine de 'italiano'.", "xp": 10},
                            {"id": 19, "type": "multiple_choice", "question": "Comment dit-on 'anglais / anglaise' ?", "options": ["inglés / inglesa", "anglo / angla", "inglés / inglesa", "anglez / angleza"], "correct_answer": "inglés / inglesa", "explanation": "Inglés (masculin) / inglesa (féminin).", "xp": 10},
                            {"id": 20, "type": "fill_in_the_blank", "question": "Complétez : Pablo es de México, es ___.", "options": None, "correct_answer": "mexicano", "explanation": "'Mexicano' est la nationalité mexicaine au masculin.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_profesiones_1",
                        "title": "Les Métiers & Professions (Partie 1)",
                        "questions": [
                            {"id": 21, "type": "multiple_choice", "question": "Comment dit-on 'Professeur' en espagnol ?", "options": ["Profesor", "Médico", "Camarero", "Bombero"], "correct_answer": "Profesor", "explanation": "'Profesor' = Professeur / Enseignant.", "xp": 10},
                            {"id": 22, "type": "fill_in_the_blank", "question": "Complétez : El ___ (médecin) trabaja en el hospital.", "options": None, "correct_answer": "médico", "explanation": "'Médico' = Médecin.", "xp": 10},
                            {"id": 23, "type": "multiple_choice", "question": "Que signifie 'El camarero' ?", "options": ["Le serveur", "Le cuisinier", "Le pharmacien", "Le chauffeur"], "correct_answer": "Le serveur", "explanation": "'Camarero' = Serveur (restaurant/bar).", "xp": 10},
                            {"id": 24, "type": "multiple_choice", "question": "Une femme qui étudie à l'université est une :", "options": ["estudiante", "profesora", "doctora", "enfermera"], "correct_answer": "estudiante", "explanation": "'Estudiante' s'utilise aussi bien pour le masculin que le féminin.", "xp": 10},
                            {"id": 25, "type": "fill_in_the_blank", "question": "Complétez : Mi hermano es ___ (avocat).", "options": None, "correct_answer": "abogado", "explanation": "'Abogado' = Avocat.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_profesiones_2",
                        "title": "Les Métiers & Professions (Partie 2)",
                        "questions": [
                            {"id": 26, "type": "multiple_choice", "question": "Comment dit-on 'Infirmière' ?", "options": ["Enfermera", "Cocinera", "Peluquera", "Secretaria"], "correct_answer": "Enfermera", "explanation": "'Enfermera' = Infirmière.", "xp": 10},
                            {"id": 27, "type": "fill_in_the_blank", "question": "Complétez : El ___ (ingénieur) diseña puentes.", "options": None, "correct_answer": "ingeniero", "explanation": "'Ingeniero' = Ingénieur.", "xp": 10},
                            {"id": 28, "type": "multiple_choice", "question": "Que fait un 'bombero' ?", "options": ["Éteindre des incendies", "Cuisiner", "Enseigner", "Vendre des vêtements"], "correct_answer": "Éteindre des incendies", "explanation": "'Bombero' = Pompier.", "xp": 10},
                            {"id": 29, "type": "multiple_choice", "question": "Comment dit-on 'Journaliste' (masculin) ?", "options": ["Periodista", "Periodisto", "Periódico", "Reportero"], "correct_answer": "Periodista", "explanation": "Les métiers en -ista restent identiques au masculin et au féminin (el/la periodista).", "xp": 10},
                            {"id": 30, "type": "fill_in_the_blank", "question": "Complétez : La ___ (cuisinière) prepara la comida.", "options": None, "correct_answer": "cocinera", "explanation": "'Cocinera' = Cuisinière.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_numeros_1",
                        "title": "Chiffres de 0 à 15",
                        "questions": [
                            {"id": 31, "type": "multiple_choice", "question": "Quel nombre correspond à 'Cero' ?", "options": ["0", "1", "10", "100"], "correct_answer": "0", "explanation": "'Cero' = 0.", "xp": 10},
                            {"id": 32, "type": "fill_in_the_blank", "question": "Complétez : uno, dos, tres, ___ (quatre).", "options": None, "correct_answer": "cuatro", "explanation": "'Cuatro' = 4.", "xp": 10},
                            {"id": 33, "type": "multiple_choice", "question": "Comment écrit-on le nombre 12 ?", "options": ["Doce", "Diez", "Dos", "Treche"], "correct_answer": "Doce", "explanation": "'Doce' = 12.", "xp": 10},
                            {"id": 34, "type": "multiple_choice", "question": "Quel chiffre est 'Quince' ?", "options": ["15", "5", "50", "14"], "correct_answer": "15", "explanation": "'Quince' = 15.", "xp": 10},
                            {"id": 35, "type": "fill_in_the_blank", "question": "Complétez : seis, siete, ___ (huit).", "options": None, "correct_answer": "ocho", "explanation": "'Ocho' = 8.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_numeros_2",
                        "title": "Chiffres de 16 à 30",
                        "questions": [
                            {"id": 36, "type": "multiple_choice", "question": "Comment s'écrit 16 en un seul mot ?", "options": ["Dieciséis", "Diez y seis", "Diecisiete", "Deciséis"], "correct_answer": "Dieciséis", "explanation": "Les nombres de 16 à 29 s'écrivent en un seul mot soudé.", "xp": 10},
                            {"id": 37, "type": "fill_in_the_blank", "question": "Complétez : 20 se dit ___.", "options": None, "correct_answer": "veinte", "explanation": "'Veinte' = 20.", "xp": 10},
                            {"id": 38, "type": "multiple_choice", "question": "Quel est le nombre 'Veinticinco' ?", "options": ["25", "24", "15", "35"], "correct_answer": "25", "explanation": "'Veinticinco' = 25.", "xp": 10},
                            {"id": 39, "type": "multiple_choice", "question": "Comment dit-on 30 ?", "options": ["Treinta", "Tres", "Trece", "Treintena"], "correct_answer": "Treinta", "explanation": "'Treinta' = 30.", "xp": 10},
                            {"id": 40, "type": "fill_in_the_blank", "question": "Complétez : 21 s'écrit ___.", "options": None, "correct_answer": "veintiuno", "explanation": "'Veintiuno' = 21.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_numeros_3",
                        "title": "Dizaines et nombres jusqu'à 100",
                        "questions": [
                            {"id": 41, "type": "multiple_choice", "question": "Comment dit-on 40 en espagnol ?", "options": ["Cuarenta", "Cincuenta", "Cuatro", "Catorce"], "correct_answer": "Cuarenta", "explanation": "'Cuarenta' = 40.", "xp": 10},
                            {"id": 42, "type": "fill_in_the_blank", "question": "Complétez : 50 s'écrit ___.", "options": None, "correct_answer": "cincuenta", "explanation": "'Cincuenta' = 50.", "xp": 10},
                            {"id": 43, "type": "multiple_choice", "question": "Comment s'écrit 73 ?", "options": ["Setenta y tres", "Sesenta y tres", "Siete y tres", "Setentaitres"], "correct_answer": "Setenta y tres", "explanation": "À partir de 31, les dizaines et unités sont séparées par 'y'.", "xp": 10},
                            {"id": 44, "type": "multiple_choice", "question": "Quel nombre vaut 'Cien' ?", "options": ["100", "10", "1000", "50"], "correct_answer": "100", "explanation": "'Cien' = 100.", "xp": 10},
                            {"id": 45, "type": "fill_in_the_blank", "question": "Complétez : 90 s'écrit ___.", "options": None, "correct_answer": "noventa", "explanation": "'Noventa' = 90.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_datos_1",
                        "title": "Données personnelles (Âge, Téléphone, Adresse)",
                        "questions": [
                            {"id": 46, "type": "multiple_choice", "question": "Comment demande-t-on l'âge en espagnol ?", "options": ["¿Cuántos años tienes?", "¿Qué edad eres?", "¿Cómo tienes de años?", "¿Cuándo es tu cumpleaños?"], "correct_answer": "¿Cuántos años tienes?", "explanation": "On utilise le verbe 'tener' pour l'âge.", "xp": 10},
                            {"id": 47, "type": "fill_in_the_blank", "question": "Complétez : Yo ___ 25 años (verbe tener).", "options": None, "correct_answer": "tengo", "explanation": "1ère personne : 'Yo tengo'.", "xp": 10},
                            {"id": 48, "type": "multiple_choice", "question": "Que signifie '¿Cuál es tu número de teléfono?' ?", "options": ["Quel est ton numéro de téléphone ?", "Où est ton téléphone ?", "As-tu un téléphone ?", "Quel est ton nom ?"], "correct_answer": "Quel est ton numéro de téléphone ?", "explanation": "'Número de teléfono' = Numéro de téléphone.", "xp": 10},
                            {"id": 49, "type": "multiple_choice", "question": "Comment dit-on 'adresse e-mail' en espagnol ?", "options": ["Correo electrónico", "Carta digital", "Mensaje postal", "Dirección de carta"], "correct_answer": "Correo electrónico", "explanation": "'Correo electrónico' = E-mail.", "xp": 10},
                            {"id": 50, "type": "fill_in_the_blank", "question": "Complétez : Mi ___ (adresse) es Calle Mayor 10.", "options": None, "correct_answer": "dirección", "explanation": "'Dirección' = Adresse.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_casa_habitaciones_1",
                        "title": "Les pièces de la maison (Partie 1)",
                        "questions": [
                            {"id": 201, "type": "multiple_choice", "question": "Comment dit-on 'La cuisine' en espagnol ?", "options": ["La cocina", "El salón", "El baño", "El dormitorio"], "correct_answer": "La cocina", "explanation": "'La cocina' = La cuisine.", "xp": 10},
                            {"id": 202, "type": "fill_in_the_blank", "question": "Complétez : Descanso en el ___ (salon).", "options": None, "correct_answer": "salón", "explanation": "'El salón' = Le salon / La salle de séjour.", "xp": 10},
                            {"id": 203, "type": "multiple_choice", "question": "Que signifie 'El dormitorio' ?", "options": ["La chambre à coucher", "La salle de bain", "Le couloir", "Le grenier"], "correct_answer": "La chambre à coucher", "explanation": "'El dormitorio' (ou 'la habitación') = La chambre à coucher.", "xp": 10},
                            {"id": 204, "type": "multiple_choice", "question": "Comment dit-on 'La salle de bain' ?", "options": ["El cuarto de baño", "El comedor", "La terraza", "La entrada"], "correct_answer": "El cuarto de baño", "explanation": "'El cuarto de baño' (ou 'el baño') = La salle de bain.", "xp": 10},
                            {"id": 205, "type": "fill_in_the_blank", "question": "Complétez : Comemos en el ___ (salle à manger).", "options": None, "correct_answer": "comedor", "explanation": "'El comedor' = La salle à manger.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_casa_habitaciones_2",
                        "title": "Les pièces et espaces extérieurs (Partie 2)",
                        "questions": [
                            {"id": 206, "type": "multiple_choice", "question": "Comment dit-on 'Le jardin' ?", "options": ["El jardín", "El patio", "El garaje", "El balcón"], "correct_answer": "El jardín", "explanation": "'El jardín' = Le jardin.", "xp": 10},
                            {"id": 207, "type": "fill_in_the_blank", "question": "Complétez : El coche está en el ___ (garage).", "options": None, "correct_answer": "garaje", "explanation": "'El garaje' = Le garage.", "xp": 10},
                            {"id": 208, "type": "multiple_choice", "question": "Que signifie 'El pasillo' ?", "options": ["Le couloir", "L'escalier", "Le balcon", "La cave"], "correct_answer": "Le couloir", "explanation": "'El pasillo' = Le couloir.", "xp": 10},
                            {"id": 209, "type": "multiple_choice", "question": "Comment dit-on 'L'escalier' en espagnol ?", "options": ["La escalera", "El ascensor", "La puerta", "La ventana"], "correct_answer": "La escalera", "explanation": "'La escalera' = L'escalier.", "xp": 10},
                            {"id": 210, "type": "fill_in_the_blank", "question": "Complétez : Tomo el sol en la ___ (terrasse).", "options": None, "correct_answer": "terraza", "explanation": "'La terraza' = La terrasse.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_muebles_1",
                        "title": "Les meubles essentiels (Salon & Chambre)",
                        "questions": [
                            {"id": 211, "type": "multiple_choice", "question": "Comment dit-on 'Le lit' ?", "options": ["La cama", "La mesa", "La silla", "El armario"], "correct_answer": "La cama", "explanation": "'La cama' = Le lit.", "xp": 10},
                            {"id": 212, "type": "fill_in_the_blank", "question": "Complétez : Me siento en el ___ (canapé).", "options": None, "correct_answer": "sofá", "explanation": "'El sofá' = Le canapé.", "xp": 10},
                            {"id": 213, "type": "multiple_choice", "question": "Que signifie 'La mesa' ?", "options": ["La table", "La chaise", "L'armoire", "L'étagère"], "correct_answer": "La table", "explanation": "'La mesa' = La table.", "xp": 10},
                            {"id": 214, "type": "multiple_choice", "question": "Comment dit-on 'La chaise' ?", "options": ["La silla", "El sillón", "La estantería", "El escritorio"], "correct_answer": "La silla", "explanation": "'La silla' = La chaise.", "xp": 10},
                            {"id": 215, "type": "fill_in_the_blank", "question": "Complétez : Guardo mi ropa en el ___ (armoire / penderie).", "options": None, "correct_answer": "armario", "explanation": "'El armario' = L'armoire / Le placard.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_muebles_2",
                        "title": "Les meubles et rangements (Partie 2)",
                        "questions": [
                            {"id": 216, "type": "multiple_choice", "question": "Comment dit-on 'Le fauteuil' en espagnol ?", "options": ["El sillón", "El sofá", "La silla", "El taburete"], "correct_answer": "El sillón", "explanation": "'El sillón' = Le fauteuil.", "xp": 10},
                            {"id": 217, "type": "fill_in_the_blank", "question": "Complétez : Los libros están en la ___ (étagère / bibliothèque).", "options": None, "correct_answer": "estantería", "explanation": "'La estantería' = L'étagère / La bibliothèque.", "xp": 10},
                            {"id": 218, "type": "multiple_choice", "question": "Que signifie 'El escritorio' ?", "options": ["Le bureau (meuble)", "L'ordinateur", "La table de nuit", "Le tiroir"], "correct_answer": "Le bureau (meuble)", "explanation": "'El escritorio' = Le bureau de travail.", "xp": 10},
                            {"id": 219, "type": "multiple_choice", "question": "Comment dit-on 'La table de chevet' ?", "options": ["La mesilla de noche", "La mesa baja", "El cajón", "La cómoda"], "correct_answer": "La mesilla de noche", "explanation": "'La mesilla de noche' = La table de chevet.", "xp": 10},
                            {"id": 220, "type": "fill_in_the_blank", "question": "Complétez : Guardo los calcetines en el ___ (tiroir).", "options": None, "correct_answer": "cajón", "explanation": "'El cajón' = Le tiroir.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_electrodomesticos_1",
                        "title": "Électroménager et équipement",
                        "questions": [
                            {"id": 221, "type": "multiple_choice", "question": "Comment dit-on 'Le réfrigérateur' en espagnol ?", "options": ["La nevera", "El horno", "La lavadora", "El microondas"], "correct_answer": "La nevera", "explanation": "'La nevera' (ou 'el frigorífico') = Le réfrigérateur.", "xp": 10},
                            {"id": 222, "type": "fill_in_the_blank", "question": "Complétez : Lavo la ropa en la ___ (machine à laver).", "options": None, "correct_answer": "lavadora", "explanation": "'La lavadora' = La machine à laver le linge.", "xp": 10},
                            {"id": 223, "type": "multiple_choice", "question": "Que signifie 'El lavavajillas' ?", "options": ["Le lave-vaisselle", "L'évier", "Le lave-linge", "Le fer à repasser"], "correct_answer": "Le lave-vaisselle", "explanation": "'El lavavajillas' (ou 'el lavaplatos') = Le lave-vaisselle.", "xp": 10},
                            {"id": 224, "type": "multiple_choice", "question": "Comment dit-on 'Le four' ?", "options": ["El horno", "La sartén", "El fuego", "La olla"], "correct_answer": "El horno", "explanation": "'El horno' = Le four.", "xp": 10},
                            {"id": 225, "type": "fill_in_the_blank", "question": "Complétez : Caliento la leche en el ___ (micro-ondes).", "options": None, "correct_answer": "microondas", "explanation": "'El microondas' = Le micro-ondes.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_objetos_cotidianos_1",
                        "title": "Objets et éléments du quotidien",
                        "questions": [
                            {"id": 226, "type": "multiple_choice", "question": "Comment dit-on 'La lampe' ?", "options": ["La lámpara", "La bombilla", "La vela", "La linterna"], "correct_answer": "La lampe", "explanation": "'La lámpara' = La lampe.", "xp": 10},
                            {"id": 227, "type": "fill_in_the_blank", "question": "Complétez : Me miro en el ___ (miroir).", "options": None, "correct_answer": "espejo", "explanation": "'El espejo' = Le miroir.", "xp": 10},
                            {"id": 228, "type": "multiple_choice", "question": "Que signifie 'La alfombra' ?", "options": ["Le tapis", "Le rideau", "Le tableau", "Le coussin"], "correct_answer": "Le tapis", "explanation": "'La alfombra' = Le tapis / La moquette.", "xp": 10},
                            {"id": 229, "type": "multiple_choice", "question": "Comment dit-on 'Les rideaux' ?", "options": ["Las cortinas", "Las sábanas", "Las toallas", "Las mantas"], "correct_answer": "Las cortinas", "explanation": "'Las cortinas' = Les rideaux.", "xp": 10},
                            {"id": 230, "type": "fill_in_the_blank", "question": "Complétez : Abro la ___ para ver la calle (fenêtre).", "options": None, "correct_answer": "ventana", "explanation": "'La ventana' = La fenêtre.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_barrio_lugares_1",
                        "title": "Les lieux du quartier (Partie 1)",
                        "questions": [
                            {"id": 231, "type": "multiple_choice", "question": "Comment dit-on 'La place' en espagnol ?", "options": ["La plaza", "La calle", "La avenida", "El parque"], "correct_answer": "La plaza", "explanation": "'La plaza' = La place publique.", "xp": 10},
                            {"id": 232, "type": "fill_in_the_blank", "question": "Complétez : Compro comida en el ___ (supermarché).", "options": None, "correct_answer": "supermercado", "explanation": "'El supermercado' = Le supermarché.", "xp": 10},
                            {"id": 233, "type": "multiple_choice", "question": "Que signifie 'La farmacia' ?", "options": ["La pharmacie", "L'hôpital", "La mairie", "La poste"], "correct_answer": "La pharmacie", "explanation": "'La farmacia' = La pharmacie.", "xp": 10},
                            {"id": 234, "type": "multiple_choice", "question": "Comment dit-on 'La boulangerie' ?", "options": ["La panadería", "La carnicería", "La pescadería", "La frutería"], "correct_answer": "La panadería", "explanation": "'La panadería' = La boulangerie.", "xp": 10},
                            {"id": 235, "type": "fill_in_the_blank", "question": "Complétez : Paseo por el ___ (parc).", "options": None, "correct_answer": "parque", "explanation": "'El parque' = Le parc.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_barrio_lugares_2",
                        "title": "Les commerces et services du quartier (Partie 2)",
                        "questions": [
                            {"id": 236, "type": "multiple_choice", "question": "Comment dit-on 'L'école' ?", "options": ["La escuela", "La biblioteca", "La comisaría", "El banco"], "correct_answer": "La escuela", "explanation": "'La escuela' (ou 'el colegio') = L'école.", "xp": 10},
                            {"id": 237, "type": "fill_in_the_blank", "question": "Complétez : Saco dinero del ___ (banque).", "options": None, "correct_answer": "banco", "explanation": "'El banco' = La banque.", "xp": 10},
                            {"id": 238, "type": "multiple_choice", "question": "Que signifie 'La estación de tren' ?", "options": ["La gare ferroviaire", "L'arrêt de bus", "La station de métro", "L'aéroport"], "correct_answer": "La gare ferroviaire", "explanation": "'La estación de tren' = La gare de train.", "xp": 10},
                            {"id": 239, "type": "multiple_choice", "question": "Comment dit-on 'L'hôpital' ?", "options": ["El hospital", "El centro cívico", "El museo", "El teatro"], "correct_answer": "El hospital", "explanation": "'El hospital' = L'hôpital.", "xp": 10},
                            {"id": 240, "type": "fill_in_the_blank", "question": "Complétez : Tomo un café en la ___ (cafétéria / café).", "options": None, "correct_answer": "cafetería", "explanation": "'La cafetería' = Le café / La cafétéria.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_tipos_vivienda",
                        "title": "Types de logements et caractéristiques",
                        "questions": [
                            {"id": 241, "type": "multiple_choice", "question": "Comment dit-on 'Un appartement' en Espagne ?", "options": ["Un piso", "Un jardín", "Un hotel", "Un garaje"], "correct_answer": "Un piso", "explanation": "'Un piso' (ou 'un apartamento') = Un appartement.", "xp": 10},
                            {"id": 242, "type": "fill_in_the_blank", "question": "Complétez : Vivo en una ___ individual (maison).", "options": None, "correct_answer": "casa", "explanation": "'La casa' = La maison.", "xp": 10},
                            {"id": 243, "type": "multiple_choice", "question": "Le contraire de 'grande' (grand) pour un logement est :", "options": ["pequeño", "luminoso", "antiguo", "ruidoso"], "correct_answer": "pequeño", "explanation": "'Pequeño' = Petit.", "xp": 10},
                            {"id": 244, "type": "multiple_choice", "question": "Un appartement avec beaucoup de lumière naturelle est :", "options": ["luminoso", "oscuro", "antiguo", "estrecho"], "correct_answer": "luminoso", "explanation": "'Luminoso' = Lumineux.", "xp": 10},
                            {"id": 245, "type": "fill_in_the_blank", "question": "Complétez : El piso está en la tercera ___ (étage).", "options": None, "correct_answer": "planta", "explanation": "'La planta' (ou 'el piso') = L'étage.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_barrio_adjetivos",
                        "title": "Qualificatifs pour décrire son quartier",
                        "questions": [
                            {"id": 246, "type": "multiple_choice", "question": "Comment qualifie-t-on un quartier 'calme' ?", "options": ["tranquilo", "ruidoso", "peligroso", "sucio"], "correct_answer": "tranquilo", "explanation": "'Tranquilo' = Calme / Tranquille.", "xp": 10},
                            {"id": 247, "type": "fill_in_the_blank", "question": "Complétez : El centro es muy ___ (animé / vivant).", "options": None, "correct_answer": "animado", "explanation": "'Animado' = Animé / Vivant.", "xp": 10},
                            {"id": 248, "type": "multiple_choice", "question": "Que signifie un quartier 'ruidoso' ?", "options": ["Bruyant", "Propre", "Moderne", "Éloigné"], "correct_answer": "Bruyant", "explanation": "'Ruidoso' = Bruyant.", "xp": 10},
                            {"id": 249, "type": "multiple_choice", "question": "Comment dit-on 'moderne' en espagnol ?", "options": ["moderno", "antiguo", "lejano", "estrecho"], "correct_answer": "moderno", "explanation": "'Moderno' = Moderne.", "xp": 10},
                            {"id": 250, "type": "fill_in_the_blank", "question": "Complétez : Mi calle está muy ___ (propre).", "options": None, "correct_answer": "limpia", "explanation": "'Limpia' = Propre (accord au féminin singulier).", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_alimentos_basicos_1",
                        "title": "Les aliments du quotidien (Partie 1)",
                        "questions": [
                            {"id": 301, "type": "multiple_choice", "question": "Comment dit-on 'Le pain' en espagnol ?", "options": ["El pan", "El queso", "El arroz", "El huevo"], "correct_answer": "El pan", "explanation": "'El pan' = Le pain.", "xp": 10},
                            {"id": 302, "type": "fill_in_the_blank", "question": "Complétez : Para el desayuno tomo pan con ___ (fromage).", "options": None, "correct_answer": "queso", "explanation": "'El queso' = Le fromage.", "xp": 10},
                            {"id": 303, "type": "multiple_choice", "question": "Que signifie 'El huevo' ?", "options": ["L'œuf", "Le beurre", "Le lait", "Le poisson"], "correct_answer": "L'œuf", "explanation": "'El huevo' = L'œuf.", "xp": 10},
                            {"id": 304, "type": "multiple_choice", "question": "Comment dit-on 'Le riz' ?", "options": ["El arroz", "La pasta", "El azúcar", "La harina"], "correct_answer": "El arroz", "explanation": "'El arroz' = Le riz.", "xp": 10},
                            {"id": 305, "type": "fill_in_the_blank", "question": "Complétez : Cocino con aceite de ___ (olive).", "options": None, "correct_answer": "oliva", "explanation": "'Aceite de oliva' = Huile d'olive.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_frutas_verduras_1",
                        "title": "Fruits et Légumes",
                        "questions": [
                            {"id": 306, "type": "multiple_choice", "question": "Comment dit-on 'La pomme' ?", "options": ["La manzana", "La naranja", "El plátano", "La fresa"], "correct_answer": "La manzana", "explanation": "'La manzana' = La pomme.", "xp": 10},
                            {"id": 307, "type": "fill_in_the_blank", "question": "Complétez : Me gusta el zumo de ___ (orange).", "options": None, "correct_answer": "naranja", "explanation": "'La naranja' = L'orange.", "xp": 10},
                            {"id": 308, "type": "multiple_choice", "question": "Que signifie 'El tomate' ?", "options": ["La tomate", "La pomme de terre", "L'oignon", "La carotte"], "correct_answer": "La tomate", "explanation": "'El tomate' = La tomate.", "xp": 10},
                            {"id": 309, "type": "multiple_choice", "question": "Comment dit-on 'La pomme de terre' en Espagne ?", "options": ["La patata", "La lechuga", "El pepino", "El ajo"], "correct_answer": "La patata", "explanation": "'La patata' (ou 'la papa' en Amérique latine) = La pomme de terre.", "xp": 10},
                            {"id": 310, "type": "fill_in_the_blank", "question": "Complétez : La ensalada lleva lechuga y ___ (oignon).", "options": None, "correct_answer": "cebolla", "explanation": "'La cebolla' = L'oignon.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_carnes_pescados_1",
                        "title": "Viandes, Poissons et Fruits de mer",
                        "questions": [
                            {"id": 311, "type": "multiple_choice", "question": "Comment dit-on 'Le poulet' ?", "options": ["El pollo", "El昆pescado", "La carne", "El jamón"], "correct_answer": "El pollo", "explanation": "'El pollo' = Le poulet.", "xp": 10},
                            {"id": 312, "type": "fill_in_the_blank", "question": "Complétez : En España comen mucho ___ ibérico (jambon).", "options": None, "correct_answer": "jamón", "explanation": "'El jamón' = Le jambon.", "xp": 10},
                            {"id": 313, "type": "multiple_choice", "question": "Que signifie 'El pescado' ?", "options": ["Le poisson (aliment)", "La viande de bœuf", "Le porc", "Les crevettes"], "correct_answer": "Le poisson (aliment)", "explanation": "'El pescado' = Le poisson servi ou pêché.", "xp": 10},
                            {"id": 314, "type": "multiple_choice", "question": "Comment dit-on 'La viande' ?", "options": ["La carne", "El marisco", "El cordero", "La ternera"], "correct_answer": "La carne", "explanation": "'La carne' = La viande.", "xp": 10},
                            {"id": 315, "type": "fill_in_the_blank", "question": "Complétez : La paella marinera tiene ___ (fruits de mer).", "options": None, "correct_answer": "marisco", "explanation": "'El marisco' = Les fruits de mer.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_bebidas_1",
                        "title": "Les boissons",
                        "questions": [
                            {"id": 316, "type": "multiple_choice", "question": "Comment dit-on 'L'eau' en espagnol ?", "options": ["El agua", "La leche", "El vino", "La cerveza"], "correct_answer": "El agua", "explanation": "'El agua' = L'eau.", "xp": 10},
                            {"id": 317, "type": "fill_in_the_blank", "question": "Complétez : Quiero un vaso de ___ con gas (eau).", "options": None, "correct_answer": "agua", "explanation": "'Agua con gas' = Eau gazeuse.", "xp": 10},
                            {"id": 318, "type": "multiple_choice", "question": "Que signifie 'El vino tinto' ?", "options": ["Le vin rouge", "Le vin blanc", "Le vin rosé", "Le jus de raisin"], "correct_answer": "Le vin rouge", "explanation": "'Vino tinto' = Vin rouge.", "xp": 10},
                            {"id": 319, "type": "multiple_choice", "question": "Comment commande-t-on 'Un café au lait' ?", "options": ["Un café con leche", "Un café solo", "Un café cortado", "Un té con leche"], "correct_answer": "Un café con leche", "explanation": "'Café con leche' = Café au lait.", "xp": 10},
                            {"id": 320, "type": "fill_in_the_blank", "question": "Complétez : Para brindar pedimos una ___ (bière).", "options": None, "correct_answer": "cerveza", "explanation": "'La cerveza' = La bière.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_mesa_cubiertos_1",
                        "title": "La table et les couverts",
                        "questions": [
                            {"id": 321, "type": "multiple_choice", "question": "Comment dit-on 'La fourchette' ?", "options": ["El tenedor", "El cuchillo", "La cuchara", "El plato"], "correct_answer": "El tenedor", "explanation": "'El tenedor' = La fourchette.", "xp": 10},
                            {"id": 322, "type": "fill_in_the_blank", "question": "Complétez : Corto la carne con el ___ (couteau).", "options": None, "correct_answer": "cuchillo", "explanation": "'El cuchillo' = Le couteau.", "xp": 10},
                            {"id": 323, "type": "multiple_choice", "question": "Que signifie 'La cuchara' ?", "options": ["La cuillère", "La serviette", "Le verre", "La bouteille"], "correct_answer": "La cuillère", "explanation": "'La cuchara' = La cuillère.", "xp": 10},
                            {"id": 324, "type": "multiple_choice", "question": "Comment dit-on 'Le verre' ?", "options": ["El vaso", "La copa", "La taza", "El plato"], "correct_answer": "El vaso", "explanation": "'El vaso' = Le verre.", "xp": 10},
                            {"id": 325, "type": "fill_in_the_blank", "question": "Complétez : Me limpio con la ___ (serviette de table).", "options": None, "correct_answer": "servilleta", "explanation": "'La servilleta' = La serviette de table.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_menu_restaurante_1",
                        "title": "La structure du menu au restaurant",
                        "questions": [
                            {"id": 326, "type": "multiple_choice", "question": "Comment désigne-t-on l'entrée / le premier plat ?", "options": ["El primer plato", "El segundo plato", "El postre", "La cuenta"], "correct_answer": "El primer plato", "explanation": "'El primer plato' = L'entrée.", "xp": 10},
                            {"id": 327, "type": "fill_in_the_blank", "question": "Complétez : De ___ quiero flan casero (dessert).", "options": None, "correct_answer": "postre", "explanation": "'El postre' = Le dessert.", "xp": 10},
                            {"id": 328, "type": "multiple_choice", "question": "Que signifie 'El menú del día' ?", "options": ["Le menu du jour", "La carte des vins", "La liste des prix", "La note du repas"], "correct_answer": "Le menu du jour", "explanation": "'El menú del día' = La formule du midi.", "xp": 10},
                            {"id": 329, "type": "multiple_choice", "question": "Comment dit-on 'Le plat principal' ?", "options": ["El segundo plato", "El plato hondo", "El aperitivo", "La merienda"], "correct_answer": "El segundo plato", "explanation": "'El segundo plato' = Le plat principal.", "xp": 10},
                            {"id": 330, "type": "fill_in_the_blank", "question": "Complétez : Para picar pedimos unas ___ (petites portions / tapas).", "options": None, "correct_answer": "tapas", "explanation": "'Las tapas' = Les tapas.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_compras_mercado_1",
                        "title": "Faire les courses au marché (Quantités)",
                        "questions": [
                            {"id": 331, "type": "multiple_choice", "question": "Comment dit-on 'Un kilo de tomates' ?", "options": ["Un kilo de tomates", "Un litro de tomates", "Un gramo de tomates", "Una botella de tomates"], "correct_answer": "Un kilo de tomates", "explanation": "'Un kilo' = Un kilogramme.", "xp": 10},
                            {"id": 332, "type": "fill_in_the_blank", "question": "Complétez : Quiero medio ___ de manzanas (kilo).", "options": None, "correct_answer": "kilo", "explanation": "'Medio kilo' = 500 grammes.", "xp": 10},
                            {"id": 333, "type": "multiple_choice", "question": "Que demande-t-on avec 'Una docena de huevos' ?", "options": ["Une douzaine d'œufs", "Dix œufs", "Deux œufs", "Une boîte d'œufs"], "correct_answer": "Une douzaine d'œufs", "explanation": "'Una docena' = Une douzaine.", "xp": 10},
                            {"id": 334, "type": "multiple_choice", "question": "Comment dit-on 'Une bouteille d'eau' ?", "options": ["Una botella de agua", "Un paquete de agua", "Una lata de agua", "Un trozo de agua"], "correct_answer": "Una botella de agua", "explanation": "'Una botella' = Une bouteille.", "xp": 10},
                            {"id": 335, "type": "fill_in_the_blank", "question": "Complétez : Póngame un ___ de queso (morceau / tranche).", "options": None, "correct_answer": "trozo", "explanation": "'Un trozo' = Un morceau.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_comercios_alimentacion_1",
                        "title": "Les commerces de bouche",
                        "questions": [
                            {"id": 336, "type": "multiple_choice", "question": "Où achète-t-on la viande ?", "options": ["En la carnicería", "En la panadería", "En la frutería", "En la pescadería"], "correct_answer": "En la carnicería", "explanation": "'La carnicería' = La boucherie.", "xp": 10},
                            {"id": 337, "type": "fill_in_the_blank", "question": "Complétez : Compro fruta fresca en la ___ (primeur / fruiterie).", "options": None, "correct_answer": "frutería", "explanation": "'La frutería' = Le primeur.", "xp": 10},
                            {"id": 338, "type": "multiple_choice", "question": "Que vend-on dans une 'pescadería' ?", "options": ["Du poisson et des fruits de mer", "Du pain", "Des gâteaux", "Des produits laitiers"], "correct_answer": "Du poisson et des fruits de mer", "explanation": "'La pescadería' = La poissonnerie.", "xp": 10},
                            {"id": 339, "type": "multiple_choice", "question": "Où achète-t-on des pâtisseries et gâteaux ?", "options": ["En la pastelería", "En la verdulería", "En el estanco", "En la farmacia"], "correct_answer": "En la pastelería", "explanation": "'La pastelería' = La pâtisserie.", "xp": 10},
                            {"id": 340, "type": "fill_in_the_blank", "question": "Complétez : Los sábados voy al ___ municipal a comprar (marché).", "options": None, "correct_answer": "mercado", "explanation": "'El mercado' = Le marché.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_sabores_platos_1",
                        "title": "Goûts, saveurs et cuisson",
                        "questions": [
                            {"id": 341, "type": "multiple_choice", "question": "Le contraire de 'dulce' (sucré) est :", "options": ["salado", "rico", "frío", "caliente"], "correct_answer": "salado", "explanation": "'Salado' = Salé.", "xp": 10},
                            {"id": 342, "type": "fill_in_the_blank", "question": "Complétez : Este café está muy ___ (chaud).", "options": None, "correct_answer": "caliente", "explanation": "'Caliente' = Chaud.", "xp": 10},
                            {"id": 343, "type": "multiple_choice", "question": "Que signifie 'picante' ?", "options": ["Piquant / Épicé", "Acide", "Amer", "Fade"], "correct_answer": "Piquant / Épicé", "explanation": "'Picante' = Épicé / Piquant.", "xp": 10},
                            {"id": 344, "type": "multiple_choice", "question": "Si un plat est délicieux, on dit qu'il est :", "options": ["rico", "malo", "soso", "seco"], "correct_answer": "rico", "explanation": "'Está rico' = C'est délicieux.", "xp": 10},
                            {"id": 345, "type": "fill_in_the_blank", "question": "Complétez : Quiero un agua bien ___ (fraîche / froide).", "options": None, "correct_answer": "fría", "explanation": "'Fría' = Froide.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_pagos_cuenta_1",
                        "title": "L'addition, monnaie et moyens de paiement",
                        "questions": [
                            {"id": 346, "type": "multiple_choice", "question": "Comment demande-t-on 'L'addition, s'il vous plaît' ?", "options": ["La cuenta, por favor", "La carta, por favor", "El menú, por favor", "El precio, por favor"], "correct_answer": "La cuenta, por favor", "explanation": "'La cuenta' = L'addition.", "xp": 10},
                            {"id": 347, "type": "fill_in_the_blank", "question": "Complétez : ¿Puedo pagar con ___ de crédito? (carte)", "options": None, "correct_answer": "tarjeta", "explanation": "'Tarjeta de crédito' = Carte bancaire.", "xp": 10},
                            {"id": 348, "type": "multiple_choice", "question": "Que signifie 'Pagar en efectivo' ?", "options": ["Payer en espèces / liquide", "Payer par virement", "Payer par chèque", "Payer plus tard"], "correct_answer": "Payer en espèces / liquide", "explanation": "'En efectivo' = En espèces.", "xp": 10},
                            {"id": 349, "type": "multiple_choice", "question": "L'argent laissé en plus pour le service s'appelle :", "options": ["La propina", "El cambio", "El recibo", "La oferta"], "correct_answer": "La propina", "explanation": "'La propina' = Le pourboire.", "xp": 10},
                            {"id": 350, "type": "fill_in_the_blank", "question": "Complétez : Aquí tiene su ___ (monnaie rendue).", "options": None, "correct_answer": "cambio", "explanation": "'El cambio' = La monnaie rendue.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_dias_semana_1",
                        "title": "Les jours de la semaine",
                        "questions": [
                            {"id": 401, "type": "multiple_choice", "question": "Comment dit-on 'Lundi' en espagnol ?", "options": ["Lunes", "Martes", "Miércoles", "Jueves"], "correct_answer": "Lunes", "explanation": "'Lunes' = Lundi.", "xp": 10},
                            {"id": 402, "type": "fill_in_the_blank", "question": "Complétez : El día después del martes es el ___ (mercredi).", "options": None, "correct_answer": "miércoles", "explanation": "'Miércoles' = Mercredi.", "xp": 10},
                            {"id": 403, "type": "multiple_choice", "question": "Que signifie 'El fin de semana' ?", "options": ["Le week-end", "Le début de semaine", "Le mois prochain", "Les vacances"], "correct_answer": "Le week-end", "explanation": "'El fin de semana' = Le week-end.", "xp": 10},
                            {"id": 404, "type": "multiple_choice", "question": "Comment dit-on 'Vendredi' ?", "options": ["Viernes", "Jueves", "Sábado", "Domingo"], "correct_answer": "Viernes", "explanation": "'Viernes' = Vendredi.", "xp": 10},
                            {"id": 405, "type": "fill_in_the_blank", "question": "Complétez : El último día de la semana es el ___ (dimanche).", "options": None, "correct_answer": "domingo", "explanation": "'Domingo' = Dimanche.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_meses_ano_1",
                        "title": "Les mois de l'année",
                        "questions": [
                            {"id": 406, "type": "multiple_choice", "question": "Quel est le premier mois de l'année ?", "options": ["Enero", "Febrero", "Marzo", "Abril"], "correct_answer": "Enero", "explanation": "'Enero' = Janvier.", "xp": 10},
                            {"id": 407, "type": "fill_in_the_blank", "question": "Complétez : La fiesta nacional de España es en ___ (octobre).", "options": None, "correct_answer": "octubre", "explanation": "'Octubre' = Octobre.", "xp": 10},
                            {"id": 408, "type": "multiple_choice", "question": "Comment dit-on 'Août' en espagnol ?", "options": ["Agosto", "Julio", "Junio", "Septiembre"], "correct_answer": "Agosto", "explanation": "'Agosto' = Août.", "xp": 10},
                            {"id": 409, "type": "multiple_choice", "question": "Que signifie 'Mayo' ?", "options": ["Mai", "Mars", "Juin", "Avril"], "correct_answer": "Mai", "explanation": "'Mayo' = Mai.", "xp": 10},
                            {"id": 410, "type": "fill_in_the_blank", "question": "Complétez : Navidad se celebra en ___ (décembre).", "options": None, "correct_answer": "diciembre", "explanation": "'Diciembre' = Décembre.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_estaciones_1",
                        "title": "Les quatre saisons",
                        "questions": [
                            {"id": 411, "type": "multiple_choice", "question": "Comment dit-on 'L'été' en espagnol ?", "options": ["El verano", "La primavera", "El otoño", "El invierno"], "correct_answer": "El verano", "explanation": "'El verano' = L'été.", "xp": 10},
                            {"id": 412, "type": "fill_in_the_blank", "question": "Complétez : Las flores florecen en ___ (le printemps).", "options": None, "correct_answer": "primavera", "explanation": "'La primavera' = Le printemps.", "xp": 10},
                            {"id": 413, "type": "multiple_choice", "question": "Quelle saison commence en décembre dans l'hémisphère nord ?", "options": ["El invierno", "El verano", "El otoño", "La primavera"], "correct_answer": "El invierno", "explanation": "'El invierno' = L'hiver.", "xp": 10},
                            {"id": 414, "type": "multiple_choice", "question": "Que signifie 'El otoño' ?", "options": ["L'automne", "L'hiver", "Le printemps", "L'été"], "correct_answer": "L'automne", "explanation": "'El otoño' = L'automne.", "xp": 10},
                            {"id": 415, "type": "fill_in_the_blank", "question": "Complétez : Hace mucho frío durante el ___ (hiver).", "options": None, "correct_answer": "invierno", "explanation": "'El invierno' = L'hiver.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_clima_meteo_1",
                        "title": "Le climat et les expressions météo (Partie 1)",
                        "questions": [
                            {"id": 416, "type": "multiple_choice", "question": "Comment dit-on 'Il fait chaud' ?", "options": ["Hace calor", "Hace frío", "Hace sol", "Hace viento"], "correct_answer": "Hace calor", "explanation": "'Hace calor' = Il fait chaud.", "xp": 10},
                            {"id": 417, "type": "fill_in_the_blank", "question": "Complétez : En invierno hace mucho ___ (froid).", "options": None, "correct_answer": "frío", "explanation": "'Hace frío' = Il fait froid.", "xp": 10},
                            {"id": 418, "type": "multiple_choice", "question": "Que signifie 'Hace buen tiempo' ?", "options": ["Il fait beau temps", "Il fait mauvais temps", "Il fait nuit", "Il est tôt"], "correct_answer": "Il fait beau temps", "explanation": "'Hace buen tiempo' = Il fait beau.", "xp": 10},
                            {"id": 419, "type": "multiple_choice", "question": "Comment dit-on 'Il y a du soleil' / 'Il fait soleil' ?", "options": ["Hace sol", "Hace niebla", "Llueve", "Nieva"], "correct_answer": "Hace sol", "explanation": "'Hace sol' = Il fait soleil.", "xp": 10},
                            {"id": 420, "type": "fill_in_the_blank", "question": "Complétez : Hoy hace mal ___ (temps).", "options": None, "correct_answer": "tiempo", "explanation": "'Hace mal tiempo' = Il fait mauvais temps.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_clima_meteo_2",
                        "title": "Phénomènes météo (Pluie, Neige, Ciel)",
                        "questions": [
                            {"id": 421, "type": "multiple_choice", "question": "Comment dit-on 'Il pleut' en espagnol ?", "options": ["Llueve", "Nieva", "Hace viento", "Está despejado"], "correct_answer": "Llueve", "explanation": "'Llueve' = Il pleut.", "xp": 10},
                            {"id": 422, "type": "fill_in_the_blank", "question": "Complétez : En la montaña ___ mucho en enero (il neige).", "options": None, "correct_answer": "nieva", "explanation": "'Nieva' = Il neige.", "xp": 10},
                            {"id": 423, "type": "multiple_choice", "question": "Que signifie 'Está nublado' ?", "options": ["C'est nuageux / couvert", "C'est ensoleillé", "Il pleut", "Il gèle"], "correct_answer": "C'est nuageux / couvert", "explanation": "'Está nublado' = Le ciel est couvert.", "xp": 10},
                            {"id": 424, "type": "multiple_choice", "question": "Comment dit-on 'Il y a du vent' ?", "options": ["Hace viento", "Hace sol", "Hay niebla", "Llueve"], "correct_answer": "Hace viento", "explanation": "'Hace viento' = Il fait du vent.", "xp": 10},
                            {"id": 425, "type": "fill_in_the_blank", "question": "Complétez : Llevo paraguas porque cae mucha ___ (pluie).", "options": None, "correct_answer": "lluvia", "explanation": "'La lluvia' = La pluie.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_partes_dia_1",
                        "title": "Les moments de la journée",
                        "questions": [
                            {"id": 426, "type": "multiple_choice", "question": "Comment dit-on 'Le matin' ?", "options": ["La mañana", "La tarde", "La noche", "El mediodía"], "correct_answer": "La mañana", "explanation": "'La mañana' = Le matin.", "xp": 10},
                            {"id": 427, "type": "fill_in_the_blank", "question": "Complétez : Como a las dos del ___ (midi).", "options": None, "correct_answer": "mediodía", "explanation": "'El mediodía' = Le midi.", "xp": 10},
                            {"id": 428, "type": "multiple_choice", "question": "Que signifie 'Por la tarde' ?", "options": ["L'après-midi / En fin de journée", "Le matin", "La nuit", "À l'aube"], "correct_answer": "L'après-midi / En fin de journée", "explanation": "'Por la tarde' = L'après-midi.", "xp": 10},
                            {"id": 429, "type": "multiple_choice", "question": "Comment dit-on 'Minuit' ?", "options": ["Medianoche", "Mediodía", "Madrugada", "Tarde"], "correct_answer": "Medianoche", "explanation": "'La medianoche' = Minuit.", "xp": 10},
                            {"id": 430, "type": "fill_in_the_blank", "question": "Complétez : Duermo profundamente por la ___ (nuit).", "options": None, "correct_answer": "noche", "explanation": "'La noche' = La nuit.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_rutina_acciones_1",
                        "title": "Les actions de la routine du matin",
                        "questions": [
                            {"id": 431, "type": "multiple_choice", "question": "Comment dit-on 'Se réveiller' en espagnol ?", "options": ["Despertarse", "Levantarse", "Ducharse", "Vestirse"], "correct_answer": "Despertarse", "explanation": "'Despertarse' = Se réveiller.", "xp": 10},
                            {"id": 432, "type": "fill_in_the_blank", "question": "Complétez : Me ___ de la cama a las siete (se lever).", "options": None, "correct_answer": "levanto", "explanation": "'Levantarse' = Se lever.", "xp": 10},
                            {"id": 433, "type": "multiple_choice", "question": "Que signifie 'Ducharse' ?", "options": ["Prendre une douche", "Prendre un bain", "Se brosser les dents", "S'habiller"], "correct_answer": "Prendre une douche", "explanation": "'Ducharse' = Prendre une douche.", "xp": 10},
                            {"id": 434, "type": "multiple_choice", "question": "Comment dit-on 'Prendre son petit-déjeuner' ?", "options": ["Desayunar", "Comer", "Cenar", "Merendar"], "correct_answer": "Desayunar", "explanation": "'Desayunar' = Prendre le petit-déjeuner.", "xp": 10},
                            {"id": 435, "type": "fill_in_the_blank", "question": "Complétez : Me lavo los ___ después de comer (dents).", "options": None, "correct_answer": "dientes", "explanation": "'Lavarse los dientes' = Se brosser les dents.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_rutina_acciones_2",
                        "title": "Les repas et activités quotidiennes",
                        "questions": [
                            {"id": 436, "type": "multiple_choice", "question": "Comment dit-on 'Déjeuner' (le repas du midi) ?", "options": ["Comer / Almorzar", "Cenar", "Desayunar", "Cocinar"], "correct_answer": "Comer / Almorzar", "explanation": "'Comer' ou 'almorzar' = Déjeuner.", "xp": 10},
                            {"id": 437, "type": "fill_in_the_blank", "question": "Complétez : En España se ___ tarde por la noche (dîner).", "options": None, "correct_answer": "cena", "explanation": "'Cenar' = Dîner.", "xp": 10},
                            {"id": 438, "type": "multiple_choice", "question": "Que signifie 'Acostarse' ?", "options": ["Se coucher / Aller au lit", "Se lever", "S'habiller", "Se reposer"], "correct_answer": "Se coucher / Aller au lit", "explanation": "'Acostarse' = Se coucher.", "xp": 10},
                            {"id": 439, "type": "multiple_choice", "question": "Comment dit-on 'S'habiller' ?", "options": ["Vestirse", "Peinarse", "Bañarse", "Maquillarse"], "correct_answer": "Vestirse", "explanation": "'Vestirse' = S'habiller.", "xp": 10},
                            {"id": 440, "type": "fill_in_the_blank", "question": "Complétez : Por la tarde voy al ___ para hacer deporte (salle de sport).", "options": None, "correct_answer": "gimnasio", "explanation": "'El gimnasio' = La salle de sport.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_frecuencia_tiempo",
                        "title": "Indicateurs de fréquence et de temps",
                        "questions": [
                            {"id": 441, "type": "multiple_choice", "question": "Comment dit-on 'Toujours' en espagnol ?", "options": ["Siempre", "Nunca", "A veces", "A menudo"], "correct_answer": "Siempre", "explanation": "'Siempre' = Toujours.", "xp": 10},
                            {"id": 442, "type": "fill_in_the_blank", "question": "Complétez : ___ como pescado (jamais).", "options": None, "correct_answer": "Nunca", "explanation": "'Nunca' = Jamais.", "xp": 10},
                            {"id": 443, "type": "multiple_choice", "question": "Que signifie 'A veces' ?", "options": ["Parfois / De temps en temps", "Tous les jours", "Souvent", "Rarement"], "correct_answer": "Parfois / De temps en temps", "explanation": "'A veces' = Parfois.", "xp": 10},
                            {"id": 444, "type": "multiple_choice", "question": "Comment dit-on 'Tous les jours' ?", "options": ["Todos los días", "Cada mes", "Raras veces", "Casi nunca"], "correct_answer": "Todos los días", "explanation": "'Todos los días' = Tous les jours.", "xp": 10},
                            {"id": 445, "type": "fill_in_the_blank", "question": "Complétez : Voy al cine a ___ (souvent).", "options": None, "correct_answer": "menudo", "explanation": "'A menudo' = Souvent.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_hora_expresiones_1",
                        "title": "Vocabulaire pour donner l'heure",
                        "questions": [
                            {"id": 446, "type": "multiple_choice", "question": "Comment dit-on 'Et quart' en donnant l'heure ?", "options": ["Y cuarto", "Y media", "Menos cuarto", "En punto"], "correct_answer": "Y cuarto", "explanation": "'Y cuarto' = Et quart.", "xp": 10},
                            {"id": 447, "type": "fill_in_the_blank", "question": "Complétez : Son las dos y ___ (et demie - :30).", "options": None, "correct_answer": "media", "explanation": "'Y media' = Et demie.", "xp": 10},
                            {"id": 448, "type": "multiple_choice", "question": "Que signifie 'En punto' ?", "options": ["Pile / Précises", "Et demie", "Moins le quart", "En retard"], "correct_answer": "Pile / Précises", "explanation": "'En punto' = Pile.", "xp": 10},
                            {"id": 449, "type": "multiple_choice", "question": "Comment exprime-t-on 'Moins le quart' (:45) ?", "options": ["Menos cuarto", "Y cuarto", "Menos diez", "Menos media"], "correct_answer": "Menos cuarto", "explanation": "'Menos cuarto' = Moins le quart.", "xp": 10},
                            {"id": 450, "type": "fill_in_the_blank", "question": "Complétez : ¿Tienes ___? (l'heure)", "options": None, "correct_answer": "hora", "explanation": "'¿Tienes hora?' = As-tu l'heure ?", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_ciudad_lugares_1",
                        "title": "Les lieux de la ville (Partie 1)",
                        "questions": [
                            {"id": 501, "type": "multiple_choice", "question": "Comment dit-on 'La place principale' en espagnol ?", "options": ["La Plaza Mayor", "La calle ancha", "El parque central", "La avenida"], "correct_answer": "La Plaza Mayor", "explanation": "'La Plaza Mayor' est la place centrale typique des villes espagnoles.", "xp": 10},
                            {"id": 502, "type": "fill_in_the_blank", "question": "Complétez : El alcalde trabaja en el ___ (mairie).", "options": None, "correct_answer": "ayuntamiento", "explanation": "'El ayuntamiento' = La mairie / L'hôtel de ville.", "xp": 10},
                            {"id": 503, "type": "multiple_choice", "question": "Que signifie 'La catedral' ?", "options": ["La cathédrale", "Le musée", "Le château", "La bibliothèque"], "correct_answer": "La cathédrale", "explanation": "'La catedral' = La cathédrale.", "xp": 10},
                            {"id": 504, "type": "multiple_choice", "question": "Comment dit-on 'Le musée' ?", "options": ["El museo", "El teatro", "El cine", "El monumento"], "correct_answer": "El museo", "explanation": "'El museo' = Le musée.", "xp": 10},
                            {"id": 505, "type": "fill_in_the_blank", "question": "Complétez : Leo libros en la ___ municipal (bibliothèque).", "options": None, "correct_answer": "biblioteca", "explanation": "'La biblioteca' = La bibliothèque.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_ciudad_lugares_2",
                        "title": "Les lieux de la ville et services (Partie 2)",
                        "questions": [
                            {"id": 506, "type": "multiple_choice", "question": "Comment dit-on 'Le commissariat de police' ?", "options": ["La comisaría", "El hospital", "El cuartel", "El juzgado"], "correct_answer": "La comisaría", "explanation": "'La comisaría' = Le commissariat de police.", "xp": 10},
                            {"id": 507, "type": "fill_in_the_blank", "question": "Complétez : Envío una carta en la oficina de ___ (poste).", "options": None, "correct_answer": "correos", "explanation": "'La oficina de correos' (ou 'Correos') = Le bureau de poste.", "xp": 10},
                            {"id": 508, "type": "multiple_choice", "question": "Que signifie 'La oficina de turismo' ?", "options": ["L'office de tourisme", "L'agence de voyage", "La gare routière", "Le bureau de change"], "correct_answer": "L'office de tourisme", "explanation": "'La oficina de turismo' = L'office de tourisme.", "xp": 10},
                            {"id": 509, "type": "multiple_choice", "question": "Comment dit-on 'L'hôtel' ?", "options": ["El hotel", "El hostal", "El albergue", "El piso"], "correct_answer": "El hotel", "explanation": "'El hotel' = L'hôtel.", "xp": 10},
                            {"id": 510, "type": "fill_in_the_blank", "question": "Complétez : Compro ropa en el centro ___ (commercial).", "options": None, "correct_answer": "comercial", "explanation": "'El centro comercial' = Le centre commercial.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_transportes_terrestres_1",
                        "title": "Moyens de transport terrestres",
                        "questions": [
                            {"id": 511, "type": "multiple_choice", "question": "Comment dit-on 'Le bus' en Espagne ?", "options": ["El autobús", "El tren", "El metro", "El tranvía"], "correct_answer": "El autobús", "explanation": "'El autobús' (ou 'el bus') = Le bus / L'autobus.", "xp": 10},
                            {"id": 512, "type": "fill_in_the_blank", "question": "Complétez : Voy al trabajo en ___ subterráneo (métro).", "options": None, "correct_answer": "metro", "explanation": "'El metro' = Le métro.", "xp": 10},
                            {"id": 513, "type": "multiple_choice", "question": "Que signifie 'El tren de alta velocidad' (AVE en Espagne) ?", "options": ["Le train à grande vitesse", "Le train de banlieue", "Le train de marchandises", "Le tramway"], "correct_answer": "Le train à grande vitesse", "explanation": "'El tren de alta velocidad' = Le TGV / train à grande vitesse.", "xp": 10},
                            {"id": 514, "type": "multiple_choice", "question": "Comment dit-on 'La voiture' en espagnol ?", "options": ["El coche", "La moto", "La bicicleta", "El camión"], "correct_answer": "El coche", "explanation": "'El coche' (en Espagne) / 'el carro' ou 'el auto' (en Amérique latine) = La voiture.", "xp": 10},
                            {"id": 515, "type": "fill_in_the_blank", "question": "Complétez : Me muevo por la ciudad en ___ (vélo).", "options": None, "correct_answer": "bicicleta", "explanation": "'La bicicleta' (ou 'la bici') = Le vélo.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_transportes_otros_2",
                        "title": "Autres moyens de transport et déplacements",
                        "questions": [
                            {"id": 516, "type": "multiple_choice", "question": "Comment dit-on 'L'avion' ?", "options": ["El avión", "El barco", "El helicóptero", "El taxi"], "correct_answer": "El avión", "explanation": "'El avión' = L'avion.", "xp": 10},
                            {"id": 517, "type": "fill_in_the_blank", "question": "Complétez : Si llueve prefiero tomar un ___ (taxi).", "options": None, "correct_answer": "taxi", "explanation": "'El taxi' = Le taxi.", "xp": 10},
                            {"id": 518, "type": "multiple_choice", "question": "Que signifie 'Ir a pie' ?", "options": ["Aller à pied / Marcher", "Prendre les transports", "Faire du stop", "Courir vite"], "correct_answer": "Aller à pied / Marcher", "explanation": "'Ir a pie' (ou 'ir andando') = Aller à pied.", "xp": 10},
                            {"id": 519, "type": "multiple_choice", "question": "Comment dit-on 'Le bateau' ?", "options": ["El barco", "El puerto", "El río", "El mar"], "correct_answer": "El barco", "explanation": "'El barco' = Le bateau.", "xp": 10},
                            {"id": 520, "type": "fill_in_the_blank", "question": "Complétez : Para viajar rápido sobre raíles tomo el ___ (tramway).", "options": None, "correct_answer": "tranvía", "explanation": "'El tranvía' = Le tramway.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_infraestructuras_transporte_1",
                        "title": "Gares, stations et arrêts",
                        "questions": [
                            {"id": 521, "type": "multiple_choice", "question": "Comment dit-on 'L'arrêt de bus' ?", "options": ["La parada de autobús", "La estación de tren", "El andén", "El aeropuerto"], "correct_answer": "La parada de autobús", "explanation": "'La parada de autobús' = L'arrêt de bus.", "xp": 10},
                            {"id": 522, "type": "fill_in_the_blank", "question": "Complétez : Los aviones despegan del ___ (aéroport).", "options": None, "correct_answer": "aeropuerto", "explanation": "'El aeropuerto' = L'aéroport.", "xp": 10},
                            {"id": 523, "type": "multiple_choice", "question": "Que signifie 'El andén' dans une gare ?", "options": ["Le quai de gare / voie", "La salle d'attente", "Le guichet", "Le panneau d'affichage"], "correct_answer": "Le quai de gare / voie", "explanation": "'El andén' = Le quai de gare ou de métro.", "xp": 10},
                            {"id": 524, "type": "multiple_choice", "question": "Comment désigne-t-on la station de métro ?", "options": ["La estación de metro", "La parada de metro", "La línea de metro", "El túnel de metro"], "correct_answer": "La estación de metro", "explanation": "'La estación de metro' = La station de métro.", "xp": 10},
                            {"id": 525, "type": "fill_in_the_blank", "question": "Complétez : Espero el tren en la sala de ___ (attente).", "options": None, "correct_answer": "espera", "explanation": "'La sala de espera' = La salle d'attente.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_billetes_tarifas_1",
                        "title": "Billets, titres de transport et tarifs",
                        "questions": [
                            {"id": 526, "type": "multiple_choice", "question": "Comment dit-on 'Un billet simple / aller simple' ?", "options": ["Un billete sencillo", "Un billete de ida y vuelta", "Un abono transporte", "Un suplemento"], "correct_answer": "Un billete sencillo", "explanation": "'Un billete sencillo' (ou 'de ida') = Un aller simple.", "xp": 10},
                            {"id": 527, "type": "fill_in_the_blank", "question": "Complétez : Quiero un billete de ida y ___ (retour).", "options": None, "correct_answer": "vuelta", "explanation": "'Ida y vuelta' = Aller-retour.", "xp": 10},
                            {"id": 528, "type": "multiple_choice", "question": "Que signifie 'El abono mensual' ?", "options": ["Le pass / abonnement mensuel", "Le ticket 10 voyages", "Le tarif réduit", "L'amende"], "correct_answer": "Le pass / abonnement mensuel", "explanation": "'El abono mensual' = L'abonnement mensuel.", "xp": 10},
                            {"id": 529, "type": "multiple_choice", "question": "Où achète-t-on un ticket de train au guichet ?", "options": ["En la taquilla", "En el andén", "En el vagón", "En la puerta"], "correct_answer": "En la taquilla", "explanation": "'La taquilla' (ou 'la ventanilla') = Le guichet / la billetterie.", "xp": 10},
                            {"id": 530, "type": "fill_in_the_blank", "question": "Complétez : Compro el billete en la máquina ___ (automatique).", "options": None, "correct_answer": "automática", "explanation": "'Máquina automática' = Distributeur automatique de billets.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_vias_urbanas_1",
                        "title": "Voies urbaines et voirie",
                        "questions": [
                            {"id": 531, "type": "multiple_choice", "question": "Comment dit-on 'La rue' en espagnol ?", "options": ["La calle", "La avenida", "El paseo", "El puente"], "correct_answer": "La calle", "explanation": "'La calle' = La rue.", "xp": 10},
                            {"id": 532, "type": "fill_in_the_blank", "question": "Complétez : Una calle muy ancha y con árboles es una ___ (avenue).", "options": None, "correct_answer": "avenida", "explanation": "'La avenida' = L'avenue.", "xp": 10},
                            {"id": 533, "type": "multiple_choice", "question": "Que signifie 'El paso de peatones' ?", "options": ["Le passage piéton", "Le trottoir", "Le feu tricolore", "Le rond-point"], "correct_answer": "Le passage piéton", "explanation": "'El paso de peatones' (ou 'paso de cebra') = Le passage piéton.", "xp": 10},
                            {"id": 534, "type": "multiple_choice", "question": "Comment dit-on 'Le trottoir' ?", "options": ["La acera", "La calzada", "El carril", "La esquina"], "correct_answer": "La acera", "explanation": "'La acera' = Le trottoir.", "xp": 10},
                            {"id": 535, "type": "fill_in_the_blank", "question": "Complétez : Quedamos en la ___ de la calle (coin / angle).", "options": None, "correct_answer": "esquina", "explanation": "'La esquina' = Le coin / L'angle de rue.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_senales_transito_1",
                        "title": "Signalisation et carrefours",
                        "questions": [
                            {"id": 536, "type": "multiple_choice", "question": "Comment dit-on 'Le feu rouge / feu de circulation' ?", "options": ["El semáforo", "La señal", "El cruce", "La rotonda"], "correct_answer": "El semáforo", "explanation": "'El semáforo' = Le feu de signalisation / feu tricolore.", "xp": 10},
                            {"id": 537, "type": "fill_in_the_blank", "question": "Complétez : En la ___ toma la tercera salida (rond-point).", "options": None, "correct_answer": "rotonda", "explanation": "'La rotonda' (ou 'la glorieta') = Le rond-point / giratoire.", "xp": 10},
                            {"id": 538, "type": "multiple_choice", "question": "Que signifie 'El cruce' ?", "options": ["Le carrefour / L'intersection", "Le pont", "Le tunnel", "Le péage"], "correct_answer": "Le carrefour / L'intersection", "explanation": "'El cruce' = Le croisement / Le carrefour.", "xp": 10},
                            {"id": 539, "type": "multiple_choice", "question": "Comment dit-on 'Le pont' ?", "options": ["El puente", "El puerto", "El paseo", "El parque"], "correct_answer": "El puente", "explanation": "'El puente' = Le pont.", "xp": 10},
                            {"id": 540, "type": "fill_in_the_blank", "question": "Complétez : El coche se detiene en el semáforo en ___ (rouge).", "options": None, "correct_answer": "rojo", "explanation": "'Semáforo en rojo' = Feu rouge.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_orientacion_direcciones_1",
                        "title": "Lexique de l'orientation spatiale",
                        "questions": [
                            {"id": 541, "type": "multiple_choice", "question": "Comment dit-on 'À gauche' ?", "options": ["A la izquierda", "A la derecha", "Todo recto", "Al final"], "correct_answer": "A la izquierda", "explanation": "'A la izquierda' = À gauche.", "xp": 10},
                            {"id": 542, "type": "fill_in_the_blank", "question": "Complétez : Gira a la ___ en el banco (droite).", "options": None, "correct_answer": "derecha", "explanation": "'A la derecha' = À droite.", "xp": 10},
                            {"id": 543, "type": "multiple_choice", "question": "Que signifie 'Todo recto' ?", "options": ["Tout droit", "À gauche", "Au fond", "En arrière"], "correct_answer": "Tout droit", "explanation": "'Todo recto' (ou 'todo derecho') = Tout droit.", "xp": 10},
                            {"id": 544, "type": "multiple_choice", "question": "Comment dit-on 'Au bout / Au fond de la rue' ?", "options": ["Al final de la calle", "Al principio de la calle", "Cerca de la calle", "Detrás de la calle"], "correct_answer": "Al final de la calle", "explanation": "'Al final de...' = Au bout de... / À l'extrémité.", "xp": 10},
                            {"id": 545, "type": "fill_in_the_blank", "question": "Complétez : El museo está al ___ de la avenida (début / commencement).", "options": None, "correct_answer": "principio", "explanation": "'Al principio de...' = Au début de...", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_planos_mapas_1",
                        "title": "Cartes, repères et déplacements",
                        "questions": [
                            {"id": 546, "type": "multiple_choice", "question": "Comment dit-on 'Le plan de la ville' ?", "options": ["El plano de la ciudad", "El libro de la ciudad", "La foto de la ciudad", "El billete de la ciudad"], "correct_answer": "El plano de la ciudad", "explanation": "'El plano' = Le plan (urbain/métro).", "xp": 10},
                            {"id": 547, "type": "fill_in_the_blank", "question": "Complétez : Miro el ___ para no perderme (plan / carte).", "options": None, "correct_answer": "mapa", "explanation": "'El mapa' = La carte géographique / routière.", "xp": 10},
                            {"id": 548, "type": "multiple_choice", "question": "Que signifie 'Estar perdido / perdida' ?", "options": ["Être perdu(e)", "Être en avance", "Être pressé(e)", "Être fatigué(e)"], "correct_answer": "Être perdu(e)", "explanation": "'Estar perdido/a' = Avoir perdu son chemin / être égaré(e).", "xp": 10},
                            {"id": 549, "type": "multiple_choice", "question": "Comment dit-on 'La ligne 3 du métro' ?", "options": ["La línea 3 del metro", "El andén 3 del metro", "La vía 3 del metro", "El tren 3 del metro"], "correct_answer": "La línea 3 del metro", "explanation": "'La línea de metro' = La ligne de métro.", "xp": 10},
                            {"id": 550, "type": "fill_in_the_blank", "question": "Complétez : Hay que hacer un ___ de la línea 1 a la 2 (changement / correspondance).", "options": None, "correct_answer": "transbordo", "explanation": "'El transbordo' (ou 'el cambio de línea') = Le changement / la correspondance.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_cuerpo_cabeza_1",
                        "title": "La tête et le visage",
                        "questions": [
                            {"id": 601, "type": "multiple_choice", "question": "Comment dit-on 'La tête' en espagnol ?", "options": ["La cabeza", "La cara", "El cuello", "La boca"], "correct_answer": "La cabeza", "explanation": "'La cabeza' = La tête.", "xp": 10},
                            {"id": 602, "type": "fill_in_the_blank", "question": "Complétez : Miro con los ___ (yeux).", "options": None, "correct_answer": "ojos", "explanation": "'Los ojos' = Les yeux ('el ojo' au singulier).", "xp": 10},
                            {"id": 603, "type": "multiple_choice", "question": "Que signifie 'La nariz' ?", "options": ["Le nez", "La bouche", "L'oreille", "La gorge"], "correct_answer": "Le nez", "explanation": "'La nariz' = Le nez.", "xp": 10},
                            {"id": 604, "type": "multiple_choice", "question": "Comment dit-on 'La bouche' ?", "options": ["La boca", "La oreja", "La lengua", "El labio"], "correct_answer": "La boca", "explanation": "'La boca' = La bouche.", "xp": 10},
                            {"id": 605, "type": "fill_in_the_blank", "question": "Complétez : Escucho los sonidos con las ___ (oreilles).", "options": None, "correct_answer": "orejas", "explanation": "'Las orejas' (ou 'los oídos' pour l'organe interne de l'ouïe) = Les oreilles.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_cuerpo_tronco_1",
                        "title": "Le cou et le tronc",
                        "questions": [
                            {"id": 606, "type": "multiple_choice", "question": "Comment dit-on 'Le dos' en espagnol ?", "options": ["La espalda", "El pecho", "El estómago", "El cuello"], "correct_answer": "La espalda", "explanation": "'La espalda' = Le dos.", "xp": 10},
                            {"id": 607, "type": "fill_in_the_blank", "question": "Complétez : El collar se lleva en el ___ (cou).", "options": None, "correct_answer": "cuello", "explanation": "'El cuello' = Le cou.", "xp": 10},
                            {"id": 608, "type": "multiple_choice", "question": "Que signifie 'El estómago' ?", "options": ["L'estomac / Le ventre", "Le cœur", "Le dos", "L'épaule"], "correct_answer": "L'estomac / Le ventre", "explanation": "'El estómago' (ou familièrement 'la barriga' / 'la tripa') = L'estomac / Le ventre.", "xp": 10},
                            {"id": 609, "type": "multiple_choice", "question": "Comment dit-on 'La gorge' ?", "options": ["La garganta", "El hombro", "El pecho", "La boca"], "correct_answer": "La garganta", "explanation": "'La garganta' = La gorge.", "xp": 10},
                            {"id": 610, "type": "fill_in_the_blank", "question": "Complétez : Respiro aire limpio en el ___ (poitrine / torse).", "options": None, "correct_answer": "pecho", "explanation": "'El pecho' = La poitrine / Le torse.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_cuerpo_extremidades_1",
                        "title": "Les membres supérieurs (Bras, Mains)",
                        "questions": [
                            {"id": 611, "type": "multiple_choice", "question": "Comment dit-on 'Le bras' en espagnol ?", "options": ["El brazo", "La pierna", "La mano", "El codo"], "correct_answer": "El brazo", "explanation": "'El brazo' = Le bras.", "xp": 10},
                            {"id": 612, "type": "fill_in_the_blank", "question": "Complétez : Escribo con la ___ derecha (main).", "options": None, "correct_answer": "mano", "explanation": "'La mano' (nom féminin bien que terminé en -o) = La main.", "xp": 10},
                            {"id": 613, "type": "multiple_choice", "question": "Que signifie 'Los dedos' ?", "options": ["Les doigts", "Les bras", "Les ongles", "Les poignets"], "correct_answer": "Les doigts", "explanation": "'Los dedos' (de la mano) = Les doigts.", "xp": 10},
                            {"id": 614, "type": "multiple_choice", "question": "Comment dit-on 'L'épaule' ?", "options": ["El hombro", "El codo", "La muñeca", "El brazo"], "correct_answer": "El hombro", "explanation": "'El hombro' = L'épaule.", "xp": 10},
                            {"id": 615, "type": "fill_in_the_blank", "question": "Complétez : La articulación del medio del brazo es el ___ (coude).", "options": None, "correct_answer": "codo", "explanation": "'El codo' = Le coude.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_cuerpo_extremidades_2",
                        "title": "Les membres inférieurs (Jambes, Pieds)",
                        "questions": [
                            {"id": 616, "type": "multiple_choice", "question": "Comment dit-on 'La jambe' en espagnol ?", "options": ["La pierna", "El pie", "La rodilla", "El tobillo"], "correct_answer": "La pierna", "explanation": "'La pierna' = La jambe.", "xp": 10},
                            {"id": 617, "type": "fill_in_the_blank", "question": "Complétez : Me pongo los zapatos en los ___ (pieds).", "options": None, "correct_answer": "pies", "explanation": "'Los pies' (singulier : 'el pie') = Les pieds.", "xp": 10},
                            {"id": 618, "type": "multiple_choice", "question": "Que signifie 'La rodilla' ?", "options": ["Le genou", "La cheville", "Le mollet", "La cuisse"], "correct_answer": "Le genou", "explanation": "'La rodilla' = Le genou.", "xp": 10},
                            {"id": 619, "type": "multiple_choice", "question": "Comment dit-on 'La cheville' ?", "options": ["El tobillo", "El dedo del pie", "El talón", "La cadera"], "correct_answer": "El tobillo", "explanation": "'El tobillo' = La cheville.", "xp": 10},
                            {"id": 620, "type": "fill_in_the_blank", "question": "Complétez : Me duele el ___ derecho al caminar (pied).", "options": None, "correct_answer": "pie", "explanation": "'El pie' = Le pied.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_cuerpo_dientes_pelo",
                        "title": "Dents, cheveux et peau",
                        "questions": [
                            {"id": 621, "type": "multiple_choice", "question": "Comment dit-on 'Les dents' en espagnol ?", "options": ["Los dientes", "Las muelas", "Los labios", "Las encías"], "correct_answer": "Los dientes", "explanation": "'Los dientes' = Les dents.", "xp": 10},
                            {"id": 622, "type": "fill_in_the_blank", "question": "Complétez : El dentista me cura una ___ (dent / molaire).", "options": None, "correct_answer": "muela", "explanation": "'La muela' = La dent molaire.", "xp": 10},
                            {"id": 623, "type": "multiple_choice", "question": "Que signifie 'El pelo' (ou 'el cabello') ?", "options": ["Les cheveux / Les poils", "La peau", "Le front", "Le menton"], "correct_answer": "Les cheveux / Les poils", "explanation": "'El pelo' = Les cheveux / Le pelage.", "xp": 10},
                            {"id": 624, "type": "multiple_choice", "question": "Comment dit-on 'La peau' ?", "options": ["La piel", "El cuerpo", "La cara", "El hueso"], "correct_answer": "La piel", "explanation": "'La piel' = La peau.", "xp": 10},
                            {"id": 625, "type": "fill_in_the_blank", "question": "Complétez : Me lavo los ___ después de cada comida (dents).", "options": None, "correct_answer": "dientes", "explanation": "'Los dientes' = Les dents.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_sintomas_enfermedades_1",
                        "title": "Symptômes et maux courants",
                        "questions": [
                            {"id": 626, "type": "multiple_choice", "question": "Comment dit-on 'La fièvre' en espagnol ?", "options": ["La fiebre", "La tos", "La gripe", "El catarro"], "correct_answer": "La fiebre", "explanation": "'La fiebre' = La fièvre.", "xp": 10},
                            {"id": 627, "type": "fill_in_the_blank", "question": "Complétez : No puedo hablar bien porque tengo mucha ___ (toux).", "options": None, "correct_answer": "tos", "explanation": "'La tos' = La toux.", "xp": 10},
                            {"id": 628, "type": "multiple_choice", "question": "Que signifie 'Estar resfriado / resfriada' ?", "options": ["Être enrhumé(e)", "Avoir faim", "Avoir chaud", "Être blessé(e)"], "correct_answer": "Être enrhumé(e)", "explanation": "'Estar resfriado/a' (ou 'estar acatarrado/a') = Être enrhumé(e).", "xp": 10},
                            {"id": 629, "type": "multiple_choice", "question": "Comment dit-on 'La grippe' ?", "options": ["La gripe", "El resfriado", "El dolor", "La alergia"], "correct_answer": "La gripe", "explanation": "'La gripe' = La grippe.", "xp": 10},
                            {"id": 630, "type": "fill_in_the_blank", "question": "Complétez : En primavera sufro de ___ al polen (allergie).", "options": None, "correct_answer": "alergia", "explanation": "'La alergia' = L'allergie.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_estados_salud_1",
                        "title": "États physiques et fatigue",
                        "questions": [
                            {"id": 631, "type": "multiple_choice", "question": "Comment dit-on 'Être malade' ?", "options": ["Estar enfermo / enferma", "Estar cansado / cansada", "Estar sano / sana", "Estar triste"], "correct_answer": "Estar enfermo / enferma", "explanation": "'Estar enfermo/a' = Être malade.", "xp": 10},
                            {"id": 632, "type": "fill_in_the_blank", "question": "Complétez : He trabajado doce horas, estoy muy ___ (fatigué - masculin).", "options": None, "correct_answer": "cansado", "explanation": "'Cansado' = Fatigué.", "xp": 10},
                            {"id": 633, "type": "multiple_choice", "question": "Que signifie 'Estar mareado / mareada' ?", "options": ["Avoir la tête qui tourne / le vertige / être nauséeux", "Avoir froid", "Avoir soif", "Être en forme"], "correct_answer": "Avoir la tête qui tourne / le vertige / être nauséeux", "explanation": "'Estar mareado/a' = Avoir le vertige, le mal des transports ou des nausées.", "xp": 10},
                            {"id": 634, "type": "multiple_choice", "question": "Le contraire de 'enfermo' (malade) est :", "options": ["sano", "débil", "grave", "pálido"], "correct_answer": "sano", "explanation": "'Sano' = Sain / En bonne santé.", "xp": 10},
                            {"id": 635, "type": "fill_in_the_blank", "question": "Complétez : Hoy no puedo ir al trabajo porque me siento ___ (mal).", "options": None, "correct_answer": "mal", "explanation": "'Sentirse mal' = Se sentir mal / Ne pas être bien.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_medicamentos_farmacia_1",
                        "title": "Médicaments et produits de pharmacie",
                        "questions": [
                            {"id": 636, "type": "multiple_choice", "question": "Comment dit-on 'Un comprimé / une pilule' ?", "options": ["Una pastilla", "Un jarabe", "Una tirita", "Una venda"], "correct_answer": "Una pastilla", "explanation": "'Una pastilla' (ou 'un comprimido') = Une pilule / Un comprimé.", "xp": 10},
                            {"id": 637, "type": "fill_in_the_blank", "question": "Complétez : Para la tos el médico me receta un ___ (sirop).", "options": None, "correct_answer": "jarabe", "explanation": "'El jarabe' = Le sirop.", "xp": 10},
                            {"id": 638, "type": "multiple_choice", "question": "Que signifie 'Una tirita' en Espagne ?", "options": ["Un pansement adhésif", "Une bande", "Une seringue", "Un thermomètre"], "correct_answer": "Un pansement adhésif", "explanation": "'Una tirita' = Un pansement (type sparadrap).", "xp": 10},
                            {"id": 639, "type": "multiple_choice", "question": "Comment dit-on 'Une ordonnance médicale' ?", "options": ["Una receta médica", "Una factura médica", "Una carta médica", "Una tarjeta sanitaria"], "correct_answer": "Una receta médica", "explanation": "'La receta médica' = L'ordonnance du médecin.", "xp": 10},
                            {"id": 640, "type": "fill_in_the_blank", "question": "Complétez : Mido mi temperatura corporal con un ___ (thermomètre).", "options": None, "correct_answer": "termómetro", "explanation": "'El termómetro' = Le thermomètre.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_centros_sanitarios_1",
                        "title": "Lieux et professionnels de santé",
                        "questions": [
                            {"id": 641, "type": "multiple_choice", "question": "Comment s'appelle le dispensaire / centre de santé de quartier en Espagne ?", "options": ["El centro de salud", "El centro cívico", "El ayuntamiento", "El polideportivo"], "correct_answer": "El centro de santé", "explanation": "'El centro de salud' (ou 'ambulatorio') = Le centre médical de proximité.", "xp": 10},
                            {"id": 642, "type": "fill_in_the_blank", "question": "Complétez : En caso de accidente grave vamos a ___ (urgences).", "options": None, "correct_answer": "urgencias", "explanation": "'Urgencias' = Les urgences hospitalières.", "xp": 10},
                            {"id": 643, "type": "multiple_choice", "question": "Que signifie 'El farmacéutico / La farmacéutica' ?", "options": ["Le pharmacien / La pharmacienne", "L'infirmier / L'infirmière", "Le chirurgien", "Le dentiste"], "correct_answer": "Le pharmacien / La pharmacienne", "explanation": "'El/la farmacéutico/a' = Le/la pharmacien(ne).", "xp": 10},
                            {"id": 644, "type": "multiple_choice", "question": "Comment dit-on 'Le médecin de famille / généraliste' ?", "options": ["El médico de cabecera", "El médico de guardia", "El enfermero jefe", "El especialista"], "correct_answer": "El médico de cabecera", "explanation": "'El médico de cabecera' = Le médecin de famille / médecin traitant.", "xp": 10},
                            {"id": 645, "type": "fill_in_the_blank", "question": "Complétez : Tengo una ___ con el doctor a las cuatro (rendez-vous).", "options": None, "correct_answer": "cita", "explanation": "'Tener cita' = Avoir un rendez-vous (médical).", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_remedios_cuidados_1",
                        "title": "Conseils et remèdes simples",
                        "questions": [
                            {"id": 646, "type": "multiple_choice", "question": "Comment dit-on 'Se reposer' en espagnol ?", "options": ["Descansar", "Correr", "Trabajar", "Comer"], "correct_answer": "Descansar", "explanation": "'Descansar' = Se reposer.", "xp": 10},
                            {"id": 647, "type": "fill_in_the_blank", "question": "Complétez : Cuando estás enfermo debes guardar ___ (repos au lit / garder le lit).", "options": None, "correct_answer": "cama", "explanation": "'Guardar cama' = Garder le lit / rester couché.", "xp": 10},
                            {"id": 648, "type": "multiple_choice", "question": "Que signifie 'Tomar una infusión de manzanilla' ?", "options": ["Boire une tisane de camomille", "Prendre un café", "Manger des fruits", "Prendre une douche"], "correct_answer": "Boire une tisane de camomille", "explanation": "'La manzanilla' = La camomille (remède traditionnel pour l'estomac).", "xp": 10},
                            {"id": 649, "type": "multiple_choice", "question": "Comment dit-on 'Mettre de la glace' ?", "options": ["Poner hielo", "Poner fuego", "Poner agua caliente", "Poner sal"], "correct_answer": "Poner hielo", "explanation": "'El hielo' = La glace.", "xp": 10},
                            {"id": 650, "type": "fill_in_the_blank", "question": "Complétez : Es importante ___ mucha agua durante el día (boire).", "options": None, "correct_answer": "beber", "explanation": "'Beber' = Boire.", "xp": 10}
                        ]
                    }

                ]
            },
            "conjugaison": {
                "title": "Conjugaison & Grammaire",
                "exercises": [
                    {
                        "id": "a1_conj_ser_1",
                        "title": "Le verbe SER (Identité & Nationalité)",
                        "questions": [
                            {"id": 51, "type": "fill_in_the_blank", "question": "Yo ___ (ser) español.", "options": None, "correct_answer": "soy", "explanation": "Yo soy.", "xp": 15},
                            {"id": 52, "type": "multiple_choice", "question": "¿De dónde ___ tú?", "options": ["eres", "es", "somos", "son"], "correct_answer": "eres", "explanation": "Tú eres.", "xp": 15},
                            {"id": 53, "type": "fill_in_the_blank", "question": "Ella ___ (ser) médica.", "options": None, "correct_answer": "es", "explanation": "Él/Ella/Usted es.", "xp": 15},
                            {"id": 54, "type": "multiple_choice", "question": "Nosotros ___ de Madrid.", "options": ["somos", "sois", "son", "somos"], "correct_answer": "somos", "explanation": "Nosotros somos.", "xp": 15},
                            {"id": 55, "type": "fill_in_the_blank", "question": "Ellos ___ (ser) profesores.", "options": None, "correct_answer": "son", "explanation": "Ellos/Ellas/Ustedes son.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_llamarse_1",
                        "title": "Le verbe pronominal LLAMARSE",
                        "questions": [
                            {"id": 56, "type": "fill_in_the_blank", "question": "Yo me ___ (llamarse) Lucía.", "options": None, "correct_answer": "llamo", "explanation": "Yo me llamo.", "xp": 15},
                            {"id": 57, "type": "multiple_choice", "question": "¿Cómo te ___ tú?", "options": ["llamas", "llama", "llamo", "llamáis"], "correct_answer": "llamas", "explanation": "Tú te llamas.", "xp": 15},
                            {"id": 58, "type": "fill_in_the_blank", "question": "Él se ___ (llamarse) Mateo.", "options": None, "correct_answer": "llama", "explanation": "Él se llama.", "xp": 15},
                            {"id": 59, "type": "multiple_choice", "question": "Mis hermanos se ___ David y Pablo.", "options": ["llaman", "llamamos", "llama", "llamas"], "correct_answer": "llaman", "explanation": "Ellos se llaman.", "xp": 15},
                            {"id": 60, "type": "fill_in_the_blank", "question": "Nosotros nos ___ (llamarse) Martínez de apellido.", "options": None, "correct_answer": "llamamos", "explanation": "Nosotros nos llamamos.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_tener_1",
                        "title": "Le verbe TENER (Âge et Possession)",
                        "questions": [
                            {"id": 61, "type": "fill_in_the_blank", "question": "Yo ___ (tener) 20 años.", "options": None, "correct_answer": "tengo", "explanation": "Yo tengo (irrégulier).", "xp": 15},
                            {"id": 62, "type": "multiple_choice", "question": "¿Cuántos años ___ tú?", "options": ["tienes", "tiene", "tenemos", "tenéis"], "correct_answer": "tienes", "explanation": "Tú tienes.", "xp": 15},
                            {"id": 63, "type": "fill_in_the_blank", "question": "Usted ___ (tener) pasaporte.", "options": None, "correct_answer": "tiene", "explanation": "Usted tiene.", "xp": 15},
                            {"id": 64, "type": "multiple_choice", "question": "Nosotros ___ una clase de español.", "options": ["tenemos", "tienen", "tenéis", "tengo"], "correct_answer": "tenemos", "explanation": "Nosotros tenemos.", "xp": 15},
                            {"id": 65, "type": "fill_in_the_blank", "question": "Ellos ___ (tener) 18 años.", "options": None, "correct_answer": "tienen", "explanation": "Ellos tienen.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_vivir_1",
                        "title": "Le verbe VIVIR (Lieu de résidence)",
                        "questions": [
                            {"id": 66, "type": "fill_in_the_blank", "question": "Yo ___ (vivir) en Barcelona.", "options": None, "correct_answer": "vivo", "explanation": "Yo vivo.", "xp": 15},
                            {"id": 67, "type": "multiple_choice", "question": "¿Dónde ___ tú?", "options": ["vives", "vive", "vivo", "vivís"], "correct_answer": "vives", "explanation": "Tú vives.", "xp": 15},
                            {"id": 68, "type": "fill_in_the_blank", "question": "¿Dónde ___ (vivir) usted?", "options": None, "correct_answer": "vive", "explanation": "Usted vive.", "xp": 15},
                            {"id": 69, "type": "multiple_choice", "question": "Nosotros ___ en Francia.", "options": ["vivimos", "viven", "vivo", "vivís"], "correct_answer": "vivimos", "explanation": "Nosotros vivimos.", "xp": 15},
                            {"id": 70, "type": "fill_in_the_blank", "question": "Ellas ___ (vivir) en Valencia.", "options": None, "correct_answer": "viven", "explanation": "Ellas viven.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_tu_usted_1",
                        "title": "Formel (Usted) vs Informel (Tú)",
                        "questions": [
                            {"id": 71, "type": "multiple_choice", "question": "Pour vouvoyer une personne âgée poliment, on emploie :", "options": ["Usted", "Tú", "Vosotros", "Ellos"], "correct_answer": "Usted", "explanation": "'Usted' marque le vouvoiement formel au singulier.", "xp": 15},
                            {"id": 72, "type": "fill_in_the_blank", "question": "Complétez (forme formelle) : ¿Cómo se ___ usted? (llamarse)", "options": None, "correct_answer": "llama", "explanation": "Usted se conjugue à la 3e personne du singulier : se llama.", "xp": 15},
                            {"id": 73, "type": "multiple_choice", "question": "Quelle salutation est la plus formelle ?", "options": ["Buenos días, señor López", "¡Hola, qué tal!", "¡Ey, buenas!", "¡Hola, tío!"], "correct_answer": "Buenos días, señor López", "explanation": "'Buenos días' avec le titre de civilité est formel.", "xp": 15},
                            {"id": 74, "type": "multiple_choice", "question": "Complétez avec la forme familière : '¿De dónde ___ tú?'", "options": ["eres", "es", "sea", "somos"], "correct_answer": "eres", "explanation": "'Eres' est la 2e personne du singulier (tú).", "xp": 15},
                            {"id": 75, "type": "fill_in_the_blank", "question": "Complétez (forme formelle) : ¿De dónde ___ usted? (verbe ser)", "options": None, "correct_answer": "es", "explanation": "'Usted es' pour la provenance formelle.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_trabajar_dedicarse",
                        "title": "Parler de son activité (Trabajar / Dedicarse)",
                        "questions": [
                            {"id": 76, "type": "multiple_choice", "question": "¿A qué te ___? (À quoi te consacres-tu / Quel est ton métier ?)", "options": ["dedicas", "dedica", "dedico", "dedicamos"], "correct_answer": "dedicas", "explanation": "'¿A qué te dedicas?' avec 'tú'.", "xp": 15},
                            {"id": 77, "type": "fill_in_the_blank", "question": "Yo ___ (trabajar) en una oficina.", "options": None, "correct_answer": "trabajo", "explanation": "Yo trabajo.", "xp": 15},
                            {"id": 78, "type": "multiple_choice", "question": "Elle travaille à l'école -> Ella ___ en la escuela.", "options": ["trabaja", "trabajas", "trabajan", "trabajo"], "correct_answer": "trabaja", "explanation": "Ella trabaja.", "xp": 15},
                            {"id": 79, "type": "fill_in_the_blank", "question": "Complétez (forme formelle) : ¿A qué se ___ usted? (dedicarse)", "options": None, "correct_answer": "dedica", "explanation": "Usted se dedica.", "xp": 15},
                            {"id": 80, "type": "multiple_choice", "question": "¿Dónde ___ vosotros? (trabajar)", "options": ["trabajáis", "trabajan", "trabajamos", "trabajas"], "correct_answer": "trabajáis", "explanation": "Vosotros trabajáis.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ser_origen",
                        "title": "Exprimer l'origine (Ser de + Pays)",
                        "questions": [
                            {"id": 81, "type": "fill_in_the_blank", "question": "Yo soy ___ Colombia (préposition).", "options": None, "correct_answer": "de", "explanation": "On utilise la préposition 'de' pour exprimer l'origine : 'ser de'.", "xp": 15},
                            {"id": 82, "type": "multiple_choice", "question": "Comment dire 'Nous venons d'Argentine' ?", "options": ["Somos de Argentina", "Estamos de Argentina", "Tenemos Argentina", "Vamos de Argentina"], "correct_answer": "Somos de Argentina", "explanation": "'Ser de' exprime l'origine.", "xp": 15},
                            {"id": 83, "type": "fill_in_the_blank", "question": "¿Vosotros ___ de Italia? (verbe ser)", "options": None, "correct_answer": "sois", "explanation": "Vosotros sois.", "xp": 15},
                            {"id": 84, "type": "multiple_choice", "question": "¿Ellos son de Perú? - Sí, ellos ___ peruanos.", "options": ["son", "están", "tienen", "es"], "correct_answer": "son", "explanation": "Nationalité = verbe ser (son).", "xp": 15},
                            {"id": 85, "type": "fill_in_the_blank", "question": "María y yo ___ (ser) de Sevilla.", "options": None, "correct_answer": "somos", "explanation": "María y yo = nosotros somos.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_interrogativos_1",
                        "title": "Mots interrogatifs d'identité (Cómo, Cuál, Dónde, Quién)",
                        "questions": [
                            {"id": 86, "type": "multiple_choice", "question": "¿___ te llamas?", "options": ["Cómo", "Dónde", "Quién", "Cuánto"], "correct_answer": "Cómo", "explanation": "'¿Cómo te llamas?' = Comment t'appelles-tu ?", "xp": 15},
                            {"id": 87, "type": "fill_in_the_blank", "question": "¿___ eres? (D'où es-tu ?)", "options": None, "correct_answer": "De dónde", "explanation": "'De dónde' = D'où.", "xp": 15},
                            {"id": 88, "type": "multiple_choice", "question": "¿___ es tu número de teléfono?", "options": ["Cuál", "Qué", "Quién", "Dónde"], "correct_answer": "Cuál", "explanation": "On utilise 'Cuál' suivi de 'es' pour demander une information précise.", "xp": 15},
                            {"id": 89, "type": "multiple_choice", "question": "¿___ es él? - Es el profesor nuevo.", "options": ["Quién", "Cómo", "Dónde", "Cuál"], "correct_answer": "Quién", "explanation": "'Quién' = Qui.", "xp": 15},
                            {"id": 90, "type": "fill_in_the_blank", "question": "¿___ años tienes? (Combien)", "options": None, "correct_answer": "Cuántos", "explanation": "'Cuántos' s'accorde avec le nom pluriel 'años'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_dialogo_recap_1",
                        "title": "Dialogue d'introduction informel",
                        "questions": [
                            {"id": 91, "type": "multiple_choice", "question": "- ¡Hola! ¿Cómo estás? - ___", "options": ["¡Muy bien, gracias! ¿Y tú?", "Tengo 20 años", "Soy de París", "Me llamo Juan"], "correct_answer": "¡Muy bien, gracias! ¿Y tú?", "explanation": "Réponse adaptée à une salutation informelle.", "xp": 15},
                            {"id": 92, "type": "fill_in_the_blank", "question": "Complétez : - ¿De dónde eres? - Yo ___ de Bogotá.", "options": None, "correct_answer": "soy", "explanation": "Yo soy de...", "xp": 15},
                            {"id": 93, "type": "multiple_choice", "question": "- ¿Eres estudiante? - No, yo ___ arquitecto.", "options": ["soy", "estoy", "tengo", "hago"], "correct_answer": "soy", "explanation": "On emploie 'ser' sans article devant la profession.", "xp": 15},
                            {"id": 94, "type": "multiple_choice", "question": "- ¡Mucho gusto! - ___", "options": ["Igualmente", "Por favor", "Hasta luego", "Buenos días"], "correct_answer": "Igualmente", "explanation": "'Igualmente' signifie 'De même / Partagé'.", "xp": 15},
                            {"id": 95, "type": "fill_in_the_blank", "question": "Complétez : - Adiós. - ¡___ pronto! (À bientôt)", "options": None, "correct_answer": "Hasta", "explanation": "'Hasta pronto' = À bientôt.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_dialogo_recap_2",
                        "title": "Dialogue d'introduction formel",
                        "questions": [
                            {"id": 96, "type": "multiple_choice", "question": "- Buenos días, señorita Vega. ¿Cómo ___ usted?", "options": ["está", "estás", "estoy", "están"], "correct_answer": "está", "explanation": "3e personne avec 'usted' : ¿Cómo está usted?", "xp": 15},
                            {"id": 97, "type": "fill_in_the_blank", "question": "Complétez : - ¿Cuál es ___ profesión, señor? (votre - formel)", "options": None, "correct_answer": "su", "explanation": "'Su' est l'adjectif possessif pour 'usted'.", "xp": 15},
                            {"id": 98, "type": "multiple_choice", "question": "- Soy el director. Le ___ a mi colega María.", "options": ["presento", "presentas", "presentan", "presente"], "correct_answer": "presento", "explanation": "'Le presento a...' = Je vous présente...", "xp": 15},
                            {"id": 99, "type": "multiple_choice", "question": "- Encantada de conocerle. - ___", "options": ["El gusto es mío", "Hasta nunca", "Por nada", "Bienvenido"], "correct_answer": "El gusto es mío", "explanation": "'El gusto es mío' = Tout le plaisir est pour moi.", "xp": 15},
                            {"id": 100, "type": "fill_in_the_blank", "question": "Complétez : ¡Que tenga un buen ___! (Bonne journée - formel)", "options": None, "correct_answer": "día", "explanation": "'Que tenga un buen día' = Passez une bonne journée.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_estar_localizacion_1",
                        "title": "Le verbe ESTAR pour situer dans l'espace",
                        "questions": [
                            {"id": 251, "type": "fill_in_the_blank", "question": "El sofá ___ (estar) en el salón.", "options": None, "correct_answer": "está", "explanation": "3e personne du singulier : 'está'.", "xp": 15},
                            {"id": 252, "type": "multiple_choice", "question": "Mis llaves ___ encima de la mesa.", "options": ["están", "está", "son", "hay"], "correct_answer": "están", "explanation": "Sujet pluriel : 'Mis llaves están'.", "xp": 15},
                            {"id": 253, "type": "fill_in_the_blank", "question": "Yo ___ (estar) en mi habitación.", "options": None, "correct_answer": "estoy", "explanation": "1ère personne : 'Yo estoy'.", "xp": 15},
                            {"id": 254, "type": "multiple_choice", "question": "¿Dónde ___ vosotros ahora?", "options": ["estáis", "están", "estamos", "sois"], "correct_answer": "estáis", "explanation": "Vosotros estáis.", "xp": 15},
                            {"id": 255, "type": "fill_in_the_blank", "question": "Nosotros ___ (estar) cerca del parque.", "options": None, "correct_answer": "estamos", "explanation": "Nosotros estamos.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_preposiciones_espacio_1",
                        "title": "Prépositions d'espace : Encima, Debajo, Delante, Detrás",
                        "questions": [
                            {"id": 256, "type": "multiple_choice", "question": "Comment dit-on 'devant la maison' ?", "options": ["delante de la casa", "detrás de la casa", "debajo de la casa", "encima de la casa"], "correct_answer": "delante de la casa", "explanation": "'Delante de' = Devant.", "xp": 15},
                            {"id": 257, "type": "fill_in_the_blank", "question": "Complétez : El perro duerme ___ de la mesa (sous).", "options": None, "correct_answer": "debajo", "explanation": "'Debajo de' = Sous / Au-dessous de.", "xp": 15},
                            {"id": 258, "type": "multiple_choice", "question": "Que signifie 'detrás del edificio' ?", "options": ["Derrière le bâtiment", "Devant le bâtiment", "À côté du bâtiment", "Dans le bâtiment"], "correct_answer": "Derrière le bâtiment", "explanation": "'Detrás de' = Derrière.", "xp": 15},
                            {"id": 259, "type": "multiple_choice", "question": "Le livre est posé 'sur' la table -> El libro está ___ la mesa.", "options": ["encima de", "debajo de", "detrás de", "lejos de"], "correct_answer": "encima de", "explanation": "'Encima de' (ou 'sobre') = Sur / Au-dessus de.", "xp": 15},
                            {"id": 260, "type": "fill_in_the_blank", "question": "Complétez : La farmacia está ___ de la tienda (en face).", "options": None, "correct_answer": "enfrente", "explanation": "'Enfrente de' = En face de.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_preposiciones_espacio_2",
                        "title": "Prépositions d'espace : Al lado, Entre, Cerca, Lejos",
                        "questions": [
                            {"id": 261, "type": "multiple_choice", "question": "Comment dit-on 'à côté du supermarché' ?", "options": ["al lado del supermercado", "lejos del supermercado", "dentro del supermercado", "detrás del supermercado"], "correct_answer": "al lado del supermercado", "explanation": "'Al lado de' = À côté de.", "xp": 15},
                            {"id": 262, "type": "fill_in_the_blank", "question": "Complétez : La mesa está ___ las dos sillas (entre).", "options": None, "correct_answer": "entre", "explanation": "'Entre' = Entre.", "xp": 15},
                            {"id": 263, "type": "multiple_choice", "question": "Que signifie 'Mi casa está muy cerca' ?", "options": ["Ma maison est très près", "Ma maison est très loin", "Ma maison est grande", "Ma maison est en face"], "correct_answer": "Ma maison est très près", "explanation": "'Cerca de' = Près de.", "xp": 15},
                            {"id": 264, "type": "multiple_choice", "question": "Le contraire de 'cerca de' (près de) est :", "options": ["lejos de", "al lado de", "delante de", "dentro de"], "correct_answer": "lejos de", "explanation": "'Lejos de' = Loin de.", "xp": 15},
                            {"id": 265, "type": "fill_in_the_blank", "question": "Complétez : Las llaves están ___ del bolso (à l'intérieur / dedans).", "options": None, "correct_answer": "dentro", "explanation": "'Dentro de' = À l'intérieur de / Dans.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_direcciones_orientacion",
                        "title": "Donner et suivre des indications d'orientation",
                        "questions": [
                            {"id": 266, "type": "multiple_choice", "question": "Comment dit-on 'tourner à droite' ?", "options": ["girar a la derecha", "girar a la izquierda", "seguir todo recto", "cruzar la calle"], "correct_answer": "girar a la derecha", "explanation": "'A la derecha' = À droite.", "xp": 15},
                            {"id": 267, "type": "fill_in_the_blank", "question": "Complétez : Para ir al museo, gira a la ___ (gauche).", "options": None, "correct_answer": "izquierda", "explanation": "'A la izquierda' = À gauche.", "xp": 15},
                            {"id": 268, "type": "multiple_choice", "question": "Que signifie 'Seguir todo recto' ?", "options": ["Continuer tout droit", "Faire demi-tour", "Traverser le parc", "S'arrêter au feu"], "correct_answer": "Continuer tout droit", "explanation": "'Todo recto' = Tout droit.", "xp": 15},
                            {"id": 269, "type": "multiple_choice", "question": "Comment dit-on 'traverser la rue' ?", "options": ["Cruzar la calle", "Bajar la calle", "Subir la calle", "Parar la calle"], "correct_answer": "Cruzar la calle", "explanation": "'Cruzar' = Traverser.", "xp": 15},
                            {"id": 270, "type": "fill_in_the_blank", "question": "Complétez : Toma la segunda calle a la ___ (droite).", "options": None, "correct_answer": "derecha", "explanation": "'A la derecha' = À droite.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_hay_vs_esta_1",
                        "title": "HAY (existence) vs ESTÁ/ESTÁN (localisation)",
                        "questions": [
                            {"id": 271, "type": "multiple_choice", "question": "Complétez : En mi barrio ___ un parque muy bonito.", "options": ["hay", "está", "es", "son"], "correct_answer": "hay", "explanation": "On emploie 'hay' avec un article indéfini pour exprimer l'existence.", "xp": 15},
                            {"id": 272, "type": "fill_in_the_blank", "question": "Complétez : El parque ___ cerca del metro (verbe estar).", "options": None, "correct_answer": "está", "explanation": "On utilise 'estar' pour situer un élément spécifique et déterminé.", "xp": 15},
                            {"id": 273, "type": "multiple_choice", "question": "Complétez : En la cocina ___ muchas sillas.", "options": ["hay", "están", "son", "tienen"], "correct_answer": "hay", "explanation": "'Hay' s'utilise avec les quantificateurs indéfinis (muchas, pocas, etc.).", "xp": 15},
                            {"id": 274, "type": "multiple_choice", "question": "¿Dónde ___ los cuartos de baño?", "options": ["están", "hay", "es", "queda"], "correct_answer": "están", "explanation": "'Están' localise un sujet déterminé pluriel.", "xp": 15},
                            {"id": 275, "type": "fill_in_the_blank", "question": "Complétez : ¿___ una farmacia por aquí? (Il y a)", "options": None, "correct_answer": "Hay", "explanation": "'Hay' = Il y a.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_haber_cuantificadores",
                        "title": "HAY avec les articles indéfinis et quantités",
                        "questions": [
                            {"id": 276, "type": "multiple_choice", "question": "Quelle phrase est correcte ?", "options": ["En mi piso hay tres habitaciones", "En mi piso está tres habitaciones", "En mi piso son tres habitaciones", "En mi piso hay las habitaciones"], "correct_answer": "En mi piso hay tres habitaciones", "explanation": "'Hay' s'associe aux nombres pour désigner des quantités.", "xp": 15},
                            {"id": 277, "type": "fill_in_the_blank", "question": "Complétez : No ___ ningún cine en este barrio.", "options": None, "correct_answer": "hay", "explanation": "'No hay ningún...' = Il n'y a aucun...", "xp": 15},
                            {"id": 278, "type": "multiple_choice", "question": "Complétez : En el frigorífico no ___ leche.", "options": ["hay", "está", "es", "tiene"], "correct_answer": "hay", "explanation": "'Hay' s'utilise avec un nom indénombrable sans article.", "xp": 15},
                            {"id": 279, "type": "fill_in_the_blank", "question": "Complétez : En mi calle hay ___ tiendas (beaucoup de).", "options": None, "correct_answer": "muchas", "explanation": "'Muchas' s'accorde au féminin pluriel avec 'tiendas'.", "xp": 15},
                            {"id": 280, "type": "multiple_choice", "question": "Complétez : En el salón ___ una alfombra grande.", "options": ["hay", "está", "son", "es"], "correct_answer": "hay", "explanation": "'Hay una alfombra' (article indéfini).", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_tener_casa",
                        "title": "Le verbe TENER pour décrire un logement",
                        "questions": [
                            {"id": 281, "type": "fill_in_the_blank", "question": "Mi casa ___ (tener) dos plantas.", "options": None, "correct_answer": "tiene", "explanation": "3e personne : 'Mi casa tiene'.", "xp": 15},
                            {"id": 282, "type": "multiple_choice", "question": "Yo ___ un piso luminoso con terraza.", "options": ["tengo", "tiene", "tenemos", "tienen"], "correct_answer": "tengo", "explanation": "Yo tengo.", "xp": 15},
                            {"id": 283, "type": "fill_in_the_blank", "question": "Nosotros ___ (tener) un jardín grande.", "options": None, "correct_answer": "tenemos", "explanation": "Nosotros tenemos.", "xp": 15},
                            {"id": 284, "type": "multiple_choice", "question": "¿Cuántas habitaciones ___ tu casa?", "options": ["tiene", "tienes", "tienen", "tengo"], "correct_answer": "tiene", "explanation": "Le sujet est 'tu casa' (3e personne du singulier).", "xp": 15},
                            {"id": 285, "type": "fill_in_the_blank", "question": "Los dormitorios ___ (tener) armarios empotrados.", "options": None, "correct_answer": "tienen", "explanation": "Sujet pluriel : 'tienen'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_vivir_ubicacion",
                        "title": "Le verbe VIVIR (Quartier et Logement)",
                        "questions": [
                            {"id": 286, "type": "multiple_choice", "question": "Yo ___ en un barrio muy céntrico.", "options": ["vivo", "vives", "vive", "vivimos"], "correct_answer": "vivo", "explanation": "Yo vivo.", "xp": 15},
                            {"id": 287, "type": "fill_in_the_blank", "question": "¿En qué piso ___ tú? (vivir)", "options": None, "correct_answer": "vives", "explanation": "Tú vives.", "xp": 15},
                            {"id": 288, "type": "multiple_choice", "question": "Mis abuelos ___ en una casa de campo.", "options": ["viven", "vive", "vivimos", "vivís"], "correct_answer": "viven", "explanation": "Ellos viven.", "xp": 15},
                            {"id": 289, "type": "fill_in_the_blank", "question": "Nosotros ___ (vivir) en la avenida principal.", "options": None, "correct_answer": "vivimos", "explanation": "Nosotros vivimos.", "xp": 15},
                            {"id": 290, "type": "multiple_choice", "question": "¿Dónde ___ usted, señor Ruiz?", "options": ["vive", "vives", "vivo", "viven"], "correct_answer": "vive", "explanation": "Usted vive.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_dialogo_barrio_1",
                        "title": "Dialogue : Demander son chemin dans le quartier",
                        "questions": [
                            {"id": 291, "type": "multiple_choice", "question": "- Por favor, ¿para ir a la estación? - ___", "options": ["Sigue todo recto y gira a la derecha", "Tengo dos habitaciones", "Vivo en el centro", "El piso es luminoso"], "correct_answer": "Sigue todo recto y gira a la derecha", "explanation": "Réponse adaptée pour guider un itinéraire.", "xp": 15},
                            {"id": 292, "type": "fill_in_the_blank", "question": "Complétez : - ¿___ una farmacia cerca? - Sí, al lado del banco.", "options": None, "correct_answer": "Hay", "explanation": "'¿Hay una farmacia cerca?' pour s'enquérir d'un commerce.", "xp": 15},
                            {"id": 293, "type": "multiple_choice", "question": "- ¿La parada de autobús está lejos? - No, está muy ___.", "options": ["cerca", "lejos", "dentro", "encima"], "correct_answer": "cerca", "explanation": "'Cerca' est le contraire direct de 'lejos'.", "xp": 15},
                            {"id": 294, "type": "fill_in_the_blank", "question": "Complétez : - ¿Dónde está el museo? - Está ___ de la catedral (en face).", "options": None, "correct_answer": "enfrente", "explanation": "'Enfrente de' = En face de.", "xp": 15},
                            {"id": 295, "type": "multiple_choice", "question": "- Muchas gracias por la ayuda. - ___", "options": ["De nada, ¡buen día!", "Mucho gusto", "Hasta ayer", "Por favor"], "correct_answer": "De nada, ¡buen día!", "explanation": "Formule polie de réponse.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_dialogo_casa_recap_2",
                        "title": "Dialogue : Décrire et faire visiter sa maison",
                        "questions": [
                            {"id": 296, "type": "multiple_choice", "question": "- ¿Cómo es tu piso nuevo? - ___", "options": ["Es pequeño pero muy luminoso", "Está encima de la mesa", "Tiene sesenta años", "Gira a la izquierda"], "correct_answer": "Es pequeño pero muy luminoso", "explanation": "Description qualitative globale d'un habitat.", "xp": 15},
                            {"id": 297, "type": "fill_in_the_blank", "question": "Complétez : - ¿Cuántas habitaciones tiene? - ___ tres dormitorios (verbe tener).", "options": None, "correct_answer": "Tiene", "explanation": "3e personne : 'Tiene tres dormitorios'.", "xp": 15},
                            {"id": 298, "type": "multiple_choice", "question": "- ¿Dónde ___ la cocina? - Al final del pasillo.", "options": ["está", "hay", "es", "tiene"], "correct_answer": "está", "explanation": "On emploie 'está' pour la position d'un lieu défini.", "xp": 15},
                            {"id": 299, "type": "fill_in_the_blank", "question": "Complétez : - ¿Hay ascensor en el edificio? - Sí, ___ ascensor.", "options": None, "correct_answer": "hay", "explanation": "Forme d'affirmation : 'hay ascensor'.", "xp": 15},
                            {"id": 300, "type": "multiple_choice", "question": "- ¡Me encanta tu casa! - ¡Muchas gracias, ___!", "options": ["bienvenido a mi casa", "hasta nunca", "lo siento mucho", "por favor"], "correct_answer": "bienvenido a mi casa", "explanation": "'Bienvenido' = Bienvenue.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_gustar_comida_1",
                        "title": "Le verbe GUSTAR (Singulier / Pluriel)",
                        "questions": [
                            {"id": 351, "type": "fill_in_the_blank", "question": "A mí me ___ el pescado (verbe gustar).", "options": None, "correct_answer": "gusta", "explanation": "Sujet singulier (el pescado) -> 'gusta'.", "xp": 15},
                            {"id": 352, "type": "multiple_choice", "question": "A nosotros no nos ___ las verduras.", "options": ["gustan", "gusta", "gustamos", "gustas"], "correct_answer": "gustan", "explanation": "Sujet pluriel (las verduras) -> 'gustan'.", "xp": 15},
                            {"id": 353, "type": "fill_in_the_blank", "question": "¿A ti te ___ las frutas? (gustar)", "options": None, "correct_answer": "gustan", "explanation": "'Las frutas' est au pluriel -> 'gustan'.", "xp": 15},
                            {"id": 354, "type": "multiple_choice", "question": "A Juan le ___ cocinar paella.", "options": ["gusta", "gustan", "guste", "gustó"], "correct_answer": "gusta", "explanation": "Devant un verbe à l'infinitif (cocinar) -> 'gusta' au singulier.", "xp": 15},
                            {"id": 355, "type": "fill_in_the_blank", "question": "A ellos les ___ mucho los postres (gustar).", "options": None, "correct_answer": "gustan", "explanation": "'Los postres' est au pluriel -> 'gustan'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_querer_pedir_1",
                        "title": "Le verbe QUERER pour commander",
                        "questions": [
                            {"id": 356, "type": "fill_in_the_blank", "question": "Yo ___ (querer) una ensalada mixta.", "options": None, "correct_answer": "quiero", "explanation": "Yo quiero (verbe à diphtongue e -> ie).", "xp": 15},
                            {"id": 357, "type": "multiple_choice", "question": "¿Qué ___ vosotros de segundo plato?", "options": ["queréis", "quieren", "queremos", "quieres"], "correct_answer": "queréis", "explanation": "Vosotros queréis (pas de diphtongue).", "xp": 15},
                            {"id": 358, "type": "fill_in_the_blank", "question": "¿Qué ___ tomar usted? (querer)", "options": None, "correct_answer": "quiere", "explanation": "Usted quiere.", "xp": 15},
                            {"id": 359, "type": "multiple_choice", "question": "Nosotros ___ una botella de vino blanco.", "options": ["queremos", "quieren", "queréis", "quiero"], "correct_answer": "queremos", "explanation": "Nosotros queremos.", "xp": 15},
                            {"id": 360, "type": "fill_in_the_blank", "question": "¿Tú ___ postre o café? (querer)", "options": None, "correct_answer": "quieres", "explanation": "Tú quieres.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_poner_tomar_1",
                        "title": "Les verbes PONER et TOMAR pour commander",
                        "questions": [
                            {"id": 361, "type": "multiple_choice", "question": "Au bar, comment demander poliment un café avec 'poner' ?", "options": ["¿Me pone un café, por favor?", "¿Pongo un café?", "¿Pones usted?", "¿Ponen un café?"], "correct_answer": "¿Me pone un café, por favor?", "explanation": "'¿Me pone...?' (3e personne de politesse) est la formule standard au comptoir.", "xp": 15},
                            {"id": 362, "type": "fill_in_the_blank", "question": "Complétez : De primero voy a ___ sopa (prendre / boire / manger).", "options": None, "correct_answer": "tomar", "explanation": "'Tomar' s'utilise pour consommer nourriture ou boisson.", "xp": 15},
                            {"id": 363, "type": "multiple_choice", "question": "¿Qué ___ ustedes para beber?", "options": ["van a tomar", "va a tomar", "vas a tomar", "voy a tomar"], "correct_answer": "van a tomar", "explanation": "Accord avec 'ustedes' (pluriel formel).", "xp": 15},
                            {"id": 364, "type": "fill_in_the_blank", "question": "Complétez : ¿Nos ___ una ración de bravas? (poner - formel)", "options": None, "correct_answer": "pone", "explanation": "'¿Nos pone...?' = Vous nous mettez... ?", "xp": 15},
                            {"id": 365, "type": "multiple_choice", "question": "Yo siempre ___ café solo por las mañanas.", "options": ["tomo", "tomas", "toma", "tomamos"], "correct_answer": "tomo", "explanation": "Yo tomo.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_preferir_comer_beber",
                        "title": "Exprimer ses préférences (Preferir / Comer / Beber)",
                        "questions": [
                            {"id": 366, "type": "multiple_choice", "question": "Yo ___ comer carne que pescado.", "options": ["prefiero", "prefieres", "prefiere", "preferimos"], "correct_answer": "prefiero", "explanation": "Yo prefiero (e -> ie).", "xp": 15},
                            {"id": 367, "type": "fill_in_the_blank", "question": "¿Qué ___ comer hoy? (preferir - tú)", "options": None, "correct_answer": "prefieres", "explanation": "Tú prefieres.", "xp": 15},
                            {"id": 368, "type": "multiple_choice", "question": "Nosotros nunca ___ alcohol durante la semana.", "options": ["bebemos", "beben", "bebes", "bebo"], "correct_answer": "bebemos", "explanation": "Nosotros bebemos.", "xp": 15},
                            {"id": 369, "type": "fill_in_the_blank", "question": "Ellos ___ (comer) en el restaurante del hotel.", "options": None, "correct_answer": "comen", "explanation": "Ellos comen.", "xp": 15},
                            {"id": 370, "type": "multiple_choice", "question": "¿Vosotros qué ___ beber?", "options": ["preferís", "prefieren", "preferimos", "prefieres"], "correct_answer": "preferís", "explanation": "Vosotros preferís.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_precios_costar_valer",
                        "title": "Demander le prix (Costar / Valer / Ser)",
                        "questions": [
                            {"id": 371, "type": "multiple_choice", "question": "Comment demande-t-on le prix d'un kilo de pommes ?", "options": ["¿Cuánto cuesta el kilo de manzanas?", "¿Cómo cuesta el kilo?", "¿Dónde cuesta el kilo?", "¿Qué vale las manzanas?"], "correct_answer": "¿Cuánto cuesta el kilo de manzanas?", "explanation": "Sujet singulier (el kilo) -> '¿Cuánto cuesta...?'", "xp": 15},
                            {"id": 372, "type": "fill_in_the_blank", "question": "Complétez : ¿Cuánto ___ estos tomates? (costar)", "options": None, "correct_answer": "cuestan", "explanation": "Sujet pluriel (estos tomates) -> 'cuestan' (o -> ue).", "xp": 15},
                            {"id": 373, "type": "multiple_choice", "question": "Quelle question permet de demander le montant total ?", "options": ["¿Cuánto es todo?", "¿Quién es todo?", "¿Dónde es todo?", "¿Cuál es todo?"], "correct_answer": "¿Cuánto es todo?", "explanation": "'¿Cuánto es?' = Combien cela fait-il ?", "xp": 15},
                            {"id": 374, "type": "multiple_choice", "question": "La botella de aceite ___ 4 euros.", "options": ["cuesta", "cuestan", "costamos", "costar"], "correct_answer": "cuesta", "explanation": "La botella (singulier) -> cuesta.", "xp": 15},
                            {"id": 375, "type": "fill_in_the_blank", "question": "Complétez : ¿Cuánto ___ las naranjas? (valer - pluriel)", "options": None, "correct_answer": "valen", "explanation": "'Las naranjas valen'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_traer_llevar_camarero",
                        "title": "Interactions avec le serveur (Traer / Llevar)",
                        "questions": [
                            {"id": 376, "type": "multiple_choice", "question": "Comment demander poliment un peu de pain au serveur ?", "options": ["¿Nos trae un poco de pan, por favor?", "¿Llevas pan?", "¿Tienes traído pan?", "¿Es pan por favor?"], "correct_answer": "¿Nos trae un poco de pan, por favor?", "explanation": "'¿Nos trae...?' (verbe traer à la 3e personne) = Pouvez-vous nous apporter... ?", "xp": 15},
                            {"id": 377, "type": "fill_in_the_blank", "question": "Complétez : Camarero, ¿me ___ la cuenta? (traer - formel)", "options": None, "correct_answer": "trae", "explanation": "Usted me trae.", "xp": 15},
                            {"id": 378, "type": "multiple_choice", "question": "Que demande le client qui dit '¿Para llevar o para tomar aquí?' ?", "options": ["À emporter ou sur place ?", "Avec ou sans sucre ?", "Chaud ou froid ?", "Payé ou gratuit ?"], "correct_answer": "À emporter ou sur place ?", "explanation": "'Para llevar' = À emporter, 'para tomar aquí' = Sur place.", "xp": 15},
                            {"id": 379, "type": "multiple_choice", "question": "Complétez la réponse du serveur : 'Ahora mismo se lo ___'.", "options": ["traigo", "llevas", "tomo", "pongo"], "correct_answer": "traigo", "explanation": "'Yo se lo traigo' = Je vous l'apporte tout de suite.", "xp": 15},
                            {"id": 380, "type": "fill_in_the_blank", "question": "Complétez : ¿Nos puede ___ otra botella de agua? (infinitif de traer)", "options": None, "correct_answer": "traer", "explanation": "Après 'puede' on emploie l'infinitif 'traer'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_interrogativos_restaurante",
                        "title": "Questions usuelles au restaurant et au marché",
                        "questions": [
                            {"id": 381, "type": "multiple_choice", "question": "¿___ es el plato típico de la casa?", "options": ["Cuál", "Cuánto", "Quién", "Dónde"], "correct_answer": "Cuál", "explanation": "'¿Cuál es...?' pour identifier un plat parmi d'autres.", "xp": 15},
                            {"id": 382, "type": "fill_in_the_blank", "question": "¿___ cuesta el menú del día? (Combien)", "options": None, "correct_answer": "Cuánto", "explanation": "'Cuánto' pour demander un prix.", "xp": 15},
                            {"id": 383, "type": "multiple_choice", "question": "¿___ lleva la ensalada mixta?", "options": ["Qué", "Cuál", "Quién", "Cuánto"], "correct_answer": "Qué", "explanation": "'¿Qué lleva...?' = Qu'y a-t-il dans... ? / Quels sont les ingrédients ?", "xp": 15},
                            {"id": 384, "type": "multiple_choice", "question": "¿___ está el servicio / baño?", "options": ["Dónde", "Cómo", "Por qué", "Cuándo"], "correct_answer": "Dónde", "explanation": "'¿Dónde está...?' = Où se trouve... ?", "xp": 15},
                            {"id": 385, "type": "fill_in_the_blank", "question": "¿___ desea tomar de postre? (Que - formel)", "options": None, "correct_answer": "Qué", "explanation": "'¿Qué desea...?' = Que désirez-vous... ?", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_expresar_deseo_pedidos",
                        "title": "Exprimer son choix (Para mí, De primero, Quería)",
                        "questions": [
                            {"id": 386, "type": "multiple_choice", "question": "Comment introduire sa commande personnelle ?", "options": ["Para mí, la merluza a la plancha", "Por mí, la merluza", "Conmigo la merluza", "Sobre mí la merluza"], "correct_answer": "Para mí, la merluza a la plancha", "explanation": "'Para mí...' = Pour moi...", "xp": 15},
                            {"id": 387, "type": "fill_in_the_blank", "question": "Complétez : De segundo, ___ el pollo asado (prendre - verbe querer).", "options": None, "correct_answer": "quiero", "explanation": "Yo quiero.", "xp": 15},
                            {"id": 388, "type": "multiple_choice", "question": "Formule très polie pour commander au comptoir :", "options": ["Quería un café con leche", "Doy un café", "Hago un café", "Vengo un café"], "correct_answer": "Quería un café con leche", "explanation": "'Quería...' = Je voudrais / J'aimerais.", "xp": 15},
                            {"id": 389, "type": "fill_in_the_blank", "question": "Complétez : De ___ plato tomo sopa (premier).", "options": None, "correct_answer": "primer", "explanation": "'Primer' s'apocope devant un nom masculin singulier (plato).", "xp": 15},
                            {"id": 390, "type": "multiple_choice", "question": "Pour indiquer qu'on a terminé de commander :", "options": ["Nada más, gracias", "Todo menos", "Nunca más", "Siempre gracias"], "correct_answer": "Nada más, gracias", "explanation": "'Nada más, gracias' = Rien d'autre, merci.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_dialogo_mercado_1",
                        "title": "Dialogue : Faire ses achats au marché",
                        "questions": [
                            {"id": 391, "type": "multiple_choice", "question": "- ¡Hola! ¿Qué le pongo? - ___", "options": ["Quería un kilo de plátanos y medio de fresas", "La cuenta, por favor", "Está muy rico", "De segundo plato tomo carne"], "correct_answer": "Quería un kilo de plátanos y medio de fresas", "explanation": "Réponse adaptée au primeur.", "xp": 15},
                            {"id": 392, "type": "fill_in_the_blank", "question": "Complétez : - ¿Desea algo ___? - No, nada más. (autre / plus)", "options": None, "correct_answer": "más", "explanation": "'¿Algo más?' = Autre chose ?", "xp": 15},
                            {"id": 393, "type": "multiple_choice", "question": "- ¿Cuánto es todo? - Son seis ___ con cincuenta céntimos.", "options": ["euros", "kilos", "litros", "trozos"], "correct_answer": "euros", "explanation": "Monnaie de référence en Espagne.", "xp": 15},
                            {"id": 394, "type": "fill_in_the_blank", "question": "Complétez : - ¿Va a pagar con tarjeta o en ___? (liquide)", "options": None, "correct_answer": "efectivo", "explanation": "'En efectivo' = En espèces.", "xp": 15},
                            {"id": 395, "type": "multiple_choice", "question": "- Aquí tiene diez euros. - Gracias, su ___ son tres euros con cincuenta.", "options": ["cambio", "precio", "factura", "plato"], "correct_answer": "cambio", "explanation": "'El cambio' = La monnaie rendue.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_dialogo_restaurante_recap_2",
                        "title": "Dialogue complet au restaurant",
                        "questions": [
                            {"id": 396, "type": "multiple_choice", "question": "- Buenas tardes, ¿tienen mesa para dos personas? - ___", "options": ["Sí, pasen por aquí, por favor", "Son diez euros", "Quiero una sopa", "Está delicioso"], "correct_answer": "Sí, pasen por aquí, por favor", "explanation": "Accueil du restaurateur.", "xp": 15},
                            {"id": 397, "type": "fill_in_the_blank", "question": "Complétez : - ¿Qué van a ___ para beber? (boire / consommer)", "options": None, "correct_answer": "tomar", "explanation": "'¿Qué van a tomar?' = Que prendrez-vous ?", "xp": 15},
                            {"id": 398, "type": "multiple_choice", "question": "- ¿Qué tal está la comida? - ___", "options": ["Está todo riquísimo", "La cuenta, por favor", "Para dos personas", "De primero ensalada"], "correct_answer": "Está todo riquísimo", "explanation": "'Riquísimo' exprime une appréciation très positive.", "xp": 15},
                            {"id": 399, "type": "fill_in_the_blank", "question": "Complétez : - ¿Nos trae la ___ cuando pueda? (addition)", "options": None, "correct_answer": "cuenta", "explanation": "'La cuenta' = L'addition.", "xp": 15},
                            {"id": 400, "type": "multiple_choice", "question": "- ¿El servicio está incluido? - Sí, todo está ___ en la cuenta.", "options": ["incluido", "pagado", "puesto", "servido"], "correct_answer": "incluido", "explanation": "'Incluido' = Inclus.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_dar_la_hora_1",
                        "title": "Exprimer et demander l'heure (SER)",
                        "questions": [
                            {"id": 451, "type": "fill_in_the_blank", "question": "Complétez : ___ la una de la tarde (verbe ser).", "options": None, "correct_answer": "Es", "explanation": "Pour 1h00 on utilise le singulier : 'Es la una'.", "xp": 15},
                            {"id": 452, "type": "multiple_choice", "question": "Comment dit-on 'Il est trois heures' ?", "options": ["Son las tres", "Es las tres", "Está a las tres", "Hay tres horas"], "correct_answer": "Son las tres", "explanation": "Pour toutes les heures sauf une heure, on emploie 'Son las...'.", "xp": 15},
                            {"id": 453, "type": "fill_in_the_blank", "question": "¿A qué hora empieza? - Empieza ___ las ocho (à).", "options": None, "correct_answer": "a", "explanation": "On emploie la préposition 'a' pour indiquer l'heure d'un événement : 'a las ocho'.", "xp": 15},
                            {"id": 454, "type": "multiple_choice", "question": "Quelle question est correcte pour demander l'heure ?", "options": ["¿Qué hora es?", "¿Qué hora tiene?", "¿Cuál hora está?", "¿Cómo hora es?"], "correct_answer": "¿Qué hora es?", "explanation": "'¿Qué hora es?' est la tournure standard.", "xp": 15},
                            {"id": 455, "type": "fill_in_the_blank", "question": "Son las cinco ___ diez (moins dix - 4:50).", "options": None, "correct_answer": "menos", "explanation": "'Menos' sert à soustraire les minutes après la demie.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_verbos_reflexivos_1",
                        "title": "Verbes pronominaux : LEVANTARSE et DUCHARSE",
                        "questions": [
                            {"id": 456, "type": "fill_in_the_blank", "question": "Yo ___ levanto a las siete (pronom réfléchi).", "options": None, "correct_answer": "me", "explanation": "Pronom pour 'yo' : 'me'.", "xp": 15},
                            {"id": 457, "type": "multiple_choice", "question": "¿A qué hora te ___ tú?", "options": ["levantas", "levanta", "levanto", "levantáis"], "correct_answer": "levantas", "explanation": "Tú te levantas.", "xp": 15},
                            {"id": 458, "type": "fill_in_the_blank", "question": "Él se ___ (ducharse) con agua caliente.", "options": None, "correct_answer": "ducha", "explanation": "Él se ducha.", "xp": 15},
                            {"id": 459, "type": "multiple_choice", "question": "Nosotros ___ duchamos por la mañana.", "options": ["nos", "os", "se", "me"], "correct_answer": "nos", "explanation": "Nosotros nos duchamos.", "xp": 15},
                            {"id": 460, "type": "fill_in_the_blank", "question": "Ellos se ___ (levantarse) temprano los lunes.", "options": None, "correct_answer": "levantan", "explanation": "Ellos se levantan.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_verbos_bota_rutina_1",
                        "title": "Verbes à diphtongue de la routine : DESPERTARSE (E->IE)",
                        "questions": [
                            {"id": 461, "type": "fill_in_the_blank", "question": "Yo me ___ (despertarse) a las seis.", "options": None, "correct_answer": "despierto", "explanation": "Diphtongue : e -> ie (yo me despierto).", "xp": 15},
                            {"id": 462, "type": "multiple_choice", "question": "¿Tú a qué hora te ___?", "options": ["despiertas", "despierta", "despertamos", "despertáis"], "correct_answer": "despiertas", "explanation": "Tú te despiertas.", "xp": 15},
                            {"id": 463, "type": "fill_in_the_blank", "question": "Mi hijo se ___ (despertarse) con el despertador.", "options": None, "correct_answer": "despierta", "explanation": "Él se despierta.", "xp": 15},
                            {"id": 464, "type": "multiple_choice", "question": "Nosotros nos ___ muy tarde los domingos.", "options": ["despertamos", "despiertamos", "despiertan", "despertáis"], "correct_answer": "despertamos", "explanation": "'Nosotros' ne diphtongue jamais au présent.", "xp": 15},
                            {"id": 465, "type": "fill_in_the_blank", "question": "Ellas se ___ (despertarse) a las ocho.", "options": None, "correct_answer": "despiertan", "explanation": "Ellas se despiertan.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_verbos_bota_rutina_2",
                        "title": "Verbes à diphtongue de la routine : ACOSTARSE (O->UE)",
                        "questions": [
                            {"id": 466, "type": "fill_in_the_blank", "question": "Yo me ___ (acostarse) a las once de la noche.", "options": None, "correct_answer": "acuesto", "explanation": "Diphtongue : o -> ue (yo me acuesto).", "xp": 15},
                            {"id": 467, "type": "multiple_choice", "question": "¿A qué hora te ___ tú?", "options": ["acuestas", "acuesta", "acostamos", "acostáis"], "correct_answer": "acuestas", "explanation": "Tú te acuestas.", "xp": 15},
                            {"id": 468, "type": "fill_in_the_blank", "question": "Usted se ___ (acostarse) temprano.", "options": None, "correct_answer": "acuesta", "explanation": "Usted se acuesta.", "xp": 15},
                            {"id": 469, "type": "multiple_choice", "question": "Nosotros nos ___ a medianoche.", "options": ["acostamos", "acuestamos", "acuestan", "acostáis"], "correct_answer": "acostamos", "explanation": "'Nosotros' conserve le radical régulier 'acost-'.", "xp": 15},
                            {"id": 470, "type": "fill_in_the_blank", "question": "Los niños se ___ (acostarse) a las nueve.", "options": None, "correct_answer": "acuestan", "explanation": "Ellos se acuestan.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_verbo_vestirse_1",
                        "title": "Verbe à affaiblissement : VESTIRSE (E->I)",
                        "questions": [
                            {"id": 471, "type": "fill_in_the_blank", "question": "Yo me ___ (vestirse) rápido por la mañana.", "options": None, "correct_answer": "visto", "explanation": "Affaiblissement du e -> i : yo me visto.", "xp": 15},
                            {"id": 472, "type": "multiple_choice", "question": "¿Cómo te ___ para ir a trabajar?", "options": ["vistes", "vestís", "viste", "vestimos"], "correct_answer": "vistes", "explanation": "Tú te vistes.", "xp": 15},
                            {"id": 473, "type": "fill_in_the_blank", "question": "Ella se ___ (vestirse) de color azul.", "options": None, "correct_answer": "viste", "explanation": "Ella se viste.", "xp": 15},
                            {"id": 474, "type": "multiple_choice", "question": "Nosotros nos ___ con ropa cómoda.", "options": ["vestimos", "vistimos", "visten", "vestís"], "correct_answer": "vestimos", "explanation": "'Nosotros' reste régulier : vestimos.", "xp": 15},
                            {"id": 475, "type": "fill_in_the_blank", "question": "Mis hermanos se ___ (vestirse) solos.", "options": None, "correct_answer": "visten", "explanation": "Ellos se visten.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_hacer_tiempo_meteo",
                        "title": "Le verbe impersonnel HACER pour la météo",
                        "questions": [
                            {"id": 476, "type": "multiple_choice", "question": "Quelle forme du verbe HACER s'utilise pour exprimer la météo ?", "options": ["Hace", "Hacen", "Hago", "Hacemos"], "correct_answer": "Hace", "explanation": "On utilise la 3e personne du singulier invariable : 'Hace...'.", "xp": 15},
                            {"id": 477, "type": "fill_in_the_blank", "question": "En verano ___ mucho calor (verbe hacer).", "options": None, "correct_answer": "hace", "explanation": "'Hace calor'.", "xp": 15},
                            {"id": 478, "type": "multiple_choice", "question": "Complétez : Hoy no ___ viento en la costa.", "options": ["hace", "está", "es", "tiene"], "correct_answer": "hace", "explanation": "'Hace viento'.", "xp": 15},
                            {"id": 479, "type": "fill_in_the_blank", "question": "¿Qué tiempo ___ hoy? (verbe hacer)", "options": None, "correct_answer": "hace", "explanation": "'¿Qué tiempo hace?' = Quel temps fait-il ?", "xp": 15},
                            {"id": 480, "type": "multiple_choice", "question": "En primavera casi siempre ___ buen tiempo.", "options": ["hace", "está", "hay", "son"], "correct_answer": "hace", "explanation": "'Hace buen tiempo'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_horarios_desde_hasta",
                        "title": "Exprimer les créneaux horaires (De... a... / Desde... hasta...)",
                        "questions": [
                            {"id": 481, "type": "fill_in_the_blank", "question": "Trabajo de nueve ___ cinco (à).", "options": None, "correct_answer": "a", "explanation": "Structure corrélative : 'de ... a ...'", "xp": 15},
                            {"id": 482, "type": "multiple_choice", "question": "La tienda abre ___ las 10:00 hasta las 20:00.", "options": ["desde", "de", "a", "en"], "correct_answer": "desde", "explanation": "Structure corrélative : 'desde las ... hasta las ...'", "xp": 15},
                            {"id": 483, "type": "fill_in_the_blank", "question": "La clase dura desde las dos ___ las cuatro.", "options": None, "correct_answer": "hasta", "explanation": "'Hasta' = Jusqu'à.", "xp": 15},
                            {"id": 484, "type": "multiple_choice", "question": "El museo está abierto ___ lunes a viernes.", "options": ["de", "desde", "en", "por"], "correct_answer": "de", "explanation": "'De lunes a viernes' = Du lundi au vendredi.", "xp": 15},
                            {"id": 485, "type": "fill_in_the_blank", "question": "Como todos los días ___ las dos de la tarde (à).", "options": None, "correct_answer": "a", "explanation": "'A las dos' = À deux heures.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ir_a_infinitivo_rutina",
                        "title": "Futur proche pour planifier sa journée (IR + A + Infinitif)",
                        "questions": [
                            {"id": 486, "type": "fill_in_the_blank", "question": "Esta tarde yo voy ___ estudiar español (préposition).", "options": None, "correct_answer": "a", "explanation": "La structure du futur proche est 'ir + a + infinitivo'.", "xp": 15},
                            {"id": 487, "type": "multiple_choice", "question": "¿Qué ___ a hacer tú este fin de semana?", "options": ["vas", "va", "vamos", "van"], "correct_answer": "vas", "explanation": "Tú vas a hacer.", "xp": 15},
                            {"id": 488, "type": "fill_in_the_blank", "question": "Nosotros ___ (ir) a cenar con unos amigos.", "options": None, "correct_answer": "vamos", "explanation": "Nosotros vamos a...", "xp": 15},
                            {"id": 489, "type": "multiple_choice", "question": "Mañana ellos van a ___ temprano.", "options": ["levantarse", "se levantan", "levantan", "levantamos"], "correct_answer": "levantarse", "explanation": "Après 'van a', le verbe se met à l'infinitif.", "xp": 15},
                            {"id": 490, "type": "fill_in_the_blank", "question": "Ella ___ (ir) a salir a correr por la mañana.", "options": None, "correct_answer": "va", "explanation": "Ella va a...", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_dialogo_horarios_rutina",
                        "title": "Dialogue : Parler de son emploi du temps",
                        "questions": [
                            {"id": 491, "type": "multiple_choice", "question": "- ¿A qué hora te levantas normalmente? - ___", "options": ["Me levanto a las siete de la mañana", "Es la una y media", "Hace mucho sol", "De postre quiero flan"], "correct_answer": "Me levanto a las siete de la mañana", "explanation": "Réponse adaptée à une question sur la routine horaire.", "xp": 15},
                            {"id": 492, "type": "fill_in_the_blank", "question": "Complétez : - ¿Qué haces después de trabajar? - Voy ___ gimnasio (au).", "options": None, "correct_answer": "al", "explanation": "Contraction : a + el = al.", "xp": 15},
                            {"id": 493, "type": "multiple_choice", "question": "- ¿Cenas muy tarde? - No, ceno siempre ___ las nueve.", "options": ["a", "en", "de", "por"], "correct_answer": "a", "explanation": "'A las nueve' pour indiquer l'heure fixe.", "xp": 15},
                            {"id": 494, "type": "fill_in_the_blank", "question": "Complétez : - ¿Qué días tienes clase? - Los ___ y jueves (mardis).", "options": None, "correct_answer": "martes", "explanation": "'Martes' = Mardi.", "xp": 15},
                            {"id": 495, "type": "multiple_choice", "question": "- ¡Buen fin de semana! - ¡Gracias, ___!", "options": ["igualmente", "mucho gusto", "por favor", "de nada"], "correct_answer": "igualmente", "explanation": "'Igualmente' = À toi / vous aussi.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_dialogo_tiempo_planes",
                        "title": "Dialogue : Parler de la météo et faire des projets",
                        "questions": [
                            {"id": 496, "type": "multiple_choice", "question": "- ¿Qué tiempo hace hoy en Madrid? - ___", "options": ["Hace sol y no hace nada de frío", "Son las diez en punto", "Me llamo Carlos", "Tengo dos hermanos"], "correct_answer": "Hace sol y no hace nada de frío", "explanation": "Description météo.", "xp": 15},
                            {"id": 497, "type": "fill_in_the_blank", "question": "Complétez : - ¿Vamos a la playa? - No, porque hoy ___ (il pleut).", "options": None, "correct_answer": "llueve", "explanation": "'Llueve' = Il pleut.", "xp": 10},
                            {"id": 498, "type": "multiple_choice", "question": "- ¿Qué estación del año prefieres? - Prefiero el ___ porque voy a esquiar.", "options": ["invierno", "verano", "otoño", "primavera"], "correct_answer": "invierno", "explanation": "On skie en hiver (invierno).", "xp": 15},
                            {"id": 499, "type": "fill_in_the_blank", "question": "Complétez : - ¿Qué vas a hacer mañana? - ___ a descansar en casa (verbe ir).", "options": None, "correct_answer": "Voy", "explanation": "Yo voy a descansar.", "xp": 15},
                            {"id": 500, "type": "multiple_choice", "question": "- ¡Abrígate bien! - Sí, porque en la calle ___ mucho frío.", "options": ["hace", "está", "es", "tiene"], "correct_answer": "hace", "explanation": "'Hace mucho frío'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ir_transportes_1",
                        "title": "Le verbe IR avec les moyens de transport (EN / A)",
                        "questions": [
                            {"id": 551, "type": "fill_in_the_blank", "question": "Yo ___ (ir) al trabajo en metro.", "options": None, "correct_answer": "voy", "explanation": "Yo voy (irrégulier).", "xp": 15},
                            {"id": 552, "type": "multiple_choice", "question": "Quelle préposition s'utilise pour les transports motorisés (coche, autobús, tren) ?", "options": ["en", "a", "por", "de"], "correct_answer": "en", "explanation": "On emploie 'en' devant les moyens de transport (en autobús, en coche, en tren).", "xp": 15},
                            {"id": 553, "type": "fill_in_the_blank", "question": "Nosotros vamos ___ pie al colegio (à pied).", "options": None, "correct_answer": "a", "explanation": "Exception : 'a pie' (à pied) ou 'a caballo' (à cheval).", "xp": 15},
                            {"id": 554, "type": "multiple_choice", "question": "¿Cómo ___ vosotros a la universidad?", "options": ["vais", "van", "vamos", "vas"], "correct_answer": "vais", "explanation": "Vosotros vais.", "xp": 15},
                            {"id": 555, "type": "fill_in_the_blank", "question": "Ellos ___ (ir) en avión a Mallorca.", "options": None, "correct_answer": "van", "explanation": "Ellos van.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_coger_tomar_transporte",
                        "title": "Prendre un transport : COGER et TOMAR",
                        "questions": [
                            {"id": 556, "type": "fill_in_the_blank", "question": "Yo ___ (tomar) el autobús número diez.", "options": None, "correct_answer": "tomo", "explanation": "Yo tomo.", "xp": 15},
                            {"id": 557, "type": "multiple_choice", "question": "¿Dónde ___ tú el metro?", "options": ["coges", "coge", "cogéis", "cojo"], "correct_answer": "coges", "explanation": "Tú coges (très courant en Espagne pour prendre un transport).", "xp": 15},
                            {"id": 558, "type": "fill_in_the_blank", "question": "En la estación, yo ___ (coger - 1ère personne) el tren.", "options": None, "correct_answer": "cojo", "explanation": "Attention à l'orthographe : yo cojo (g -> j devant 'o').", "xp": 15},
                            {"id": 559, "type": "multiple_choice", "question": "Nosotros ___ un taxi para ir al aeropuerto.", "options": ["tomamos", "toman", "tomáis", "tomo"], "correct_answer": "tomamos", "explanation": "Nosotros tomamos.", "xp": 15},
                            {"id": 560, "type": "fill_in_the_blank", "question": "Usted ___ (coger) la línea roja de metro.", "options": None, "correct_answer": "coge", "explanation": "Usted coge.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_girar_doblar_itinerario",
                        "title": "Verbes d'action pour orienter : GIRAR et DOBLAR",
                        "questions": [
                            {"id": 561, "type": "fill_in_the_blank", "question": "Tú ___ (girar) a la izquierda en la farmacia.", "options": None, "correct_answer": "giras", "explanation": "Tú giras.", "xp": 15},
                            {"id": 562, "type": "multiple_choice", "question": "Forme formelle de politesse : 'Señor, ___ usted a la derecha'.", "options": ["gire", "gira", "giras", "giramos"], "correct_answer": "gire", "explanation": "Impératif formel (usted) de girar : gire.", "xp": 15},
                            {"id": 563, "type": "fill_in_the_blank", "question": "En la esquina, usted ___ (doblar - indicatif présent) a la izquierda.", "options": None, "correct_answer": "dobla", "explanation": "Usted dobla.", "xp": 15},
                            {"id": 564, "type": "multiple_choice", "question": "Tú (impératif informel) : '¡___ a la derecha en el semáforo!'", "options": ["Gira", "Gire", "Giras", "Giro"], "correct_answer": "Gira", "explanation": "Impératif informel (tú) : gira.", "xp": 15},
                            {"id": 565, "type": "fill_in_the_blank", "question": "Nosotros ___ (girar) en la segunda calle.", "options": None, "correct_answer": "giramos", "explanation": "Nosotros giramos.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_seguir_continuar_itinerario",
                        "title": "Continuer son chemin : SEGUIR et CONTINUAR",
                        "questions": [
                            {"id": 566, "type": "fill_in_the_blank", "question": "Yo ___ (seguir) todo recto por esta avenida.", "options": None, "correct_answer": "sigo", "explanation": "Yo sigo (e -> i et terminaison -go).", "xp": 15},
                            {"id": 567, "type": "multiple_choice", "question": "¿Tú ___ todo recto hasta la plaza?", "options": ["sigues", "segues", "sigue", "seguimos"], "correct_answer": "sigues", "explanation": "Tú sigues (e -> i).", "xp": 15},
                            {"id": 568, "type": "fill_in_the_blank", "question": "Usted ___ (seguir - indicatif) hasta el final de la calle.", "options": None, "correct_answer": "sigue", "explanation": "Usted sigue.", "xp": 15},
                            {"id": 569, "type": "multiple_choice", "question": "Nosotros ___ por el paseo marítimo.", "options": ["continuamos", "continúan", "continuáis", "continuo"], "correct_answer": "continuamos", "explanation": "Nosotros continuamos.", "xp": 15},
                            {"id": 570, "type": "fill_in_the_blank", "question": "Ellos ___ (seguir) las señales de tráfico.", "options": None, "correct_answer": "siguen", "explanation": "Ellos siguen.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_cruzar_pasar_calle",
                        "title": "Traverser et longer : CRUZAR et PASAR",
                        "questions": [
                            {"id": 571, "type": "multiple_choice", "question": "Tú ___ la calle por el paso de peatones.", "options": ["cruzas", "cruza", "cruzo", "cruzáis"], "correct_answer": "cruzas", "explanation": "Tú cruzas.", "xp": 15},
                            {"id": 572, "type": "fill_in_the_blank", "question": "Yo ___ (cruzar) el puente todas las mañanas.", "options": None, "correct_answer": "cruzo", "explanation": "Yo cruzo.", "xp": 15},
                            {"id": 573, "type": "multiple_choice", "question": "Para llegar al museo, usted ___ por delante de la iglesia.", "options": ["pasa", "pasas", "paso", "pasan"], "correct_answer": "pasa", "explanation": "Usted pasa.", "xp": 15},
                            {"id": 574, "type": "fill_in_the_blank", "question": "Nosotros ___ (cruzar) el parque a pie.", "options": None, "correct_answer": "cruzamos", "explanation": "Nosotros cruzamos.", "xp": 15},
                            {"id": 575, "type": "multiple_choice", "question": "Ellos ___ por la plaza principal.", "options": ["pasan", "pasa", "pasamos", "pasas"], "correct_answer": "pasan", "explanation": "Ellos pasan.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_parar_bajar_subir_transporte",
                        "title": "Actions dans les transports : SUBIR, BAJAR, PARAR",
                        "questions": [
                            {"id": 576, "type": "multiple_choice", "question": "Comment dit-on 'Monter dans le bus' ?", "options": ["Subir al autobús", "Bajar del autobús", "Parar el autobús", "Cruzar el autobús"], "correct_answer": "Subir al autobús", "explanation": "'Subir a...' = Monter dans...", "xp": 15},
                            {"id": 577, "type": "fill_in_the_blank", "question": "Yo me ___ en la próxima parada (descendre - verbe bajarse).", "options": None, "correct_answer": "bajo", "explanation": "Yo me bajo del autobús.", "xp": 15},
                            {"id": 578, "type": "multiple_choice", "question": "El autobús no ___ en esta parada.", "options": ["para", "paras", "paramos", "paran"], "correct_answer": "para", "explanation": "El autobús para.", "xp": 15},
                            {"id": 579, "type": "fill_in_the_blank", "question": "Nosotros ___ (subir) al tren en el andén dos.", "options": None, "correct_answer": "subimos", "explanation": "Nosotros subimos.", "xp": 15},
                            {"id": 580, "type": "multiple_choice", "question": "¿Dónde os ___ vosotros del metro?", "options": ["bajáis", "bajan", "bajamos", "bajas"], "correct_answer": "bajáis", "explanation": "Vosotros os bajáis.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_preguntar_camino_interrogativos",
                        "title": "Questions usuelles pour s'orienter en ville",
                        "questions": [
                            {"id": 581, "type": "multiple_choice", "question": "¿___ se va a la estación de tren?", "options": ["Cómo", "Cuánto", "Quién", "Qué"], "correct_answer": "Cómo", "explanation": "'¿Cómo se va a...?' = Comment va-t-on à... ?", "xp": 15},
                            {"id": 582, "type": "fill_in_the_blank", "question": "Por favor, ¿___ está la parada de taxis? (Où)", "options": None, "correct_answer": "dónde", "explanation": "'¿Dónde está...?' = Où est... ?", "xp": 15},
                            {"id": 583, "type": "multiple_choice", "question": "¿___ autobús va al centro histórico?", "options": ["Qué", "Cómo", "Dónde", "Quién"], "correct_answer": "Qué", "explanation": "'¿Qué autobús...?' = Quel bus... ?", "xp": 15},
                            {"id": 584, "type": "multiple_choice", "question": "¿A cuántos minutos ___ la plaza caminando?", "options": ["queda / está", "hay", "es", "tiene"], "correct_answer": "queda / está", "explanation": "'¿A cuánto queda/está?' = À quelle distance/temps se trouve... ?", "xp": 15},
                            {"id": 585, "type": "fill_in_the_blank", "question": "Disculpe, ¿___ una parada de metro por aquí? (Il y a)", "options": None, "correct_answer": "hay", "explanation": "'¿Hay una parada...?' pour demander l'existence d'une station.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_perífrasis_tener_que_itinerario",
                        "title": "Exprimer l'obligation d'itinéraire (Tener que + Infinitif)",
                        "questions": [
                            {"id": 586, "type": "fill_in_the_blank", "question": "Para ir al museo, tú ___ que tomar la línea 1 (tener).", "options": None, "correct_answer": "tienes", "explanation": "Tú tienes que...", "xp": 15},
                            {"id": 587, "type": "multiple_choice", "question": "Usted ___ que cambiar de tren en la estación central.", "options": ["tiene", "tienes", "tienen", "tenemos"], "correct_answer": "tiene", "explanation": "Usted tiene que...", "xp": 15},
                            {"id": 588, "type": "fill_in_the_blank", "question": "Nosotros ___ (tener) que comprar el billete antes de subir.", "options": None, "correct_answer": "tenemos", "explanation": "Nosotros tenemos que...", "xp": 15},
                            {"id": 589, "type": "multiple_choice", "question": "Para llegar rápido, yo tengo que ___ un taxi.", "options": ["coger", "cojo", "coges", "cogiendo"], "correct_answer": "coger", "explanation": "Après 'tener que', on emploie l'infinitif.", "xp": 15},
                            {"id": 590, "type": "fill_in_the_blank", "question": "Ellos ___ (tener) que validar el billete en la entrada.", "options": None, "correct_answer": "tienen", "explanation": "Ellos tienen que...", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_dialogo_camino_calle_1",
                        "title": "Dialogue : Demander et indiquer un itinéraire dans la rue",
                        "questions": [
                            {"id": 591, "type": "multiple_choice", "question": "- Por favor, ¿para ir a la Plaza Mayor? - ___", "options": ["Sigue todo recto y gira a la derecha", "Cuesta dos euros", "El tren sale a las diez", "Me llamo Roberto"], "correct_answer": "Sigue todo recto y gira a la derecha", "explanation": "Indication d'orientation claire et appropriée.", "xp": 15},
                            {"id": 592, "type": "fill_in_the_blank", "question": "Complétez : - ¿Está lejos? - No, ___ a cinco minutos a pie (verbe estar).", "options": None, "correct_answer": "está", "explanation": "'Está a cinco minutos'.", "xp": 15},
                            {"id": 593, "type": "multiple_choice", "question": "- ¿Tengo que cruzar la avenida? - Sí, cruza por el paso de ___.", "options": ["peatones", "coches", "trenes", "aviones"], "correct_answer": "peatones", "explanation": "'Paso de peatones' = Passage piéton.", "xp": 15},
                            {"id": 594, "type": "fill_in_the_blank", "question": "Complétez : - Muchas gracias por su ayuda. - De ___, ¡buen viaje!", "options": None, "correct_answer": "nada", "explanation": "'De nada' = De rien.", "xp": 15},
                            {"id": 595, "type": "multiple_choice", "question": "- ¿La catedral está a la izquierda o a la derecha? - Está a la ___.", "options": ["derecha", "recto", "lejos", "andando"], "correct_answer": "derecha", "explanation": "'A la derecha' indique le côté.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_dialogo_estacion_recap_2",
                        "title": "Dialogue : Acheter un billet à la gare",
                        "questions": [
                            {"id": 596, "type": "multiple_choice", "question": "- ¡Hola! Quería un billete para Sevilla, por favor. - ___", "options": ["¿De ida o de ida y vuelta?", "¿Qué hora es?", "¿Dónde vive usted?", "¿Cómo está la comida?"], "correct_answer": "¿De ida o de ida y vuelta?", "explanation": "Question type de l'agent de billetterie.", "xp": 15},
                            {"id": 597, "type": "fill_in_the_blank", "question": "Complétez : - De ida y vuelta, por favor. ¿A qué hora ___ el tren? (partir / verbe salir)", "options": None, "correct_answer": "sale", "explanation": "El tren sale.", "xp": 15},
                            {"id": 598, "type": "multiple_choice", "question": "- Sale a las 11:30 del andén número cuatro. - ¿___ cuesta?", "options": ["Cuánto", "Cómo", "Dónde", "Quién"], "correct_answer": "Cuánto", "explanation": "'¿Cuánto cuesta?' = Combien coûte-t-il ?", "xp": 15},
                            {"id": 599, "type": "fill_in_the_blank", "question": "Complétez : - Son cuarenta euros. ¿Va a pagar con ___ o en efectivo? (carte)", "options": None, "correct_answer": "tarjeta", "explanation": "'Tarjeta' = Carte de paiement.", "xp": 15},
                            {"id": 600, "type": "multiple_choice", "question": "- Con tarjeta. Aquí tiene. - Gracias, que ___ un buen viaje.", "options": ["tenga", "tienes", "tengo", "tenemos"], "correct_answer": "tenga", "explanation": "'Que tenga un buen viaje' (souhait de politesse avec usted).", "xp": 15}
                        ]
                    },

                    {
                        "id": "a1_conj_doler_singular_1",
                        "title": "Le verbe DOLER avec sujet singulier (Duele)",
                        "questions": [
                            {"id": 651, "type": "fill_in_the_blank", "question": "A mí me ___ la cabeza (verbe doler).", "options": None, "correct_answer": "duele", "explanation": "Sujet singulier (la cabeza) -> 'duele' (diphtongue o -> ue).", "xp": 15},
                            {"id": 652, "type": "multiple_choice", "question": "¿A ti qué te ___?", "options": ["duele", "duelen", "dueles", "doléis"], "correct_answer": "duele", "explanation": "Question générique sur la douleur au singulier : '¿Qué te duele?'.", "xp": 15},
                            {"id": 653, "type": "fill_in_the_blank", "question": "A Juan le ___ el estómago (doler).", "options": None, "correct_answer": "duele", "explanation": "Sujet singulier (el estómago) -> 'duele'.", "xp": 15},
                            {"id": 654, "type": "multiple_choice", "question": "A nosotros nos ___ la garganta después de cantar.", "options": ["duele", "duelen", "dolemos", "duelimos"], "correct_answer": "duele", "explanation": "'La garganta' est singulier -> 'nos duele'.", "xp": 15},
                            {"id": 655, "type": "fill_in_the_blank", "question": "¿A usted le ___ la espalda? (doler - formel)", "options": None, "correct_answer": "duele", "explanation": "Sujet singulier (la espalda) -> 'duele'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_doler_plural_1",
                        "title": "Le verbe DOLER avec sujet pluriel (Duelen)",
                        "questions": [
                            {"id": 656, "type": "fill_in_the_blank", "question": "Me ___ los pies de tanto caminar (doler).", "options": None, "correct_answer": "duelen", "explanation": "Sujet pluriel (los pies) -> 'duelen'.", "xp": 15},
                            {"id": 657, "type": "multiple_choice", "question": "¿A ti te ___ las muelas?", "options": ["duelen", "duele", "dueles", "dolen"], "correct_answer": "duelen", "explanation": "Sujet pluriel (las muelas) -> 'duelen'.", "xp": 15},
                            {"id": 658, "type": "fill_in_the_blank", "question": "A ella le ___ los ojos por la pantalla (doler).", "options": None, "correct_answer": "duelen", "explanation": "Sujet pluriel (los ojos) -> 'duelen'.", "xp": 15},
                            {"id": 659, "type": "multiple_choice", "question": "A vosotros os ___ las piernas tras hacer deporte.", "options": ["duelen", "duele", "doléis", "duelenis"], "correct_answer": "duelen", "explanation": "Sujet pluriel (las piernas) -> 'duelen'.", "xp": 15},
                            {"id": 660, "type": "fill_in_the_blank", "question": "A ellos les ___ los oídos por el frío (doler).", "options": None, "correct_answer": "duelen", "explanation": "Sujet pluriel (los oídos) -> 'duelen'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_pronombres_doler",
                        "title": "Pronoms indirects avec DOLER (Me, Te, Le, Nos, Os, Les)",
                        "questions": [
                            {"id": 661, "type": "fill_in_the_blank", "question": "A mí ___ duele el brazo derecho (pronom indirect).", "options": None, "correct_answer": "me", "explanation": "Pronom COI pour 'a mí' : 'me'.", "xp": 15},
                            {"id": 662, "type": "multiple_choice", "question": "A mi madre ___ duele la espalda.", "options": ["le", "la", "se", "me"], "correct_answer": "le", "explanation": "Pronom COI 3e personne du singulier : 'le'.", "xp": 15},
                            {"id": 663, "type": "fill_in_the_blank", "question": "¿A vosotros ___ duelen las rodillas? (pronom)", "options": None, "correct_answer": "os", "explanation": "Pronom COI pour 'a vosotros' : 'os'.", "xp": 15},
                            {"id": 664, "type": "multiple_choice", "question": "A los niños ___ duele la barriga.", "options": ["les", "los", "se", "nos"], "correct_answer": "les", "explanation": "Pronom COI 3e personne du pluriel : 'les'.", "xp": 15},
                            {"id": 665, "type": "fill_in_the_blank", "question": "A nosotros ___ duele la cabeza por el ruido (pronom).", "options": None, "correct_answer": "nos", "explanation": "Pronom COI pour 'a nosotros' : 'nos'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_tener_sintomas",
                        "title": "Le verbe TENER pour exprimer les symptômes physiques",
                        "questions": [
                            {"id": 666, "type": "fill_in_the_blank", "question": "Yo ___ (tener) fiebre de 38 grados.", "options": None, "correct_answer": "tengo", "explanation": "Yo tengo.", "xp": 15},
                            {"id": 667, "type": "multiple_choice", "question": "¿Tú ___ dolor de garganta?", "options": ["tienes", "tiene", "tenemos", "tenéis"], "correct_answer": "tienes", "explanation": "Tú tienes.", "xp": 15},
                            {"id": 668, "type": "fill_in_the_blank", "question": "El paciente ___ (tener) gripe.", "options": None, "correct_answer": "tiene", "explanation": "Él tiene.", "xp": 15},
                            {"id": 669, "type": "multiple_choice", "question": "Nosotros ___ mucha tos y mocos.", "options": ["tenemos", "tienen", "tenéis", "tengo"], "correct_answer": "tenemos", "explanation": "Nosotros tenemos.", "xp": 15},
                            {"id": 670, "type": "fill_in_the_blank", "question": "Ellos ___ (tener) mareos continuos.", "options": None, "correct_answer": "tienen", "explanation": "Ellos tienen.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_sentirse_estados",
                        "title": "Le verbe réflexif SENTIRSE (Bien, Mal, Fatal)",
                        "questions": [
                            {"id": 671, "type": "fill_in_the_blank", "question": "Yo me ___ (sentirse) muy cansado hoy.", "options": None, "correct_answer": "siento", "explanation": "Diphtongue e -> ie : yo me siento.", "xp": 15},
                            {"id": 672, "type": "multiple_choice", "question": "¿Cómo te ___ tú esta mañana?", "options": ["sientes", "siente", "sentimos", "sentís"], "correct_answer": "sientes", "explanation": "Tú te sientes.", "xp": 15},
                            {"id": 673, "type": "fill_in_the_blank", "question": "Ella se ___ (sentirse) mareada en el coche.", "options": None, "correct_answer": "siente", "explanation": "Ella se siente.", "xp": 15},
                            {"id": 674, "type": "multiple_choice", "question": "Nosotros nos ___ fenomenal con el tratamiento.", "options": ["sentimos", "sientimos", "sienten", "sentís"], "correct_answer": "sentimos", "explanation": "'Nosotros' ne diphtongue pas : nos sentimos.", "xp": 15},
                            {"id": 675, "type": "fill_in_the_blank", "question": "Mis abuelos se ___ (sentirse) mejor hoy.", "options": None, "correct_answer": "sienten", "explanation": "Ellos se sienten.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_estar_adjetivos_salud",
                        "title": "Le verbe ESTAR pour exprimer l'état de santé",
                        "questions": [
                            {"id": 676, "type": "multiple_choice", "question": "Yo no voy al colegio porque ___ enfermo.", "options": ["estoy", "soy", "tengo", "hago"], "correct_answer": "estoy", "explanation": "Les états de santé temporaires s'expriment avec 'estar' : 'estoy enfermo'.", "xp": 15},
                            {"id": 677, "type": "fill_in_the_blank", "question": "¿Tú ___ resfriado? (verbe estar)", "options": None, "correct_answer": "estás", "explanation": "Tú estás.", "xp": 15},
                            {"id": 678, "type": "multiple_choice", "question": "María ___ muy pálida y cansada.", "options": ["está", "es", "tiene", "queda"], "correct_answer": "está", "explanation": "Ella está.", "xp": 15},
                            {"id": 679, "type": "fill_in_the_blank", "question": "Nosotros ___ (estar) agotados tras la carrera.", "options": None, "correct_answer": "estamos", "explanation": "Nosotros estamos.", "xp": 15},
                            {"id": 680, "type": "multiple_choice", "question": "¿Vosotros ___ ya recuperados de la gripe?", "options": ["estáis", "están", "sois", "estamos"], "correct_answer": "estáis", "explanation": "Vosotros estáis.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_tener_que_deber_salud",
                        "title": "Obligations et conseils de santé (Tener que / Deber)",
                        "questions": [
                            {"id": 681, "type": "fill_in_the_blank", "question": "Tienes que ___ (tomar) esta pastilla cada 8 horas.", "options": None, "correct_answer": "tomar", "explanation": "Après 'tener que', verbe à l'infinitif.", "xp": 15},
                            {"id": 682, "type": "multiple_choice", "question": "Usted ___ guardar cama durante tres días.", "options": ["debe", "debes", "debemos", "deben"], "correct_answer": "debe", "explanation": "Usted debe + infinitif.", "xp": 15},
                            {"id": 683, "type": "fill_in_the_blank", "question": "Yo ___ (deber) beber más agua al día.", "options": None, "correct_answer": "debo", "explanation": "Yo debo.", "xp": 15},
                            {"id": 684, "type": "multiple_choice", "question": "Tú tienes que ___ al médico si no mejora el dolor.", "options": ["ir", "vas", "irás", "ido"], "correct_answer": "ir", "explanation": "Tener que + infinitif (ir).", "xp": 15},
                            {"id": 685, "type": "fill_in_the_blank", "question": "Vosotros ___ (tener) que descansar más tiempo.", "options": None, "correct_answer": "tenéis", "explanation": "Vosotros tenéis que...", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_preguntas_medico_consulta",
                        "title": "Questions usuelles lors d'une consultation médicale",
                        "questions": [
                            {"id": 686, "type": "multiple_choice", "question": "¿___ le ocurre / qué le pasa?", "options": ["Qué", "Cómo", "Quién", "Cuánto"], "correct_answer": "Qué", "explanation": "'¿Qué le pasa?' / '¿Qué le ocurre?' = Que vous arrive-t-il ?", "xp": 15},
                            {"id": 687, "type": "fill_in_the_blank", "question": "¿Desde ___ le duele la garganta? (Quand)", "options": None, "correct_answer": "cuándo", "explanation": "'¿Desde cuándo...?' = Depuis quand... ?", "xp": 15},
                            {"id": 688, "type": "multiple_choice", "question": "¿___ le duele exactamente?", "options": ["Dónde", "Cuál", "Quién", "Cuánto"], "correct_answer": "Dónde", "explanation": "'¿Dónde le duele?' = Où avez-vous mal ?", "xp": 15},
                            {"id": 689, "type": "multiple_choice", "question": "¿___ fiebre?", "options": ["Tiene", "Es", "Está", "Hace"], "correct_answer": "Tiene", "explanation": "'¿Tiene fiebre?' = Avez-vous de la fièvre ?", "xp": 15},
                            {"id": 690, "type": "fill_in_the_blank", "question": "¿Es usted alérgico a ___ medicamento? (aucun / quelque)", "options": None, "correct_answer": "algún", "explanation": "'¿Es alérgico a algún medicamento?' = Êtes-vous allergique à un médicament quelconque ?", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_dialogo_farmacia_1",
                        "title": "Dialogue : Demander conseil à la pharmacie",
                        "questions": [
                            {"id": 691, "type": "multiple_choice", "question": "- Buenos días. ¿Qué desea? - ___", "options": ["Quería algo para el dolor de cabeza, por favor", "Vivo en el centro", "Tengo dos hermanos", "La cuenta, por favor"], "correct_answer": "Quería algo para el dolor de cabeza, por favor", "explanation": "Demande adaptée en pharmacie.", "xp": 15},
                            {"id": 692, "type": "fill_in_the_blank", "question": "Complétez : - ¿Tiene ___ médica? - No, no tengo receta del doctor.", "options": None, "correct_answer": "receta", "explanation": "'Receta médica' = Ordonnance.", "xp": 15},
                            {"id": 693, "type": "multiple_choice", "question": "- Puede tomar este jarabe. Debe tomar una cucharada ___ las comidas.", "options": ["después de", "dentro de", "lejos de", "encima de"], "correct_answer": "después de", "explanation": "'Después de las comidas' = Après les repas.", "xp": 15},
                            {"id": 694, "type": "fill_in_the_blank", "question": "Complétez : - ¿___ cuesta esta caja de aspirinas? (Combien)", "options": None, "correct_answer": "Cuánto", "explanation": "'¿Cuánto cuesta...?' pour s'enquérir du prix.", "xp": 15},
                            {"id": 695, "type": "multiple_choice", "question": "- Son cinco euros con veinte. - ¡Muchas gracias! - ¡Que se ___ pronto!", "options": ["mejore", "llama", "gira", "tenga"], "correct_answer": "mejore", "explanation": "'¡Que se mejore!' = Bon rétablissement / Remettez-vous vite !", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_dialogo_medico_recap_2",
                        "title": "Dialogue complet chez le médecin",
                        "questions": [
                            {"id": 696, "type": "multiple_choice", "question": "- Buenas tardes, doctor. - Buenas tardes. Siéntese, ¿qué le ___?", "options": ["pasa", "comes", "llamas", "vives"], "correct_answer": "pasa", "explanation": "'¿Qué le pasa?' formule médicale standard.", "xp": 15},
                            {"id": 697, "type": "fill_in_the_blank", "question": "Complétez : - Me siento fatal, me ___ mucho la cabeza y tengo fiebre (doler).", "options": None, "correct_answer": "duele", "explanation": "Sujet singulier (la cabeza) -> 'duele'.", "xp": 15},
                            {"id": 698, "type": "multiple_choice", "question": "- Abra la boca, por favor... Tiene la garganta muy ___.", "options": ["roja", "azul", "lejos", "rápida"], "correct_answer": "roja", "explanation": "'Garganta roja' (gorge rouge / irritée).", "xp": 15},
                            {"id": 699, "type": "fill_in_the_blank", "question": "Complétez : - Le voy a recetar un ___ para la infección (antibiotique).", "options": None, "correct_answer": "antibiótico", "explanation": "'El antibiótico' = L'antibiotique.", "xp": 15},
                            {"id": 700, "type": "multiple_choice", "question": "- Beba mucho líquido y descanse tres días. - Muchas gracias, doctor. - De nada, ¡a ___!", "options": ["cuidarse", "levantarse", "llamarse", "lavarse"], "correct_answer": "cuidarse", "explanation": "'¡A cuidarse!' = Prenez bien soin de vous !", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ser_formes_1",
                        "title": "SER : Conjugaison au présent (Formes singulières)",
                        "questions": [
                            {"id": 701, "type": "fill_in_the_blank", "question": "Yo ___ (ser) estudiante de español.", "options": None, "correct_answer": "soy", "explanation": "1ère personne : 'Yo soy'.", "xp": 15},
                            {"id": 702, "type": "multiple_choice", "question": "¿Tú ___ de Madrid?", "options": ["eres", "es", "soy", "somos"], "correct_answer": "eres", "explanation": "2e personne : 'Tú eres'.", "xp": 15},
                            {"id": 703, "type": "fill_in_the_blank", "question": "Él ___ (ser) profesor de matemáticas.", "options": None, "correct_answer": "es", "explanation": "3e personne : 'Él es'.", "xp": 15},
                            {"id": 704, "type": "multiple_choice", "question": "Ella ___ muy amable.", "options": ["es", "eres", "soy", "son"], "correct_answer": "es", "explanation": "'Ella es'.", "xp": 15},
                            {"id": 705, "type": "fill_in_the_blank", "question": "Usted ___ (ser) el nuevo director.", "options": None, "correct_answer": "es", "explanation": "'Usted' prend la 3e personne du singulier : 'es'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ser_formes_2",
                        "title": "SER : Conjugaison au présent (Formes plurielles)",
                        "questions": [
                            {"id": 706, "type": "fill_in_the_blank", "question": "Nosotros ___ (ser) amigos desde la infancia.", "options": None, "correct_answer": "somos", "explanation": "'Nosotros somos'.", "xp": 15},
                            {"id": 707, "type": "multiple_choice", "question": "¿Vosotros ___ franceses o italianos?", "options": ["sois", "somos", "son", "eres"], "correct_answer": "sois", "explanation": "'Vosotros sois'.", "xp": 15},
                            {"id": 708, "type": "fill_in_the_blank", "question": "Ellos ___ (ser) ingenieros.", "options": None, "correct_answer": "son", "explanation": "'Ellos son'.", "xp": 15},
                            {"id": 709, "type": "multiple_choice", "question": "Ellas ___ muy inteligentes.", "options": ["son", "somos", "sois", "es"], "correct_answer": "son", "explanation": "'Ellas son'.", "xp": 15},
                            {"id": 710, "type": "fill_in_the_blank", "question": "Ustedes ___ (ser) bienvenidos a nuestro hotel.", "options": None, "correct_answer": "son", "explanation": "'Ustedes son'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ser_uso_identidad",
                        "title": "SER : Emploi pour l'identité et la profession",
                        "questions": [
                            {"id": 711, "type": "multiple_choice", "question": "Mi hermano ___ médico en el hospital central.", "options": ["es", "está", "tiene", "hay"], "correct_answer": "es", "explanation": "La profession s'exprime avec le verbe SER.", "xp": 15},
                            {"id": 712, "type": "fill_in_the_blank", "question": "Yo ___ (ser) Carmen y esta es mi hermana.", "options": None, "correct_answer": "soy", "explanation": "L'identité se formule avec SER : 'Yo soy'.", "xp": 15},
                            {"id": 713, "type": "multiple_choice", "question": "¿Vosotras ___ abogadas?", "options": ["sois", "estáis", "tenéis", "erais"], "correct_answer": "sois", "explanation": "Profession avec vosotros : 'sois'.", "xp": 15},
                            {"id": 714, "type": "fill_in_the_blank", "question": "Mi padre ___ (ser) arquitecto.", "options": None, "correct_answer": "es", "explanation": "SER + profession sans article.", "xp": 15},
                            {"id": 715, "type": "multiple_choice", "question": "Nosotros ___ los nuevos alumnos de la clase.", "options": ["somos", "estamos", "tenemos", "hay"], "correct_answer": "somos", "explanation": "Identification des personnes : 'somos'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ser_uso_origen_nacionalidad",
                        "title": "SER : Emploi pour l'origine et la nationalité",
                        "questions": [
                            {"id": 716, "type": "fill_in_the_blank", "question": "Mis abuelos ___ (ser) de un pueblo de Andalucía.", "options": None, "correct_answer": "son", "explanation": "Origine (ser de) : 'Ellos son'.", "xp": 15},
                            {"id": 717, "type": "multiple_choice", "question": "¿De dónde ___ tú? - Soy de México.", "options": ["eres", "estás", "tienes", "vienes"], "correct_answer": "eres", "explanation": "Demander l'origine : '¿De dónde eres?'.", "xp": 15},
                            {"id": 718, "type": "fill_in_the_blank", "question": "Nosotras ___ (ser) peruanas.", "options": None, "correct_answer": "somos", "explanation": "Nationalité : 'Nosotras somos'.", "xp": 15},
                            {"id": 719, "type": "multiple_choice", "question": "Ella no ___ alemana, es suiza.", "options": ["es", "está", "tiene", "queda"], "correct_answer": "es", "explanation": "Nationalité : 'Ella es'.", "xp": 15},
                            {"id": 720, "type": "fill_in_the_blank", "question": "Yo ___ (ser) de Tokio, la capital de Japón.", "options": None, "correct_answer": "soy", "explanation": "'Yo soy de'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ser_uso_caracteristicas",
                        "title": "SER : Caractéristiques physiques et morales essentielles",
                        "questions": [
                            {"id": 721, "type": "multiple_choice", "question": "La casa de mis padres ___ muy grande y moderna.", "options": ["es", "está", "tiene", "hay"], "correct_answer": "es", "explanation": "Caractéristique intrinsèque : 'La casa es'.", "xp": 15},
                            {"id": 722, "type": "fill_in_the_blank", "question": "Pablo ___ (ser) muy alto y delgado.", "options": None, "correct_answer": "es", "explanation": "Caractéristique physique : 'Él es alto'.", "xp": 15},
                            {"id": 723, "type": "multiple_choice", "question": "Mis amigos ___ muy simpáticos y generosos.", "options": ["son", "están", "tienen", "hacen"], "correct_answer": "son", "explanation": "Traits de caractère permanents : SER.", "xp": 15},
                            {"id": 724, "type": "fill_in_the_blank", "question": "Este examen ___ (ser) fácil.", "options": None, "correct_answer": "es", "explanation": "Caractéristique de l'examen : 'es fácil'.", "xp": 15},
                            {"id": 725, "type": "multiple_choice", "question": "Las flores ___ amarillas.", "options": ["son", "están", "tienen", "quedan"], "correct_answer": "son", "explanation": "La couleur s'exprime avec SER.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ser_uso_tiempo_fecha",
                        "title": "SER : Heure, date et événements",
                        "questions": [
                            {"id": 726, "type": "fill_in_the_blank", "question": "Hoy ___ (ser) martes 14 de mayo.", "options": None, "correct_answer": "es", "explanation": "La date s'exprime avec 'Hoy es...'.", "xp": 15},
                            {"id": 727, "type": "multiple_choice", "question": "¿Qué hora ___? - Son las tres y media.", "options": ["es", "está", "tiene", "hace"], "correct_answer": "es", "explanation": "'¿Qué hora es?'.", "xp": 15},
                            {"id": 728, "type": "fill_in_the_blank", "question": "La fiesta de cumpleaños ___ (ser) en mi casa (lieu de l'événement).", "options": None, "correct_answer": "es", "explanation": "Le lieu d'un événement / d'une fête s'exprime avec SER (avoir lieu).", "xp": 15},
                            {"id": 729, "type": "multiple_choice", "question": "El concierto ___ a las nueve de la noche.", "options": ["es", "está", "tiene", "queda"], "correct_answer": "es", "explanation": "L'horaire d'un événement : 'El concierto es'.", "xp": 15},
                            {"id": 730, "type": "fill_in_the_blank", "question": "Ahora ___ (ser) la una de la tarde.", "options": None, "correct_answer": "es", "explanation": "1h00 : 'Es la una'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ser_uso_material_posesion",
                        "title": "SER : Matière, relation et possession",
                        "questions": [
                            {"id": 731, "type": "multiple_choice", "question": "La mesa ___ de madera noble.", "options": ["es", "está", "tiene", "queda"], "correct_answer": "es", "explanation": "La matière s'exprime avec SER DE.", "xp": 15},
                            {"id": 732, "type": "fill_in_the_blank", "question": "Este libro ___ (ser) de Juan.", "options": None, "correct_answer": "es", "explanation": "Possession (ser de) : 'es de Juan'.", "xp": 15},
                            {"id": 733, "type": "multiple_choice", "question": "Aquellas llaves ___ mías.", "options": ["son", "están", "tienen", "hacen"], "correct_answer": "son", "explanation": "Possession avec pronom possessif : SER.", "xp": 15},
                            {"id": 734, "type": "fill_in_the_blank", "question": "La camisa ___ (ser) de algodón 100%.", "options": None, "correct_answer": "es", "explanation": "Matière : 'es de algodón'.", "xp": 15},
                            {"id": 735, "type": "multiple_choice", "question": "María y Laura ___ hermanas.", "options": ["son", "están", "tienen", "hacen"], "correct_answer": "son", "explanation": "Lien de parenté / relation : SER.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ser_repaso_global",
                        "title": "SER : Synthèse et révision globale",
                        "questions": [
                            {"id": 736, "type": "fill_in_the_blank", "question": "¿Quién ___ (ser) ese chico? - Es mi primo.", "options": None, "correct_answer": "es", "explanation": "Identification : '¿Quién es?'.", "xp": 15},
                            {"id": 737, "type": "multiple_choice", "question": "Vosotros ___ los responsables de la organización.", "options": ["sois", "somos", "estáis", "son"], "correct_answer": "sois", "explanation": "Vosotros sois.", "xp": 15},
                            {"id": 738, "type": "fill_in_the_blank", "question": "El coche nuevo ___ (ser) rojo.", "options": None, "correct_answer": "es", "explanation": "Couleur : 'es rojo'.", "xp": 15},
                            {"id": 739, "type": "multiple_choice", "question": "¿Ustedes ___ de Colombia?", "options": ["son", "están", "somos", "sois"], "correct_answer": "son", "explanation": "Origine avec Ustedes : 'son de'.", "xp": 15},
                            {"id": 740, "type": "fill_in_the_blank", "question": "Mi comida favorita ___ (ser) la paella.", "options": None, "correct_answer": "es", "explanation": "'Mi comida es'.", "xp": 15}
                        ]
                    },

                    # ---------------------------------------------------------
                    # SECTION 2 : CONJUGAISON & EMPLOI DU VERBE ESTAR (Quiz 9 à 16)
                    # ---------------------------------------------------------
                    {
                        "id": "a1_conj_estar_formes_1",
                        "title": "ESTAR : Conjugaison au présent (Formes singulières)",
                        "questions": [
                            {"id": 741, "type": "fill_in_the_blank", "question": "Yo ___ (estar) en mi habitación.", "options": None, "correct_answer": "estoy", "explanation": "1ère personne : 'Yo estoy' (forme en -oy).", "xp": 15},
                            {"id": 742, "type": "multiple_choice", "question": "¿Cómo ___ tú hoy?", "options": ["estás", "está", "estoy", "estamos"], "correct_answer": "estás", "explanation": "'Tú estás' (avec accent).", "xp": 15},
                            {"id": 743, "type": "fill_in_the_blank", "question": "Carlos ___ (estar) cansado de trabajar tanto.", "options": None, "correct_answer": "está", "explanation": "'Él está'.", "xp": 15},
                            {"id": 744, "type": "multiple_choice", "question": "La puerta de la entrada ___ abierta.", "options": ["está", "es", "estoy", "están"], "correct_answer": "está", "explanation": "État temporaire : 'está abierta'.", "xp": 15},
                            {"id": 745, "type": "fill_in_the_blank", "question": "Usted ___ (estar) en la lista de invitados.", "options": None, "correct_answer": "está", "explanation": "Usted está.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_estar_formes_2",
                        "title": "ESTAR : Conjugaison au présent (Formes plurielles)",
                        "questions": [
                            {"id": 746, "type": "fill_in_the_blank", "question": "Nosotros ___ (estar) listos para salir.", "options": None, "correct_answer": "estamos", "explanation": "'Nosotros estamos'.", "xp": 15},
                            {"id": 747, "type": "multiple_choice", "question": "¿Dónde ___ vosotras?", "options": ["estáis", "estamos", "están", "sois"], "correct_answer": "estáis", "explanation": "'Vosotras estáis'.", "xp": 15},
                            {"id": 748, "type": "fill_in_the_blank", "question": "Mis llaves ___ (estar) encima de la cómoda.", "options": None, "correct_answer": "están", "explanation": "'Ellas están'.", "xp": 15},
                            {"id": 749, "type": "multiple_choice", "question": "Los niños ___ en el parque jugando.", "options": ["están", "está", "son", "estamos"], "correct_answer": "están", "explanation": "Sujet pluriel : 'están'.", "xp": 15},
                            {"id": 750, "type": "fill_in_the_blank", "question": "Ustedes ___ (estar) en el lugar correcto.", "options": None, "correct_answer": "están", "explanation": "'Ustedes están'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_estar_uso_localizacion",
                        "title": "ESTAR : Localisation dans l'espace",
                        "questions": [
                            {"id": 751, "type": "multiple_choice", "question": "Madrid ___ en el centro de España.", "options": ["está", "es", "hay", "tiene"], "correct_answer": "está", "explanation": "Localisation géographique : ESTAR.", "xp": 15},
                            {"id": 752, "type": "fill_in_the_blank", "question": "El hospital ___ (estar) cerca de la estación.", "options": None, "correct_answer": "está", "explanation": "Position dans l'espace : 'está cerca'.", "xp": 15},
                            {"id": 753, "type": "multiple_choice", "question": "¿Dónde ___ los servicios / baños?", "options": ["están", "son", "hay", "quedan"], "correct_answer": "están", "explanation": "Localisation d'éléments précis au pluriel : 'están'.", "xp": 15},
                            {"id": 754, "type": "fill_in_the_blank", "question": "Yo ___ (estar) en la parada de autobús esperándote.", "options": None, "correct_answer": "estoy", "explanation": "Yo estoy.", "xp": 15},
                            {"id": 755, "type": "multiple_choice", "question": "Las gafas ___ debajo del periódico.", "options": ["están", "está", "son", "hay"], "correct_answer": "están", "explanation": "Pluriel : 'están debajo'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_estar_uso_estados_fisicos",
                        "title": "ESTAR : États physiques et passagers",
                        "questions": [
                            {"id": 756, "type": "multiple_choice", "question": "Hoy no voy a clase porque ___ muy enfermo.", "options": ["estoy", "soy", "tengo", "hago"], "correct_answer": "estoy", "explanation": "État de santé passager : 'estoy enfermo'.", "xp": 15},
                            {"id": 757, "type": "fill_in_the_blank", "question": "La sopa ___ (estar) muy caliente, espera un poco.", "options": None, "correct_answer": "está", "explanation": "État thermique résultant : 'está caliente'.", "xp": 15},
                            {"id": 758, "type": "multiple_choice", "question": "¿Tú ___ cansada después del viaje?", "options": ["estás", "eres", "tienes", "está"], "correct_answer": "estás", "explanation": "Fatigue : 'estás cansada'.", "xp": 15},
                            {"id": 759, "type": "fill_in_the_blank", "question": "La ventana ___ (estar) cerrada porque hace viento.", "options": None, "correct_answer": "está", "explanation": "État résultant d'une action : 'está cerrada'.", "xp": 15},
                            {"id": 760, "type": "multiple_choice", "question": "Los platos ya ___ limpios.", "options": ["están", "son", "tienen", "hay"], "correct_answer": "están", "explanation": "État de propreté : 'están limpios'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_estar_uso_estados_animo",
                        "title": "ESTAR : Sentiments et états d'âme",
                        "questions": [
                            {"id": 761, "type": "fill_in_the_blank", "question": "María ___ (estar) muy contenta con sus notas.", "options": None, "correct_answer": "está", "explanation": "Humeur / Joie : 'está contenta'.", "xp": 15},
                            {"id": 762, "type": "multiple_choice", "question": "Nosotros ___ preocupados por el examen.", "options": ["estamos", "somos", "tenemos", "estáis"], "correct_answer": "estamos", "explanation": "État d'inquiétude : 'estamos preocupados'.", "xp": 15},
                            {"id": 763, "type": "fill_in_the_blank", "question": "¿Por qué ___ (estar) tú tan triste?", "options": None, "correct_answer": "estás", "explanation": "Tristesse passagère : 'estás triste'.", "xp": 15},
                            {"id": 764, "type": "multiple_choice", "question": "Ellos ___ enfadados con nosotros.", "options": ["están", "son", "tienen", "hacen"], "correct_answer": "están", "explanation": "Colère : 'están enfadados'.", "xp": 15},
                            {"id": 765, "type": "fill_in_the_blank", "question": "Yo ___ (estar) muy tranquilo en este pueblo.", "options": None, "correct_answer": "estoy", "explanation": "État de sérénité : 'estoy tranquilo'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_estar_con_gerundio",
                        "title": "ESTAR + Gérondif : Action en cours d'accomplissement",
                        "questions": [
                            {"id": 766, "type": "fill_in_the_blank", "question": "Yo ___ (estar) estudiando gramática ahora mismo.", "options": None, "correct_answer": "estoy", "explanation": "Structure progressive : 'estoy estudiando'.", "xp": 15},
                            {"id": 767, "type": "multiple_choice", "question": "¿Qué ___ comiendo vosotros?", "options": ["estáis", "estamos", "están", "sois"], "correct_answer": "estáis", "explanation": "'Vosotros estáis comiendo'.", "xp": 15},
                            {"id": 768, "type": "fill_in_the_blank", "question": "Silencio, el bebé ___ (estar) durmiendo.", "options": None, "correct_answer": "está", "explanation": "'El bebé está durmiendo'.", "xp": 15},
                            {"id": 769, "type": "multiple_choice", "question": "Mis amigos ___ escuchando música en su cuarto.", "options": ["están", "son", "está", "tienen"], "correct_answer": "están", "explanation": "Pluriel : 'están escuchando'.", "xp": 15},
                            {"id": 770, "type": "fill_in_the_blank", "question": "Nosotros ___ (estar) preparando la cena.", "options": None, "correct_answer": "estamos", "explanation": "'Nosotros estamos preparando'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_estar_preposiciones_lugar",
                        "title": "ESTAR + Prépositions de lieu",
                        "questions": [
                            {"id": 771, "type": "multiple_choice", "question": "El gato ___ encima del tejado.", "options": ["está", "es", "hay", "tiene"], "correct_answer": "está", "explanation": "'Está encima de'.", "xp": 15},
                            {"id": 772, "type": "fill_in_the_blank", "question": "La farmacia ___ (estar) al lado del supermercado.", "options": None, "correct_answer": "está", "explanation": "'Está al lado de'.", "xp": 15},
                            {"id": 773, "type": "multiple_choice", "question": "Mis zapatillas ___ debajo de la cama.", "options": ["están", "está", "son", "hay"], "correct_answer": "están", "explanation": "'Están debajo de'.", "xp": 15},
                            {"id": 774, "type": "fill_in_the_blank", "question": "Nosotros ___ (estar) delante del cine esperándote.", "options": None, "correct_answer": "estamos", "explanation": "'Estamos delante de'.", "xp": 15},
                            {"id": 775, "type": "multiple_choice", "question": "¿Dónde ___ la parada del metro más cercana?", "options": ["está", "hay", "es", "queda"], "correct_answer": "está", "explanation": "Localiser un lieu défini singulier : 'está'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_estar_repaso_global",
                        "title": "ESTAR : Synthèse et révision globale",
                        "questions": [
                            {"id": 776, "type": "fill_in_the_blank", "question": "¿Cómo ___ (estar) usted, señor Gómez?", "options": None, "correct_answer": "está", "explanation": "Formule de salutation polie : '¿Cómo está usted?'.", "xp": 15},
                            {"id": 777, "type": "multiple_choice", "question": "El café ___ frío, ¿puedes calentarlo?", "options": ["está", "es", "tiene", "hay"], "correct_answer": "está", "explanation": "Température actuelle / état : 'está frío'.", "xp": 15},
                            {"id": 778, "type": "fill_in_the_blank", "question": "Todos los miembros del grupo ___ (estar) de acuerdo.", "options": None, "correct_answer": "están", "explanation": "Expression : 'estar de acuerdo'.", "xp": 15},
                            {"id": 779, "type": "multiple_choice", "question": "Yo ___ de vacaciones en la playa.", "options": ["estoy", "soy", "tengo", "hago"], "correct_answer": "estoy", "explanation": "Expression : 'estar de vacaciones'.", "xp": 15},
                            {"id": 780, "type": "fill_in_the_blank", "question": "¿Vosotros ___ (estar) listos para salir?", "options": None, "correct_answer": "estáis", "explanation": "'Estar listo' = être prêt.", "xp": 15}
                        ]
                    },

                    # ---------------------------------------------------------
                    # SECTION 3 : DISTINCTION SER vs ESTAR (Quiz 17 à 24)
                    # ---------------------------------------------------------
                    {
                        "id": "a1_conj_ser_vs_estar_1",
                        "title": "SER vs ESTAR : Nature permanente vs État temporaire",
                        "questions": [
                            {"id": 781, "type": "multiple_choice", "question": "Mi hermano ___ profesor (nature/métier) y hoy ___ enfermo (état passager).", "options": ["es / está", "está / es", "es / es", "está / está"], "correct_answer": "es / está", "explanation": "Profession = SER, maladie temporaire = ESTAR.", "xp": 15},
                            {"id": 782, "type": "fill_in_the_blank", "question": "La nieve ___ (ser/estar) blanca.", "options": None, "correct_answer": "es", "explanation": "Caractéristique naturelle permanente : SER.", "xp": 15},
                            {"id": 783, "type": "multiple_choice", "question": "La sopa ___ muy buena hoy.", "options": ["está", "es", "hay", "tiene"], "correct_answer": "está", "explanation": "Appréciation gustative ponctuelle : ESTAR.", "xp": 15},
                            {"id": 784, "type": "fill_in_the_blank", "question": "Mi abuela ___ (ser/estar) una persona muy generosa.", "options": None, "correct_answer": "es", "explanation": "Trait de personnalité : SER.", "xp": 15},
                            {"id": 785, "type": "multiple_choice", "question": "El coche no arranca porque ___ roto.", "options": ["está", "es", "tiene", "hay"], "correct_answer": "está", "explanation": "État de l'objet : 'está roto' (cassé).", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ser_vs_estar_2",
                        "title": "SER vs ESTAR : Changement de sens des adjectifs (Partie 1)",
                        "questions": [
                            {"id": 786, "type": "multiple_choice", "question": "'Ser listo' signifie :", "options": ["Être intelligent / astucieux", "Être prêt", "Être rapide", "Être fatigué"], "correct_answer": "Être intelligent / astucieux", "explanation": "Ser listo = Intelligent. Estar listo = Être prêt.", "xp": 15},
                            {"id": 787, "type": "fill_in_the_blank", "question": "No puedo salir todavía, no ___ (estar) lista (prête).", "options": None, "correct_answer": "estoy", "explanation": "Estar listo/a = Être prêt(e).", "xp": 15},
                            {"id": 788, "type": "multiple_choice", "question": "'Esta manzana está verde' signifie que la pomme :", "options": ["N'est pas mûre", "Est d'une race de couleur verte", "Est pourrie", "Est cuite"], "correct_answer": "N'est pas mûre", "explanation": "Estar verde = Ne pas être mûr (état). Ser verde = De couleur verte.", "xp": 15},
                            {"id": 789, "type": "fill_in_the_blank", "question": "La hierba del campo ___ (ser) verde (couleur).", "options": None, "correct_answer": "es", "explanation": "Couleur constitutive : SER.", "xp": 15},
                            {"id": 790, "type": "multiple_choice", "question": "Ese chico ___ muy listo, siempre saca las mejores notas.", "options": ["es", "está", "tiene", "hace"], "correct_answer": "es", "explanation": "Intelligence : 'es listo'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ser_vs_estar_3",
                        "title": "SER vs ESTAR : Changement de sens des adjectifs (Partie 2)",
                        "questions": [
                            {"id": 791, "type": "multiple_choice", "question": "'Ser rico' signifie :", "options": ["Avoir beaucoup d'argent (fortuné)", "Avoir bon goût (plat)", "Être généreux", "Être joyeux"], "correct_answer": "Avoir beaucoup d'argent (fortuné)", "explanation": "Ser rico = Avoir de la fortune. Estar rico = Être délicieux (nourriture).", "xp": 15},
                            {"id": 792, "type": "fill_in_the_blank", "question": "¡Este pastel ___ (ser/estar) riquísimo! (goût)", "options": None, "correct_answer": "está", "explanation": "Goût d'un aliment au moment présent : ESTAR.", "xp": 15},
                            {"id": 793, "type": "multiple_choice", "question": "'Juan es aburrido' signifie :", "options": ["Juan est ennuyeux (comme personne)", "Juan s'ennuie en ce moment", "Juan est fatigué", "Juan est drôle"], "correct_answer": "Juan est ennuyeux (comme personne)", "explanation": "Ser aburrido = Rendre ennuyeux. Estar aburrido = S'ennuyer.", "xp": 15},
                            {"id": 794, "type": "fill_in_the_blank", "question": "En la clase de hoy yo ___ (ser/estar) muy aburrido (je m'ennuie).", "options": None, "correct_answer": "estoy", "explanation": "Sentiment passager d'ennui : ESTAR.", "xp": 15},
                            {"id": 795, "type": "multiple_choice", "question": "Bill Gates ___ muy rico.", "options": ["es", "está", "tiene", "queda"], "correct_answer": "es", "explanation": "Richesse financière : SER.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ser_vs_estar_4",
                        "title": "SER vs ESTAR : Emplacement d'objets vs Lieu d'événements",
                        "questions": [
                            {"id": 796, "type": "multiple_choice", "question": "El museo ___ en el centro, pero la conferencia ___ en el hotel.", "options": ["está / es", "es / está", "está / está", "es / es"], "correct_answer": "está / es", "explanation": "Bâtiment/objet physique = ESTAR, événement (concurrence/fête/conférence) = SER.", "xp": 15},
                            {"id": 797, "type": "fill_in_the_blank", "question": "La fiesta de graduación ___ (ser/estar) en la playa.", "options": None, "correct_answer": "es", "explanation": "Lieu d'un événement / fête : SER (avoir lieu).", "xp": 15},
                            {"id": 798, "type": "multiple_choice", "question": "La playa de la ciudad ___ al este.", "options": ["está", "es", "hay", "tiene"], "correct_answer": "está", "explanation": "Lieu géographique fixe : ESTAR.", "xp": 15},
                            {"id": 799, "type": "fill_in_the_blank", "question": "El partido de fútbol ___ (ser/estar) a las ocho en el estadio.", "options": None, "correct_answer": "es", "explanation": "Lieu et heure d'un match / événement : SER.", "xp": 15},
                            {"id": 800, "type": "multiple_choice", "question": "El estadio de fútbol ___ al final de la avenida.", "options": ["está", "es", "hay", "queda"], "correct_answer": "está", "explanation": "Localisation du monument physique : ESTAR.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ser_vs_estar_5",
                        "title": "SER vs ESTAR : Nationalité / Origine vs Présence ponctuelle",
                        "questions": [
                            {"id": 801, "type": "multiple_choice", "question": "Yo ___ español, pero ahora ___ en Francia por trabajo.", "options": ["soy / estoy", "estoy / soy", "soy / soy", "estoy / estoy"], "correct_answer": "soy / estoy", "explanation": "Nationalité = SER, séjour/lieu temporaire = ESTAR.", "xp": 15},
                            {"id": 802, "type": "fill_in_the_blank", "question": "Ellos ___ (ser) de México pero este mes están en Madrid.", "options": None, "correct_answer": "son", "explanation": "Origine : 'son de México'.", "xp": 15},
                            {"id": 803, "type": "multiple_choice", "question": "¿Dónde ___ tú ahora mismo? - En mi casa.", "options": ["estás", "eres", "tienes", "haces"], "correct_answer": "estás", "explanation": "Lieu actuel : ESTAR.", "xp": 15},
                            {"id": 804, "type": "fill_in_the_blank", "question": "¿De qué país ___ (ser) vosotros?", "options": None, "correct_answer": "sois", "explanation": "Pays d'origine : SER.", "xp": 15},
                            {"id": 805, "type": "multiple_choice", "question": "Nosotros ___ en el aeropuerto esperando el vuelo.", "options": ["estamos", "somos", "tenemos", "hay"], "correct_answer": "estamos", "explanation": "Lieu où l'on se trouve : ESTAR.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ser_vs_estar_6",
                        "title": "SER vs ESTAR : Jugements et appréciations",
                        "questions": [
                            {"id": 806, "type": "multiple_choice", "question": "Este ejercicio ___ muy difícil.", "options": ["es", "está", "tiene", "hay"], "correct_answer": "es", "explanation": "Évaluation intrinsèque : 'es difícil'.", "xp": 15},
                            {"id": 807, "type": "fill_in_the_blank", "question": "¡Qué guapa ___ (estar) hoy con ese vestido!", "options": None, "correct_answer": "estás", "explanation": "Compliment sur l'apparence actuelle / ponctuelle : ESTAR.", "xp": 15},
                            {"id": 808, "type": "multiple_choice", "question": "Ella ___ una modelo profesional (très belle en général).", "options": ["es muy guapa", "está muy guapa", "tiene muy guapa", "hace muy guapa"], "correct_answer": "es muy guapa", "explanation": "Beauté constitutive : SER guapo/a.", "xp": 15},
                            {"id": 809, "type": "fill_in_the_blank", "question": "La paella de este restaurante ___ (ser) famosa en toda la ciudad.", "options": None, "correct_answer": "es", "explanation": "Notoriété / réputation : SER.", "xp": 15},
                            {"id": 810, "type": "multiple_choice", "question": "El café ___ amargo sin azúcar.", "options": ["es", "está", "tiene", "hay"], "correct_answer": "es", "explanation": "Propriété générale du café : SER.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ser_vs_estar_7",
                        "title": "SER vs ESTAR : Contrastes en contexte de dialogue",
                        "questions": [
                            {"id": 811, "type": "multiple_choice", "question": "- ¿Quién ___ ese hombre? - ___ mi tío.", "options": ["es / Es", "está / Está", "es / Está", "está / Es"], "correct_answer": "es / Es", "explanation": "Identification : SER.", "xp": 15},
                            {"id": 812, "type": "fill_in_the_blank", "question": "- ¿Dónde ___ (estar) tu tío? - En el jardín.", "options": None, "correct_answer": "está", "explanation": "Localisation : ESTAR.", "xp": 15},
                            {"id": 813, "type": "multiple_choice", "question": "- ¿Cómo ___ el examen? - ___ muy nervioso.", "options": ["estás / Estoy", "eres / Soy", "es / Es", "está / Está"], "correct_answer": "estás / Estoy", "explanation": "État émotionnel : ESTAR.", "xp": 15},
                            {"id": 814, "type": "fill_in_the_blank", "question": "- ¿De qué material ___ (ser) tus zapatos? - De cuero.", "options": None, "correct_answer": "son", "explanation": "Matière : SER.", "xp": 15},
                            {"id": 815, "type": "multiple_choice", "question": "- ¿La puerta del garaje ___ cerrada? - Sí.", "options": ["está", "es", "tiene", "hay"], "correct_answer": "está", "explanation": "État de la porte : ESTAR.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ser_vs_estar_8",
                        "title": "SER vs ESTAR : Grand test récapitulatif",
                        "questions": [
                            {"id": 816, "type": "multiple_choice", "question": "Mi abuelo ___ muy viejo, pero hoy ___ lleno de energía.", "options": ["es / está", "está / es", "es / es", "está / está"], "correct_answer": "es / está", "explanation": "Âge/caractéristique = SER, forme/énergie actuelle = ESTAR.", "xp": 15},
                            {"id": 817, "type": "fill_in_the_blank", "question": "La reunión ___ (ser) a las diez en la sala dos.", "options": None, "correct_answer": "es", "explanation": "Événement : SER.", "xp": 15},
                            {"id": 818, "type": "multiple_choice", "question": "La sala dos ___ en la segunda planta.", "options": ["está", "es", "hay", "tiene"], "correct_answer": "está", "explanation": "Localisation spatiale du lieu physique : ESTAR.", "xp": 15},
                            {"id": 819, "type": "fill_in_the_blank", "question": "Nosotros ___ (ser) franceses y ahora estamos aprendiendo español.", "options": None, "correct_answer": "somos", "explanation": "Nationalité : SER.", "xp": 15},
                            {"id": 820, "type": "multiple_choice", "question": "El agua del mar ___ muy fría esta mañana.", "options": ["está", "es", "hay", "tiene"], "correct_answer": "está", "explanation": "État thermique temporaire : ESTAR.", "xp": 15}
                        ]
                    },

                    # ---------------------------------------------------------
                    # SECTION 4 : HAY vs ESTAR vs TENER (Quiz 25 à 32)
                    # ---------------------------------------------------------
                    {
                        "id": "a1_conj_hay_vs_estar_1",
                        "title": "HAY vs ESTAR : Existence (indéfini) vs Localisation (défini)",
                        "questions": [
                            {"id": 821, "type": "multiple_choice", "question": "En este barrio ___ una farmacia de guardia.", "options": ["hay", "está", "es", "tiene"], "correct_answer": "hay", "explanation": "Article indéfini ('una farmacia') -> HAY (existence).", "xp": 15},
                            {"id": 822, "type": "fill_in_the_blank", "question": "La farmacia de guardia ___ al lado del hospital (verbe estar).", "options": None, "correct_answer": "está", "explanation": "Article défini ('La farmacia') -> ESTAR (localisation).", "xp": 15},
                            {"id": 823, "type": "multiple_choice", "question": "¿Dónde ___ los libros de español?", "options": ["están", "hay", "son", "tienen"], "correct_answer": "están", "explanation": "'Los libros' (défini pluriel) -> están.", "xp": 15},
                            {"id": 824, "type": "fill_in_the_blank", "question": "En la biblioteca ___ (haber) muchos libros interesantes.", "options": None, "correct_answer": "hay", "explanation": "Quantificateur indéfini ('muchos libros') -> HAY.", "xp": 15},
                            {"id": 825, "type": "multiple_choice", "question": "En la mesa ___ dos vasos de agua.", "options": ["hay", "están", "son", "tienen"], "correct_answer": "hay", "explanation": "Numéral/quantité -> HAY.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_hay_vs_estar_2",
                        "title": "HAY vs ESTAR : Noms sans article vs Déterminants définis",
                        "questions": [
                            {"id": 826, "type": "multiple_choice", "question": "No ___ leche en la nevera.", "options": ["hay", "está", "es", "tiene"], "correct_answer": "hay", "explanation": "Nom indénombrable sans article -> HAY.", "xp": 15},
                            {"id": 827, "type": "fill_in_the_blank", "question": "La botella de leche ___ (estar) dentro del frigorífico.", "options": None, "correct_answer": "está", "explanation": "Sujet défini 'La botella' -> está.", "xp": 15},
                            {"id": 828, "type": "multiple_choice", "question": "¿___ algún médico en la sala?", "options": ["Hay", "Está", "Es", "Tiene"], "correct_answer": "Hay", "explanation": "Indéfini 'algún' -> HAY.", "xp": 15},
                            {"id": 829, "type": "fill_in_the_blank", "question": "El doctor López ___ en su consulta (verbe estar).", "options": None, "correct_answer": "está", "explanation": "Personne identifiée par son nom -> está.", "xp": 15},
                            {"id": 830, "type": "multiple_choice", "question": "En el centro comercial ___ muchas tiendas.", "options": ["hay", "están", "son", "tienen"], "correct_answer": "hay", "explanation": "'Muchas tiendas' -> HAY.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_tener_vs_hay_1",
                        "title": "TENER vs HAY : Possession avec sujet vs Existence impersonnelle",
                        "questions": [
                            {"id": 831, "type": "multiple_choice", "question": "Yo ___ dos hermanos y un perro.", "options": ["tengo", "hay", "estoy", "soy"], "correct_answer": "tengo", "explanation": "Possession personnelle (sujet 'Yo') -> TENER.", "xp": 15},
                            {"id": 832, "type": "fill_in_the_blank", "question": "En mi familia ___ (haber) cinco personas.", "options": None, "correct_answer": "hay", "explanation": "Existence globale impersonnelle -> HAY.", "xp": 15},
                            {"id": 833, "type": "multiple_choice", "question": "¿Cuántos años ___ tú?", "options": ["tienes", "hay", "estás", "eres"], "correct_answer": "tienes", "explanation": "Âge d'une personne -> TENER : '¿Cuántos años tienes?'.", "xp": 15},
                            {"id": 834, "type": "fill_in_the_blank", "question": "En el calendario ___ (haber) doce meses.", "options": None, "correct_answer": "hay", "explanation": "Constat d'existence impersonnel -> HAY.", "xp": 15},
                            {"id": 835, "type": "multiple_choice", "question": "Mi casa ___ un jardín muy grande.", "options": ["tiene", "hay", "está", "es"], "correct_answer": "tiene", "explanation": "Le sujet grammatical est 'Mi casa' -> TENER.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_tener_formes_1",
                        "title": "TENER : Conjugaison complète au présent (G-diphtongue)",
                        "questions": [
                            {"id": 836, "type": "fill_in_the_blank", "question": "Yo ___ (tener) un coche nuevo.", "options": None, "correct_answer": "tengo", "explanation": "1ère personne irrégulière en -go : 'Yo tengo'.", "xp": 15},
                            {"id": 837, "type": "multiple_choice", "question": "¿Tú ___ tiempo para ayudarme?", "options": ["tienes", "tiene", "tenemos", "tenéis"], "correct_answer": "tienes", "explanation": "Diphtongue e -> ie : 'Tú tienes'.", "xp": 15},
                            {"id": 838, "type": "fill_in_the_blank", "question": "Ella ___ (tener) fiebre alta.", "options": None, "correct_answer": "tiene", "explanation": "'Ella tiene'.", "xp": 15},
                            {"id": 839, "type": "multiple_choice", "question": "Nosotros no ___ dinero suelto.", "options": ["tenemos", "tienen", "tenéis", "tengo"], "correct_answer": "tenemos", "explanation": "Forme régulière pour nosotros : 'tenemos'.", "xp": 15},
                            {"id": 840, "type": "fill_in_the_blank", "question": "Vosotros ___ (tener) una casa preciosa.", "options": None, "correct_answer": "tenéis", "explanation": "'Vosotros tenéis'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_tener_idiomatismes",
                        "title": "Expressions idiomatiques avec TENER (Hambre, Sed, Frío, Miedo)",
                        "questions": [
                            {"id": 841, "type": "multiple_choice", "question": "Son las dos de la tarde, yo ___ mucha hambre.", "options": ["tengo", "estoy", "soy", "hago"], "correct_answer": "tengo", "explanation": "Tener hambre = Avoir faim.", "xp": 15},
                            {"id": 842, "type": "fill_in_the_blank", "question": "Si tienes sed, debes ___ agua (boire).", "options": None, "correct_answer": "beber", "explanation": "Tener sed = Avoir soif.", "xp": 15},
                            {"id": 843, "type": "multiple_choice", "question": "En invierno nosotros siempre ___ frío.", "options": ["tenemos", "estamos", "somos", "hacemos"], "correct_answer": "tenemos", "explanation": "Tener frío = Avoir froid.", "xp": 15},
                            {"id": 844, "type": "fill_in_the_blank", "question": "Los niños ___ (tener) miedo a la oscuridad.", "options": None, "correct_answer": "tienen", "explanation": "Tener miedo = Avoir peur.", "xp": 15},
                            {"id": 845, "type": "multiple_choice", "question": "¿Tú ___ prisa o podemos hablar?", "options": ["tienes", "estás", "eres", "haces"], "correct_answer": "tienes", "explanation": "Tener prisa = Être pressé.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_tener_que_infinitivo",
                        "title": "Obligation personnelle : TENER QUE + Infinitif",
                        "questions": [
                            {"id": 846, "type": "fill_in_the_blank", "question": "Yo ___ (tener) que levantarme temprano mañana.", "options": None, "correct_answer": "tengo", "explanation": "Yo tengo que + infinitif.", "xp": 15},
                            {"id": 847, "type": "multiple_choice", "question": "¿Qué ___ que hacer tú esta tarde?", "options": ["tienes", "tiene", "tenemos", "tienen"], "correct_answer": "tienes", "explanation": "Tú tienes que...", "xp": 15},
                            {"id": 848, "type": "fill_in_the_blank", "question": "Usted ___ (tener) que firmar este documento.", "options": None, "correct_answer": "tiene", "explanation": "Usted tiene que...", "xp": 15},
                            {"id": 849, "type": "multiple_choice", "question": "Nosotros tenemos que ___ para el examen.", "options": ["estudiar", "estudiamos", "estudia", "estudian"], "correct_answer": "estudiar", "explanation": "Après 'tener que', verbe toujours à l'infinitif.", "xp": 15},
                            {"id": 850, "type": "fill_in_the_blank", "question": "Ellos ___ (tener) que comprar los billetes hoy.", "options": None, "correct_answer": "tienen", "explanation": "Ellos tienen que...", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_hay_que_infinitivo",
                        "title": "Obligation impersonnelle : HAY QUE + Infinitif",
                        "questions": [
                            {"id": 851, "type": "multiple_choice", "question": "Para hablar bien español, ___ practicar a diario.", "options": ["hay que", "tiene que", "está que", "es que"], "correct_answer": "hay que", "explanation": "'Hay que + infinitif' exprime une nécessité générale sans sujet précis.", "xp": 15},
                            {"id": 852, "type": "fill_in_the_blank", "question": "En el museo no ___ que hacer fotos con flash (falloir).", "options": None, "correct_answer": "hay", "explanation": "'No hay que...'.", "xp": 15},
                            {"id": 853, "type": "multiple_choice", "question": "Para viajar al extranjero ___ tener el pasaporte en regla.", "options": ["hay que", "tiene que", "son que", "está que"], "correct_answer": "hay que", "explanation": "'Hay que' = Il faut.", "xp": 15},
                            {"id": 854, "type": "fill_in_the_blank", "question": "Hay que ___ (comer) fruta todos los días.", "options": None, "correct_answer": "comer", "explanation": "Infinitif obligatoire après 'hay que'.", "xp": 15},
                            {"id": 855, "type": "multiple_choice", "question": "La diferencia entre 'tienes que' y 'hay que' es que 'hay que' :", "options": ["Es impersonal (para todo el mundo)", "Solo se usa con 'yo'", "Significa tener posesión", "Solo se usa en pasado"], "correct_answer": "Es impersonal (para todo el mundo)", "explanation": "'Hay que' n'a pas de sujet défini.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_hay_estar_tener_triada",
                        "title": "Le trio : HAY / ESTAR / TENER en comparaison",
                        "questions": [
                            {"id": 856, "type": "multiple_choice", "question": "En mi habitación ___ una cama, la cama ___ limpia y yo ___ sueño.", "options": ["hay / está / tengo", "está / es / hay", "tiene / está / soy", "hay / es / estoy"], "correct_answer": "hay / está / tengo", "explanation": "Existence ('hay una cama') / État ('está limpia') / Sensation ('tengo sueño').", "xp": 15},
                            {"id": 857, "type": "fill_in_the_blank", "question": "El profesor ___ en clase y nosotros tenemos una duda (verbe estar).", "options": None, "correct_answer": "está", "explanation": "Localisation du professeur : está.", "xp": 15},
                            {"id": 858, "type": "multiple_choice", "question": "¿Cuántas paradas de metro ___ en esta línea?", "options": ["hay", "están", "tienen", "son"], "correct_answer": "hay", "explanation": "Quantité globale : HAY.", "xp": 15},
                            {"id": 859, "type": "fill_in_the_blank", "question": "Nosotros ___ (tener) tres entradas para el cine.", "options": None, "correct_answer": "tenemos", "explanation": "Possession : tenemos.", "xp": 15},
                            {"id": 860, "type": "multiple_choice", "question": "Las llaves ___ en el bolso que ___ en la entrada.", "options": ["están / está", "hay / tiene", "son / es", "tienen / hay"], "correct_answer": "están / está", "explanation": "Localisation des deux objets définis : están / está.", "xp": 15}
                        ]
                    },

                    # ---------------------------------------------------------
                    # SECTION 5 : LES VERBES RÉGULIERS EN -AR (Quiz 33 à 41)
                    # ---------------------------------------------------------
                    {
                        "id": "a1_conj_ar_hablar_1",
                        "title": "Verbes en -AR : Modèle HABLAR",
                        "questions": [
                            {"id": 861, "type": "fill_in_the_blank", "question": "Yo ___ (hablar) tres idiomas con fluidez.", "options": None, "correct_answer": "hablo", "explanation": "Yo hablo (terminaison -o).", "xp": 15},
                            {"id": 862, "type": "multiple_choice", "question": "¿Tú ___ español con tus amigos?", "options": ["hablas", "habla", "hablo", "habláis"], "correct_answer": "hablas", "explanation": "Tú hablas (terminaison -as).", "xp": 15},
                            {"id": 863, "type": "fill_in_the_blank", "question": "Él ___ (hablar) muy rápido.", "options": None, "correct_answer": "habla", "explanation": "Él habla (terminaison -a).", "xp": 15},
                            {"id": 864, "type": "multiple_choice", "question": "Nosotros ___ por teléfono todos los días.", "options": ["hablamos", "hablan", "habláis", "hablo"], "correct_answer": "hablamos", "explanation": "Nosotros hablamos (terminaison -amos).", "xp": 15},
                            {"id": 865, "type": "fill_in_the_blank", "question": "Ellos ___ (hablar) con el recepcionista.", "options": None, "correct_answer": "hablan", "explanation": "Ellos hablan (terminaison -an).", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ar_trabajar_estudiar",
                        "title": "Verbes en -AR : TRABAJAR et ESTUDIAR",
                        "questions": [
                            {"id": 866, "type": "fill_in_the_blank", "question": "Yo ___ (trabajar) en una empresa internacional.", "options": None, "correct_answer": "trabajo", "explanation": "Yo trabajo.", "xp": 15},
                            {"id": 867, "type": "multiple_choice", "question": "¿Dónde ___ tú los fines de semana?", "options": ["trabajas", "trabaja", "trabajamos", "trabajáis"], "correct_answer": "trabajas", "explanation": "Tú trabajas.", "xp": 15},
                            {"id": 868, "type": "fill_in_the_blank", "question": "Ana ___ (estudiar) medicina en la universidad.", "options": None, "correct_answer": "estudia", "explanation": "Ella estudia.", "xp": 15},
                            {"id": 869, "type": "multiple_choice", "question": "Nosotros ___ español en la academia.", "options": ["estudiamos", "estudian", "estudio", "estudiáis"], "correct_answer": "estudiamos", "explanation": "Nosotros estudiamos.", "xp": 15},
                            {"id": 870, "type": "fill_in_the_blank", "question": "Mis hermanos ___ (trabajar) desde casa.", "options": None, "correct_answer": "trabajan", "explanation": "Ellos trabajan.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ar_escuchar_mirar",
                        "title": "Verbes en -AR : ESCUCHAR et MIRAR",
                        "questions": [
                            {"id": 871, "type": "fill_in_the_blank", "question": "Yo ___ (escuchar) la radio por las mañanas.", "options": None, "correct_answer": "escucho", "explanation": "Yo escucho.", "xp": 15},
                            {"id": 872, "type": "multiple_choice", "question": "¿Qué programa ___ vosotros en la televisión?", "options": ["miráis", "miran", "miramos", "miras"], "correct_answer": "miráis", "explanation": "Vosotros miráis (terminaison -áis).", "xp": 15},
                            {"id": 873, "type": "fill_in_the_blank", "question": "Ella ___ (mirar) el mapa de la ciudad.", "options": None, "correct_answer": "mira", "explanation": "Ella mira.", "xp": 15},
                            {"id": 874, "type": "multiple_choice", "question": "Nosotros ___ con atención la explicación.", "options": ["escuchamos", "escuchan", "escucháis", "escucho"], "correct_answer": "escuchamos", "explanation": "Nosotros escuchamos.", "xp": 15},
                            {"id": 875, "type": "fill_in_the_blank", "question": "Los estudiantes ___ (escuchar) al profesor.", "options": None, "correct_answer": "escuchan", "explanation": "Ellos escuchan.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ar_comprar_pagar",
                        "title": "Verbes en -AR : COMPRAR et PAGAR",
                        "questions": [
                            {"id": 876, "type": "fill_in_the_blank", "question": "Yo ___ (comprar) el pan en la panadería.", "options": None, "correct_answer": "compro", "explanation": "Yo compro.", "xp": 15},
                            {"id": 877, "type": "multiple_choice", "question": "¿Cómo ___ tú la cuenta?", "options": ["pagas", "paga", "pago", "pagáis"], "correct_answer": "pagas", "explanation": "Tú pagas.", "xp": 15},
                            {"id": 878, "type": "fill_in_the_blank", "question": "Usted ___ (pagar) con tarjeta de crédito.", "options": None, "correct_answer": "paga", "explanation": "Usted paga.", "xp": 15},
                            {"id": 879, "type": "multiple_choice", "question": "Nosotros ___ fruta en el mercado central.", "options": ["compramos", "compran", "compro", "compráis"], "correct_answer": "compramos", "explanation": "Nosotros compramos.", "xp": 15},
                            {"id": 880, "type": "fill_in_the_blank", "question": "Ellos ___ (comprar) ropa en las rebajas.", "options": None, "correct_answer": "compran", "explanation": "Ellos compran.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ar_viajar_caminar",
                        "title": "Verbes en -AR : VIAJAR et CAMINAR",
                        "questions": [
                            {"id": 881, "type": "fill_in_the_blank", "question": "Yo ___ (viajar) a España todos los veranos.", "options": None, "correct_answer": "viajo", "explanation": "Yo viajo.", "xp": 15},
                            {"id": 882, "type": "multiple_choice", "question": "¿Tú ___ mucho por las tardes?", "options": ["caminas", "camina", "camino", "camináis"], "correct_answer": "caminas", "explanation": "Tú caminas.", "xp": 15},
                            {"id": 883, "type": "fill_in_the_blank", "question": "Mi abuelo ___ (caminar) una hora al día.", "options": None, "correct_answer": "camina", "explanation": "Él camina.", "xp": 15},
                            {"id": 884, "type": "multiple_choice", "question": "Nosotros ___ en tren por toda Europa.", "options": ["viajamos", "viajan", "viajáis", "viajo"], "correct_answer": "viajamos", "explanation": "Nosotros viajamos.", "xp": 15},
                            {"id": 885, "type": "fill_in_the_blank", "question": "Mis amigos ___ (viajar) en avión.", "options": None, "correct_answer": "viajan", "explanation": "Ellos viajan.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ar_cocinar_cenar_desayunar",
                        "title": "Verbes en -AR de la nourriture : COCINAR, CENAR, DESAYUNAR",
                        "questions": [
                            {"id": 886, "type": "fill_in_the_blank", "question": "Yo ___ (cocinar) pasta los domingos.", "options": None, "correct_answer": "cocino", "explanation": "Yo cocino.", "xp": 15},
                            {"id": 887, "type": "multiple_choice", "question": "¿A qué hora ___ tú por las mañanas?", "options": ["desayunas", "desayuna", "desayuno", "desayunáis"], "correct_answer": "desayunas", "explanation": "Tú desayunas.", "xp": 15},
                            {"id": 888, "type": "fill_in_the_blank", "question": "Mi familia ___ (cenar) a las nueve de la noche.", "options": None, "correct_answer": "cena", "explanation": "La familia (sujet singulier) cena.", "xp": 15},
                            {"id": 889, "type": "multiple_choice", "question": "Nosotros ___ café con tostadas.", "options": ["desayunamos", "desayunan", "desayunáis", "desayuno"], "correct_answer": "desayunamos", "explanation": "Nosotros desayunamos.", "xp": 15},
                            {"id": 890, "type": "fill_in_the_blank", "question": "¿Vosotros qué ___ (cenar) hoy?", "options": None, "correct_answer": "cenáis", "explanation": "Vosotros cenáis.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ar_bailar_cantar",
                        "title": "Verbes en -AR des loisirs : BAILAR et CANTAR",
                        "questions": [
                            {"id": 891, "type": "fill_in_the_blank", "question": "Yo ___ (bailar) salsa los viernes.", "options": None, "correct_answer": "bailo", "explanation": "Yo bailo.", "xp": 15},
                            {"id": 892, "type": "multiple_choice", "question": "¿Tú ___ en el coro del colegio?", "options": ["cantas", "canta", "canto", "cantáis"], "correct_answer": "cantas", "explanation": "Tú cantas.", "xp": 15},
                            {"id": 893, "type": "fill_in_the_blank", "question": "Ella ___ (cantar) muy bien.", "options": None, "correct_answer": "canta", "explanation": "Ella canta.", "xp": 15},
                            {"id": 894, "type": "multiple_choice", "question": "Nosotros ___ tango en la academia.", "options": ["bailamos", "bailan", "bailáis", "bailo"], "correct_answer": "bailamos", "explanation": "Nosotros bailamos.", "xp": 8},
                            {"id": 895, "type": "fill_in_the_blank", "question": "Los niños ___ (cantar) canciones infantiles.", "options": None, "correct_answer": "cantan", "explanation": "Ellos cantan.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ar_terminaciones_focus",
                        "title": "Verbes en -AR : Focus sur la grille des terminaisons (-o, -as, -a, -amos, -áis, -an)",
                        "questions": [
                            {"id": 896, "type": "multiple_choice", "question": "Quelle est la terminaison de la 2e personne du pluriel (vosotros) pour les verbes en -AR ?", "options": ["-áis", "-éis", "-ís", "-as"], "correct_answer": "-áis", "explanation": "Exemple : vosotr-os habláis.", "xp": 15},
                            {"id": 897, "type": "fill_in_the_blank", "question": "Vosotros ___ (tomar) apuntes en clase.", "options": None, "correct_answer": "tomáis", "explanation": "Vosotros tomáis.", "xp": 15},
                            {"id": 898, "type": "multiple_choice", "question": "Quelle personne correspond à la forme 'ayudan' ?", "options": ["Ellos / Ellas / Ustedes", "Nosotros", "Tú", "Yo"], "correct_answer": "Ellos / Ellas / Ustedes", "explanation": "Terminaison -an = 3e personne du pluriel.", "xp": 15},
                            {"id": 899, "type": "fill_in_the_blank", "question": "Yo ___ (buscar) mis llaves.", "options": None, "correct_answer": "busco", "explanation": "Yo busco.", "xp": 15},
                            {"id": 900, "type": "multiple_choice", "question": "¿Cuál es la forma correcta para 'nosotros' del verbo 'esperar'?", "options": ["esperamos", "esperan", "esperáis", "espero"], "correct_answer": "esperamos", "explanation": "Nosotros esperamos.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ar_repaso_global",
                        "title": "Verbes en -AR : Synthèse et phrases mélangées",
                        "questions": [
                            {"id": 901, "type": "fill_in_the_blank", "question": "Tú ___ (llegar) puntual a la cita.", "options": None, "correct_answer": "llegas", "explanation": "Tú llegas.", "xp": 15},
                            {"id": 902, "type": "multiple_choice", "question": "Ustedes ___ el camino correcto.", "options": ["preguntan", "preguntamos", "preguntas", "pregunta"], "correct_answer": "preguntan", "explanation": "Ustedes preguntan.", "xp": 15},
                            {"id": 903, "type": "fill_in_the_blank", "question": "Nosotros ___ (invitar) a nuestros amigos a casa.", "options": None, "correct_answer": "invitamos", "explanation": "Nosotros invitamos.", "xp": 15},
                            {"id": 904, "type": "multiple_choice", "question": "Yo ___ en un hotel céntrico cuando visito Madrid.", "options": ["descanso", "descansas", "descansa", "descansamos"], "correct_answer": "descanso", "explanation": "Yo descanso.", "xp": 15},
                            {"id": 905, "type": "fill_in_the_blank", "question": "Ella ___ (organizar) su agenda cada semana.", "options": None, "correct_answer": "organiza", "explanation": "Ella organiza.", "xp": 15}
                        ]
                    },

                    # ---------------------------------------------------------
                    # SECTION 6 : LES VERBES RÉGULIERS EN -ER (Quiz 42 à 50)
                    # ---------------------------------------------------------
                    {
                        "id": "a1_conj_er_comer_1",
                        "title": "Verbes en -ER : Modèle COMER",
                        "questions": [
                            {"id": 906, "type": "fill_in_the_blank", "question": "Yo ___ (comer) ensalada todos los días.", "options": None, "correct_answer": "como", "explanation": "Yo como (terminaison -o).", "xp": 15},
                            {"id": 907, "type": "multiple_choice", "question": "¿Qué ___ tú al mediodía?", "options": ["comes", "come", "como", "coméis"], "correct_answer": "comes", "explanation": "Tú comes (terminaison -es).", "xp": 15},
                            {"id": 908, "type": "fill_in_the_blank", "question": "Carlos ___ (comer) en el restaurante de la esquina.", "options": None, "correct_answer": "come", "explanation": "Él come (terminaison -e).", "xp": 15},
                            {"id": 909, "type": "multiple_choice", "question": "Nosotros ___ fruta fresca de postre.", "options": ["comemos", "comen", "coméis", "como"], "correct_answer": "comemos", "explanation": "Nosotros comemos (terminaison -emos).", "xp": 15},
                            {"id": 910, "type": "fill_in_the_blank", "question": "Ellos ___ (comer) juntos los domingos.", "options": None, "correct_answer": "comen", "explanation": "Ellos comen (terminaison -en).", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_er_beber_1",
                        "title": "Verbes en -ER : Modèle BEBER",
                        "questions": [
                            {"id": 911, "type": "fill_in_the_blank", "question": "Yo ___ (beber) dos litros de agua al día.", "options": None, "correct_answer": "bebo", "explanation": "Yo bebo.", "xp": 15},
                            {"id": 912, "type": "multiple_choice", "question": "¿Tú ___ té o café por la mañana?", "options": ["bebes", "bebe", "bebo", "bebéis"], "correct_answer": "bebes", "explanation": "Tú bebes.", "xp": 15},
                            {"id": 913, "type": "fill_in_the_blank", "question": "Él no ___ (beber) refrescos con azúcar.", "options": None, "correct_answer": "bebe", "explanation": "Él bebe.", "xp": 15},
                            {"id": 914, "type": "multiple_choice", "question": "Nosotros ___ zumo de naranja natural.", "options": ["bebemos", "beben", "bebéis", "bebo"], "correct_answer": "bebemos", "explanation": "Nosotros bebemos.", "xp": 15},
                            {"id": 915, "type": "fill_in_the_blank", "question": "¿Vosotros qué ___ (beber) para cenar?", "options": None, "correct_answer": "bebéis", "explanation": "Vosotros bebéis (terminaison -éis).", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_er_aprender_comprender",
                        "title": "Verbes en -ER : APRENDER et COMPRENDER",
                        "questions": [
                            {"id": 916, "type": "fill_in_the_blank", "question": "Yo ___ (aprender) vocabulario nuevo cada día.", "options": None, "correct_answer": "aprendo", "explanation": "Yo aprendo.", "xp": 15},
                            {"id": 917, "type": "multiple_choice", "question": "¿Tú ___ la explicación de la profesora?", "options": ["comprendes", "comprende", "comprendo", "comprendéis"], "correct_answer": "comprendes", "explanation": "Tú comprendes.", "xp": 15},
                            {"id": 918, "type": "fill_in_the_blank", "question": "Ella ___ (aprender) a tocar la guitarra.", "options": None, "correct_answer": "aprende", "explanation": "Ella aprende.", "xp": 15},
                            {"id": 919, "type": "multiple_choice", "question": "Nosotros ___ las reglas del juego.", "options": ["comprendemos", "comprenden", "comprendéis", "comprendo"], "correct_answer": "comprendemos", "explanation": "Nosotros comprendemos.", "xp": 15},
                            {"id": 920, "type": "fill_in_the_blank", "question": "Ellos ___ (aprender) español muy rápido.", "options": None, "correct_answer": "aprenden", "explanation": "Ellos aprenden.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_er_leer_1",
                        "title": "Verbes en -ER : Modèle LEER",
                        "questions": [
                            {"id": 921, "type": "fill_in_the_blank", "question": "Yo ___ (leer) el periódico por la mañana.", "options": None, "correct_answer": "leo", "explanation": "Yo leo.", "xp": 15},
                            {"id": 922, "type": "multiple_choice", "question": "¿Tú ___ novelas de misterio?", "options": ["lees", "lee", "leo", "leéis"], "correct_answer": "lees", "explanation": "Tú lees.", "xp": 15},
                            {"id": 923, "type": "fill_in_the_blank", "question": "Mi padre ___ (leer) un libro antes de dormir.", "options": None, "correct_answer": "lee", "explanation": "Él lee.", "xp": 15},
                            {"id": 924, "type": "multiple_choice", "question": "Nosotros ___ revistas en la sala de espera.", "options": ["leemos", "leen", "leéis", "leo"], "correct_answer": "leemos", "explanation": "Nosotros leemos.", "xp": 15},
                            {"id": 925, "type": "fill_in_the_blank", "question": "Los estudiantes ___ (leer) en silencio.", "options": None, "correct_answer": "leen", "explanation": "Ellos leen.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_er_correr_vender",
                        "title": "Verbes en -ER : CORRER et VENDER",
                        "questions": [
                            {"id": 926, "type": "fill_in_the_blank", "question": "Yo ___ (correr) cinco kilómetros por el parque.", "options": None, "correct_answer": "corro", "explanation": "Yo corro.", "xp": 15},
                            {"id": 927, "type": "multiple_choice", "question": "¿Qué productos ___ ustedes en su tienda?", "options": ["venden", "vendemos", "vende", "vendéis"], "correct_answer": "venden", "explanation": "Ustedes venden.", "xp": 15},
                            {"id": 928, "type": "fill_in_the_blank", "question": "Ese señor ___ (vender) periódicos en el quiosco.", "options": None, "correct_answer": "vende", "explanation": "Él vende.", "xp": 15},
                            {"id": 929, "type": "multiple_choice", "question": "Nosotros ___ maratones en primavera.", "options": ["corremos", "corren", "corréis", "corro"], "correct_answer": "corremos", "explanation": "Nosotros corremos.", "xp": 15},
                            {"id": 930, "type": "fill_in_the_blank", "question": "¿Vosotros ___ (correr) todos los fines de semana?", "options": None, "correct_answer": "corréis", "explanation": "Vosotros corréis.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_er_creer_responder",
                        "title": "Verbes en -ER : CREER et RESPONDER",
                        "questions": [
                            {"id": 931, "type": "fill_in_the_blank", "question": "Yo ___ (creer) que la respuesta es correcta.", "options": None, "correct_answer": "creo", "explanation": "Yo creo.", "xp": 15},
                            {"id": 932, "type": "multiple_choice", "question": "¿Por qué no ___ tú a mis mensajes?", "options": ["respondes", "responde", "respondo", "respondéis"], "correct_answer": "respondes", "explanation": "Tú respondes.", "xp": 15},
                            {"id": 933, "type": "fill_in_the_blank", "question": "El alumno ___ (responder) a la pregunta.", "options": None, "correct_answer": "responde", "explanation": "Él responde.", "xp": 15},
                            {"id": 934, "type": "multiple_choice", "question": "Nosotros ___ en tus posibilidades de aprobar.", "options": ["creemos", "creen", "creéis", "creo"], "correct_answer": "creemos", "explanation": "Nosotros creemos.", "xp": 15},
                            {"id": 935, "type": "fill_in_the_blank", "question": "Ellos siempre ___ (responder) rápido por correo.", "options": None, "correct_answer": "responden", "explanation": "Ellos responden.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_er_deber_romper",
                        "title": "Verbes en -ER : DEBER et ROMPER",
                        "questions": [
                            {"id": 936, "type": "fill_in_the_blank", "question": "Yo ___ (deber) estudiar más para el examen.", "options": None, "correct_answer": "debo", "explanation": "Yo debo.", "xp": 15},
                            {"id": 937, "type": "multiple_choice", "question": "Tú ___ descansar si tienes fiebre.", "options": ["debes", "debe", "debemos", "debéis"], "correct_answer": "debes", "explanation": "Tú debes.", "xp": 15},
                            {"id": 938, "type": "fill_in_the_blank", "question": "El niño siempre ___ (romper) sus juguetes.", "options": None, "correct_answer": "rompe", "explanation": "Él rompe.", "xp": 15},
                            {"id": 939, "type": "multiple_choice", "question": "Nosotros no ___ llegar tarde al trabajo.", "options": ["debemos", "deben", "debéis", "debo"], "correct_answer": "debemos", "explanation": "Nosotros debemos.", "xp": 15},
                            {"id": 940, "type": "fill_in_the_blank", "question": "¿Vosotros ___ (deber) dinero al banco?", "options": None, "correct_answer": "debéis", "explanation": "Vosotros debéis.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_er_terminaciones_focus",
                        "title": "Verbes en -ER : Focus sur la grille des terminaisons (-o, -es, -e, -emos, -éis, -en)",
                        "questions": [
                            {"id": 941, "type": "multiple_choice", "question": "Quelle est la terminaison de 'vosotros' pour les verbes en -ER ?", "options": ["-éis", "-áis", "-ís", "-es"], "correct_answer": "-éis", "explanation": "Exemple : com-éis, beb-éis.", "xp": 15},
                            {"id": 942, "type": "fill_in_the_blank", "question": "Vosotros ___ (aprender) mucho vocabulario.", "options": None, "correct_answer": "aprendéis", "explanation": "Vosotros aprendéis.", "xp": 15},
                            {"id": 943, "type": "multiple_choice", "question": "Quelle personne correspond à la forme 'meten' (verbe meter) ?", "options": ["Ellos / Ellas / Ustedes", "Nosotros", "Tú", "Yo"], "correct_answer": "Ellos / Ellas / Ustedes", "explanation": "Terminaison -en = 3e personne du pluriel.", "xp": 15},
                            {"id": 944, "type": "fill_in_the_blank", "question": "Yo ___ (prometer) llegar a tiempo.", "options": None, "correct_answer": "prometo", "explanation": "Yo prometo.", "xp": 15},
                            {"id": 945, "type": "multiple_choice", "question": "¿Cuál es la forma correcta para 'nosotros' del verbo 'temer'?", "options": ["tememos", "temen", "teméis", "temo"], "correct_answer": "tememos", "explanation": "Nosotros tememos.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_er_repaso_global",
                        "title": "Verbes en -ER : Synthèse et phrases mélangées",
                        "questions": [
                            {"id": 946, "type": "fill_in_the_blank", "question": "Tú ___ (vender) tu bicicleta vieja.", "options": None, "correct_answer": "vendes", "explanation": "Tú vendes.", "xp": 15},
                            {"id": 947, "type": "multiple_choice", "question": "Nosotros ___ la lección dos veces.", "options": ["leemos", "leen", "leéis", "leo"], "correct_answer": "leemos", "explanation": "Nosotros leemos.", "xp": 15},
                            {"id": 948, "type": "fill_in_the_blank", "question": "Ellos ___ (correr) hacia la parada de autobús.", "options": None, "correct_answer": "corren", "explanation": "Ellos corren.", "xp": 15},
                            {"id": 949, "type": "multiple_choice", "question": "Yo ___ que todo va a salir bien.", "options": ["creo", "crees", "cree", "creemos"], "correct_answer": "creo", "explanation": "Yo creo.", "xp": 15},
                            {"id": 950, "type": "fill_in_the_blank", "question": "Usted ___ (beber) mucho té verde.", "options": None, "correct_answer": "bebe", "explanation": "Usted bebe.", "xp": 15}
                        ]
                    },

                    # ---------------------------------------------------------
                    # SECTION 7 : LES VERBES RÉGULIERS EN -IR (Quiz 51 à 58)
                    # ---------------------------------------------------------
                    {
                        "id": "a1_conj_ir_vivir_1",
                        "title": "Verbes en -IR : Modèle VIVIR",
                        "questions": [
                            {"id": 951, "type": "fill_in_the_blank", "question": "Yo ___ (vivir) en el centro de la ciudad.", "options": None, "correct_answer": "vivo", "explanation": "Yo vivo (terminaison -o).", "xp": 15},
                            {"id": 952, "type": "multiple_choice", "question": "¿Dónde ___ tú?", "options": ["vives", "vive", "vivo", "vivís"], "correct_answer": "vives", "explanation": "Tú vives (terminaison -es).", "xp": 15},
                            {"id": 953, "type": "fill_in_the_blank", "question": "Mi familia ___ (vivir) en una casa de campo.", "options": None, "correct_answer": "vive", "explanation": "La familia (sujet singulier) vive.", "xp": 15},
                            {"id": 954, "type": "multiple_choice", "question": "Nosotros ___ en un piso compartido.", "options": ["vivimos", "viven", "vivís", "vivo"], "correct_answer": "vivimos", "explanation": "Nosotros vivimos (terminaison -imos).", "xp": 15},
                            {"id": 955, "type": "fill_in_the_blank", "question": "Ellos ___ (vivir) en Barcelona.", "options": None, "correct_answer": "viven", "explanation": "Ellos viven (terminaison -en).", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ir_escribir_1",
                        "title": "Verbes en -IR : Modèle ESCRIBIR",
                        "questions": [
                            {"id": 956, "type": "fill_in_the_blank", "question": "Yo ___ (escribir) una carta a mi amigo.", "options": None, "correct_answer": "escribo", "explanation": "Yo escribo.", "xp": 15},
                            {"id": 957, "type": "multiple_choice", "question": "¿Tú ___ en tu diario todos los días?", "options": ["escribes", "escribe", "escribo", "escribís"], "correct_answer": "escribes", "explanation": "Tú escribes.", "xp": 15},
                            {"id": 958, "type": "fill_in_the_blank", "question": "El autor ___ (escribir) novelas históricas.", "options": None, "correct_answer": "escribe", "explanation": "Él escribe.", "xp": 15},
                            {"id": 959, "type": "multiple_choice", "question": "Nosotros ___ correos electrónicos a los clientes.", "options": ["escribimos", "escriben", "escribís", "escribo"], "correct_answer": "escribimos", "explanation": "Nosotros escribimos.", "xp": 15},
                            {"id": 960, "type": "fill_in_the_blank", "question": "¿Vosotros ___ (escribir) con bolígrafo azul o negro?", "options": None, "correct_answer": "escribís", "explanation": "Vosotros escribís (terminaison -ís).", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ir_abrir_1",
                        "title": "Verbes en -IR : Modèle ABRIR",
                        "questions": [
                            {"id": 961, "type": "fill_in_the_blank", "question": "Yo ___ (abrir) la ventana porque hace calor.", "options": None, "correct_answer": "abro", "explanation": "Yo abro.", "xp": 15},
                            {"id": 962, "type": "multiple_choice", "question": "¿A qué hora ___ la tienda por la mañana?", "options": ["abre", "abres", "abro", "abren"], "correct_answer": "abre", "explanation": "La tienda (singulier) abre.", "xp": 15},
                            {"id": 963, "type": "fill_in_the_blank", "question": "Tú ___ (abrir) la puerta con tu llave.", "options": None, "correct_answer": "abres", "explanation": "Tú abres.", "xp": 15},
                            {"id": 964, "type": "multiple_choice", "question": "Nosotros ___ los paquetes de correos.", "options": ["abrimos", "abren", "abrís", "abro"], "correct_answer": "abrimos", "explanation": "Nosotros abrimos.", "xp": 15},
                            {"id": 965, "type": "fill_in_the_blank", "question": "Los bancos ___ (abrir) a las ocho y media.", "options": None, "correct_answer": "abren", "explanation": "Ellos abren.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ir_decidir_permitir",
                        "title": "Verbes en -IR : DECIDIR et PERMITIR",
                        "questions": [
                            {"id": 966, "type": "fill_in_the_blank", "question": "Yo ___ (decidir) qué película ver esta noche.", "options": None, "correct_answer": "decido", "explanation": "Yo decido.", "xp": 15},
                            {"id": 967, "type": "multiple_choice", "question": "El reglamento no ___ usar el móvil en clase.", "options": ["permite", "permites", "permiten", "permitimos"], "correct_answer": "permite", "explanation": "El reglamento permite.", "xp": 15},
                            {"id": 968, "type": "fill_in_the_blank", "question": "Nosotros ___ (decidir) viajar a Sevilla.", "options": None, "correct_answer": "decidimos", "explanation": "Nosotros decidimos.", "xp": 15},
                            {"id": 969, "type": "multiple_choice", "question": "¿Qué ___ tú al final?", "options": ["decides", "decide", "decido", "decidís"], "correct_answer": "decides", "explanation": "Tú decides.", "xp": 15},
                            {"id": 970, "type": "fill_in_the_blank", "question": "Mis padres no me ___ (permitir) salir hasta tarde.", "options": None, "correct_answer": "permiten", "explanation": "Ellos permiten.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ir_recibir_subir",
                        "title": "Verbes en -IR : RECIBIR et SUBIR",
                        "questions": [
                            {"id": 971, "type": "fill_in_the_blank", "question": "Yo ___ (recibir) muchas cartas por mi cumpleaños.", "options": None, "correct_answer": "recibo", "explanation": "Yo recibo.", "xp": 15},
                            {"id": 972, "type": "multiple_choice", "question": "¿Tú ___ por la escalera o en ascensor?", "options": ["subes", "sube", "subo", "subís"], "correct_answer": "subes", "explanation": "Tú subes.", "xp": 15},
                            {"id": 973, "type": "fill_in_the_blank", "question": "El autobús ___ (subir) por la colina.", "options": None, "correct_answer": "sube", "explanation": "Él sube.", "xp": 15},
                            {"id": 974, "type": "multiple_choice", "question": "Nosotros ___ al tren en el andén uno.", "options": ["subimos", "suben", "subís", "subo"], "correct_answer": "subimos", "explanation": "Nosotros subimos.", "xp": 15},
                            {"id": 975, "type": "fill_in_the_blank", "question": "Ellos ___ (recibir) buenas noticias de su familia.", "options": None, "correct_answer": "reciben", "explanation": "Ellos reciben.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ir_compartir_discutir",
                        "title": "Verbes en -IR : COMPARTIR et DISCUTIR",
                        "questions": [
                            {"id": 976, "type": "fill_in_the_blank", "question": "Yo ___ (compartir) piso con dos estudiantes.", "options": None, "correct_answer": "comparto", "explanation": "Yo comparto.", "xp": 15},
                            {"id": 977, "type": "multiple_choice", "question": "¿Por qué ___ vosotros siempre por tonterías?", "options": ["discutís", "discuten", "discutimos", "discutes"], "correct_answer": "discutís", "explanation": "Vosotros discutís.", "xp": 15},
                            {"id": 978, "type": "fill_in_the_blank", "question": "Ella ___ (compartir) sus fotos en redes sociales.", "options": None, "correct_answer": "comparte", "explanation": "Ella comparte.", "xp": 15},
                            {"id": 979, "type": "multiple_choice", "question": "Nosotros ___ el postre en el restaurante.", "options": ["compartimos", "comparten", "compartís", "comparto"], "correct_answer": "compartimos", "explanation": "Nosotros compartimos.", "xp": 15},
                            {"id": 980, "type": "fill_in_the_blank", "question": "Ellos no ___ (discutir) nunca sobre política.", "options": None, "correct_answer": "discuten", "explanation": "Ellos discuten.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ir_terminaciones_focus",
                        "title": "Verbes en -IR : Focus sur la différence -ER vs -IR (nosotros / vosotros)",
                        "questions": [
                            {"id": 981, "type": "multiple_choice", "question": "Quelle est la différence majeure de terminaison entre -ER et -IR au présent ?", "options": ["Nosotros (-emos vs -imos) et Vosotros (-éis vs -ís)", "Toutes les personnes sont différentes", "Seulement la personne 'yo'", "Il n'y a aucune différence"], "correct_answer": "Nosotros (-emos vs -imos) et Vosotros (-éis vs -ís)", "explanation": "Com-emos / Viv-imos, Com-éis / Viv-ís. Les formes yo, tú, él, ellos ont les mêmes terminaisons en -o, -es, -e, -en.", "xp": 15},
                            {"id": 982, "type": "fill_in_the_blank", "question": "Nosotros ___ (escribir) correctamente en español.", "options": None, "correct_answer": "escribimos", "explanation": "Terminaison -imos pour nous en -IR.", "xp": 15},
                            {"id": 983, "type": "multiple_choice", "question": "Vosotros ___ (abrir) la tienda a las nueve.", "options": ["abrís", "abréis", "abráis", "abren"], "correct_answer": "abrís", "explanation": "Terminaison -ís pour vosotros en -IR.", "xp": 15},
                            {"id": 984, "type": "fill_in_the_blank", "question": "Yo ___ (unir) los dos cables.", "options": None, "correct_answer": "uno", "explanation": "Yo uno.", "xp": 15},
                            {"id": 985, "type": "multiple_choice", "question": "Ustedes ___ el documento con atención.", "options": ["imprimen", "imprimimos", "imprimís", "imprime"], "correct_answer": "imprimen", "explanation": "Ustedes imprimen.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ir_repaso_global",
                        "title": "Verbes en -IR : Synthèse et phrases mélangées",
                        "questions": [
                            {"id": 986, "type": "fill_in_the_blank", "question": "Tú ___ (cumplir) años en noviembre.", "options": None, "correct_answer": "cumples", "explanation": "Tú cumples.", "xp": 15},
                            {"id": 987, "type": "multiple_choice", "question": "Nosotros ___ en una ciudad muy tranquila.", "options": ["vivimos", "viven", "vivís", "vivo"], "correct_answer": "vivimos", "explanation": "Nosotros vivimos.", "xp": 15},
                            {"id": 988, "type": "fill_in_the_blank", "question": "El dependiente ___ (añadir) el total de la compra.", "options": None, "correct_answer": "añade", "explanation": "Él añade.", "xp": 15},
                            {"id": 989, "type": "multiple_choice", "question": "Yo ___ el paquete con cuidado.", "options": ["abro", "abres", "abre", "abrimos"], "correct_answer": "abro", "explanation": "Yo abro.", "xp": 15},
                            {"id": 990, "type": "fill_in_the_blank", "question": "Ellos ___ (subir) las fotos a internet.", "options": None, "correct_answer": "suben", "explanation": "Ellos suben.", "xp": 15}
                        ]
                    },

                    # ---------------------------------------------------------
                    # SECTION 8 : GRAND BILAN DES 3 GROUPES ET DE LA GRAMMAIRE (Quiz 59 et 60)
                    # ---------------------------------------------------------
                    {
                        "id": "a1_conj_mix_tres_grupos",
                        "title": "Mix des 3 groupes réguliers (-AR, -ER, -IR)",
                        "questions": [
                            {"id": 991, "type": "multiple_choice", "question": "Yo ___ (hablar -AR) español, ___ (comer -ER) paella y ___ (vivir -IR) en Madrid.", "options": ["hablo / como / vivo", "hablas / comes / vives", "habla / come / vive", "hablamos / comemos / vivimos"], "correct_answer": "hablo / como / vivo", "explanation": "Terminaison régulière de la 1ère personne pour les 3 groupes : -o.", "xp": 15},
                            {"id": 992, "type": "fill_in_the_blank", "question": "Nosotros ___ (estudiar -AR) mucho para el examen.", "options": None, "correct_answer": "estudiamos", "explanation": "Nosotros estudiamos (-amos).", "xp": 15},
                            {"id": 993, "type": "multiple_choice", "question": "Vosotros ___ (beber -ER) agua y ___ (escribir -IR) cartas.", "options": ["bebéis / escribís", "bebís / escribéis", "beben / escriben", "bebemos / escribimos"], "correct_answer": "bebéis / escribís", "explanation": "Vosotros : -éis pour -ER et -ís pour -IR.", "xp": 15},
                            {"id": 994, "type": "fill_in_the_blank", "question": "Ellos ___ (aprender -ER) vocabulario y lo ___ (escribir -IR) en su cuaderno.", "options": None, "correct_answer": "escriben", "explanation": "Ellos aprenden / ellos escriben (terminaison -en).", "xp": 15},
                            {"id": 995, "type": "multiple_choice", "question": "Tú ___ (cocinar -AR) muy bien y siempre ___ (abrir -IR) la puerta a tus invitados.", "options": ["cocinas / abres", "cocina / abre", "cocino / abro", "cocináis / abrís"], "correct_answer": "cocinas / abres", "explanation": "Tú cocinas (-as) / tú abres (-es).", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_gran_repaso_final_a1",
                        "title": "Grand bilan final Présent A1 : Ser, Estar, Hay, Tener et Verbes réguliers",
                        "questions": [
                            {"id": 996, "type": "multiple_choice", "question": "En la mesa ___ (haber) un libro que ___ (ser) de Juan y ___ (estar) abierto.", "options": ["hay / es / está", "está / es / hay", "tiene / está / es", "hay / está / es"], "correct_answer": "hay / es / está", "explanation": "Existence indéfinie = HAY, appartenance = SER, état physique = ESTAR.", "xp": 15},
                            {"id": 997, "type": "fill_in_the_blank", "question": "Nosotros ___ (tener) que estudiar porque el examen es difícil.", "options": None, "correct_answer": "tenemos", "explanation": "Nosotros tenemos que...", "xp": 15},
                            {"id": 998, "type": "multiple_choice", "question": "María ___ (ser) médica, ___ (trabajar -AR) en el hospital y ___ (estar) cansada hoy.", "options": ["es / trabaja / está", "está / trabaja / es", "es / trabajo / está", "tiene / trabaja / es"], "correct_answer": "es / trabaja / está", "explanation": "Profession = SER, action régulière = trabaja, état = ESTAR.", "xp": 15},
                            {"id": 999, "type": "fill_in_the_blank", "question": "Yo ___ (vivir -IR) cerca de la playa y voy andando todos los días.", "options": None, "correct_answer": "vivo", "explanation": "Yo vivo.", "xp": 15},
                            {"id": 1000, "type": "multiple_choice", "question": "¿Vosotros ___ (comprender -ER) bien la diferencia entre SER y ESTAR?", "options": ["comprendéis", "comprendemos", "comprenden", "comprendes"], "correct_answer": "comprendéis", "explanation": "Vosotros comprendéis.", "xp": 15}
                        ]
                    },

                    {
                        "id": "a1_conj_diph_querer_1",
                        "title": "Diphtongue E -> IE : QUERER",
                        "questions": [
                            {"id": 1001, "type": "fill_in_the_blank", "question": "Yo ___ (querer) aprender español rápidamente.", "options": None, "correct_answer": "quiero", "explanation": "Diphtongue E -> IE : 'Yo quiero'.", "xp": 15},
                            {"id": 1002, "type": "multiple_choice", "question": "¿Qué ___ tomar tú para desayunar?", "options": ["quieres", "queres", "quiere", "queréis"], "correct_answer": "quieres", "explanation": "Tú quieres.", "xp": 15},
                            {"id": 1003, "type": "fill_in_the_blank", "question": "Ella ___ (querer) viajar a América Latina.", "options": None, "correct_answer": "quiere", "explanation": "Ella quiere.", "xp": 15},
                            {"id": 1004, "type": "multiple_choice", "question": "Nosotros ___ una mesa para cuatro personas.", "options": ["queremos", "quieremos", "quieren", "queréis"], "correct_answer": "queremos", "explanation": "Attention : 'nosotros' ne diphtongue jamais au présent.", "xp": 15},
                            {"id": 1005, "type": "fill_in_the_blank", "question": "Mis padres ___ (querer) comprar una casa nueva.", "options": None, "correct_answer": "quieren", "explanation": "Ellos quieren.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_entender_1",
                        "title": "Diphtongue E -> IE : ENTENDER",
                        "questions": [
                            {"id": 1006, "type": "fill_in_the_blank", "question": "Yo no ___ (entender) esta regla gramatical.", "options": None, "correct_answer": "entiendo", "explanation": "Yo entiendo.", "xp": 15},
                            {"id": 1007, "type": "multiple_choice", "question": "¿___ tú cuando la gente habla rápido?", "options": ["Entiendes", "Entendes", "Entiende", "Entendéis"], "correct_answer": "Entiendes", "explanation": "Tú entiendes.", "xp": 15},
                            {"id": 1008, "type": "fill_in_the_blank", "question": "El alumno ___ (entender) el ejercicio perfectamente.", "options": None, "correct_answer": "entiende", "explanation": "Él entiende.", "xp": 15},
                            {"id": 1009, "type": "multiple_choice", "question": "Nosotros ___ muy bien el italiano.", "options": ["entendemos", "entiendemos", "entienden", "entendéis"], "correct_answer": "entendemos", "explanation": "Nosotros entendemos (forme régulière).", "xp": 15},
                            {"id": 1010, "type": "fill_in_the_blank", "question": "Ellos no ___ (entender) por qué llegas tarde.", "options": None, "correct_answer": "entienden", "explanation": "Ellos entienden.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_pensar_1",
                        "title": "Diphtongue E -> IE : PENSAR",
                        "questions": [
                            {"id": 1011, "type": "fill_in_the_blank", "question": "Yo ___ (pensar) que esta es la mejor opción.", "options": None, "correct_answer": "pienso", "explanation": "Yo pienso.", "xp": 15},
                            {"id": 1012, "type": "multiple_choice", "question": "¿Qué ___ tú de esta película?", "options": ["piensas", "pensas", "piensa", "pensáis"], "correct_answer": "piensas", "explanation": "Tú piensas.", "xp": 15},
                            {"id": 1013, "type": "fill_in_the_blank", "question": "Marta ___ (pensar) cambiar de trabajo.", "options": None, "correct_answer": "piensa", "explanation": "Ella piensa.", "xp": 15},
                            {"id": 1014, "type": "multiple_choice", "question": "Nosotros ___ en nuestras próximas vacaciones.", "options": ["pensamos", "piensamos", "piensan", "pensáis"], "correct_answer": "pensamos", "explanation": "Nosotros pensamos.", "xp": 15},
                            {"id": 1015, "type": "fill_in_the_blank", "question": "¿Vosotros qué ___ (pensar) hacer hoy?", "options": None, "correct_answer": "pensáis", "explanation": "Vosotros pensáis (sans diphtongue).", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_preferir_1",
                        "title": "Diphtongue E -> IE : PREFERIR",
                        "questions": [
                            {"id": 1016, "type": "fill_in_the_blank", "question": "Yo ___ (preferir) el café con leche.", "options": None, "correct_answer": "prefiero", "explanation": "Yo prefiero.", "xp": 15},
                            {"id": 1017, "type": "multiple_choice", "question": "¿Qué ___ comer tú hoy?", "options": ["prefieres", "preferes", "prefiere", "preferís"], "correct_answer": "prefieres", "explanation": "Tú prefieres.", "xp": 15},
                            {"id": 1018, "type": "fill_in_the_blank", "question": "Usted ___ (preferir) pagar en efectivo.", "options": None, "correct_answer": "prefiere", "explanation": "Usted prefiere.", "xp": 15},
                            {"id": 1019, "type": "multiple_choice", "question": "Nosotros ___ viajar en tren.", "options": ["preferimos", "prefierimos", "prefieren", "preferís"], "correct_answer": "preferimos", "explanation": "Nosotros preferimos.", "xp": 15},
                            {"id": 1020, "type": "fill_in_the_blank", "question": "¿Vosotros ___ (preferir) té o zumo?", "options": None, "correct_answer": "preferís", "explanation": "Vosotros preferís.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_empezar_comenzar",
                        "title": "Diphtongue E -> IE : EMPEZAR et COMENZAR",
                        "questions": [
                            {"id": 1021, "type": "fill_in_the_blank", "question": "La clase ___ (empezar) a las nueve en punto.", "options": None, "correct_answer": "empieza", "explanation": "La clase empieza.", "xp": 15},
                            {"id": 1022, "type": "multiple_choice", "question": "Yo ___ a estudiar a las ocho de la mañana.", "options": ["empiezo", "empezo", "empieza", "empezamos"], "correct_answer": "empiezo", "explanation": "Yo empiezo.", "xp": 15},
                            {"id": 1023, "type": "fill_in_the_blank", "question": "El concierto ___ (comenzar) en diez minutos.", "options": None, "correct_answer": "comienza", "explanation": "El concierto comienza.", "xp": 15},
                            {"id": 1024, "type": "multiple_choice", "question": "¿A qué hora ___ vosotros a trabajar?", "options": ["empezáis", "empiezáis", "empiezan", "empezamos"], "correct_answer": "empezáis", "explanation": "Vosotros empezáis.", "xp": 15},
                            {"id": 1025, "type": "fill_in_the_blank", "question": "Nosotros ___ (comenzar) un nuevo curso hoy.", "options": None, "correct_answer": "comenzamos", "explanation": "Nosotros comenzamos.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_cerrar_1",
                        "title": "Diphtongue E -> IE : CERRAR",
                        "questions": [
                            {"id": 1026, "type": "fill_in_the_blank", "question": "Yo ___ (cerrar) la puerta con llave.", "options": None, "correct_answer": "cierro", "explanation": "Yo cierro.", "xp": 15},
                            {"id": 1027, "type": "multiple_choice", "question": "¿A qué hora ___ las tiendas en tu ciudad?", "options": ["cierran", "cerran", "cierra", "cerramos"], "correct_answer": "cierran", "explanation": "Las tiendas cierran.", "xp": 15},
                            {"id": 1028, "type": "fill_in_the_blank", "question": "¿Tú ___ (cerrar) la ventana, por favor?", "options": None, "correct_answer": "cierras", "explanation": "Tú cierras.", "xp": 15},
                            {"id": 1029, "type": "multiple_choice", "question": "Nosotros ___ el restaurante a medianoche.", "options": ["cerramos", "cierramos", "cierran", "cerráis"], "correct_answer": "cerramos", "explanation": "Nosotros cerramos.", "xp": 15},
                            {"id": 1030, "type": "fill_in_the_blank", "question": "El banco ___ (cerrar) a las dos de la tarde.", "options": None, "correct_answer": "cierra", "explanation": "El banco cierra.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_perder_1",
                        "title": "Diphtongue E -> IE : PERDER",
                        "questions": [
                            {"id": 1031, "type": "fill_in_the_blank", "question": "Yo siempre ___ (perder) las llaves del coche.", "options": None, "correct_answer": "pierdo", "explanation": "Yo pierdo.", "xp": 15},
                            {"id": 1032, "type": "multiple_choice", "question": "Si no corres, tú ___ el tren.", "options": ["pierdes", "perdes", "pierde", "perdéis"], "correct_answer": "pierdes", "explanation": "Tú pierdes.", "xp": 15},
                            {"id": 1033, "type": "fill_in_the_blank", "question": "Nuestro equipo de fútbol nunca ___ (perder) en casa.", "options": None, "correct_answer": "pierde", "explanation": "El equipo pierde.", "xp": 15},
                            {"id": 1034, "type": "multiple_choice", "question": "Nosotros no ___ la esperanza de ganar.", "options": ["perdemos", "pierdemos", "pierden", "perdéis"], "correct_answer": "perdemos", "explanation": "Nosotros perdemos.", "xp": 15},
                            {"id": 1035, "type": "fill_in_the_blank", "question": "Ellos ___ (perder) mucho tiempo en internet.", "options": None, "correct_answer": "pierden", "explanation": "Ellos pierden.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_sentir_sentirse",
                        "title": "Diphtongue E -> IE : SENTIR et SENTIRSE",
                        "questions": [
                            {"id": 1036, "type": "fill_in_the_blank", "question": "Yo me ___ (sentirse) muy feliz hoy.", "options": None, "correct_answer": "siento", "explanation": "Yo me siento.", "xp": 15},
                            {"id": 1037, "type": "multiple_choice", "question": "¿Cómo te ___ tú esta mañana?", "options": ["sientes", "sentes", "siente", "sentís"], "correct_answer": "sientes", "explanation": "Tú te sientes.", "xp": 15},
                            {"id": 1038, "type": "fill_in_the_blank", "question": "Él ___ (sentir) mucho la pérdida de su perro.", "options": None, "correct_answer": "siente", "explanation": "Él siente.", "xp": 15},
                            {"id": 1039, "type": "multiple_choice", "question": "Nosotros nos ___ muy cómodos aquí.", "options": ["sentimos", "sientimos", "sienten", "sentís"], "correct_answer": "sentimos", "explanation": "Nosotros nos sentimos.", "xp": 15},
                            {"id": 1040, "type": "fill_in_the_blank", "question": "¿Vosotros os ___ (sentirse) cansados?", "options": None, "correct_answer": "sentís", "explanation": "Vosotros os sentís.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_despertarse_1",
                        "title": "Diphtongue E -> IE : DESPERTARSE",
                        "questions": [
                            {"id": 1041, "type": "fill_in_the_blank", "question": "Yo me ___ (despertarse) a las seis y media.", "options": None, "correct_answer": "despierto", "explanation": "Yo me despierto.", "xp": 15},
                            {"id": 1042, "type": "multiple_choice", "question": "¿A qué hora te ___ tú los domingos?", "options": ["despiertas", "despertas", "despierta", "despertáis"], "correct_answer": "despiertas", "explanation": "Tú te despiertas.", "xp": 15},
                            {"id": 1043, "type": "fill_in_the_blank", "question": "El niño se ___ (despertarse) con el ruido.", "options": None, "correct_answer": "despierta", "explanation": "Él se despierta.", "xp": 15},
                            {"id": 1044, "type": "multiple_choice", "question": "Nosotros nos ___ temprano todos los días.", "options": ["despertamos", "despiertamos", "despiertan", "despertáis"], "correct_answer": "despertamos", "explanation": "Nosotros nos despertamos.", "xp": 15},
                            {"id": 1045, "type": "fill_in_the_blank", "question": "Ellos se ___ (despertarse) tarde los fines de semana.", "options": None, "correct_answer": "despiertan", "explanation": "Ellos se despiertan.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_merendar_1",
                        "title": "Diphtongue E -> IE : MERENDAR",
                        "questions": [
                            {"id": 1046, "type": "fill_in_the_blank", "question": "Yo ___ (merendar) fruta y galletas a las cinco.", "options": None, "correct_answer": "meriendo", "explanation": "Yo meriendo.", "xp": 15},
                            {"id": 1047, "type": "multiple_choice", "question": "¿Qué ___ tú por las tardes?", "options": ["meriendas", "merendas", "merienda", "merendáis"], "correct_answer": "meriendas", "explanation": "Tú meriendas.", "xp": 15},
                            {"id": 1048, "type": "fill_in_the_blank", "question": "Mi hijo ___ (merendar) un bocadillo de queso.", "options": None, "correct_answer": "merienda", "explanation": "Él merienda.", "xp": 15},
                            {"id": 1049, "type": "multiple_choice", "question": "Nosotros ___ juntos en el parque.", "options": ["merendamos", "meriendamos", "merienden", "merendáis"], "correct_answer": "merendamos", "explanation": "Nosotros merendamos.", "xp": 15},
                            {"id": 1050, "type": "fill_in_the_blank", "question": "Los niños ___ (merendar) chocolate con churros.", "options": None, "correct_answer": "meriendan", "explanation": "Ellos meriendan.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_encender_calentar",
                        "title": "Diphtongue E -> IE : ENCENDER et CALENTAR",
                        "questions": [
                            {"id": 1051, "type": "fill_in_the_blank", "question": "Yo ___ (encender) la luz del salón.", "options": None, "correct_answer": "enciendo", "explanation": "Yo enciendo.", "xp": 15},
                            {"id": 1052, "type": "multiple_choice", "question": "¿Tú ___ la sopa en el microondas?", "options": ["calientas", "calentas", "calienta", "calentáis"], "correct_answer": "calientas", "explanation": "Tú calientas.", "xp": 15},
                            {"id": 1053, "type": "fill_in_the_blank", "question": "El conserje ___ (encender) la calefacción.", "options": None, "correct_answer": "enciende", "explanation": "Él enciende.", "xp": 15},
                            {"id": 1054, "type": "multiple_choice", "question": "Nosotros ___ el horno antes de cocinar.", "options": ["calentamos", "calientamos", "calientan", "calentáis"], "correct_answer": "calentamos", "explanation": "Nosotros calentamos.", "xp": 15},
                            {"id": 1055, "type": "fill_in_the_blank", "question": "Ellos ___ (encender) el ordenador para trabajar.", "options": None, "correct_answer": "encienden", "explanation": "Ellos encienden.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_defender_atender",
                        "title": "Diphtongue E -> IE : DEFENDER et ATENDER",
                        "questions": [
                            {"id": 1056, "type": "fill_in_the_blank", "question": "El abogado ___ (defender) a su cliente.", "options": None, "correct_answer": "defiende", "explanation": "Él defiende.", "xp": 15},
                            {"id": 1057, "type": "multiple_choice", "question": "El médico ___ a los pacientes en su consulta.", "options": ["atiende", "atende", "atiendes", "atendemos"], "correct_answer": "atiende", "explanation": "Él atiende.", "xp": 15},
                            {"id": 1058, "type": "fill_in_the_blank", "question": "Yo ___ (atender) las llamadas de los clientes.", "options": None, "correct_answer": "atiendo", "explanation": "Yo atiendo.", "xp": 15},
                            {"id": 1059, "type": "multiple_choice", "question": "Nosotros ___ a las explicaciones del profesor.", "options": ["atendemos", "atiendemos", "atienden", "atendéis"], "correct_answer": "atendemos", "explanation": "Nosotros atendemos.", "xp": 15},
                            {"id": 1060, "type": "fill_in_the_blank", "question": "Los futbolistas ___ (defender) su portería.", "options": None, "correct_answer": "defienden", "explanation": "Ellos defienden.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_nevar_regla",
                        "title": "Diphtongue E -> IE : Verbes météo et impersonnels (NEVAR)",
                        "questions": [
                            {"id": 1061, "type": "multiple_choice", "question": "Comment conjugue-t-on 'nevar' à la 3e personne singulier ?", "options": ["Nieva", "Neva", "Nieve", "Nievan"], "correct_answer": "Nieva", "explanation": "Diphtongue E -> IE : 'Nieva mucho en invierno'.", "xp": 15},
                            {"id": 1062, "type": "fill_in_the_blank", "question": "En la sierra ___ (nevar) todos los años en enero.", "options": None, "correct_answer": "nieva", "explanation": "'Nieva'.", "xp": 15},
                            {"id": 1063, "type": "multiple_choice", "question": "L'infinitif de 'nieva' est :", "options": ["Nevar", "Nievar", "Never", "Niever"], "correct_answer": "Nevar", "explanation": "Le radical à l'infinitif est nev- (nevar).", "xp": 15},
                            {"id": 1064, "type": "fill_in_the_blank", "question": "Cuando ___ (nevar), las carreteras están resbaladizas.", "options": None, "correct_answer": "nieva", "explanation": "'Cuando nieva...'.", "xp": 15},
                            {"id": 1065, "type": "multiple_choice", "question": "La diphtongue E -> IE s'applique sur la syllabe :", "options": ["Tonique (accentuée)", "Atone (inaccentuée)", "La dernière terminaison", "Uniquement la 1re personne"], "correct_answer": "Tonique (accentuée)", "explanation": "Elle apparaît quand le radical porte l'accent tonique.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_e_ie_nosotros_vosotros",
                        "title": "Diphtongue E -> IE : Règle de NOSOTROS et VOSOTROS",
                        "questions": [
                            {"id": 1066, "type": "multiple_choice", "question": "Pourquoi 'nosotros' ne diphtongue-t-il pas ?", "options": ["L'accent tonique est sur la terminaison (-amos, -emos, -imos)", "C'est une exception arbitraire", "Parce que c'est un pronom pluriel", "Il diphtongue toujours"], "correct_answer": "L'accent tonique est sur la terminaison (-amos, -emos, -imos)", "explanation": "L'accent n'est pas sur le radical, donc pas de diphtongue.", "xp": 15},
                            {"id": 1067, "type": "fill_in_the_blank", "question": "Nosotros ___ (querer) aprender más idiomas.", "options": None, "correct_answer": "queremos", "explanation": "Nosotros queremos (pas de 'i').", "xp": 15},
                            {"id": 1068, "type": "multiple_choice", "question": "¿Vosotros ___ (cerrar) la tienda a las ocho?", "options": ["cerráis", "cierráis", "cierran", "cerramos"], "correct_answer": "cerráis", "explanation": "Vosotros cerráis.", "xp": 15},
                            {"id": 1069, "type": "fill_in_the_blank", "question": "Nosotros ___ (entender) todas las preguntas.", "options": None, "correct_answer": "entendemos", "explanation": "Nosotros entendemos.", "xp": 15},
                            {"id": 1070, "type": "multiple_choice", "question": "¿Vosotros ___ (pensar) venir a la fiesta?", "options": ["pensáis", "piensáis", "piensan", "pensamos"], "correct_answer": "pensáis", "explanation": "Vosotros pensáis.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_e_ie_mix_repaso",
                        "title": "Diphtongue E -> IE : Synthèse et phrases mélangées",
                        "questions": [
                            {"id": 1071, "type": "fill_in_the_blank", "question": "Yo ___ (preferir) descansar en casa.", "options": None, "correct_answer": "prefiero", "explanation": "Yo prefiero.", "xp": 15},
                            {"id": 1072, "type": "multiple_choice", "question": "El profesor ___ el examen a las diez.", "options": ["empieza", "empeza", "empiezo", "empezamos"], "correct_answer": "empieza", "explanation": "Él empieza.", "xp": 15},
                            {"id": 1073, "type": "fill_in_the_blank", "question": "¿Tú ___ (perder) el tiempo o estás estudiando?", "options": None, "correct_answer": "pierdes", "explanation": "Tú pierdes.", "xp": 15},
                            {"id": 1074, "type": "multiple_choice", "question": "Mis hermanos se ___ a las siete de la mañana.", "options": ["despiertan", "despertan", "despierta", "despertamos"], "correct_answer": "despiertan", "explanation": "Ellos se despiertan.", "xp": 15},
                            {"id": 1075, "type": "fill_in_the_blank", "question": "Nosotros ___ (pensar) que tienes razón.", "options": None, "correct_answer": "pensamos", "explanation": "Nosotros pensamos.", "xp": 15}
                        ]
                    },

                    # =========================================================
                    # SECTION 2 : DIPHTONGUES O -> UE (Quiz 16 à 30, id 1076-1150)
                    # =========================================================
                    {
                        "id": "a1_conj_diph_poder_1",
                        "title": "Diphtongue O -> UE : PODER",
                        "questions": [
                            {"id": 1076, "type": "fill_in_the_blank", "question": "Yo no ___ (poder) ir a la fiesta hoy.", "options": None, "correct_answer": "puedo", "explanation": "Diphtongue O -> UE : 'Yo puedo'.", "xp": 15},
                            {"id": 1077, "type": "multiple_choice", "question": "¿___ tú abrir la ventana, por favor?", "options": ["Puedes", "Podes", "Puede", "Podéis"], "correct_answer": "Puedes", "explanation": "Tú puedes.", "xp": 15},
                            {"id": 1078, "type": "fill_in_the_blank", "question": "Él ___ (poder) hablar cuatro lenguas.", "options": None, "correct_answer": "puede", "explanation": "Él puede.", "xp": 15},
                            {"id": 1079, "type": "multiple_choice", "question": "Nosotros ___ terminar el proyecto a tiempo.", "options": ["podemos", "puedemos", "pueden", "podéis"], "correct_answer": "podemos", "explanation": "Nosotros podemos (sans diphtongue).", "xp": 15},
                            {"id": 1080, "type": "fill_in_the_blank", "question": "Ellos no ___ (poder) entrar sin entrada.", "options": None, "correct_answer": "pueden", "explanation": "Ellos pueden.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_dormir_1",
                        "title": "Diphtongue O -> UE : DORMIR",
                        "questions": [
                            {"id": 1081, "type": "fill_in_the_blank", "question": "Yo ___ (dormir) ocho horas cada noche.", "options": None, "correct_answer": "duermo", "explanation": "Yo duermo.", "xp": 15},
                            {"id": 1082, "type": "multiple_choice", "question": "¿Cuántas horas ___ tú normalmente?", "options": ["duermes", "dormes", "duerme", "dormís"], "correct_answer": "duermes", "explanation": "Tú duermes.", "xp": 15},
                            {"id": 1083, "type": "fill_in_the_blank", "question": "El bebé ___ (dormir) tranquilamente.", "options": None, "correct_answer": "duerme", "explanation": "Él duerme.", "xp": 15},
                            {"id": 1084, "type": "multiple_choice", "question": "Nosotros ___ la siesta los domingos.", "options": ["dormimos", "duermimos", "duermen", "dormís"], "correct_answer": "dormimos", "explanation": "Nosotros dormimos.", "xp": 15},
                            {"id": 1085, "type": "fill_in_the_blank", "question": "¿Vosotros ___ (dormir) con la ventana abierta?", "options": None, "correct_answer": "dormís", "explanation": "Vosotros dormís.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_volver_1",
                        "title": "Diphtongue O -> UE : VOLVER",
                        "questions": [
                            {"id": 1086, "type": "fill_in_the_blank", "question": "Yo ___ (volver) a casa a las seis de la tarde.", "options": None, "correct_answer": "vuelvo", "explanation": "Yo vuelvo.", "xp": 15},
                            {"id": 1087, "type": "multiple_choice", "question": "¿A qué hora ___ tú del trabajo?", "options": ["vuelves", "volves", "vuelve", "volvéis"], "correct_answer": "vuelves", "explanation": "Tú vuelves.", "xp": 15},
                            {"id": 1088, "type": "fill_in_the_blank", "question": "Mi madre ___ (volver) de su viaje mañana.", "options": None, "correct_answer": "vuelve", "explanation": "Ella vuelve.", "xp": 15},
                            {"id": 1089, "type": "multiple_choice", "question": "Nosotros ___ a España cada verano.", "options": ["volvemos", "vuelvemos", "vuelven", "volvéis"], "correct_answer": "volvemos", "explanation": "Nosotros volvemos.", "xp": 15},
                            {"id": 1090, "type": "fill_in_the_blank", "question": "Ellos ___ (volver) tarde de la universidad.", "options": None, "correct_answer": "vuelven", "explanation": "Ellos vuelven.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_encontrar_1",
                        "title": "Diphtongue O -> UE : ENCONTRAR",
                        "questions": [
                            {"id": 1091, "type": "fill_in_the_blank", "question": "Yo nunca ___ (encontrar) mis llaves.", "options": None, "correct_answer": "encuentro", "explanation": "Yo encuentro.", "xp": 15},
                            {"id": 1092, "type": "multiple_choice", "question": "¿Tú ___ la solución a este problema?", "options": ["encuentras", "encontras", "encuentra", "encontráis"], "correct_answer": "encuentras", "explanation": "Tú encuentras.", "xp": 15},
                            {"id": 1093, "type": "fill_in_the_blank", "question": "Ella ___ (encontrar) una tienda genial en el centro.", "options": None, "correct_answer": "encuentra", "explanation": "Ella encuentra.", "xp": 15},
                            {"id": 1094, "type": "multiple_choice", "question": "Nosotros nos ___ en la cafetería a las cinco.", "options": ["encontramos", "encuentramos", "encuentran", "encontráis"], "correct_answer": "encontramos", "explanation": "Nosotros encontramos.", "xp": 15},
                            {"id": 1095, "type": "fill_in_the_blank", "question": "Ellos ___ (encontrar) trabajo fácilmente.", "options": None, "correct_answer": "encuentran", "explanation": "Ellos encuentran.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_costar_1",
                        "title": "Diphtongue O -> UE : COSTAR (Prix)",
                        "questions": [
                            {"id": 1096, "type": "multiple_choice", "question": "¿Cuánto ___ este libro?", "options": ["cuesta", "costa", "cuestan", "costamos"], "correct_answer": "cuesta", "explanation": "Sujet singulier (este libro) : cuesta.", "xp": 15},
                            {"id": 1097, "type": "fill_in_the_blank", "question": "Los zapatos ___ (costar) cincuenta euros.", "options": None, "correct_answer": "cuestan", "explanation": "Sujet pluriel : cuestan.", "xp": 15},
                            {"id": 1098, "type": "multiple_choice", "question": "¿Cuánto ___ las manzanas por kilo?", "options": ["cuestan", "cuesta", "costan", "costamos"], "correct_answer": "cuestan", "explanation": "Las manzanas (pluriel) cuestan.", "xp": 15},
                            {"id": 1099, "type": "fill_in_the_blank", "question": "El billete de metro ___ (costar) dos euros.", "options": None, "correct_answer": "cuesta", "explanation": "El billete cuesta.", "xp": 15},
                            {"id": 1100, "type": "multiple_choice", "question": "A mí me ___ mucho madrugar (effort).", "options": ["cuesta", "cuestan", "costo", "costamos"], "correct_answer": "cuesta", "explanation": "Costar + infinitif -> singulier 'cuesta'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_contar_recordar",
                        "title": "Diphtongue O -> UE : CONTAR et RECORDAR",
                        "questions": [
                            {"id": 1101, "type": "fill_in_the_blank", "question": "Yo ___ (contar) una historia a mis hijos.", "options": None, "correct_answer": "cuento", "explanation": "Yo cuento.", "xp": 15},
                            {"id": 1102, "type": "multiple_choice", "question": "¿Tú ___ el nombre del profesor?", "options": ["recuerdas", "recordas", "recuerda", "recordáis"], "correct_answer": "recuerdas", "explanation": "Tú recuerdas.", "xp": 15},
                            {"id": 1103, "type": "fill_in_the_blank", "question": "Él no ___ (recordar) dónde aparcó el coche.", "options": None, "correct_answer": "recuerda", "explanation": "Él recuerda.", "xp": 15},
                            {"id": 1104, "type": "multiple_choice", "question": "Nosotros ___ con tu ayuda para la fiesta.", "options": ["contamos", "cuentamos", "cuentan", "contáis"], "correct_answer": "contamos", "explanation": "Nosotros contamos.", "xp": 15},
                            {"id": 1105, "type": "fill_in_the_blank", "question": "Ellos ___ (contar) hasta diez en español.", "options": None, "correct_answer": "cuentan", "explanation": "Ellos cuentan.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_acostarse_1",
                        "title": "Diphtongue O -> UE : ACOSTARSE",
                        "questions": [
                            {"id": 1106, "type": "fill_in_the_blank", "question": "Yo me ___ (acostarse) a las diez de la noche.", "options": None, "correct_answer": "acuesto", "explanation": "Yo me acuesto.", "xp": 15},
                            {"id": 1107, "type": "multiple_choice", "question": "¿A qué hora te ___ tú normalmente?", "options": ["acuestas", "acostas", "acuesta", "acostáis"], "correct_answer": "acuestas", "explanation": "Tú te acuestas.", "xp": 15},
                            {"id": 1108, "type": "fill_in_the_blank", "question": "El niño se ___ (acostarse) temprano.", "options": None, "correct_answer": "acuesta", "explanation": "Él se acuesta.", "xp": 15},
                            {"id": 1109, "type": "multiple_choice", "question": "Nosotros nos ___ muy tarde los sábados.", "options": ["acostamos", "acuestamos", "acuestan", "acostáis"], "correct_answer": "acostamos", "explanation": "Nosotros nos acostamos.", "xp": 15},
                            {"id": 1110, "type": "fill_in_the_blank", "question": "¿Vosotros os ___ (acostarse) después de cenar?", "options": None, "correct_answer": "acostáis", "explanation": "Vosotros os acostáis.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_almorzar_1",
                        "title": "Diphtongue O -> UE : ALMORZAR",
                        "questions": [
                            {"id": 1111, "type": "fill_in_the_blank", "question": "Yo ___ (almorzar) a las dos de la tarde.", "options": None, "correct_answer": "almuerzo", "explanation": "Yo almuerzo.", "xp": 15},
                            {"id": 1112, "type": "multiple_choice", "question": "¿Dónde ___ tú los días de trabajo?", "options": ["almuerzas", "almorzas", "almuerza", "almorzáis"], "correct_answer": "almuerzas", "explanation": "Tú almuerzas.", "xp": 15},
                            {"id": 1113, "type": "fill_in_the_blank", "question": "Mi familia ___ (almorzar) junta los domingos.", "options": None, "correct_answer": "almuerza", "explanation": "La familia almuerza.", "xp": 15},
                            {"id": 1114, "type": "multiple_choice", "question": "Nosotros ___ un menú del día económico.", "options": ["almorzamos", "almuerzamos", "almuerzan", "almorzáis"], "correct_answer": "almorzamos", "explanation": "Nosotros almorzamos.", "xp": 15},
                            {"id": 1115, "type": "fill_in_the_blank", "question": "Ellos ___ (almorzar) en la terraza del restaurante.", "options": None, "correct_answer": "almuerzan", "explanation": "Ellos almuerzan.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_jugar_u_ue",
                        "title": "Diphtongue U -> UE : JUGAR (Cas unique)",
                        "questions": [
                            {"id": 1116, "type": "fill_in_the_blank", "question": "Yo ___ (jugar) al tenis los sábados.", "options": None, "correct_answer": "juego", "explanation": "Diphtongue U -> UE : 'Yo juego'.", "xp": 15},
                            {"id": 1117, "type": "multiple_choice", "question": "¿A qué deporte ___ tú?", "options": ["juegas", "jugas", "juega", "jugáis"], "correct_answer": "juegas", "explanation": "Tú juegas.", "xp": 15},
                            {"id": 1118, "type": "fill_in_the_blank", "question": "Mi hermano ___ (jugar) a los videojuegos.", "options": None, "correct_answer": "juega", "explanation": "Él juega.", "xp": 15},
                            {"id": 1119, "type": "multiple_choice", "question": "Nosotros ___ al fútbol en el parque.", "options": ["jugamos", "juegamos", "juegan", "jugáis"], "correct_answer": "jugamos", "explanation": "Nosotros jugamos (sans diphtongue).", "xp": 15},
                            {"id": 1120, "type": "fill_in_the_blank", "question": "Los niños ___ (jugar) en el jardín.", "options": None, "correct_answer": "juegan", "explanation": "Ellos juegan.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_volar_mostrar",
                        "title": "Diphtongue O -> UE : VOLAR et MOSTRAR",
                        "questions": [
                            {"id": 1121, "type": "fill_in_the_blank", "question": "El avión ___ (volar) a gran altura.", "options": None, "correct_answer": "vuela", "explanation": "El avión vuela.", "xp": 15},
                            {"id": 1122, "type": "multiple_choice", "question": "El guía turístico nos ___ el monumento.", "options": ["muestra", "mostra", "muestras", "mostramos"], "correct_answer": "muestra", "explanation": "Él muestra.", "xp": 15},
                            {"id": 1123, "type": "fill_in_the_blank", "question": "Yo te ___ (mostrar) mis fotos del viaje.", "options": None, "correct_answer": "muestro", "explanation": "Yo muestro.", "xp": 15},
                            {"id": 1124, "type": "multiple_choice", "question": "Nosotros ___ en avión hacia Madrid.", "options": ["volamos", "vuelamos", "vuelan", "voláis"], "correct_answer": "volamos", "explanation": "Nosotros volamos.", "xp": 15},
                            {"id": 1125, "type": "fill_in_the_blank", "question": "Las aves ___ (volar) hacia el sur.", "options": None, "correct_answer": "vuelan", "explanation": "Ellas vuelan.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_doler_o_ue",
                        "title": "Diphtongue O -> UE : DOLER",
                        "questions": [
                            {"id": 1126, "type": "multiple_choice", "question": "A mí me ___ la cabeza.", "options": ["duele", "dole", "duelen", "dolen"], "correct_answer": "duele", "explanation": "Sujet singulier : duele.", "xp": 15},
                            {"id": 1127, "type": "fill_in_the_blank", "question": "A ella le ___ (doler) los pies de tanto caminar.", "options": None, "correct_answer": "duelen", "explanation": "Sujet pluriel : duelen.", "xp": 15},
                            {"id": 1128, "type": "multiple_choice", "question": "¿A ti qué te ___?", "options": ["duele", "dueles", "doles", "duelen"], "correct_answer": "duele", "explanation": "¿Qué te duele? (singulier générique).", "xp": 15},
                            {"id": 1129, "type": "fill_in_the_blank", "question": "A nosotros nos ___ (doler) la espalda.", "options": None, "correct_answer": "duele", "explanation": "La espalda (singulier) -> duele.", "xp": 15},
                            {"id": 1130, "type": "multiple_choice", "question": "A los niños les ___ las muelas.", "options": ["duelen", "duele", "dolen", "dolemos"], "correct_answer": "duelen", "explanation": "Las muelas (pluriel) -> duelen.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_llover_o_ue",
                        "title": "Diphtongue O -> UE : LLOVER (Verbe impersonnel)",
                        "questions": [
                            {"id": 1131, "type": "multiple_choice", "question": "Comment se conjugue 'llover' au présent ?", "options": ["Llueve", "Llove", "Lluvia", "Llueven"], "correct_answer": "Llueve", "explanation": "Diphtongue O -> UE : 'Hoy llueve en Galicia'.", "xp": 15},
                            {"id": 1132, "type": "fill_in_the_blank", "question": "Coge el paraguas porque ___ (llover) mucho.", "options": None, "correct_answer": "llueve", "explanation": "'Llueve'.", "xp": 15},
                            {"id": 1133, "type": "multiple_choice", "question": "L'infinitif correspondant à 'llueve' est :", "options": ["Llover", "Lluver", "Lloviar", "Lluvear"], "correct_answer": "Llover", "explanation": "Infinitif : llover.", "xp": 15},
                            {"id": 1134, "type": "fill_in_the_blank", "question": "En otoño ___ (llover) casi todos los días.", "options": None, "correct_answer": "llueve", "explanation": "'Llueve'.", "xp": 15},
                            {"id": 1135, "type": "multiple_choice", "question": "'La lluvia' est un nom féminin, tandis que 'llueve' est :", "options": ["Une forme verbale conjuguée", "Un adjectif", "Un adverbe", "Une préposition"], "correct_answer": "Une forme verbale conjuguée", "explanation": "3e personne du singulier de llover.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_morir_o_ue",
                        "title": "Diphtongue O -> UE : MORIR",
                        "questions": [
                            {"id": 1136, "type": "fill_in_the_blank", "question": "Las plantas ___ (morir) si no tienen agua.", "options": None, "correct_answer": "mueren", "explanation": "Ellas mueren.", "xp": 15},
                            {"id": 1137, "type": "multiple_choice", "question": "En la película el protagonista ___ al final.", "options": ["muere", "more", "muero", "morimos"], "correct_answer": "muere", "explanation": "Él muere.", "xp": 15},
                            {"id": 1138, "type": "fill_in_the_blank", "question": "Yo me ___ (morir) de risa con este vídeo.", "options": None, "correct_answer": "muero", "explanation": "Yo me muero.", "xp": 15},
                            {"id": 1139, "type": "multiple_choice", "question": "Nosotros nos ___ de ganas de verte.", "options": ["morimos", "muerimos", "mueren", "morís"], "correct_answer": "morimos", "explanation": "Nosotros nos morimos (sans diphtongue).", "xp": 15},
                            {"id": 1140, "type": "fill_in_the_blank", "question": "¿Tú te ___ (morir) de sed? Toma agua.", "options": None, "correct_answer": "mueres", "explanation": "Tú te mueres.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_o_ue_nosotros_vosotros",
                        "title": "Diphtongue O -> UE : Maintien du radical régulier (Nosotros/Vosotros)",
                        "questions": [
                            {"id": 1141, "type": "multiple_choice", "question": "¿Cuál es la forma correcta para 'nosotros' de PODER?", "options": ["podemos", "puedemos", "podéis", "pueden"], "correct_answer": "podemos", "explanation": "Nosotros podemos.", "xp": 15},
                            {"id": 1142, "type": "fill_in_the_blank", "question": "Vosotros ___ (volver) a casa en autobús.", "options": None, "correct_answer": "volvéis", "explanation": "Vosotros volvéis.", "xp": 15},
                            {"id": 1143, "type": "multiple_choice", "question": "Nosotros ___ (dormir) ocho horas diarias.", "options": ["dormimos", "duermimos", "duermen", "dormís"], "correct_answer": "dormimos", "explanation": "Nosotros dormimos.", "xp": 15},
                            {"id": 1144, "type": "fill_in_the_blank", "question": "¿Vosotros ___ (encontrar) fácil el español?", "options": None, "correct_answer": "encontráis", "explanation": "Vosotros encontráis.", "xp": 15},
                            {"id": 1145, "type": "multiple_choice", "question": "Nosotros ___ (almorzar) a las dos de la tarde.", "options": ["almorzamos", "almuerzamos", "almuerzan", "almorzáis"], "correct_answer": "almorzamos", "explanation": "Nosotros almorzamos.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_o_ue_mix_repaso",
                        "title": "Diphtongue O -> UE : Synthèse et phrases mélangées",
                        "questions": [
                            {"id": 1146, "type": "fill_in_the_blank", "question": "Yo no ___ (recordar) tu número de teléfono.", "options": None, "correct_answer": "recuerdo", "explanation": "Yo recuerdo.", "xp": 15},
                            {"id": 1147, "type": "multiple_choice", "question": "¿Tú ___ venir a mi casa mañana?", "options": ["puedes", "podes", "puede", "podéis"], "correct_answer": "puedes", "explanation": "Tú puedes.", "xp": 15},
                            {"id": 1148, "type": "fill_in_the_blank", "question": "Mis amigos ___ (jugar) al baloncesto.", "options": None, "correct_answer": "juegan", "explanation": "Ellos juegan.", "xp": 15},
                            {"id": 1149, "type": "multiple_choice", "question": "La entrada de cine ___ nueve euros.", "options": ["cuesta", "costa", "cuestan", "costamos"], "correct_answer": "cuesta", "explanation": "La entrada cuesta.", "xp": 15},
                            {"id": 1150, "type": "fill_in_the_blank", "question": "Nosotros ___ (volver) el lunes que viene.", "options": None, "correct_answer": "volvemos", "explanation": "Nosotros volvemos.", "xp": 15}
                        ]
                    },

                    # =========================================================
                    # SECTION 3 : AFFAIBLISSEMENT E -> I (Quiz 31 à 42, id 1151-1210)
                    # =========================================================
                    {
                        "id": "a1_conj_aff_pedir_1",
                        "title": "Affaiblissement E -> I : PEDIR (Demander/Commander)",
                        "questions": [
                            {"id": 1151, "type": "fill_in_the_blank", "question": "Yo ___ (pedir) la cuenta al camarero.", "options": None, "correct_answer": "pido", "explanation": "Affaiblissement E -> I : 'Yo pido'.", "xp": 15},
                            {"id": 1152, "type": "multiple_choice", "question": "¿Qué ___ tú de primer plato?", "options": ["pides", "pedes", "pide", "pedís"], "correct_answer": "pides", "explanation": "Tú pides.", "xp": 15},
                            {"id": 1153, "type": "fill_in_the_blank", "question": "El cliente ___ (pedir) un vaso de agua.", "options": None, "correct_answer": "pide", "explanation": "Él pide.", "xp": 15},
                            {"id": 1154, "type": "multiple_choice", "question": "Nosotros ___ ayuda al profesor cuando no entendemos.", "options": ["pedimos", "pidimos", "piden", "pedís"], "correct_answer": "pedimos", "explanation": "Nosotros pedimos (sans changement : e régulier).", "xp": 15},
                            {"id": 1155, "type": "fill_in_the_blank", "question": "Ellos siempre ___ (pedir) comida italiana.", "options": None, "correct_answer": "piden", "explanation": "Ellos piden.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_aff_servir_1",
                        "title": "Affaiblissement E -> I : SERVIR (Servir)",
                        "questions": [
                            {"id": 1156, "type": "fill_in_the_blank", "question": "Yo ___ (servir) el café en la mesa.", "options": None, "correct_answer": "sirvo", "explanation": "Yo sirvo.", "xp": 15},
                            {"id": 1157, "type": "multiple_choice", "question": "Este botón no ___ para nada.", "options": ["sirve", "serve", "sirves", "servimos"], "correct_answer": "sirve", "explanation": "Él sirve.", "xp": 15},
                            {"id": 1158, "type": "fill_in_the_blank", "question": "¿Para qué ___ (servir) esta aplicación en el móvil?", "options": None, "correct_answer": "sirve", "explanation": "La aplicación sirve.", "xp": 15},
                            {"id": 1159, "type": "multiple_choice", "question": "Los camareros ___ la cena a las nueve.", "options": ["sirven", "serven", "sirve", "servimos"], "correct_answer": "sirven", "explanation": "Ellos sirven.", "xp": 15},
                            {"id": 1160, "type": "fill_in_the_blank", "question": "Nosotros ___ (servir) desayunos desde las siete.", "options": None, "correct_answer": "servimos", "explanation": "Nosotros servimos.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_aff_repetir_1",
                        "title": "Affaiblissement E -> I : REPETIR",
                        "questions": [
                            {"id": 1161, "type": "fill_in_the_blank", "question": "Yo ___ (repetir) las palabras para memorizarlas.", "options": None, "correct_answer": "repito", "explanation": "Yo repito.", "xp": 15},
                            {"id": 1162, "type": "multiple_choice", "question": "¿Puedes ___ la frase, por favor?", "options": ["repetir", "repites", "repito", "repite"], "correct_answer": "repetir", "explanation": "Après 'puedes', verbe à l'infinitif.", "xp": 15},
                            {"id": 1163, "type": "fill_in_the_blank", "question": "El profesor ___ (repetir) la lección con paciencia.", "options": None, "correct_answer": "repite", "explanation": "Él repite.", "xp": 15},
                            {"id": 1164, "type": "multiple_choice", "question": "Nosotros ___ los ejercicios de gramática.", "options": ["repetimos", "repitimos", "repiten", "repetís"], "correct_answer": "repetimos", "explanation": "Nosotros repetimos.", "xp": 15},
                            {"id": 1165, "type": "fill_in_the_blank", "question": "Los alumnos ___ (repetir) después del profesor.", "options": None, "correct_answer": "repiten", "explanation": "Ellos repiten.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_aff_vestirse_1",
                        "title": "Affaiblissement E -> I : VESTIRSE",
                        "questions": [
                            {"id": 1166, "type": "fill_in_the_blank", "question": "Yo me ___ (vestirse) deprisa todas las mañanas.", "options": None, "correct_answer": "visto", "explanation": "Yo me visto.", "xp": 15},
                            {"id": 1167, "type": "multiple_choice", "question": "¿Cómo te ___ tú para ir a una fiesta elegante?", "options": ["vistes", "vestes", "viste", "vestís"], "correct_answer": "vistes", "explanation": "Tú te vistes.", "xp": 15},
                            {"id": 1168, "type": "fill_in_the_blank", "question": "Ella se ___ (vestirse) con ropa de colores vivos.", "options": None, "correct_answer": "viste", "explanation": "Ella se viste.", "xp": 15},
                            {"id": 1169, "type": "multiple_choice", "question": "Nosotros nos ___ de manera informal los viernes.", "options": ["vestimos", "vistimos", "visten", "vestís"], "correct_answer": "vestimos", "explanation": "Nosotros nos vestimos.", "xp": 15},
                            {"id": 1170, "type": "fill_in_the_blank", "question": "Mis hermanos pequeños se ___ (vestirse) solos.", "options": None, "correct_answer": "visten", "explanation": "Ellos se visten.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_aff_seguir_conseguir",
                        "title": "Affaiblissement E -> I : SEGUIR et CONSEGUIR",
                        "questions": [
                            {"id": 1171, "type": "fill_in_the_blank", "question": "Yo ___ (seguir) todo recto hasta el semáforo.", "options": None, "correct_answer": "sigo", "explanation": "Yo sigo (orthographe : g devant o).", "xp": 15},
                            {"id": 1172, "type": "multiple_choice", "question": "¿Tú ___ buenas notas cuando estudias?", "options": ["consigues", "conseges", "consigue", "conseguís"], "correct_answer": "consigues", "explanation": "Tú consigues.", "xp": 15},
                            {"id": 1173, "type": "fill_in_the_blank", "question": "Él ___ (seguir) las instrucciones del manual.", "options": None, "correct_answer": "sigue", "explanation": "Él sigue.", "xp": 15},
                            {"id": 1174, "type": "multiple_choice", "question": "Nosotros ___ las indicaciones del mapa.", "options": ["seguimos", "siguimos", "siguen", "seguís"], "correct_answer": "seguimos", "explanation": "Nosotros seguimos.", "xp": 15},
                            {"id": 1175, "type": "fill_in_the_blank", "question": "Ellos ___ (conseguir) entradas para el concierto.", "options": None, "correct_answer": "consiguen", "explanation": "Ellos consiguen.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_aff_elegir_corregir",
                        "title": "Affaiblissement E -> I : ELEGIR et CORREGIR",
                        "questions": [
                            {"id": 1176, "type": "fill_in_the_blank", "question": "Yo ___ (elegir) el menú del día.", "options": None, "correct_answer": "elijo", "explanation": "Yo elijo (g devient j devant o).", "xp": 15},
                            {"id": 1177, "type": "multiple_choice", "question": "El profesor ___ los exámenes en su despacho.", "options": ["corrige", "correge", "corrijo", "corregimos"], "correct_answer": "corrige", "explanation": "Él corrige.", "xp": 15},
                            {"id": 1178, "type": "fill_in_the_blank", "question": "¿Tú qué postre ___ (elegir)?", "options": None, "correct_answer": "eliges", "explanation": "Tú eliges.", "xp": 15},
                            {"id": 1179, "type": "multiple_choice", "question": "Nosotros ___ nuestras respuestas juntos.", "options": ["corregimos", "corrijimos", "corrigen", "corregís"], "correct_answer": "corregimos", "explanation": "Nosotros corregimos.", "xp": 15},
                            {"id": 1180, "type": "fill_in_the_blank", "question": "Ellos ___ (elegir) un destino para las vacaciones.", "options": None, "correct_answer": "eligen", "explanation": "Ellos eligen.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_aff_reir_sonreir",
                        "title": "Affaiblissement E -> I : REÍR et SONREÍR",
                        "questions": [
                            {"id": 1181, "type": "fill_in_the_blank", "question": "Yo ___ (sonreír) para la foto de carné.", "options": None, "correct_answer": "sonrío", "explanation": "Yo sonrío (avec accent).", "xp": 15},
                            {"id": 1182, "type": "multiple_choice", "question": "¿De qué te ___ tú tanto?", "options": ["ríes", "rees", "ríe", "reís"], "correct_answer": "ríes", "explanation": "Tú te ríes.", "xp": 15},
                            {"id": 1183, "type": "fill_in_the_blank", "question": "Marta siempre ___ (sonreír) cuando está alegre.", "options": None, "correct_answer": "sonríe", "explanation": "Ella sonríe.", "xp": 15},
                            {"id": 1184, "type": "multiple_choice", "question": "Nosotros nos ___ mucho con tus chistes.", "options": ["reímos", "riemos", "ríen", "reís"], "correct_answer": "reímos", "explanation": "Nosotros nos reímos.", "xp": 15},
                            {"id": 1185, "type": "fill_in_the_blank", "question": "Los niños se ___ (reír) en el recreo.", "options": None, "correct_answer": "ríen", "explanation": "Ellos se ríen.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_aff_competir_medir",
                        "title": "Affaiblissement E -> I : COMPETIR et MEDIR",
                        "questions": [
                            {"id": 1186, "type": "fill_in_the_blank", "question": "Yo ___ (medir) un metro con setenta y cinco.", "options": None, "correct_answer": "mido", "explanation": "Yo mido.", "xp": 15},
                            {"id": 1187, "type": "multiple_choice", "question": "¿Cuánto ___ tú de altura?", "options": ["mides", "medes", "mide", "medís"], "correct_answer": "mides", "explanation": "Tú mides.", "xp": 15},
                            {"id": 1188, "type": "fill_in_the_blank", "question": "Los atletas ___ (competir) en la carrera final.", "options": None, "correct_answer": "compiten", "explanation": "Ellos compiten.", "xp": 15},
                            {"id": 1189, "type": "multiple_choice", "question": "Nosotros ___ en el torneo de ajedrez.", "options": ["competimos", "compitimos", "compiten", "competís"], "correct_answer": "competimos", "explanation": "Nosotros competimos.", "xp": 15},
                            {"id": 1190, "type": "fill_in_the_blank", "question": "La habitación ___ (medir) cuatro metros de largo.", "options": None, "correct_answer": "mide", "explanation": "La habitación mide.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_aff_despedir_despedirse",
                        "title": "Affaiblissement E -> I : DESPEDIR et DESPEDIRSE",
                        "questions": [
                            {"id": 1191, "type": "fill_in_the_blank", "question": "Yo me ___ (despedirse) de mis amigos en el aeropuerto.", "options": None, "correct_answer": "despido", "explanation": "Yo me despido.", "xp": 15},
                            {"id": 1192, "type": "multiple_choice", "question": "El director ___ a los empleados que no trabajan.", "options": ["despide", "despede", "despides", "despedimos"], "correct_answer": "despide", "explanation": "Él despide.", "xp": 15},
                            {"id": 1193, "type": "fill_in_the_blank", "question": "¿Por qué no te ___ (despedirse) de tus abuelos?", "options": None, "correct_answer": "despides", "explanation": "Tú te despides.", "xp": 15},
                            {"id": 1194, "type": "multiple_choice", "question": "Nosotros nos ___ de la profesora hasta mañana.", "options": ["despedimos", "despidimos", "despiden", "despedís"], "correct_answer": "despedimos", "explanation": "Nosotros nos despedimos.", "xp": 15},
                            {"id": 1195, "type": "fill_in_the_blank", "question": "Ellos se ___ (despedirse) antes de subir al tren.", "options": None, "correct_answer": "despiden", "explanation": "Ellos se despiden.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_aff_impedir_regla",
                        "title": "Affaiblissement E -> I : IMPEDIR",
                        "questions": [
                            {"id": 1196, "type": "fill_in_the_blank", "question": "La lluvia ___ (impedir) el tráfico normal.", "options": None, "correct_answer": "impide", "explanation": "Ella impide.", "xp": 15},
                            {"id": 1197, "type": "multiple_choice", "question": "Nada me ___ cumplir mis sueños.", "options": ["impide", "impede", "impido", "impedimos"], "correct_answer": "impide", "explanation": "Nada impide.", "xp": 15},
                            {"id": 1198, "type": "fill_in_the_blank", "question": "Yo no te ___ (impedir) salir con tus amigos.", "options": None, "correct_answer": "impido", "explanation": "Yo impido.", "xp": 15},
                            {"id": 1199, "type": "multiple_choice", "question": "Las leyes ___ el consumo en lugares públicos.", "options": ["impiden", "impeden", "impide", "impedimos"], "correct_answer": "impiden", "explanation": "Las leyes impiden.", "xp": 15},
                            {"id": 1200, "type": "fill_in_the_blank", "question": "Nosotros no ___ (impedir) la entrada a nadie.", "options": None, "correct_answer": "impedimos", "explanation": "Nosotros impedimos.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_aff_nosotros_vosotros_regla",
                        "title": "Affaiblissement E -> I : Maintien du E pour NOSOTROS et VOSOTROS",
                        "questions": [
                            {"id": 1201, "type": "multiple_choice", "question": "La regla del debilitamiento E -> I solo se aplica en las formas en que el acento cae en :", "options": ["La raíz (yo, tú, él, ellos)", "La terminación (nosotros, vosotros)", "Todas las personas sin excepción", "Solo la persona 'yo'"], "correct_answer": "La raíz (yo, tú, él, ellos)", "explanation": "Nosotros y vosotros gardent le E car l'accent est sur la terminaison.", "xp": 15},
                            {"id": 1202, "type": "fill_in_the_blank", "question": "Nosotros ___ (pedir) una pizza grande para cenar.", "options": None, "correct_answer": "pedimos", "explanation": "Nosotros pedimos.", "xp": 15},
                            {"id": 1203, "type": "multiple_choice", "question": "¿Vosotros ___ (servir) la mesa?", "options": ["servís", "sirvís", "sirven", "servimos"], "correct_answer": "servís", "explanation": "Vosotros servís.", "xp": 15},
                            {"id": 1204, "type": "fill_in_the_blank", "question": "Nosotros ___ (repetir) las canciones en el coro.", "options": None, "correct_answer": "repetimos", "explanation": "Nosotros repetimos.", "xp": 15},
                            {"id": 1205, "type": "multiple_choice", "question": "¿Vosotros os ___ (vestir) ya?", "options": ["vestís", "vistís", "visten", "vestimos"], "correct_answer": "vestís", "explanation": "Vosotros os vestís.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_aff_mix_repaso",
                        "title": "Affaiblissement E -> I : Synthèse et phrases mélangées",
                        "questions": [
                            {"id": 1206, "type": "fill_in_the_blank", "question": "Yo siempre ___ (pedir) perdón cuando me equivoco.", "options": None, "correct_answer": "pido", "explanation": "Yo pido.", "xp": 15},
                            {"id": 1207, "type": "multiple_choice", "question": "¿Qué menú ___ vosotros?", "options": ["elegís", "eligen", "elegimos", "eliges"], "correct_answer": "elegís", "explanation": "Vosotros elegís.", "xp": 15},
                            {"id": 1208, "type": "fill_in_the_blank", "question": "Ella me ___ (sonreír) amablemente.", "options": None, "correct_answer": "sonríe", "explanation": "Ella sonríe.", "xp": 15},
                            {"id": 1209, "type": "multiple_choice", "question": "Nosotros ___ todo recto por la avenida.", "options": ["seguimos", "siguimos", "siguen", "seguís"], "correct_answer": "seguimos", "explanation": "Nosotros seguimos.", "xp": 15},
                            {"id": 1210, "type": "fill_in_the_blank", "question": "Los camareros ___ (servir) muy rápido en este bar.", "options": None, "correct_answer": "sirven", "explanation": "Ellos sirven.", "xp": 15}
                        ]
                    },

                    # =========================================================
                    # SECTION 4 : SYNTHÈSE DES DIPHTONGUES & ALTERNANCES (Quiz 43 à 48, id 1211-1240)
                    # =========================================================
                    {
                        "id": "a1_conj_diph_vs_aff_comparativa",
                        "title": "Comparaison : Diphtongue E -> IE vs Affaiblissement E -> I",
                        "questions": [
                            {"id": 1211, "type": "multiple_choice", "question": "QUERER hace 'yo quiero' (E -> IE), mientras que PEDIR hace :", "options": ["yo pido (E -> I)", "yo piedo", "yo pedo", "yo pído"], "correct_answer": "yo pido (E -> I)", "explanation": "Pedir est un verbe à affaiblissement en -ir (E -> I).", "xp": 15},
                            {"id": 1212, "type": "fill_in_the_blank", "question": "Yo ___ (pensar) en viajar y ___ (pedir) las vacaciones (pensar / pedir).", "options": None, "correct_answer": "pienso / pido", "explanation": "Pienso (diphtongue) / pido (affaiblissement).", "xp": 15},
                            {"id": 1213, "type": "multiple_choice", "question": "SENTIR vs SERVIR en la persona 'él' :", "options": ["siente / sirve", "siente / sierve", "sinte / sirve", "sente / serve"], "correct_answer": "siente / sirve", "explanation": "Sentir diphtongue (siente) ; servir s'affaiblit (sirve).", "xp": 15},
                            {"id": 1214, "type": "fill_in_the_blank", "question": "¿Tú ___ (entender - E->IE) lo que el camarero ___ (servir - E->I)?", "options": None, "correct_answer": "entiendes / sirve", "explanation": "Entiendes / sirve.", "xp": 15},
                            {"id": 1215, "type": "multiple_choice", "question": "Tous les verbes à affaiblissement (E -> I) appartiennent au groupe :", "options": ["-IR uniquement", "-AR et -ER", "-AR uniquement", "Aux 3 groupes"], "correct_answer": "-IR uniquement", "explanation": "Les affaiblissements stricts en espagnol moderne sont en -ir (pedir, servir, etc.).", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_tres_modelos_mix_1",
                        "title": "Synthèse 3 modèles : Querer (E->IE), Poder (O->UE), Pedir (E->I)",
                        "questions": [
                            {"id": 1216, "type": "multiple_choice", "question": "Formas de 'yo' de Querer, Poder y Pedir :", "options": ["quiero / puedo / pido", "quero / podo / pedo", "quiero / podo / pido", "quero / puedo / pido"], "correct_answer": "quiero / puedo / pido", "explanation": "Quiero / puedo / pido.", "xp": 15},
                            {"id": 1217, "type": "fill_in_the_blank", "question": "Tú ___ (querer) salir pero no ___ (poder) porque tienes examen.", "options": None, "correct_answer": "quieres / puedes", "explanation": "Quieres / puedes.", "xp": 15},
                            {"id": 1218, "type": "multiple_choice", "question": "Formas de 'ellos' : Cerrar, Volver, Vestir :", "options": ["cierran / vuelven / visten", "cerran / volven / vesten", "cierran / vuelven / vesten", "cerran / vuelven / visten"], "correct_answer": "cierran / vuelven / visten", "explanation": "Cierran / vuelven / visten.", "xp": 15},
                            {"id": 1219, "type": "fill_in_the_blank", "question": "Nosotros ___ (querer), ___ (poder) y ___ (pedir).", "options": None, "correct_answer": "queremos / podemos / pedimos", "explanation": "Formes régulières au pluriel avec nosotros.", "xp": 15},
                            {"id": 1220, "type": "multiple_choice", "question": "Vosotros ___ (preferir), ___ (dormir) y ___ (repetir).", "options": ["preferís / dormís / repetís", "prefierís / duermís / repitís", "preferéis / dorméis / repetéis", "prefieren / duermen / repiten"], "correct_answer": "preferís / dormís / repetís", "explanation": "Vosotros : terminaison -ís sans altération du radical.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_tabla_bota",
                        "title": "La règle visuelle de la 'Botte' (Verbos bota)",
                        "questions": [
                            {"id": 1221, "type": "multiple_choice", "question": "¿Por qué se llaman 'verbes bottes' (verbos bota) ?", "options": ["Porque las personas afectadas (yo, tú, él, ellos) forman el dibujo de una bota en la tabla", "Porque se usan para hablar de zapatos", "Porque terminan en -ota", "Porque son del grupo -ar"], "correct_answer": "Porque las personas afectadas (yo, tú, él, ellos) forman el dibujo de una bota en la tabla", "explanation": "1s, 2s, 3s et 3p forment la forme d'une botte sur la grille.", "xp": 15},
                            {"id": 1222, "type": "fill_in_the_blank", "question": "Las dos personas que quedan FUERA de la bota son nosotros y ___.", "options": None, "correct_answer": "vosotros", "explanation": "Nosotros y vosotros restent réguliers.", "xp": 15},
                            {"id": 1223, "type": "multiple_choice", "question": "Dans le verbe 'empezar', quelle forme est DANS la botte ?", "options": ["empiezas (tú)", "empezamos (nosotros)", "empezáis (vosotros)", "empezar (infinitivo)"], "correct_answer": "empiezas (tú)", "explanation": "Tú empiezas.", "xp": 15},
                            {"id": 1224, "type": "fill_in_the_blank", "question": "La forma 'duermen' está ___ (DENTRO/FUERA) de la bota.", "options": None, "correct_answer": "DENTRO", "explanation": "3e personne du pluriel = dans la botte.", "xp": 15},
                            {"id": 1225, "type": "multiple_choice", "question": "La forma 'entendéis' está :", "options": ["FUERA de la bota (sin diptongo)", "DENTRO de la bota", "En pasado", "Mal conjugada"], "correct_answer": "FUERA de la bota (sin diptongo)", "explanation": "Vosotros está fuera.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_dialogo_restaurante",
                        "title": "Diphtongues en contexte : Commander au restaurant",
                        "questions": [
                            {"id": 1226, "type": "multiple_choice", "question": "- ¿Qué ___ ustedes de segundo plato? (querer)", "options": ["quieren", "queremos", "quieres", "queréis"], "correct_answer": "quieren", "explanation": "Ustedes quieren.", "xp": 15},
                            {"id": 1227, "type": "fill_in_the_blank", "question": "Complétez : - Yo ___ carne y mi amigo ___ pescado (preferir).", "options": None, "correct_answer": "prefiero / prefiere", "explanation": "Prefiero / prefiere.", "xp": 15},
                            {"id": 1228, "type": "multiple_choice", "question": "- Camarero, ¿nos ___ la cuenta cuando pueda? (traer/pedir)", "options": ["trae", "pide", "sirve", "vuelve"], "correct_answer": "trae", "explanation": "¿Nos trae la cuenta?", "xp": 15},
                            {"id": 1229, "type": "fill_in_the_blank", "question": "- ¿Cuánto ___ el menú del día? (costar)", "options": None, "correct_answer": "cuesta", "explanation": "¿Cuánto cuesta?", "xp": 15},
                            {"id": 1230, "type": "multiple_choice", "question": "- Nosotros no ___ pagar con tarjeta, ¿___ en efectivo? (poder / costar)", "options": ["podemos / cuesta", "puedemos / cuesta", "podemos / costamos", "pueden / cuestan"], "correct_answer": "podemos / cuesta", "explanation": "No podemos pagar.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_dialogo_rutina",
                        "title": "Diphtongues en contexte : Raconter sa journée",
                        "questions": [
                            {"id": 1231, "type": "multiple_choice", "question": "- ¿A qué hora te despiertas? - Me ___ a las siete. (despertarse)", "options": ["despierto", "desperto", "despierta", "despertamos"], "correct_answer": "despierto", "explanation": "Me despierto.", "xp": 15},
                            {"id": 1232, "type": "fill_in_the_blank", "question": "Complétez : - ¿A qué hora ___ a trabajar? - ___ a las ocho y media (empezar).", "options": None, "correct_answer": "empiezas / Empiezo", "explanation": "Empiezas / Empiezo.", "xp": 15},
                            {"id": 1233, "type": "multiple_choice", "question": "- ¿Dónde almuerzas? - ___ en la cafetería con mis compañeros.", "options": ["Almuerzo", "Almorzo", "Almuerza", "Almorzamos"], "correct_answer": "Almuerzo", "explanation": "Almuerzo.", "xp": 15},
                            {"id": 1234, "type": "fill_in_the_blank", "question": "Complétez : - ¿A qué hora ___ a casa? - ___ a las siete (volver).", "options": None, "correct_answer": "vuelves / Vuelvo", "explanation": "Vuelves / Vuelvo.", "xp": 15},
                            {"id": 1235, "type": "multiple_choice", "question": "- Por la noche me ___ a las once y ___ ocho horas. (acostarse / dormir)", "options": ["acuesto / duermo", "acosto / dormo", "acuesta / duerme", "acuesto / dormo"], "correct_answer": "acuesto / duermo", "explanation": "Me acuesto y duermo.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_diph_gran_repaso_alternancias",
                        "title": "Grand contrôle de synthèse sur toutes les alternances",
                        "questions": [
                            {"id": 1236, "type": "fill_in_the_blank", "question": "Yo ___ (entender) la pregunta pero no ___ (recordar) la respuesta.", "options": None, "correct_answer": "entiendo / recuerdo", "explanation": "Entiendo (E->IE) / recuerdo (O->UE).", "xp": 15},
                            {"id": 1237, "type": "multiple_choice", "question": "Nosotros ___ (preferir) descansar y vosotros ___ (jugar) al fútbol.", "options": ["preferimos / jugáis", "prefierimos / juegáis", "prefieren / juegan", "preferimos / juegan"], "correct_answer": "preferimos / jugáis", "explanation": "Nosotros preferimos / vosotros jugáis.", "xp": 15},
                            {"id": 1238, "type": "fill_in_the_blank", "question": "¿Tú ___ (poder) ayudarme a buscar lo que ___ (perder)?", "options": None, "correct_answer": "puedes / pierdo", "explanation": "Puedes / pierdo.", "xp": 15},
                            {"id": 1239, "type": "multiple_choice", "question": "Ellos ___ (pedir) la comida y el camarero la ___ (servir).", "options": ["piden / sirve", "peden / serve", "piden / sierve", "peden / sirve"], "correct_answer": "piden / sirve", "explanation": "Piden / sirve (affaiblissements).", "xp": 15},
                            {"id": 1240, "type": "fill_in_the_blank", "question": "La tienda ___ (cerrar) a las ocho y ___ (volver) a abrir mañana.", "options": None, "correct_answer": "cierra / vuelve", "explanation": "Cierra / vuelve.", "xp": 15}
                        ]
                    },

                    # =========================================================
                    # SECTION 5 : IRRÉGULIERS EN -YO (Quiz 49 à 68, id 1241-1340)
                    # =========================================================
                    {
                        "id": "a1_conj_yo_hacer_1",
                        "title": "Irrégulier en YO : HACER (Hago)",
                        "questions": [
                            {"id": 1241, "type": "fill_in_the_blank", "question": "Yo ___ (hacer) mis deberes por la tarde.", "options": None, "correct_answer": "hago", "explanation": "Forme irrégulière de 'yo' : 'Yo hago'.", "xp": 15},
                            {"id": 1242, "type": "multiple_choice", "question": "¿Qué ___ tú los fines de semana?", "options": ["haces", "hago", "hace", "hacéis"], "correct_answer": "haces", "explanation": "Tú haces (les autres personnes sont régulières).", "xp": 15},
                            {"id": 1243, "type": "fill_in_the_blank", "question": "Ella ___ (hacer) deporte todos los días.", "options": None, "correct_answer": "hace", "explanation": "Ella hace.", "xp": 15},
                            {"id": 1244, "type": "multiple_choice", "question": "Nosotros ___ la compra en el supermercado.", "options": ["hacemos", "hagamos", "hacen", "hacéis"], "correct_answer": "hacemos", "explanation": "Nosotros hacemos.", "xp": 15},
                            {"id": 1245, "type": "fill_in_the_blank", "question": "Ellos ___ (hacer) mucho ruido por la noche.", "options": None, "correct_answer": "hacen", "explanation": "Ellos hacen.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_yo_poner_1",
                        "title": "Irrégulier en YO : PONER (Pongo)",
                        "questions": [
                            {"id": 1246, "type": "fill_in_the_blank", "question": "Yo ___ (poner) los libros encima de la mesa.", "options": None, "correct_answer": "pongo", "explanation": "Forme irrégulière : 'Yo pongo'.", "xp": 15},
                            {"id": 1247, "type": "multiple_choice", "question": "¿Dónde ___ tú las llaves normalmente?", "options": ["pones", "pongo", "pone", "ponéis"], "correct_answer": "pones", "explanation": "Tú pones.", "xp": 15},
                            {"id": 1248, "type": "fill_in_the_blank", "question": "Mi madre ___ (poner) la mesa para cenar.", "options": None, "correct_answer": "pone", "explanation": "Ella pone.", "xp": 15},
                            {"id": 1249, "type": "multiple_choice", "question": "Nosotros nos ___ el abrigo porque hace frío.", "options": ["ponemos", "pongamos", "ponen", "ponéis"], "correct_answer": "ponemos", "explanation": "Nosotros nos ponemos.", "xp": 15},
                            {"id": 1250, "type": "fill_in_the_blank", "question": "Ellos ___ (poner) música en la fiesta.", "options": None, "correct_answer": "ponen", "explanation": "Ellos ponen.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_yo_salir_1",
                        "title": "Irrégulier en YO : SALIR (Salgo)",
                        "questions": [
                            {"id": 1251, "type": "fill_in_the_blank", "question": "Yo ___ (salir) de casa a las siete y media.", "options": None, "correct_answer": "salgo", "explanation": "Forme irrégulière : 'Yo salgo'.", "xp": 15},
                            {"id": 1252, "type": "multiple_choice", "question": "¿A qué hora ___ tú del trabajo?", "options": ["sales", "salgo", "sale", "salís"], "correct_answer": "sales", "explanation": "Tú sales.", "xp": 15},
                            {"id": 1253, "type": "fill_in_the_blank", "question": "El tren ___ (salir) del andén número dos.", "options": None, "correct_answer": "sale", "explanation": "El tren sale.", "xp": 15},
                            {"id": 1254, "type": "multiple_choice", "question": "Nosotros ___ con amigos los viernes por la noche.", "options": ["salimos", "salgamos", "salen", "salís"], "correct_answer": "salimos", "explanation": "Nosotros salimos.", "xp": 15},
                            {"id": 1255, "type": "fill_in_the_blank", "question": "¿Vosotros ___ (salir) a cenar fuera hoy?", "options": None, "correct_answer": "salís", "explanation": "Vosotros salís.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_yo_traer_caer",
                        "title": "Irrégulier en YO : TRAER (Traigo) et CAER (Caigo)",
                        "questions": [
                            {"id": 1256, "type": "fill_in_the_blank", "question": "Yo ___ (traer) el postre para la cena.", "options": None, "correct_answer": "traigo", "explanation": "Yo traigo (en -igo).", "xp": 15},
                            {"id": 1257, "type": "multiple_choice", "question": "Yo me ___ si el suelo está resbaladizo. (caerse)", "options": ["caigo", "cao", "cayo", "caes"], "correct_answer": "caigo", "explanation": "Yo me caigo.", "xp": 15},
                            {"id": 1258, "type": "fill_in_the_blank", "question": "¿Qué ___ (traer) tú en esa mochila tan grande?", "options": None, "correct_answer": "traes", "explanation": "Tú traes.", "xp": 15},
                            {"id": 1259, "type": "multiple_choice", "question": "Las hojas de los árboles ___ en otoño.", "options": ["caen", "caigo", "cae", "caemos"], "correct_answer": "caen", "explanation": "Ellas caen.", "xp": 15},
                            {"id": 1260, "type": "fill_in_the_blank", "question": "Nosotros ___ (traer) buenas noticias.", "options": None, "correct_answer": "traemos", "explanation": "Nosotros traemos.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_yo_valer_oír",
                        "title": "Irrégulier en YO : VALER (Valgo) et OÍR (Oigo)",
                        "questions": [
                            {"id": 1261, "type": "fill_in_the_blank", "question": "Yo ___ (valer) mucho como profesional.", "options": None, "correct_answer": "valgo", "explanation": "Yo valgo.", "xp": 15},
                            {"id": 1262, "type": "multiple_choice", "question": "Yo no ___ bien porque hay mucho ruido. (oír)", "options": ["oigo", "oyo", "oies", "oigo"], "correct_answer": "oigo", "explanation": "Yo oigo.", "xp": 15},
                            {"id": 1263, "type": "fill_in_the_blank", "question": "¿Cuánto ___ (valer) esta entrada de museo?", "options": None, "correct_answer": "vale", "explanation": "La entrada vale.", "xp": 15},
                            {"id": 1264, "type": "multiple_choice", "question": "¿Tú me ___ bien por teléfono?", "options": ["oyes", "oies", "oyas", "oís"], "correct_answer": "oyes", "explanation": "Tú oyes (avec y).", "xp": 15},
                            {"id": 1265, "type": "fill_in_the_blank", "question": "Ellos ___ (oír) música clásica por la radio.", "options": None, "correct_answer": "oyen", "explanation": "Ellos oyen.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_yo_conocer_1",
                        "title": "Irrégulier en YO (-ZCO) : CONOCER (Conozco)",
                        "questions": [
                            {"id": 1266, "type": "fill_in_the_blank", "question": "Yo no ___ (conocer) a esa persona.", "options": None, "correct_answer": "conozco", "explanation": "Forme en -zco : 'Yo conozco'.", "xp": 15},
                            {"id": 1267, "type": "multiple_choice", "question": "¿___ tú la ciudad de Barcelona?", "options": ["Conoces", "Conozcas", "Conoce", "Conocéis"], "correct_answer": "Conoces", "explanation": "Tú conoces.", "xp": 15},
                            {"id": 1268, "type": "fill_in_the_blank", "question": "Ella ___ (conocer) muchos países de Europa.", "options": None, "correct_answer": "conoce", "explanation": "Ella conoce.", "xp": 15},
                            {"id": 1269, "type": "multiple_choice", "question": "Nosotros ___ un restaurante mexicano excelente.", "options": ["conocemos", "conozcamos", "conocen", "conocéis"], "correct_answer": "conocemos", "explanation": "Nosotros conocemos.", "xp": 15},
                            {"id": 1270, "type": "fill_in_the_blank", "question": "¿Vosotros ___ (conocer) a mis padres?", "options": None, "correct_answer": "conocéis", "explanation": "Vosotros conocéis.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_yo_traducir_conducir",
                        "title": "Irrégulier en YO (-ZCO) : TRADUCIR et CONDUCIR",
                        "questions": [
                            {"id": 1271, "type": "fill_in_the_blank", "question": "Yo ___ (traducir) textos del francés al español.", "options": None, "correct_answer": "traduzco", "explanation": "Yo traduzco.", "xp": 15},
                            {"id": 1272, "type": "multiple_choice", "question": "Yo ___ con mucho cuidado de noche. (conducir)", "options": ["conduzco", "conduco", "conduces", "conducimos"], "correct_answer": "conduzco", "explanation": "Yo conduzco.", "xp": 15},
                            {"id": 1273, "type": "fill_in_the_blank", "question": "¿Tú ___ (conducir) coche manual o automático?", "options": None, "correct_answer": "conduces", "explanation": "Tú conduces.", "xp": 15},
                            {"id": 1274, "type": "multiple_choice", "question": "Nosotros ___ documentos oficiales en la agencia.", "options": ["traducimos", "traduzcamos", "traducen", "traducís"], "correct_answer": "traducimos", "explanation": "Nosotros traducimos.", "xp": 15},
                            {"id": 1275, "type": "fill_in_the_blank", "question": "Ellos ___ (conducir) hasta Madrid en tres horas.", "options": None, "correct_answer": "conducen", "explanation": "Ellos conducen.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_yo_parecer_ofrecer",
                        "title": "Irrégulier en YO (-ZCO) : PARECER et OFRECER",
                        "questions": [
                            {"id": 1276, "type": "fill_in_the_blank", "question": "A mí me ___ (parecer) una buena idea.", "options": None, "correct_answer": "parece", "explanation": "Construction impersonnelle : 'me parece'.", "xp": 15},
                            {"id": 1277, "type": "multiple_choice", "question": "Yo ___ mi ayuda a quien la necesita. (ofrecer)", "options": ["ofrezco", "ofreco", "ofreces", "ofrecemos"], "correct_answer": "ofrezco", "explanation": "Yo ofrezco.", "xp": 15},
                            {"id": 1278, "type": "fill_in_the_blank", "question": "Yo me ___ (parecer) mucho a mi padre físicamente.", "options": None, "correct_answer": "parezco", "explanation": "Yo me parezco.", "xp": 15},
                            {"id": 1279, "type": "multiple_choice", "question": "Este hotel ___ un servicio excelente.", "options": ["ofrece", "ofrezco", "ofrecen", "ofrecemos"], "correct_answer": "ofrece", "explanation": "El hotel ofrece.", "xp": 15},
                            {"id": 1280, "type": "fill_in_the_blank", "question": "Nosotros ___ (ofrecer) descuentos a los estudiantes.", "options": None, "correct_answer": "ofrecemos", "explanation": "Nosotros ofrecemos.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_yo_saber_1",
                        "title": "Irrégulier en YO : SABER (Sé)",
                        "questions": [
                            {"id": 1281, "type": "fill_in_the_blank", "question": "Yo no ___ (saber) hablar alemán.", "options": None, "correct_answer": "sé", "explanation": "Forme unique avec accent écrit : 'Yo sé'.", "xp": 15},
                            {"id": 1282, "type": "multiple_choice", "question": "¿___ tú dónde está la estación de metro?", "options": ["Sabes", "Sé", "Sabe", "Sabéis"], "correct_answer": "Sabes", "explanation": "Tú sabes.", "xp": 15},
                            {"id": 1283, "type": "fill_in_the_blank", "question": "Mi profesor ___ (saber) mucho de historia.", "options": None, "correct_answer": "sabe", "explanation": "Él sabe.", "xp": 15},
                            {"id": 1284, "type": "multiple_choice", "question": "Nosotros no ___ la respuesta a esta pregunta.", "options": ["sabemos", "sepamos", "saben", "sabéis"], "correct_answer": "sabemos", "explanation": "Nosotros sabemos.", "xp": 15},
                            {"id": 1285, "type": "fill_in_the_blank", "question": "Ellos ___ (saber) cocinar muy bien.", "options": None, "correct_answer": "saben", "explanation": "Ellos saben.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_saber_vs_conocer",
                        "title": "Distinction essentielle : SABER vs CONOCER",
                        "questions": [
                            {"id": 1286, "type": "multiple_choice", "question": "Yo ___ tocar el piano (capacité / compétence).", "options": ["sé", "conozco", "sabo", "conozco a"], "correct_answer": "sé", "explanation": "Saber + infinitif = Savoir faire quelque chose.", "xp": 15},
                            {"id": 1287, "type": "fill_in_the_blank", "question": "Yo ___ (conocer) a tu hermano (personne).", "options": None, "correct_answer": "conozco", "explanation": "Conocer a alguien = Connaître quelqu'un.", "xp": 15},
                            {"id": 1288, "type": "multiple_choice", "question": "¿Tú ___ la ciudad de Sevilla? (lieu)", "options": ["conoces", "sabes", "sé", "conozco"], "correct_answer": "conoces", "explanation": "Conocer un lieu = Avoir visité / Connaître un lieu.", "xp": 15},
                            {"id": 1289, "type": "fill_in_the_blank", "question": "¿Tú ___ (saber) a qué hora empieza la película? (information)", "options": None, "correct_answer": "sabes", "explanation": "Saber une information précise.", "xp": 15},
                            {"id": 1290, "type": "multiple_choice", "question": "Yo no ___ dónde vive Carlos, pero ___ a su hermana.", "options": ["sé / conozco", "conozco / sé", "sé / sé", "conozco / conozco"], "correct_answer": "sé / conozco", "explanation": "Savoir une donnée (sé) / Connaître une personne (conozco).", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_yo_ver_1",
                        "title": "Irrégulier en YO : VER (Veo)",
                        "questions": [
                            {"id": 1291, "type": "fill_in_the_blank", "question": "Yo ___ (ver) una película interesante en la tele.", "options": None, "correct_answer": "veo", "explanation": "Forme régulière en aspect mais sans diphtongue : 'Yo veo'.", "xp": 15},
                            {"id": 1292, "type": "multiple_choice", "question": "¿___ tú a María en la universidad?", "options": ["Ves", "Veo", "Ve", "Veis"], "correct_answer": "Ves", "explanation": "Tú ves (sans accent).", "xp": 15},
                            {"id": 1293, "type": "fill_in_the_blank", "question": "Desde mi ventana se ___ (ver) el mar.", "options": None, "correct_answer": "ve", "explanation": "Se ve.", "xp": 15},
                            {"id": 1294, "type": "multiple_choice", "question": "Nosotros ___ series en español con subtítulos.", "options": ["vemos", "veemos", "ven", "veis"], "correct_answer": "vemos", "explanation": "Nosotros vemos.", "xp": 15},
                            {"id": 1295, "type": "fill_in_the_blank", "question": "¿Vosotros ___ (ver) a vuestros primos a menudo?", "options": None, "correct_answer": "veis", "explanation": "Vosotros veis (sans accent).", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_yo_dar_1",
                        "title": "Irrégulier en YO : DAR (Doy)",
                        "questions": [
                            {"id": 1296, "type": "fill_in_the_blank", "question": "Yo le ___ (dar) un regalo a mi madre.", "options": None, "correct_answer": "doy", "explanation": "Forme en -oy : 'Yo doy'.", "xp": 15},
                            {"id": 1297, "type": "multiple_choice", "question": "¿Tú me ___ tu número de teléfono?", "options": ["das", "doy", "da", "dais"], "correct_answer": "das", "explanation": "Tú das.", "xp": 15},
                            {"id": 1298, "type": "fill_in_the_blank", "question": "El profesor ___ (dar) explicaciones muy claras.", "options": None, "correct_answer": "da", "explanation": "Él da.", "xp": 15},
                            {"id": 1299, "type": "multiple_choice", "question": "Nosotros ___ las gracias por la invitación.", "options": ["damos", "doy", "dan", "dais"], "correct_answer": "damos", "explanation": "Nosotros damos.", "xp": 15},
                            {"id": 1300, "type": "fill_in_the_blank", "question": "Ellos ___ (dar) un paseo por el parque.", "options": None, "correct_answer": "dan", "explanation": "Ellos dan.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_yo_caber_1",
                        "title": "Irrégulier en YO : CABER (Quepo)",
                        "questions": [
                            {"id": 1301, "type": "fill_in_the_blank", "question": "Yo no ___ (caber) en este asiento tan pequeño.", "options": None, "correct_answer": "quepo", "explanation": "Forme très irrégulière en yo : 'Yo quepo'.", "xp": 15},
                            {"id": 1302, "type": "multiple_choice", "question": "Toda la ropa ___ en la maleta.", "options": ["cabe", "quepo", "cabes", "cabemos"], "correct_answer": "cabe", "explanation": "Ella cabe.", "xp": 15},
                            {"id": 1303, "type": "fill_in_the_blank", "question": "Mis libros no ___ (caber) en la mochila.", "options": None, "correct_answer": "caben", "explanation": "Ellos caben.", "xp": 15},
                            {"id": 1304, "type": "multiple_choice", "question": "¿Tú ___ en el coche con nosotros?", "options": ["cabes", "quepes", "cabe", "cabéis"], "correct_answer": "cabes", "explanation": "Tú cabes.", "xp": 15},
                            {"id": 1305, "type": "fill_in_the_blank", "question": "Nosotros no ___ (caber) todos en este taxi.", "options": None, "correct_answer": "cabemos", "explanation": "Nosotros cabemos.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_yo_grupo_go_recap",
                        "title": "Les verbes en -GO à la 1re personne (Tableau comparatif)",
                        "questions": [
                            {"id": 1306, "type": "multiple_choice", "question": "Hacer, Poner, Salir, Traer en 'yo' son :", "options": ["hago, pongo, salgo, traigo", "haco, pono, salo, trao", "hago, pongo, salgo, trazo", "hago, poyo, salgo, traigo"], "correct_answer": "hago, pongo, salgo, traigo", "explanation": "Tous prennent la désinence -go à la 1re personne.", "xp": 15},
                            {"id": 1307, "type": "fill_in_the_blank", "question": "Yo ___ (hacer) la comida y luego ___ (poner) la mesa.", "options": None, "correct_answer": "hago / pongo", "explanation": "Hago / pongo.", "xp": 15},
                            {"id": 1308, "type": "multiple_choice", "question": "Yo ___ de fiesta y ___ a mis amigos (salir / traer) :", "options": ["salgo / traigo", "salo / trao", "salgo / trao", "salo / traigo"], "correct_answer": "salgo / traigo", "explanation": "Salgo / traigo.", "xp": 15},
                            {"id": 1309, "type": "fill_in_the_blank", "question": "Yo ___ (valer) para este trabajo porque hablo idiomas.", "options": None, "correct_answer": "valgo", "explanation": "Valgo.", "xp": 15},
                            {"id": 1310, "type": "multiple_choice", "question": "¿Qué tienen en común las formas tú, él, nosotros de estos verbos?", "options": ["Son completamente regulares según su grupo", "Tienen -go en todas las personas", "Tienen diptongo", "Son irregulares en nosotros"], "correct_answer": "Son completamente regulares según su grupo", "explanation": "L'irrégularité n'affecte QUE la personne 'yo'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_yo_grupo_zco_recap",
                        "title": "Les verbes en -ZCO à la 1re personne (Verbes en -cer / -cir)",
                        "questions": [
                            {"id": 1311, "type": "multiple_choice", "question": "La regla de -ZCO se aplica a verbos que terminan en :", "options": ["Vocal + -cer o -cir (conocer, traducir, parecer)", "Consonante + -cer", "-ar únicamente", "Cualquier verbo"], "correct_answer": "Vocal + -cer o -cir (conocer, traducir, parecer)", "explanation": "Voyelle + -cer/-cir -> -zco à la 1re personne.", "xp": 15},
                            {"id": 1312, "type": "fill_in_the_blank", "question": "Yo ___ (conocer) la ciudad y ___ (conducir) hasta allí.", "options": None, "correct_answer": "conozco / conduzco", "explanation": "Conozco / conduzco.", "xp": 15},
                            {"id": 1313, "type": "multiple_choice", "question": "Yo ___ (obedecer) las normas de la escuela.", "options": ["obedezco", "obedezo", "obedeco", "obedezca"], "correct_answer": "obedezco", "explanation": "Yo obedezco.", "xp": 15},
                            {"id": 1314, "type": "fill_in_the_blank", "question": "Yo ___ (agradecer) tu ayuda de todo corazón.", "options": None, "correct_answer": "agradezco", "explanation": "Yo agradezco.", "xp": 15},
                            {"id": 1315, "type": "multiple_choice", "question": "El verbo 'vencer' termina en consonante + cer, por lo que su 'yo' es :", "options": ["venzo (c -> z sin c)", "venzco", "venco", "venzgo"], "correct_answer": "venzo (c -> z sin c)", "explanation": "Après consonne, c devient z (venzo), pas de 'zc'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_yo_grupo_oy_recap",
                        "title": "Les verbes en -OY à la 1re personne (Dar, Estar, Ser, Ir)",
                        "questions": [
                            {"id": 1316, "type": "multiple_choice", "question": "Los 4 verbos esenciales terminados en -OY en 'yo' son :", "options": ["Dar (doy), Estar (estoy), Ser (soy), Ir (voy)", "Hacer, Poner, Salir, Traer", "Saber, Ver, Caber, Oír", "Comer, Beber, Vivir, Hablar"], "correct_answer": "Dar (doy), Estar (estoy), Ser (soy), Ir (voy)", "explanation": "Doy, estoy, soy, voy.", "xp": 15},
                            {"id": 1317, "type": "fill_in_the_blank", "question": "Yo ___ (estar) en casa y le ___ (dar) comida al perro.", "options": None, "correct_answer": "estoy / doy", "explanation": "Estoy / doy.", "xp": 15},
                            {"id": 1318, "type": "multiple_choice", "question": "Yo ___ estudiante y ___ al gimnasio por la tarde. (ser / ir)", "options": ["soy / voy", "estoy / voy", "soy / vo", "doy / voy"], "correct_answer": "soy / voy", "explanation": "Soy / voy.", "xp": 15},
                            {"id": 1319, "type": "fill_in_the_blank", "question": "Yo no le ___ (dar) importancia a este problema.", "options": None, "correct_answer": "doy", "explanation": "Doy.", "xp": 15},
                            {"id": 1320, "type": "multiple_choice", "question": "La terminación -OY existe en español en :", "options": ["Solo estos cuatro verbos en presente", "Todos los verbos regulares", "El tiempo pretérito", "El grupo -ir"], "correct_answer": "Solo estos cuatro verbos en presente", "explanation": "Soy, estoy, doy, voy.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_yo_casos_unicos_recap",
                        "title": "Cas uniques et isolés : Sé, Veo, Quepo",
                        "questions": [
                            {"id": 1321, "type": "multiple_choice", "question": "¿Cuál es la forma de 'yo' de SABER?", "options": ["sé", "sabo", "sepo", "sapo"], "correct_answer": "sé", "explanation": "Yo sé.", "xp": 15},
                            {"id": 1322, "type": "fill_in_the_blank", "question": "Yo ___ (saber) que tú me ___ (ver) desde lejos.", "options": None, "correct_answer": "sé / ves", "explanation": "Sé / ves.", "xp": 15},
                            {"id": 1323, "type": "multiple_choice", "question": "En el coche no ___ más maletas. (yo / caber) :", "options": ["quepo", "cabo", "quepa", "cabes"], "correct_answer": "quepo", "explanation": "Yo quepo.", "xp": 15},
                            {"id": 1324, "type": "fill_in_the_blank", "question": "Yo ___ (ver) las noticias todos los días.", "options": None, "correct_answer": "veo", "explanation": "Yo veo.", "xp": 15},
                            {"id": 1325, "type": "multiple_choice", "question": "El acento escrito en 'sé' sirve para distinguirlo de :", "options": ["El pronombre reflexivo 'se'", "El número seis", "La conjunción 'si'", "La preposición 'sin'"], "correct_answer": "El pronombre reflexivo 'se'", "explanation": "Accent diacritique : sé (verbe saber) vs se (pronom).", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_yo_dialogo_presentacion",
                        "title": "Irréguliers en YO en situation : Se présenter et parler de ses compétences",
                        "questions": [
                            {"id": 1326, "type": "multiple_choice", "question": "- ¡Hola! Yo ___ francés, ___ en Madrid y ___ español. (ser / vivir / saber)", "options": ["soy / vivo / sé", "estoy / vivo / conozco", "soy / vivo / conozco", "estoy / vivo / sé"], "correct_answer": "soy / vivo / sé", "explanation": "Soy / vivo / sé.", "xp": 15},
                            {"id": 1327, "type": "fill_in_the_blank", "question": "Complétez : - Yo ___ (hacer) proyectos web y ___ (traducir) artículos.", "options": None, "correct_answer": "hago / traduzco", "explanation": "Hago / traduzco.", "xp": 15},
                            {"id": 1328, "type": "multiple_choice", "question": "- ¿Conoces la ciudad? - Sí, la ___ muy bien. (conocer)", "options": ["conozco", "conoco", "sé", "sabo"], "correct_answer": "conozco", "explanation": "La conozco.", "xp": 15},
                            {"id": 1329, "type": "fill_in_the_blank", "question": "- Por las mañanas ___ (salir) a correr y luego ___ (poner) la radio.", "options": None, "correct_answer": "salgo / pongo", "explanation": "Salgo / pongo.", "xp": 15},
                            {"id": 1330, "type": "multiple_choice", "question": "- Yo te ___ mi número de teléfono. (dar)", "options": ["doy", "das", "da", "damos"], "correct_answer": "doy", "explanation": "Te doy.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_yo_transformacion_oraciones",
                        "title": "Passage de la 3e personne à la 1re personne 'Yo'",
                        "questions": [
                            {"id": 1331, "type": "multiple_choice", "question": "Transformez 'Él hace deporte' en 'Yo' :", "options": ["Yo hago deporte", "Yo haco deporte", "Yo hace deporte", "Yo haceo deporte"], "correct_answer": "Yo hago deporte", "explanation": "Hacer -> Yo hago.", "xp": 15},
                            {"id": 1332, "type": "fill_in_the_blank", "question": "Él sale temprano -> Yo ___ (salir) temprano.", "options": None, "correct_answer": "salgo", "explanation": "Salir -> Yo salgo.", "xp": 15},
                            {"id": 1333, "type": "multiple_choice", "question": "Transformez 'Ella conoce a todos' :", "options": ["Yo conozco a todos", "Yo conoco a todos", "Yo conozca a todos", "Yo sé a todos"], "correct_answer": "Yo conozco a todos", "explanation": "Conocer -> Yo conozco.", "xp": 15},
                            {"id": 1334, "type": "fill_in_the_blank", "question": "Él sabe la verdad -> Yo ___ (saber) la verdad.", "options": None, "correct_answer": "sé", "explanation": "Saber -> Yo sé.", "xp": 15},
                            {"id": 1335, "type": "multiple_choice", "question": "Transformez 'Ella pone la música' :", "options": ["Yo pongo la música", "Yo pono la música", "Yo pone la música", "Yo ponga la música"], "correct_answer": "Yo pongo la música", "explanation": "Poner -> Yo pongo.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_yo_mix_repaso_total",
                        "title": "Grand contrôle de synthèse : Tous les verbes irréguliers en YO",
                        "questions": [
                            {"id": 1336, "type": "fill_in_the_blank", "question": "Yo ___ (saber) la lección, ___ (hacer) los deberes y ___ (salir) a jugar.", "options": None, "correct_answer": "sé / hago / salgo", "explanation": "Sé / hago / salgo.", "xp": 15},
                            {"id": 1337, "type": "multiple_choice", "question": "Yo ___ (conocer) al camarero y le ___ (pedir) la carta. (conocer / pedir)", "options": ["conozco / pido", "conoco / pido", "conozco / piedo", "sé / pido"], "correct_answer": "conozco / pido", "explanation": "Conozco / pido.", "xp": 15},
                            {"id": 1338, "type": "fill_in_the_blank", "question": "Yo ___ (poner) el abrigo en el armario y te ___ (dar) las gracias.", "options": None, "correct_answer": "pongo / doy", "explanation": "Pongo / doy.", "xp": 15},
                            {"id": 1339, "type": "multiple_choice", "question": "Yo ___ (traer) el coche y ___ (conducir) hasta tu casa.", "options": ["traigo / conduzco", "trao / conduco", "traigo / conduco", "trao / conduzco"], "correct_answer": "traigo / conduzco", "explanation": "Traigo / conduzco.", "xp": 15},
                            {"id": 1340, "type": "fill_in_the_blank", "question": "Yo no ___ (oír) nada y no ___ (ver) a nadie.", "options": None, "correct_answer": "oigo / veo", "explanation": "Oigo / veo.", "xp": 15}
                        ]
                    },

                    # =========================================================
                    # SECTION 6 : LES IRRÉGULIERS TOTAUX & MAJEURS (Quiz 69 à 88, id 1341-1440)
                    # =========================================================
                    {
                        "id": "a1_conj_ir_formes_1",
                        "title": "Le verbe IR : Conjugaison complète au présent",
                        "questions": [
                            {"id": 1341, "type": "fill_in_the_blank", "question": "Yo ___ (ir) al trabajo en metro.", "options": None, "correct_answer": "voy", "explanation": "Yo voy.", "xp": 15},
                            {"id": 1342, "type": "multiple_choice", "question": "¿Adónde ___ tú este fin de semana?", "options": ["vas", "va", "voy", "vamos"], "correct_answer": "vas", "explanation": "Tú vas.", "xp": 15},
                            {"id": 1343, "type": "fill_in_the_blank", "question": "Carlos ___ (ir) al gimnasio tres veces por semana.", "options": None, "correct_answer": "va", "explanation": "Él va.", "xp": 15},
                            {"id": 1344, "type": "multiple_choice", "question": "Nosotros ___ a la playa si hace buen tiempo.", "options": ["vamos", "vais", "van", "voy"], "correct_answer": "vamos", "explanation": "Nosotros vamos.", "xp": 15},
                            {"id": 1345, "type": "fill_in_the_blank", "question": "Ellos ___ (ir) al cine esta tarde.", "options": None, "correct_answer": "van", "explanation": "Ellos van.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ir_perifrasis_futuro",
                        "title": "Le verbe IR : Futur proche (IR + A + Infinitif)",
                        "questions": [
                            {"id": 1346, "type": "fill_in_the_blank", "question": "Yo voy ___ (estudiar) toda la tarde para el examen.", "options": None, "correct_answer": "a estudiar", "explanation": "Structure : 'voy a estudiar'.", "xp": 15},
                            {"id": 1347, "type": "multiple_choice", "question": "¿Qué ___ a hacer vosotros mañana?", "options": ["vais", "van", "vamos", "vas"], "correct_answer": "vais", "explanation": "Vosotros vais a hacer.", "xp": 15},
                            {"id": 1348, "type": "fill_in_the_blank", "question": "Nosotros ___ (ir) a cenar a un restaurante típico.", "options": None, "correct_answer": "vamos", "explanation": "Nosotros vamos a cenar.", "xp": 15},
                            {"id": 1349, "type": "multiple_choice", "question": "Ella va a ___ a su familia este fin de semana.", "options": ["visitar", "visita", "visito", "visitamos"], "correct_answer": "visitar", "explanation": "Après 'va a', infinitif obligatoire.", "xp": 15},
                            {"id": 1350, "type": "fill_in_the_blank", "question": "Ellos ___ (ir) a comprar los billetes de avión.", "options": None, "correct_answer": "van", "explanation": "Ellos van a comprar.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_tener_formes_recap",
                        "title": "Le verbe TENER : Irrégulier en -GO et diphtongue (G-Bota)",
                        "questions": [
                            {"id": 1351, "type": "fill_in_the_blank", "question": "Yo ___ (tener) dos gatos y un perro.", "options": None, "correct_answer": "tengo", "explanation": "Yo tengo (en -go).", "xp": 15},
                            {"id": 1352, "type": "multiple_choice", "question": "¿Cuántos años ___ tú?", "options": ["tienes", "tiene", "tenemos", "tenéis"], "correct_answer": "tienes", "explanation": "Tú tienes (diphtongue).", "xp": 15},
                            {"id": 1353, "type": "fill_in_the_blank", "question": "Usted ___ (tener) una cita con el doctor.", "options": None, "correct_answer": "tiene", "explanation": "Usted tiene.", "xp": 15},
                            {"id": 1354, "type": "multiple_choice", "question": "Nosotros ___ mucha sed tras la caminata.", "options": ["tenemos", "tienen", "tenéis", "tengo"], "correct_answer": "tenemos", "explanation": "Nosotros tenemos (régulier).", "xp": 15},
                            {"id": 1355, "type": "fill_in_the_blank", "question": "¿Vosotros ___ (tener) cambio de veinte euros?", "options": None, "correct_answer": "tenéis", "explanation": "Vosotros tenéis.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_venir_formes_1",
                        "title": "Le verbe VENIR : Conjugaison complète au présent",
                        "questions": [
                            {"id": 1356, "type": "fill_in_the_blank", "question": "Yo ___ (venir) de la biblioteca ahora mismo.", "options": None, "correct_answer": "vengo", "explanation": "Yo vengo (en -go).", "xp": 15},
                            {"id": 1357, "type": "multiple_choice", "question": "¿A qué hora ___ tú a mi casa?", "options": ["vienes", "venes", "viene", "venís"], "correct_answer": "vienes", "explanation": "Tú vienes (diphtongue).", "xp": 15},
                            {"id": 1358, "type": "fill_in_the_blank", "question": "El autobús ___ (venir) con retraso.", "options": None, "correct_answer": "viene", "explanation": "Él viene.", "xp": 15},
                            {"id": 1359, "type": "multiple_choice", "question": "Nosotros ___ en tren desde Valencia.", "options": ["venimos", "vienimos", "vienen", "venís"], "correct_answer": "venimos", "explanation": "Nosotros venimos (régulier).", "xp": 15},
                            {"id": 1360, "type": "fill_in_the_blank", "question": "¿Vosotros ___ (venir) a la fiesta esta noche?", "options": None, "correct_answer": "venís", "explanation": "Vosotros venís.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_tener_vs_venir_paralelismo",
                        "title": "Parallélisme parfait : TENER vs VENIR",
                        "questions": [
                            {"id": 1361, "type": "multiple_choice", "question": "Si TENER hace : tengo, tienes, tiene, tenemos, tenéis, tienen, VENIR hace :", "options": ["vengo, vienes, viene, venimos, venís, vienen", "veno, venes, vene, venemos, venéis, venen", "vengo, venes, vene, venimos, venís, vienen", "vengo, vienes, viene, vienimos, vienís, vienen"], "correct_answer": "vengo, vienes, viene, venimos, venís, vienen", "explanation": "Même schéma exact d'irrégularité (1re en -go, diphtongue tú/él/ellos, nosotros/vosotros réguliers).", "xp": 15},
                            {"id": 1362, "type": "fill_in_the_blank", "question": "Yo ___ (tener) calor y ___ (venir) a beber agua.", "options": None, "correct_answer": "tengo / vengo", "explanation": "Tengo / vengo.", "xp": 15},
                            {"id": 1363, "type": "multiple_choice", "question": "Ellos ___ (tener) tiempo y ___ (venir) con nosotros.", "options": ["tienen / vienen", "tenen / venen", "tienen / venen", "tenen / vienen"], "correct_answer": "tienen / vienen", "explanation": "Tienen / vienen.", "xp": 15},
                            {"id": 1364, "type": "fill_in_the_blank", "question": "¿Tú ___ (tener) ganas de salir cuando ___ (venir) el buen tiempo?", "options": None, "correct_answer": "tienes / viene", "explanation": "Tienes / viene.", "xp": 15},
                            {"id": 1365, "type": "multiple_choice", "question": "Nosotros ___ (tener) prisa porque el tren ya ___ (venir).", "options": ["tenemos / viene", "tienen / vengo", "tenemos / vien", "tenéis / venimos"], "correct_answer": "tenemos / viene", "explanation": "Tenemos / viene.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ir_vs_venir_direccion",
                        "title": "Distinction de mouvement : IR (Aller) vs VENIR (Venir)",
                        "questions": [
                            {"id": 1366, "type": "multiple_choice", "question": "'IR' indique un mouvement qui :", "options": ["S'éloigne de la personne qui parle (Aller)", "Se rapproche de la personne qui parle (Venir)", "Reste sur place", "Indique le passé"], "correct_answer": "S'éloigne de la personne qui parle (Aller)", "explanation": "Ir = aller vers un lieu distant.", "xp": 15},
                            {"id": 1367, "type": "fill_in_the_blank", "question": "Yo ___ (ir) al supermercado a comprar comida.", "options": None, "correct_answer": "voy", "explanation": "Voy a (mouvement vers l'extérieur).", "xp": 15},
                            {"id": 1368, "type": "multiple_choice", "question": "¿A qué hora ___ tú a mi casa hoy? (vers chez moi)", "options": ["vienes", "vas", "voy", "vengo"], "correct_answer": "vienes", "explanation": "Mouvement vers l'interlocuteur = VENIR.", "xp": 15},
                            {"id": 1369, "type": "fill_in_the_blank", "question": "Mis abuelos ___ (venir) de visita este domingo.", "options": None, "correct_answer": "vienen", "explanation": "Vienen.", "xp": 15},
                            {"id": 1370, "type": "multiple_choice", "question": "Nosotros ___ de París (origen) y ___ a Madrid (destino).", "options": ["venimos / vamos", "vamos / venimos", "venimos / venimos", "vamos / vamos"], "correct_answer": "venimos / vamos", "explanation": "Venir de (origine) / Ir a (destination).", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_decir_formes_1",
                        "title": "Le verbe DECIR : Conjugaison complète au présent",
                        "questions": [
                            {"id": 1371, "type": "fill_in_the_blank", "question": "Yo siempre ___ (decir) la verdad.", "options": None, "correct_answer": "digo", "explanation": "Forme en -igo : 'Yo digo'.", "xp": 15},
                            {"id": 1372, "type": "multiple_choice", "question": "¿Qué ___ tú de esta propuesta?", "options": ["dices", "deces", "dice", "decís"], "correct_answer": "dices", "explanation": "Tú dices (affaiblissement E -> I).", "xp": 15},
                            {"id": 1373, "type": "fill_in_the_blank", "question": "El periódico ___ (decir) que mañana va a llover.", "options": None, "correct_answer": "dice", "explanation": "Él dice.", "xp": 15},
                            {"id": 1374, "type": "multiple_choice", "question": "Nosotros nunca ___ mentiras.", "options": ["decimos", "dicimos", "dicen", "decís"], "correct_answer": "decimos", "explanation": "Nosotros decimos (sans affaiblissement).", "xp": 15},
                            {"id": 1375, "type": "fill_in_the_blank", "question": "¿Vosotros qué ___ (decir) sobre el plan?", "options": None, "correct_answer": "decís", "explanation": "Vosotros decís.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_decir_vs_hablar",
                        "title": "Distinction : DECIR (Dire) vs HABLAR (Parler)",
                        "questions": [
                            {"id": 1376, "type": "multiple_choice", "question": "Yo ___ tres idiomas extranjeros. (hablar / decir)", "options": ["hablo", "digo", "haces", "sé"], "correct_answer": "hablo", "explanation": "Hablar idiomas.", "xp": 15},
                            {"id": 1377, "type": "fill_in_the_blank", "question": "¿Cómo se ___ 'bonjour' en español? (decir)", "options": None, "correct_answer": "dice", "explanation": "¿Cómo se dice? = Comment dit-on ?", "xp": 15},
                            {"id": 1378, "type": "multiple_choice", "question": "El profesor ___ que tenemos examen el lunes.", "options": ["dice", "habla", "digo", "hablas"], "correct_answer": "dice", "explanation": "Decir que + phrase = Dire que...", "xp": 15},
                            {"id": 1379, "type": "fill_in_the_blank", "question": "Nosotros ___ (hablar) por teléfono todas las semanas.", "options": None, "correct_answer": "hablamos", "explanation": "Hablar por teléfono.", "xp": 15},
                            {"id": 1380, "type": "multiple_choice", "question": "Yo te ___ que todo va a salir bien.", "options": ["digo", "hablo", "dices", "hablas"], "correct_answer": "digo", "explanation": "Decir algo a alguien.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_oir_formes_1",
                        "title": "Le verbe OÍR : Conjugaison complète au présent",
                        "questions": [
                            {"id": 1381, "type": "fill_in_the_blank", "question": "Yo ___ (oír) ruidos extraños en el jardín.", "options": None, "correct_answer": "oigo", "explanation": "Yo oigo (en -igo).", "xp": 15},
                            {"id": 1382, "type": "multiple_choice", "question": "¿___ tú el timbre de la puerta?", "options": ["Oyes", "Oies", "Oye", "Oís"], "correct_answer": "Oyes", "explanation": "Tú oyes (avec Y).", "xp": 15},
                            {"id": 1383, "type": "fill_in_the_blank", "question": "Mi abuelo no ___ (oír) muy bien.", "options": None, "correct_answer": "oye", "explanation": "Él oye.", "xp": 15},
                            {"id": 1384, "type": "multiple_choice", "question": "Nosotros ___ las noticias en la radio.", "options": ["oímos", "oyemos", "oyen", "oís"], "correct_answer": "oímos", "explanation": "Nosotros oímos (avec accent sur le i).", "xp": 15},
                            {"id": 1385, "type": "fill_in_the_blank", "question": "Ellos no ___ (oír) lo que dices por el viento.", "options": None, "correct_answer": "oyen", "explanation": "Ellos oyen.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_oir_vs_escuchar",
                        "title": "Distinction : OÍR (Entendre) vs ESCUCHAR (Écouter)",
                        "questions": [
                            {"id": 1386, "type": "multiple_choice", "question": "'ESCUCHAR' implique une action :", "options": ["Volontaire et attentive (Écouter)", "Involontaire et passive (Entendre)", "Uniquement musicale", "Impersonnelle"], "correct_answer": "Volontaire et attentive (Écouter)", "explanation": "Escuchar = Écouter avec attention. Oír = Percevoir un son (entendre).", "xp": 15},
                            {"id": 1387, "type": "fill_in_the_blank", "question": "Yo ___ (escuchar) música con auriculares mientras estudio.", "options": None, "correct_answer": "escucho", "explanation": "Escuchar música.", "xp": 15},
                            {"id": 1388, "type": "multiple_choice", "question": "¿___ ese trueno? Va a llover. (oír / escuchar)", "options": ["Oyes", "Escuchas", "Oigo", "Escuchamos"], "correct_answer": "Oyes", "explanation": "Perception auditive spontanée : oír.", "xp": 15},
                            {"id": 1389, "type": "fill_in_the_blank", "question": "Los estudiantes ___ (escuchar) con atención al profesor.", "options": None, "correct_answer": "escuchan", "explanation": "Escuchan.", "xp": 15},
                            {"id": 1390, "type": "multiple_choice", "question": "Yo no te ___, ¿puedes hablar más alto? (oír)", "options": ["oigo", "escucho", "oyes", "escuchas"], "correct_answer": "oigo", "explanation": "No oigo = Je n'entends pas.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ir_tener_venir_decir_personas_yo",
                        "title": "Les 4 géants en 'YO' : Voy, Tengo, Vengo, Digo",
                        "questions": [
                            {"id": 1391, "type": "multiple_choice", "question": "Formas de 'yo' de Ir, Tener, Venir, Decir :", "options": ["voy / tengo / vengo / digo", "vo / teno / veno / deco", "voy / tieno / vieno / digo", "va / tiene / viene / dice"], "correct_answer": "voy / tengo / vengo / digo", "explanation": "Voy / tengo / vengo / digo.", "xp": 15},
                            {"id": 1392, "type": "fill_in_the_blank", "question": "Yo ___ (ir) a clase, ___ (tener) examen y ___ (venir) cansado.", "options": None, "correct_answer": "voy / tengo / vengo", "explanation": "Voy / tengo / vengo.", "xp": 15},
                            {"id": 1393, "type": "multiple_choice", "question": "Yo te ___ que no ___ tiempo hoy. (decir / tener)", "options": ["digo / tengo", "dices / tienes", "digo / tieno", "dezo / tengo"], "correct_answer": "digo / tengo", "explanation": "Digo / tengo.", "xp": 15},
                            {"id": 1394, "type": "fill_in_the_blank", "question": "Yo ___ (venir) de Madrid y ___ (ir) hacia Barcelona.", "options": None, "correct_answer": "vengo / voy", "explanation": "Vengo / voy.", "xp": 15},
                            {"id": 1395, "type": "multiple_choice", "question": "Yo ___ la verdad y ___ a la policía. (decir / ir a ver)", "options": ["digo / voy a ver", "deces / va a ver", "digo / veo", "dices / voy"], "correct_answer": "digo / voy a ver", "explanation": "Digo / voy a ver.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ir_tener_venir_decir_personas_tu",
                        "title": "Les 4 géants en 'TÚ' : Vas, Tienes, Vienes, Dices",
                        "questions": [
                            {"id": 1396, "type": "multiple_choice", "question": "Formas de 'tú' de Ir, Tener, Venir, Decir :", "options": ["vas / tienes / vienes / dices", "vais / tenéis / venís / decís", "va / tiene / viene / dice", "ves / tenes / venes / deces"], "correct_answer": "vas / tienes / vienes / dices", "explanation": "Vas / tienes / vienes / dices.", "xp": 15},
                            {"id": 1397, "type": "fill_in_the_blank", "question": "¿Tú ___ (ir) al cine o ___ (tener) que estudiar?", "options": None, "correct_answer": "vas / tienes", "explanation": "Vas / tienes.", "xp": 15},
                            {"id": 1398, "type": "multiple_choice", "question": "¿Por qué no ___ a mi fiesta si ___ libre? (venir / tener)", "options": ["vienes / estás", "vas / eres", "vienes / tienes", "vienes / eres"], "correct_answer": "vienes / estás", "explanation": "Vienes / estás.", "xp": 15},
                            {"id": 1399, "type": "fill_in_the_blank", "question": "¿Qué ___ (decir) tú cuando no ___ (tener) razón?", "options": None, "correct_answer": "dices / tienes", "explanation": "Dices / tienes.", "xp": 15},
                            {"id": 1400, "type": "multiple_choice", "question": "¿Adónde ___ tú con tanta prisa?", "options": ["vas", "va", "voy", "van"], "correct_answer": "vas", "explanation": "Tú vas.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ir_tener_venir_decir_personas_el",
                        "title": "Les 4 géants en 'ÉL/ELLA/USTED' : Va, Tiene, Viene, Dice",
                        "questions": [
                            {"id": 1401, "type": "multiple_choice", "question": "Formas de 3a persona singular de Ir, Tener, Venir, Decir :", "options": ["va / tiene / viene / dice", "vas / tienes / vienes / dices", "voy / tengo / vengo / digo", "van / tienen / vienen / dicen"], "correct_answer": "va / tiene / viene / dice", "explanation": "Va / tiene / viene / dice.", "xp": 15},
                            {"id": 1402, "type": "fill_in_the_blank", "question": "El profesor ___ (decir) que el examen ___ (ser) fácil.", "options": None, "correct_answer": "dice / es", "explanation": "Dice / es.", "xp": 15},
                            {"id": 1403, "type": "multiple_choice", "question": "Usted ___ que firmar aquí antes de irse. (tener)", "options": ["tiene", "tienes", "tengo", "tenemos"], "correct_answer": "tiene", "explanation": "Usted tiene.", "xp": 15},
                            {"id": 1404, "type": "fill_in_the_blank", "question": "Mi amigo ___ (venir) desde muy lejos y ___ (ir) al hotel.", "options": None, "correct_answer": "viene / va", "explanation": "Viene / va.", "xp": 15},
                            {"id": 1405, "type": "multiple_choice", "question": "La televisión ___ que mañana lloverá.", "options": ["dice", "dices", "digo", "dicen"], "correct_answer": "dice", "explanation": "Dice.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ir_tener_venir_decir_personas_nosotros",
                        "title": "Les 4 géants en 'NOSOTROS' : Vamos, Tenemos, Venimos, Decimos",
                        "questions": [
                            {"id": 1406, "type": "multiple_choice", "question": "Formas de 'nosotros' de Ir, Tener, Venir, Decir :", "options": ["vamos / tenemos / venimos / decimos", "vamos / tienemos / vienimos / dicimos", "vais / tenéis / venís / decís", "van / tienen / vienen / dicen"], "correct_answer": "vamos / tenemos / venimos / decimos", "explanation": "Vamos / tenemos / venimos / decimos.", "xp": 15},
                            {"id": 1407, "type": "fill_in_the_blank", "question": "Nosotros ___ (ir) a la playa y ___ (tener) muchas ganas.", "options": None, "correct_answer": "vamos / tenemos", "explanation": "Vamos / tenemos.", "xp": 15},
                            {"id": 1408, "type": "multiple_choice", "question": "Nosotros ___ de muy lejos y ___ siempre la verdad. (venir / decir)", "options": ["venimos / decimos", "vamos / decimos", "venimos / dicimos", "vamos / hablamos"], "correct_answer": "venimos / decimos", "explanation": "Venimos / decimos.", "xp": 15},
                            {"id": 1409, "type": "fill_in_the_blank", "question": "¿Nosotros ___ (tener) clase de español hoy?", "options": None, "correct_answer": "tenemos", "explanation": "Tenemos.", "xp": 15},
                            {"id": 1410, "type": "multiple_choice", "question": "¡___ al parque a jugar!", "options": ["Vamos", "Vais", "Van", "Voy"], "correct_answer": "Vamos", "explanation": "Vamos.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ir_tener_venir_decir_personas_vosotros",
                        "title": "Les 4 géants en 'VOSOTROS' : Vais, Tenéis, Venís, Decís",
                        "questions": [
                            {"id": 1411, "type": "multiple_choice", "question": "Formas de 'vosotros' de Ir, Tener, Venir, Decir :", "options": ["vais / tenéis / venís / decís", "vamos / tenemos / venimos / decimos", "van / tienen / vienen / dicen", "vais / tienéis / vienís / dicís"], "correct_answer": "vais / tenéis / venís / decís", "explanation": "Vais / tenéis / venís / decís.", "xp": 15},
                            {"id": 1412, "type": "fill_in_the_blank", "question": "¿Vosotros ___ (ir) a la fiesta o ___ (tener) que trabajar?", "options": None, "correct_answer": "vais / tenéis", "explanation": "Vais / tenéis.", "xp": 15},
                            {"id": 1413, "type": "multiple_choice", "question": "¿Vosotros ___ a mi casa y me ___ qué opináis? (venir / decir)", "options": ["venís / decís", "venéis / decéis", "vienen / dicen", "venís / dicen"], "correct_answer": "venís / decís", "explanation": "Venís / decís.", "xp": 15},
                            {"id": 1414, "type": "fill_in_the_blank", "question": "¿Vosotros ___ (tener) frío aquí dentro?", "options": None, "correct_answer": "tenéis", "explanation": "Tenéis.", "xp": 15},
                            {"id": 1415, "type": "multiple_choice", "question": "¿Por qué no ___ nada? (vosotros / decir)", "options": ["decís", "dicís", "decéis", "dicen"], "correct_answer": "decís", "explanation": "Decís.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_ir_tener_venir_decir_personas_ellos",
                        "title": "Les 4 géants en 'ELLOS/ELLAS/USTEDES' : Van, Tienen, Vienen, Dicen",
                        "questions": [
                            {"id": 1416, "type": "multiple_choice", "question": "Formas de 3a persona plural de Ir, Tener, Venir, Decir :", "options": ["van / tienen / vienen / dicen", "vamos / tenemos / venimos / decimos", "vais / tenéis / venís / decís", "voy / tengo / vengo / digo"], "correct_answer": "van / tienen / vienen / dicen", "explanation": "Van / tienen / vienen / dicen.", "xp": 15},
                            {"id": 1417, "type": "fill_in_the_blank", "question": "Ellos ___ (ir) a Madrid porque ___ (tener) una reunión.", "options": None, "correct_answer": "van / tienen", "explanation": "Van / tienen.", "xp": 15},
                            {"id": 1418, "type": "multiple_choice", "question": "Mis amigos ___ a verme y me ___ que están contentos. (venir / decir)", "options": ["vienen / dicen", "van / dicen", "vienen / decen", "venen / dicen"], "correct_answer": "vienen / dicen", "explanation": "Vienen / dicen.", "xp": 15},
                            {"id": 1419, "type": "fill_in_the_blank", "question": "¿Ustedes ___ (tener) el billete de tren?", "options": None, "correct_answer": "tienen", "explanation": "Tienen.", "xp": 15},
                            {"id": 1420, "type": "multiple_choice", "question": "Los periódicos ___ que los precios suben.", "options": ["dicen", "decent", "dices", "dice"], "correct_answer": "dicen", "explanation": "Dicen.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_dialogo_viaje_ir_venir",
                        "title": "En situation : Organiser un voyage avec IR et VENIR",
                        "questions": [
                            {"id": 1421, "type": "multiple_choice", "question": "- ¿Cuándo ___ tú a Madrid? - ___ el próximo lunes. (ir / ir)", "options": ["vas / Voy", "vienes / Vengo", "va / Va", "vas / Vas"], "correct_answer": "vas / Voy", "explanation": "Vas / Voy.", "xp": 15},
                            {"id": 1422, "type": "fill_in_the_blank", "question": "Complétez : - ¿Y tus amigos ___ contigo? - Sí, ellos ___ en tren (venir).", "options": None, "correct_answer": "vienen / vienen", "explanation": "Vienen / vienen.", "xp": 15},
                            {"id": 1423, "type": "multiple_choice", "question": "- ¿Qué lugares ___ a visitar? (vosotros / ir)", "options": ["vais", "van", "vamos", "vas"], "correct_answer": "vais", "explanation": "Vais a visitar.", "xp": 15},
                            {"id": 1424, "type": "fill_in_the_blank", "question": "- Nosotros ___ (ir) a ver el Museo del Prado.", "options": None, "correct_answer": "vamos", "explanation": "Vamos.", "xp": 15},
                            {"id": 1425, "type": "multiple_choice", "question": "- ¡Qué bien! Yo ___ a recibiros a la estación. (ir)", "options": ["voy", "vas", "va", "vamos"], "correct_answer": "voy", "explanation": "Voy a recibiros.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_dialogo_consejos_tener_decir",
                        "title": "En situation : Donner des conseils avec TENER et DECIR",
                        "questions": [
                            {"id": 1426, "type": "multiple_choice", "question": "- Doctor, ___ fiebre y dolor de cabeza. (yo / tener)", "options": ["tengo", "tienes", "tiene", "tenemos"], "correct_answer": "tengo", "explanation": "Tengo.", "xp": 15},
                            {"id": 1427, "type": "fill_in_the_blank", "question": "Complétez : - El médico me ___ que descanse (decir).", "options": None, "correct_answer": "dice", "explanation": "Dice.", "xp": 15},
                            {"id": 1428, "type": "multiple_choice", "question": "- ¿Qué le ___ usted al paciente? (decir)", "options": ["dice", "dices", "digo", "dicen"], "correct_answer": "dice", "explanation": "Usted dice.", "xp": 15},
                            {"id": 1429, "type": "fill_in_the_blank", "question": "- Le ___ (decir - 1a pers) que ___ (tener) que tomar este jarabe.", "options": None, "correct_answer": "digo / tiene", "explanation": "Digo / tiene.", "xp": 15},
                            {"id": 1430, "type": "multiple_choice", "question": "- Nosotros ___ que cuidarnos mucho en invierno. (tener)", "options": ["tenemos", "tienen", "tenéis", "tengo"], "correct_answer": "tenemos", "explanation": "Tenemos.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_tabla_irregulares_totales",
                        "title": "Grille de synthèse : Les 5 verbes majeurs (Ser, Estar, Ir, Tener, Venir)",
                        "questions": [
                            {"id": 1431, "type": "multiple_choice", "question": "Formas de 'yo' de Ser, Estar, Ir, Tener, Venir :", "options": ["soy / estoy / voy / tengo / vengo", "soi / estoi / voi / tieno / vieno", "soy / estoy / va / tengo / vengo", "eres / estás / vas / tienes / vienes"], "correct_answer": "soy / estoy / voy / tengo / vengo", "explanation": "Soy / estoy / voy / tengo / vengo.", "xp": 15},
                            {"id": 1432, "type": "fill_in_the_blank", "question": "Formas de 'tú' : eres / estás / vas / ___ / ___ (tener / venir).", "options": None, "correct_answer": "tienes / vienes", "explanation": "Tienes / vienes.", "xp": 15},
                            {"id": 1433, "type": "multiple_choice", "question": "Formas de 'nosotros' :", "options": ["somos / estamos / vamos / tenemos / venimos", "somos / estamos / vais / tenéis / venís", "son / están / van / tienen / vienen", "somos / estamos / vamos / tienemos / vienimos"], "correct_answer": "somos / estamos / vamos / tenemos / venimos", "explanation": "Formes régulières de nous.", "xp": 15},
                            {"id": 1434, "type": "fill_in_the_blank", "question": "Formas de 'ellos' : son / están / van / ___ / ___ (tener / venir).", "options": None, "correct_answer": "tienen / vienen", "explanation": "Tienen / vienen.", "xp": 15},
                            {"id": 1435, "type": "multiple_choice", "question": "¿Cuál de estos 5 verbos NO tiene terminación en -OY en 'yo'?", "options": ["Tener (tengo)", "Ser (soy)", "Estar (estoy)", "Ir (voy)"], "correct_answer": "Tener (tengo)", "explanation": "Tener termina en -go (tengo).", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_gran_repaso_irregulares_totales",
                        "title": "Grand contrôle de synthèse : Les irréguliers majeurs",
                        "questions": [
                            {"id": 1436, "type": "fill_in_the_blank", "question": "Yo ___ (ir) a Madrid, ___ (venir) en tren y ___ (decir) hola.", "options": None, "correct_answer": "voy / vengo / digo", "explanation": "Voy / vengo / digo.", "xp": 15},
                            {"id": 1437, "type": "multiple_choice", "question": "¿Tú ___ (tener) frío? Nosotros ___ (ir) a encender la estufa.", "options": ["tienes / vamos", "tiene / va", "tienes / vais", "tengo / vamos"], "correct_answer": "tienes / vamos", "explanation": "Tienes / vamos.", "xp": 15},
                            {"id": 1438, "type": "fill_in_the_blank", "question": "Ellos ___ (decir) que ___ (venir) mañana por la tarde.", "options": None, "correct_answer": "dicen / vienen", "explanation": "Dicen / vienen.", "xp": 15},
                            {"id": 1439, "type": "multiple_choice", "question": "Usted ___ (oír) lo que yo le ___ (decir).", "options": ["oye / digo", "oyes / dices", "oigo / dice", "oye / dice"], "correct_answer": "oye / digo", "explanation": "Oye / digo.", "xp": 15},
                            {"id": 1440, "type": "fill_in_the_blank", "question": "¿Vosotros ___ (ir) o ___ (venir)?", "options": None, "correct_answer": "vais / venís", "explanation": "Vais / venís.", "xp": 15}
                        ]
                    },

                    # =========================================================
                    # SECTION 7 : GRANDS BILANS CROISÉS DU PRÉSENT A1 (Quiz 89 à 100, id 1441-1500)
                    # =========================================================
                    {
                        "id": "a1_conj_bilan_mix_1",
                        "title": "Bilan Mixte 1 : Diphtongue + Irrégulier en YO",
                        "questions": [
                            {"id": 1441, "type": "multiple_choice", "question": "Yo ___ (hacer) la maleta y ___ (cerrar) con llave. (hacer / cerrar)", "options": ["hago / cierro", "haco / cerro", "hago / cerro", "haco / cierro"], "correct_answer": "hago / cierro", "explanation": "Hago / cierro.", "xp": 15},
                            {"id": 1442, "type": "fill_in_the_blank", "question": "Yo ___ (salir) de casa cuando ___ (empezar) a llover.", "options": None, "correct_answer": "salgo / empieza", "explanation": "Salgo / empieza.", "xp": 15},
                            {"id": 1443, "type": "multiple_choice", "question": "Yo no ___ (saber) a qué hora ___ (volver) el tren.", "options": ["sé / vuelve", "conozco / vuelve", "sé / volve", "sabo / vuelve"], "correct_answer": "sé / vuelve", "explanation": "Sé / vuelve.", "xp": 15},
                            {"id": 1444, "type": "fill_in_the_blank", "question": "Yo ___ (poner) la mesa y ___ (pedir) la comida.", "options": None, "correct_answer": "pongo / pido", "explanation": "Pongo / pido.", "xp": 15},
                            {"id": 1445, "type": "multiple_choice", "question": "Yo te ___ (dar) el dinero si tú ___ (poder) comprarlo.", "options": ["doy / puedes", "doy / podes", "da / puedes", "doy / puede"], "correct_answer": "doy / puedes", "explanation": "Doy / puedes.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_bilan_mix_2",
                        "title": "Bilan Mixte 2 : Réguliers vs Irréguliers",
                        "questions": [
                            {"id": 1446, "type": "fill_in_the_blank", "question": "Yo ___ (hablar - reg) español pero no ___ (saber - irreg) alemán.", "options": None, "correct_answer": "hablo / sé", "explanation": "Hablo / sé.", "xp": 15},
                            {"id": 1447, "type": "multiple_choice", "question": "Nosotros ___ (vivir - reg) aquí y ___ (conocer - zco) a todo el barrio.", "options": ["vivimos / conocemos", "vivimos / conozcamos", "viven / conocen", "vivo / conozco"], "correct_answer": "vivimos / conocemos", "explanation": "Vivimos / conocemos.", "xp": 15},
                            {"id": 1448, "type": "fill_in_the_blank", "question": "Ellos ___ (comer - reg) juntos y luego ___ (salir - irreg) a pasear.", "options": None, "correct_answer": "comen / salen", "explanation": "Comen / salen.", "xp": 15},
                            {"id": 1449, "type": "multiple_choice", "question": "Tú ___ (estudiar - reg) mucho y ___ (tener - irreg) buenas notas.", "options": ["estudias / tienes", "estudia / tiene", "estudio / tengo", "estudias / tenes"], "correct_answer": "estudias / tienes", "explanation": "Estudias / tienes.", "xp": 15},
                            {"id": 1450, "type": "fill_in_the_blank", "question": "Vosotros ___ (escribir - reg) correos y ___ (hacer - irreg) llamadas.", "options": None, "correct_answer": "escribís / hacéis", "explanation": "Escribís / hacéis.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_bilan_mix_3",
                        "title": "Bilan Mixte 3 : Ser, Estar, Tener et Verbes de mouvement",
                        "questions": [
                            {"id": 1451, "type": "multiple_choice", "question": "Yo ___ (ser) médico, ___ (estar) en el hospital y ___ (ir) a visitar enfermos.", "options": ["soy / estoy / voy", "estoy / soy / voy", "soy / estoy / va", "estoy / estoy / voy"], "correct_answer": "soy / estoy / voy", "explanation": "Soy / estoy / voy.", "xp": 15},
                            {"id": 1452, "type": "fill_in_the_blank", "question": "¿Dónde ___ (estar) tú? Yo ya ___ (venir) de camino.", "options": None, "correct_answer": "estás / vengo", "explanation": "Estás / vengo.", "xp": 15},
                            {"id": 1453, "type": "multiple_choice", "question": "Ellos ___ (ser) de Sevilla y ___ (tener) una casa allí.", "options": ["son / tienen", "están / tienen", "son / tenen", "están / son"], "correct_answer": "son / tienen", "explanation": "Son / tienen.", "xp": 15},
                            {"id": 1454, "type": "fill_in_the_blank", "question": "Nosotros ___ (estar) cansados porque ___ (venir) andando.", "options": None, "correct_answer": "estamos / venimos", "explanation": "Estamos / venimos.", "xp": 15},
                            {"id": 1455, "type": "multiple_choice", "question": "El examen ___ (ser) difícil pero yo ___ (saber) las respuestas.", "options": ["es / sé", "está / sé", "es / conozco", "está / conozco"], "correct_answer": "es / sé", "explanation": "Es / sé.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_bilan_mix_4",
                        "title": "Bilan Mixte 4 : Les verbes de communication (Decir, Hablar, Contar, Preguntar)",
                        "questions": [
                            {"id": 1456, "type": "fill_in_the_blank", "question": "Yo ___ (hablar) despacio para que me ___ (entender - tú).", "options": None, "correct_answer": "hablo / entiendas", "explanation": "Hablo / entiendes (présent indicatif).", "xp": 15},
                            {"id": 1457, "type": "multiple_choice", "question": "¿Qué le ___ tú al profesor cuando no comprendes?", "options": ["preguntas", "dices", "hablas", "cuentas"], "correct_answer": "preguntas", "explanation": "Preguntar = Poser une question.", "xp": 15},
                            {"id": 1458, "type": "fill_in_the_blank", "question": "Mi abuelo nos ___ (contar) historias de su juventud.", "options": None, "correct_answer": "cuenta", "explanation": "Cuenta (diphtongue O -> UE).", "xp": 15},
                            {"id": 1459, "type": "multiple_choice", "question": "Nosotros ___ (decir) 'gracias' y ellos ___ (responder) 'de nada'.", "options": ["decimos / responden", "dicimos / responden", "decimos / respondes", "dicen / responden"], "correct_answer": "decimos / responden", "explanation": "Decimos / responden.", "xp": 15},
                            {"id": 1460, "type": "fill_in_the_blank", "question": "Yo siempre te ___ (decir) la verdad.", "options": None, "correct_answer": "digo", "explanation": "Yo digo.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_bilan_mix_5",
                        "title": "Bilan Mixte 5 : La vie quotidienne et les routines complètes",
                        "questions": [
                            {"id": 1461, "type": "multiple_choice", "question": "Por la mañana yo me ___ (despertar), me ___ (vestir) y ___ (salir) de casa.", "options": ["despierto / visto / salgo", "desperto / vesto / salo", "despierto / visto / salo", "desperto / visto / salgo"], "correct_answer": "despierto / visto / salgo", "explanation": "Despierto (E->IE) / visto (E->I) / salgo (irrégulier -go).", "xp": 15},
                            {"id": 1462, "type": "fill_in_the_blank", "question": "¿A qué hora ___ (empezar) tu clase y a qué hora ___ (volver) a casa?", "options": None, "correct_answer": "empieza / vuelves", "explanation": "Empieza / vuelves.", "xp": 15},
                            {"id": 1463, "type": "multiple_choice", "question": "Nosotros ___ (almorzar) a las dos y ___ (hacer) una pausa de una hora.", "options": ["almorzamos / hacemos", "almuerzamos / hacemos", "almorzamos / hagamos", "almuerzan / hacen"], "correct_answer": "almorzamos / hacemos", "explanation": "Almorzamos / hacemos.", "xp": 15},
                            {"id": 1464, "type": "fill_in_the_blank", "question": "Por la tarde yo ___ (hacer) deporte y luego ___ (ver) la televisión.", "options": None, "correct_answer": "hago / veo", "explanation": "Hago / veo.", "xp": 15},
                            {"id": 1465, "type": "multiple_choice", "question": "Por la noche ellos se ___ (acostar) y ___ (dormir) ocho horas.", "options": ["acuestan / duermen", "acostan / dormen", "acuestan / dormen", "acostan / duermen"], "correct_answer": "acuestan / duermen", "explanation": "Acuestan / duermen (O->UE).", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_bilan_mix_6",
                        "title": "Bilan Mixte 6 : Faire des achats et commander",
                        "questions": [
                            {"id": 1466, "type": "fill_in_the_blank", "question": "Yo ___ (querer) un kilo de manzanas. ¿Cuánto ___ (costar)?", "options": None, "correct_answer": "quiero / cuesta", "explanation": "Quiero / cuesta.", "xp": 15},
                            {"id": 1467, "type": "multiple_choice", "question": "¿Qué ___ (preferir) comer vosotros hoy?", "options": ["preferís", "prefierís", "prefieren", "preferimos"], "correct_answer": "preferís", "explanation": "Preferís.", "xp": 15},
                            {"id": 1468, "type": "fill_in_the_blank", "question": "El camarero nos ___ (servir) el menú y nosotros ___ (pedir) la cuenta.", "options": None, "correct_answer": "sirve / pedimos", "explanation": "Sirve / pedimos.", "xp": 15},
                            {"id": 1469, "type": "multiple_choice", "question": "Yo ___ (poner) el dinero en la mesa y te ___ (dar) el cambio.", "options": ["pongo / doy", "pono / do", "pongo / do", "pono / doy"], "correct_answer": "pongo / doy", "explanation": "Pongo / doy.", "xp": 15},
                            {"id": 1470, "type": "fill_in_the_blank", "question": "Nosotros no ___ (poder) pagar con tarjeta porque no ___ (haber) datáfono.", "options": None, "correct_answer": "podemos / hay", "explanation": "Podemos / hay.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_bilan_mix_7",
                        "title": "Bilan Mixte 7 : Orientation, Ville et Itinéraires",
                        "questions": [
                            {"id": 1471, "type": "multiple_choice", "question": "Para ir al museo, usted ___ (seguir) todo recto y ___ (girar) a la derecha.", "options": ["sigue / gira", "segue / gira", "sigo / giro", "siguen / giran"], "correct_answer": "sigue / gira", "explanation": "Sigue / gira.", "xp": 15},
                            {"id": 1472, "type": "fill_in_the_blank", "question": "Yo no ___ (conocer) este barrio y no ___ (saber) dónde está la estación.", "options": None, "correct_answer": "conozco / sé", "explanation": "Conozco / sé.", "xp": 15},
                            {"id": 1473, "type": "multiple_choice", "question": "¿Tú ___ (coger) el autobús o ___ (ir) andando?", "options": ["coges / vas", "cojo / voy", "coge / va", "cogéis / vais"], "correct_answer": "coges / vas", "explanation": "Coges / vas.", "xp": 15},
                            {"id": 1474, "type": "fill_in_the_blank", "question": "Nosotros ___ (salir) de la boca de metro y ___ (cruzar) la plaza.", "options": None, "correct_answer": "salimos / cruzamos", "explanation": "Salimos / cruzamos.", "xp": 15},
                            {"id": 1475, "type": "multiple_choice", "question": "El autobús ___ (venir) lleno y no ___ (caber) más gente.", "options": ["viene / cabe", "vienen / caben", "vengo / quepo", "va / cabe"], "correct_answer": "viene / cabe", "explanation": "Viene / cabe.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_bilan_mix_8",
                        "title": "Bilan Mixte 8 : Sentiments, Sensations et États de santé",
                        "questions": [
                            {"id": 1476, "type": "fill_in_the_blank", "question": "Yo me ___ (sentir) mareado y me ___ (doler) la cabeza.", "options": None, "correct_answer": "siento / duele", "explanation": "Siento / duele.", "xp": 15},
                            {"id": 1477, "type": "multiple_choice", "question": "¿Tú ___ (tener) fiebre o solo ___ (estar) cansado?", "options": ["tienes / estás", "tiene / está", "tienes / eres", "tengo / estoy"], "correct_answer": "tienes / estás", "explanation": "Tienes / estás.", "xp": 15},
                            {"id": 1478, "type": "fill_in_the_blank", "question": "El médico me ___ (decir) que ___ (tener) que guardar cama.", "options": None, "correct_answer": "dice / tengo", "explanation": "Dice / tengo.", "xp": 15},
                            {"id": 1479, "type": "multiple_choice", "question": "A los niños les ___ (doler) los oídos por el frío.", "options": ["duelen", "duele", "dolen", "dolemos"], "correct_answer": "duelen", "explanation": "Duelen (sujet pluriel).", "xp": 15},
                            {"id": 1480, "type": "fill_in_the_blank", "question": "Nosotros nos ___ (morir) de frío porque no funciona la calefacción.", "options": None, "correct_answer": "morimos", "explanation": "Morimos.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_bilan_mix_9",
                        "title": "Bilan Mixte 9 : Loisirs, Sports et Vacances",
                        "questions": [
                            {"id": 1481, "type": "multiple_choice", "question": "Los sábados yo ___ (jugar) al fútbol y mis amigos ___ (ir) a la piscina.", "options": ["juego / van", "jugo / van", "juego / va", "jugamos / vamos"], "correct_answer": "juego / van", "explanation": "Juego / van.", "xp": 15},
                            {"id": 1482, "type": "fill_in_the_blank", "question": "¿Vosotros ___ (hacer) deporte o ___ (preferir) ver la tele?", "options": None, "correct_answer": "hacéis / preferís", "explanation": "Hacéis / preferís.", "xp": 15},
                            {"id": 1483, "type": "multiple_choice", "question": "Nosotros ___ (querer) viajar a Italia en verano.", "options": ["queremos", "quieremos", "quieren", "queréis"], "correct_answer": "queremos", "explanation": "Queremos.", "xp": 15},
                            {"id": 1484, "type": "fill_in_the_blank", "question": "Yo ___ (conocer) una playa preciosa donde no ___ (haber) nadie.", "options": None, "correct_answer": "conozco / hay", "explanation": "Conozco / hay.", "xp": 15},
                            {"id": 1485, "type": "multiple_choice", "question": "Ellos ___ (volver) muy contentos de sus vacaciones.", "options": ["vuelven", "volven", "vuelve", "volvemos"], "correct_answer": "vuelven", "explanation": "Vuelven.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_bilan_mix_10",
                        "title": "Bilan Mixte 10 : Météo et Projets d'avenir immédiat",
                        "questions": [
                            {"id": 1486, "type": "fill_in_the_blank", "question": "Hoy ___ (hacer) sol pero mañana ___ (llover).", "options": None, "correct_answer": "hace / llueve", "explanation": "Hace / llueve.", "xp": 15},
                            {"id": 1487, "type": "multiple_choice", "question": "En invierno ___ (nevar) en la montaña y nosotros ___ (ir) a esquiar.", "options": ["nieva / vamos", "neva / vamos", "nieva / van", "neva / voy"], "correct_answer": "nieva / vamos", "explanation": "Nieva / vamos.", "xp": 15},
                            {"id": 1488, "type": "fill_in_the_blank", "question": "¿Qué ___ (pensar) hacer tú si mañana ___ (hacer) mal tiempo?", "options": None, "correct_answer": "piensas / hace", "explanation": "Piensas / hace.", "xp": 15},
                            {"id": 1489, "type": "multiple_choice", "question": "Yo voy a ___ (quedarse) en casa leyendo un libro.", "options": ["quedarme", "me quedo", "quedarse", "quedo"], "correct_answer": "quedarme", "explanation": "Voy a quedarme.", "xp": 15},
                            {"id": 1490, "type": "fill_in_the_blank", "question": "Ellos ___ (ir) a salir aunque ___ (hacer) frío.", "options": None, "correct_answer": "van / hace", "explanation": "Van / hace.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_bilan_mix_11",
                        "title": "Bilan Mixte 11 : Le grand test récapitulatif (Partie 1)",
                        "questions": [
                            {"id": 1491, "type": "multiple_choice", "question": "¿Cuál es la forma correcta de 'yo' para : Ser, Conocer, Saber, Venir, Dormir?", "options": ["soy, conozco, sé, vengo, duermo", "estoy, conoco, sé, vengo, duermo", "soy, conozco, sabo, vieno, dormo", "soy, conozco, sé, veno, duermo"], "correct_answer": "soy, conozco, sé, vengo, duermo", "explanation": "Soy, conozco, sé, vengo, duermo.", "xp": 15},
                            {"id": 1492, "type": "fill_in_the_blank", "question": "Tú ___ (hacer) la comida, él ___ (poner) la mesa y yo ___ (servir) el vino.", "options": None, "correct_answer": "haces / pone / sirvo", "explanation": "Haces / pone / sirvo.", "xp": 15},
                            {"id": 1493, "type": "multiple_choice", "question": "Nosotros ___ (querer) aprender, vosotros ___ (poder) ayudar y ellos ___ (pedir) consejos.", "options": ["queremos / podéis / piden", "quieremos / podéis / piden", "queremos / puedéis / peden", "quieren / pueden / piden"], "correct_answer": "queremos / podéis / piden", "explanation": "Queremos / podéis / piden.", "xp": 15},
                            {"id": 1494, "type": "fill_in_the_blank", "question": "Yo ___ (ir) a la tienda porque no ___ (haber) leche en la nevera.", "options": None, "correct_answer": "voy / hay", "explanation": "Voy / hay.", "xp": 15},
                            {"id": 1495, "type": "multiple_choice", "question": "El profesor ___ (decir) que nosotros ___ (hablar) muy bien español.", "options": ["dice / hablamos", "dices / hablamos", "digo / hablan", "dicen / hablamos"], "correct_answer": "dice / hablamos", "explanation": "Dice / hablamos.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_bilan_mix_12_final",
                        "title": "Bilan Mixte 12 : L'Épreuve Finale A1 (Presente de Indicativo)",
                        "questions": [
                            {"id": 1496, "type": "fill_in_the_blank", "question": "Yo ___ (ser) estudiante, ___ (tener) 20 años y ___ (vivir) en Madrid.", "options": None, "correct_answer": "soy / tengo / vivo", "explanation": "Soy / tengo / vivo.", "xp": 15},
                            {"id": 1497, "type": "multiple_choice", "question": "Todos los días yo ___ (salir) de casa a las ocho, ___ (coger) el metro y ___ (llegar) puntual.", "options": ["salgo / cojo / llego", "salo / cojo / llego", "salgo / cogo / llego", "salgo / cojo / llega"], "correct_answer": "salgo / cojo / llego", "explanation": "Salgo / cojo / llego.", "xp": 15},
                            {"id": 1498, "type": "fill_in_the_blank", "question": "¿Tú ___ (saber) a qué hora ___ (empezar) la película esta noche?", "options": None, "correct_answer": "sabes / empieza", "explanation": "Sabes / empieza.", "xp": 15},
                            {"id": 1499, "type": "multiple_choice", "question": "Nosotros ___ (entender) el ejercicio pero no ___ (recordar) la palabra exacta.", "options": ["entendemos / recordamos", "entiendemos / recuerdamos", "entendemos / recuerdan", "entienden / recordamos"], "correct_answer": "entendemos / recordamos", "explanation": "Entendemos / recordamos.", "xp": 15},
                            {"id": 1500, "type": "fill_in_the_blank", "question": "Ellos ___ (venir) a mi casa porque ___ (querer) celebrar mi cumpleaños.", "options": None, "correct_answer": "vienen / quieren", "explanation": "Vienen / quieren.", "xp": 15}
                        ]
                    }

                ]
            },
            "ecoute": {
                "title": "Écoute & Phonétique",
                "exercises": []
            }
        }
    },

     "A2": {
        "title": "Niveau A2 - Pré-intermédiaire",
        "categories": {
            "vocabulaire": {
                "title": "Vocabulaire",
                "exercises": [
                    {
                        "id": "a1_voc_datos_personales_1",
                        "title": "Données personnelles et coordonnées",
                        "questions": [
                            {"id": 1501, "type": "multiple_choice", "question": "- ¿De dónde eres? - ___", "options": ["Soy de Valencia, en España", "Tengo veinticinco años", "Vivo en la calle Mayor", "Estoy muy bien"], "correct_answer": "Soy de Valencia, en España", "explanation": "Réponse directe à la question de provenance/origine.", "xp": 10},
                            {"id": 1502, "type": "fill_in_the_blank", "question": "Complétez : - ¿A qué te ___? - Soy enfermera (consacrer / métier).", "options": None, "correct_answer": "dedicas", "explanation": "'¿A qué te dedicas?' = Quel est ton métier / Que fais-tu dans la vie ?", "xp": 10},
                            {"id": 1503, "type": "multiple_choice", "question": "- ¿Cuál es tu número de teléfono? - ___", "options": ["Es el 654 32 10 98", "Tengo dos teléfonos", "Vivo en el centro", "Me llamo Mateo"], "correct_answer": "Es el 654 32 10 98", "explanation": "Donner son numéro de téléphone avec 'Es el...'.", "xp": 10},
                            {"id": 1504, "type": "fill_in_the_blank", "question": "Complétez : - ¿Tienes correo ___? - Sí, es ana@email.com.", "options": None, "correct_answer": "electrónico", "explanation": "'Correo electrónico' = Adresse e-mail.", "xp": 10},
                            {"id": 1505, "type": "multiple_choice", "question": "- ¿Cuántos idiomas hablas? - ___", "options": ["Hablo francés y un poco de español", "Soy francés", "Estudio en París", "Vivo en Francia"], "correct_answer": "Hablo francés y un poco de español", "explanation": "Réponse sur les compétences linguistiques.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_familia_amigos_1",
                        "title": "La famille et les relations proches",
                        "questions": [
                            {"id": 1506, "type": "multiple_choice", "question": "- ¿Tienes hermanos? - ___", "options": ["Sí, tengo un hermano mayor y una hermana menor", "Tengo veinte años", "Mis padres son simpáticos", "Vivo solo"], "correct_answer": "Sí, tengo un hermano mayor y una hermana menor", "explanation": "Réponse sur la fratrie.", "xp": 10},
                            {"id": 1507, "type": "fill_in_the_blank", "question": "Complétez : Mi hermano mayor se llama Carlos y mi hermana ___ es Sofía (cadette / plus jeune).", "options": None, "correct_answer": "menor", "explanation": "'Menor' = Plus jeune / cadet(te).", "xp": 10},
                            {"id": 1508, "type": "multiple_choice", "question": "- ¿Cómo es tu mejor amigo? - ___", "options": ["Es alto, moreno y muy divertido", "Vive en el campo", "Tiene dos coches", "Trabaja en un banco"], "correct_answer": "Es alto, moreno y muy divertido", "explanation": "Description physique et morale d'un proche.", "xp": 10},
                            {"id": 1509, "type": "fill_in_the_blank", "question": "Complétez : Los padres de mi padre son mis ___ (grands-parents).", "options": None, "correct_answer": "abuelos", "explanation": "'Los abuelos' = Les grands-parents.", "xp": 10},
                            {"id": 1510, "type": "multiple_choice", "question": "- ¿Estás casado o soltero? - ___", "options": ["Estoy soltero, pero vivo con mi pareja", "Tengo dos hijos", "Soy simpático", "Tengo treinta años"], "correct_answer": "Estoy soltero, pero vivo con mi pareja", "explanation": "État civil et situation personnelle.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_rutina_diaria_1",
                        "title": "Rythme de vie et moments clés de la journée",
                        "questions": [
                            {"id": 1511, "type": "multiple_choice", "question": "- ¿A qué hora sales de trabajar los viernes? - ___", "options": ["Salgo a las tres de la tarde", "Voy en autobús", "Trabajo en una oficina", "Como con mis compañeros"], "correct_answer": "Salgo a las tres de la tarde", "explanation": "Indication d'horaire précise.", "xp": 10},
                            {"id": 1512, "type": "fill_in_the_blank", "question": "Complétez : Tomo el café y las tostadas durante el ___ (petit-déjeuner).", "options": None, "correct_answer": "desayuno", "explanation": "'El desayuno' = Le petit-déjeuner.", "xp": 10},
                            {"id": 1513, "type": "multiple_choice", "question": "- ¿Qué sueles hacer por las tardes después de clase? - ___", "options": ["Suelo ir al gimnasio o leer un rato", "Me despierto temprano", "Ceno a las nueve", "Empiezo a las ocho"], "correct_answer": "Suelo ir al gimnasio o leer un rato", "explanation": "Description des habitudes de fin de journée.", "xp": 10},
                            {"id": 1514, "type": "fill_in_the_blank", "question": "Complétez : Para relajarme después de cenar leo un ___ en la cama (livre).", "options": None, "correct_answer": "libro", "explanation": "'El libro' = Le livre.", "xp": 10},
                            {"id": 1515, "type": "multiple_choice", "question": "- ¿Cenas siempre en casa? - Casi siempre, pero los fines de semana ___", "options": ["cenamos en restaurantes con amigos", "duermo ocho horas", "me levanto a las siete", "hago la compra"], "correct_answer": "cenamos en restaurantes con amigos", "explanation": "Nuance de fréquence dans les habitudes.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_gustos_intereses_1",
                        "title": "Goûts, passions et activités de loisirs",
                        "questions": [
                            {"id": 1516, "type": "multiple_choice", "question": "- ¿Qué tipo de música te gusta? - ___", "options": ["Me gusta mucho el rock y la música pop", "Toco el piano", "Voy a conciertos", "No escucho la radio"], "correct_answer": "Me gusta mucho el rock y la música pop", "explanation": "Expression des préférences musicales.", "xp": 10},
                            {"id": 1517, "type": "fill_in_the_blank", "question": "Complétez : En mi tiempo libre mi gran pasión es la ___ de montaña (randonnée).", "options": None, "correct_answer": "senderismo", "explanation": "'El senderismo' = La randonnée.", "xp": 10},
                            {"id": 1518, "type": "multiple_choice", "question": "- A mí no me gusta el frío. - A mí ___", "options": ["tampoco", "también", "sí", "no"], "correct_answer": "tampoco", "explanation": "'Tampoco' marque l'accord avec une phrase négative (Moi non plus).", "xp": 10},
                            {"id": 1519, "type": "fill_in_the_blank", "question": "Complétez : Para ver películas en pantalla gigante voy al ___ (cinéma).", "options": None, "correct_answer": "cine", "explanation": "'El cine' = Le cinéma.", "xp": 10},
                            {"id": 1520, "type": "multiple_choice", "question": "- Me gusta mucho viajar por el mundo. - ¡A mí ___! Me encanta descubrir culturas.", "options": ["también", "tampoco", "no", "nada"], "correct_answer": "también", "explanation": "'A mí también' marque l'accord affirmatif (Moi aussi).", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_vivienda_barrio_1",
                        "title": "Description du cadre de vie et du quartier",
                        "questions": [
                            {"id": 1521, "type": "multiple_choice", "question": "- ¿Cómo es tu barrio? - ___", "options": ["Es muy tranquilo y tiene muchas zonas verdes", "Vivo en el tercer piso", "Tiene tres habitaciones", "Está cerrado"], "correct_answer": "Es muy tranquilo y tiene muchas zonas verdes", "explanation": "Description qualitative de l'environnement de vie.", "xp": 10},
                            {"id": 1522, "type": "fill_in_the_blank", "question": "Complétez : Mi piso tiene un ___ muy amplio para tomar el sol (balcon / terrasse).", "options": None, "correct_answer": "balcón", "explanation": "'El balcón' = Le balcon.", "xp": 10},
                            {"id": 1523, "type": "multiple_choice", "question": "- ¿Hay comercios cerca de tu casa? - Sí, ___", "options": ["hay una farmacia y un mercado justo al lado", "es luminoso", "son amables", "cuesta poco"], "correct_answer": "hay una farmacia y un mercado justo al lado", "explanation": "Commerces de proximité.", "xp": 10},
                            {"id": 1524, "type": "fill_in_the_blank", "question": "Complétez : El piso no tiene escaleras porque usamos el ___ (ascenseur).", "options": None, "correct_answer": "ascensor", "explanation": "'El ascensor' = L'ascenseur.", "xp": 10},
                            {"id": 1525, "type": "multiple_choice", "question": "- ¿Prefieres vivir en el centro o en las afueras? - ___", "options": ["Prefiero el centro porque todo está a mano", "Vivo en una casa", "Tengo dos ventanas", "El metro es rápido"], "correct_answer": "Prefiero el centro porque todo está a mano", "explanation": "'Estar a mano' = Être à portée de main / tout près.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_propuestas_citas_1",
                        "title": "Proposer une activité et convenir d'un rendez-vous",
                        "questions": [
                            {"id": 1526, "type": "multiple_choice", "question": "- ¿Te apetece ir a tomar algo esta tarde? - ___", "options": ["¡Sí, claro! ¿A qué hora nos vemos?", "Ayer fui al centro", "El café cuesta dos euros", "No tengo coche"], "correct_answer": "¡Sí, claro! ¿A qué hora nos vemos?", "explanation": "Accepter une proposition et organiser l'horaire.", "xp": 10},
                            {"id": 1527, "type": "fill_in_the_blank", "question": "Complétez : ¿Quedamos en la ___ del cine a las siete? (entrée / porte)", "options": None, "correct_answer": "puerta", "explanation": "'En la puerta del cine' = À l'entrée du cinéma.", "xp": 10},
                            {"id": 1528, "type": "multiple_choice", "question": "- ¿Qué tal si quedamos el sábado por la mañana? - ___", "options": ["Perfecto, me viene genial a esa hora", "Ayer fue viernes", "El sábado llovió", "Tengo hambre"], "correct_answer": "Perfecto, me viene genial a esa hora", "explanation": "'Me viene genial' = Ça me convient parfaitement.", "xp": 10},
                            {"id": 1529, "type": "fill_in_the_blank", "question": "Complétez : Lo siento, hoy no puedo porque tengo mucho ___ (travail).", "options": None, "correct_answer": "trabajo", "explanation": "'Tener mucho trabajo' = Avoir beaucoup de travail.", "xp": 10},
                            {"id": 1530, "type": "multiple_choice", "question": "- Si no puedes hoy, ¿lo dejamos para el domingo? - ___", "options": ["Sí, el domingo estoy completamente libre", "El domingo es el último día", "Cierran a las diez", "Voy a pie"], "correct_answer": "Sí, el domingo estoy completamente libre", "explanation": "Confirmation de disponibilité.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_compras_tiendas_1",
                        "title": "Achats de vêtements et interactions en magasin",
                        "questions": [
                            {"id": 1531, "type": "multiple_choice", "question": "- ¿En qué puedo ayudarle? - ___", "options": ["Buscaba una chaqueta azul para el invierno", "Tengo dos abrigos", "La tienda es moderna", "Llevo gafas"], "correct_answer": "Buscaba una chaqueta azul para el invierno", "explanation": "Exprimer son besoin à un vendeur.", "xp": 10},
                            {"id": 1532, "type": "fill_in_the_blank", "question": "Complétez : ¿Tiene esta camisa en una ___ mediana? (taille)", "options": None, "correct_answer": "talla", "explanation": "'La talla' = La taille du vêtement.", "xp": 10},
                            {"id": 1533, "type": "multiple_choice", "question": "- ¿Dónde están los probadores? - ___", "options": ["Al fondo a la derecha", "Cuesta cincuenta euros", "Es de lana", "Están pagados"], "correct_answer": "Al fondo a la derecha", "explanation": "Localisation des cabines d'essayage.", "xp": 10},
                            {"id": 1534, "type": "fill_in_the_blank", "question": "Complétez : El pantalón me queda muy ___ (étroit / serré).", "options": None, "correct_answer": "estrecho", "explanation": "'Estrecho' = Serré / étroit.", "xp": 10},
                            {"id": 1535, "type": "multiple_choice", "question": "- ¿Va a pagar en efectivo o con tarjeta? - ___", "options": ["Con tarjeta, aquí tiene", "Es caro", "Me gusta el color", "Vuelvo mañana"], "correct_answer": "Con tarjeta, aquí tiene", "explanation": "Choix du moyen de paiement.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_fines_de_semana_actividades",
                        "title": "Activités et loisirs de fin de semaine",
                        "questions": [
                            {"id": 1536, "type": "multiple_choice", "question": "- ¿Qué planes tienes para el fin de semana? - ___", "options": ["Voy a hacer una excursión con unos amigos", "Trabajo de nueve a cinco", "El viernes fue festivo", "Tengo clase de inglés"], "correct_answer": "Voy a hacer una excursión con unos amigos", "explanation": "Annonce de projet de loisir.", "xp": 10},
                            {"id": 1537, "type": "fill_in_the_blank", "question": "Complétez : Los sábados por la tarde nos reunimos para jugar al ___ (football).", "options": None, "correct_answer": "fútbol", "explanation": "'El fútbol' = Le football.", "xp": 10},
                            {"id": 1538, "type": "multiple_choice", "question": "- ¿Haces algo especial los domingos? - Normalmente ___", "options": ["organizo una comida con toda la familia", "me levanto a las seis", "estoy en la oficina", "tomo el metro"], "correct_answer": "organizo una comida con toda la familia", "explanation": "Activité dominicale typique.", "xp": 10},
                            {"id": 1539, "type": "fill_in_the_blank", "question": "Complétez : Por la noche solemos ver una ___ de comedia en casa (film).", "options": None, "correct_answer": "película", "explanation": "'La película' = Le film.", "xp": 10},
                            {"id": 1540, "type": "multiple_choice", "question": "- ¿A qué hora vuelves a casa los domingos? - ___", "options": ["Temprano, para preparar las cosas del lunes", "El lunes trabajo", "Es un buen plan", "Voy andando"], "correct_answer": "Temprano, para preparar las cosas del lunes", "explanation": "Précision d'horaire et motif.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_mundo_laboral_estudios",
                        "title": "Études, métiers et univers professionnel",
                        "questions": [
                            {"id": 1541, "type": "multiple_choice", "question": "- ¿Qué estudias en la universidad? - ___", "options": ["Estudio Periodismo y Comunicación", "Tengo veinte años", "La universidad está lejos", "Estudio todos los días"], "correct_answer": "Estudio Periodismo y Comunicación", "explanation": "Indication de la filière d'études.", "xp": 10},
                            {"id": 1542, "type": "fill_in_the_blank", "question": "Complétez : Comparto despacho con tres ___ muy simpáticos (collègues).", "options": None, "correct_answer": "compañeros", "explanation": "'Los compañeros' = Les collègues / camarades.", "xp": 10},
                            {"id": 1543, "type": "multiple_choice", "question": "- ¿Cuál es tu profesión? - ___", "options": ["Soy arquitecto en un estudio de diseño", "Trabajo ocho horas", "Gano en euros", "Tengo coche de empresa"], "correct_answer": "Soy arquitecto en un estudio de diseño", "explanation": "Métier et lieu de travail.", "xp": 10},
                            {"id": 1544, "type": "fill_in_the_blank", "question": "Complétez : Trabajo en una gran ___ de telecomunicaciones (entreprise).", "options": None, "correct_answer": "empresa", "explanation": "'La empresa' = L'entreprise / la société.", "xp": 10},
                            {"id": 1545, "type": "multiple_choice", "question": "- ¿Qué es lo que más te gusta de tu trabajo? - ___", "options": ["El buen ambiente de equipo y los proyectos creativos", "Tengo ordenador", "La oficina es blanca", "Empiezo en septiembre"], "correct_answer": "El buen ambiente de equipo y los proyectos creativos", "explanation": "Appréciation des conditions de travail.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_estancia_hotel_viaje",
                        "title": "Séjour à l'hôtel et services de voyage",
                        "questions": [
                            {"id": 1546, "type": "multiple_choice", "question": "- Buenas tardes, tengo una reserva a nombre de Carlos Ramos. - ___", "options": ["Buenas tardes, permítame su documento de identidad, por favor", "La habitación es grande", "El hotel tiene piscina", "Hasta mañana"], "correct_answer": "Buenas tardes, permítame su documento de identidad, por favor", "explanation": "Formalité d'enregistrement à l'hôtel.", "xp": 10},
                            {"id": 1547, "type": "fill_in_the_blank", "question": "Complétez : El hotel ofrece conexión a internet ___ en todas las habitaciones (gratuite).", "options": None, "correct_answer": "gratis", "explanation": "'Gratis' (ou 'gratuita') = Gratuit(e).", "xp": 10},
                            {"id": 1548, "type": "multiple_choice", "question": "- ¿A qué hora sirven el desayuno? - ___", "options": ["De siete a diez de la mañana en el comedor", "Cuesta doce euros", "Es continental", "En el primer piso"], "correct_answer": "De siete a diez de la mañana en el comedor", "explanation": "Horaire du service du petit-déjeuner.", "xp": 10},
                            {"id": 1549, "type": "fill_in_the_blank", "question": "Complétez : ¿Me puede dar la ___ de la habitación 302? (clé)", "options": None, "correct_answer": "llave", "explanation": "'La llave' = La clé.", "xp": 10},
                            {"id": 1550, "type": "multiple_choice", "question": "- ¿Hay aparcamiento para los clientes? - Sí, ___", "options": ["tenemos un garaje privado en el sótano", "el coche es rápido", "está lejos", "cuesta poco"], "correct_answer": "tenemos un garaje privado en el sótano", "explanation": "Information sur le stationnement.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_eventos_festividades_1",
                        "title": "Fêtes, anniversaires et célébrations",
                        "questions": [
                            {"id": 1551, "type": "multiple_choice", "question": "- ¡Feliz cumpleaños! - ___", "options": ["¡Muchas gracias por acordarte!", "Tengo una fiesta", "Cumplo treinta", "De nada"], "correct_answer": "¡Muchas gracias por acordarte!", "explanation": "Remerciement pour un souhait d'anniversaire.", "xp": 10},
                            {"id": 1552, "type": "fill_in_the_blank", "question": "Complétez : Para celebrar el éxito de la fiesta brindamos con una copa de ___ (cidre / champagne / vin mousseux espagnol).", "options": None, "correct_answer": "cava", "explanation": "'El cava' = Le vin effervescent espagnol.", "xp": 10},
                            {"id": 1553, "type": "multiple_choice", "question": "- ¿Qué le vas a regalar a María por su boda? - ___", "options": ["Un juego de café y una tarjeta de felicitación", "La boda es el sábado", "Están muy contentos", "Tengo traje nuevo"], "correct_answer": "Un juego de café y una tarjeta de felicitación", "explanation": "Choix d'un cadeau de célébration.", "xp": 10},
                            {"id": 1554, "type": "fill_in_the_blank", "question": "Complétez : Apagamos las velas de la ___ de chocolate (gâteau d'anniversaire).", "options": None, "correct_answer": "tarta", "explanation": "'La tarta' = Le gâteau / la tarte.", "xp": 10},
                            {"id": 1555, "type": "multiple_choice", "question": "- ¡Enhorabuena por tu nuevo puesto! - ___", "options": ["¡Muchas gracias, estoy muy ilusionado!", "Empiezo a las ocho", "El puesto está en el centro", "Tengo dos contratos"], "correct_answer": "¡Muchas gracias, estoy muy ilusionado!", "explanation": "Réponse chaleureuse à des félicitations.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_clima_planes_tiempo",
                        "title": "Météo et adaptation des activités de loisirs",
                        "questions": [
                            {"id": 1556, "type": "multiple_choice", "question": "- ¿Qué tiempo hace hoy en la costa? - ___", "options": ["Hace un día soleado y muy agradable", "Son las doce", "La playa es grande", "Voy en coche"], "correct_answer": "Hace un día soleado y muy agradable", "explanation": "Description des conditions météorologiques.", "xp": 10},
                            {"id": 1557, "type": "fill_in_the_blank", "question": "Complétez : Como está lloviendo mucho no podemos salir sin el ___ (parapluie).", "options": None, "correct_answer": "paraguas", "explanation": "'El paraguas' = Le parapluie.", "xp": 10},
                            {"id": 1558, "type": "multiple_choice", "question": "- Si hace frío este fin de semana, ¿qué hacemos? - ___", "options": ["Podemos quedarnos en casa y ver una serie", "Voy en tren", "El frío es blanco", "Tengo vacaciones"], "correct_answer": "Podemos quedarnos en casa y ver una serie", "explanation": "Adaptation d'un plan en fonction du temps.", "xp": 10},
                            {"id": 1559, "type": "fill_in_the_blank", "question": "Complétez : En verano la temperatura sube a más de treinta ___ (degrés).", "options": None, "correct_answer": "grados", "explanation": "'Los grados' = Les degrés.", "xp": 10},
                            {"id": 1560, "type": "multiple_choice", "question": "- El cielo está completamente despejado. - ¡Genial! Entonces ___", "options": ["podemos comer en la terraza del jardín", "coge el abrigo", "abro el paraguas", "está oscuro"], "correct_answer": "podemos comer en la terraza del jardín", "explanation": "Décision de sortie par beau temps.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_transporte_desplazamientos_1",
                        "title": "Déplacements et informations sur les transports",
                        "questions": [
                            {"id": 1561, "type": "multiple_choice", "question": "- ¿Cómo vas normalmente a la universidad? - ___", "options": ["Cojo la línea 3 del metro todas las mañanas", "La universidad es grande", "Tengo dos clases", "Empiezo en octubre"], "correct_answer": "Cojo la línea 3 del metro todas las mañanas", "explanation": "Mode de transport habituel.", "xp": 10},
                            {"id": 1562, "type": "fill_in_the_blank", "question": "Complétez : El billete de diez viajes es más ___ que el billete sencillo (économique / pas cher).", "options": None, "correct_answer": "barato", "explanation": "'Barato' = Pas cher / bon marché.", "xp": 10},
                            {"id": 1563, "type": "multiple_choice", "question": "- ¿Cuánto tiempo tardas en llegar al centro? - ___", "options": ["Tardo unos veinte minutos en autobús", "El centro es bonito", "Cuesta un euro", "Salgo a las ocho"], "correct_answer": "Tardo unos veinte minutos en autobús", "explanation": "Durée estimée d'un trajet.", "xp": 10},
                            {"id": 1564, "type": "fill_in_the_blank", "question": "Complétez : Para cruzar de una orilla a otra tomamos el ___ (bateau / ferry).", "options": None, "correct_answer": "barco", "explanation": "'El barco' = Le bateau.", "xp": 10},
                            {"id": 1565, "type": "multiple_choice", "question": "- ¿Prefieres el tren o el avión para distancias medias? - ___", "options": ["Prefiero el tren porque es más cómodo y puntual", "El avión vuela alto", "Tengo pasaporte", "La estación es antigua"], "correct_answer": "Prefiero el tren porque es más cómodo y puntual", "explanation": "Argumentation sur un moyen de transport.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_restauracion_platos_tipicos",
                        "title": "Lexique des sorties au restaurant et gastronomie",
                        "questions": [
                            {"id": 1566, "type": "multiple_choice", "question": "- ¿Qué nos recomienda de la casa? - ___", "options": ["El pescado fresco a la sal y el arroz con bogavante", "La cuenta son veinte euros", "El baño está al fondo", "Cerramos los domingos"], "correct_answer": "El pescado fresco a la sal y el arroz con bogavante", "explanation": "Recommandation de spécialités par le restaurateur.", "xp": 10},
                            {"id": 1567, "type": "fill_in_the_blank", "question": "Complétez : De segundo plato quiero una ___ de ternera con patatas (steak / filet).", "options": None, "correct_answer": "carne", "explanation": "'La carne' (ou 'el filete') = La viande / le filet.", "xp": 10},
                            {"id": 1568, "type": "multiple_choice", "question": "- ¿Qué postres caseros tienen hoy? - ___", "options": ["Tenemos flan de huevo, tarta de queso y fruta del tiempo", "El menú cuesta quince euros", "Cocinamos con aceite", "Están servidos"], "correct_answer": "Tenemos flan de huevo, tarta de queso y fruta del tiempo", "explanation": "Liste des desserts maison.", "xp": 10},
                            {"id": 1569, "type": "fill_in_the_blank", "question": "Complétez : Pedimos una jarra de ___ fría para toda la mesa (eau).", "options": None, "correct_answer": "agua", "explanation": "'Agua' = Eau.", "xp": 10},
                            {"id": 1570, "type": "multiple_choice", "question": "- ¿Todo ha sido de su agrado? - Sí, ___", "options": ["la comida estaba deliciosa y el trato ha sido magnífico", "la cuenta, por favor", "tenemos prisa", "son las diez"], "correct_answer": "la comida estaba deliciosa y el trato ha sido magnífico", "explanation": "Compliment sur la qualité du repas.", "xp": 10}
                        ]
                    },
                    {
                        "id": "a1_voc_repaso_comunicacion_global",
                        "title": "Synthèse lexicale des situations du quotidien",
                        "questions": [
                            {"id": 1571, "type": "multiple_choice", "question": "Pour demander poliment le chemin à un passant dans la rue, on dit :", "options": ["Disculpe, ¿para ir a la catedral?", "¡Oye, la catedral!", "Tengo que ir a la catedral", "¿Dónde es?"], "correct_answer": "Disculpe, ¿para ir a la catedral?", "explanation": "Formule polie de prise de contact.", "xp": 10},
                            {"id": 1572, "type": "fill_in_the_blank", "question": "Complétez : Cuando conocemos a alguien por primera vez decimos: '¡Mucho ___!' (enchanté).", "options": None, "correct_answer": "gusto", "explanation": "'¡Mucho gusto!' = Enchanté(e) !", "xp": 10},
                            {"id": 1573, "type": "multiple_choice", "question": "Pour demander à quelqu'un de répéter plus lentement :", "options": ["¿Puede repetir más despacio, por favor?", "¿Por qué hablas?", "Habla rápido", "No te oigo nada"], "correct_answer": "¿Puede repetir más despacio, por favor?", "explanation": "Demande de clarification polie.", "xp": 10},
                            {"id": 1574, "type": "fill_in_the_blank", "question": "Complétez : Para desear suerte antes de un examen decimos: '¡Mucha ___!' (chance).", "options": None, "correct_answer": "suerte", "explanation": "'¡Mucha suerte!' = Bonne chance !", "xp": 10},
                            {"id": 1575, "type": "multiple_choice", "question": "Pour prendre congé d'un ami en fin de journée :", "options": ["¡Hasta mañana, que descanses!", "Buenas tardes señor", "Encantado de conocerle", "De nada"], "correct_answer": "¡Hasta mañana, que descanses!", "explanation": "Prise de congé informelle et amicale.", "xp": 10}
                        ]
                    }


                ]},
                "conjugaison": {"title": "Conjugaison", "exercises": [
                    {
                        "id": "a1_conj_perfecto_haber_auxiliar",
                        "title": "L'auxiliaire HABER au présent pour le récit au passé composé",
                        "questions": [
                            {"id": 1576, "type": "fill_in_the_blank", "question": "Yo ___ (haber) hablado con mi hermano esta mañana.", "options": None, "correct_answer": "he", "explanation": "1ère personne : 'Yo he'.", "xp": 15},
                            {"id": 1577, "type": "multiple_choice", "question": "¿Qué ___ hecho tú hoy?", "options": ["has", "he", "ha", "hemos"], "correct_answer": "has", "explanation": "2e personne : 'Tú has'.", "xp": 15},
                            {"id": 1578, "type": "fill_in_the_blank", "question": "Marta ___ (haber) llegado puntual al trabajo.", "options": None, "correct_answer": "ha", "explanation": "3e personne : 'Ella ha'.", "xp": 15},
                            {"id": 1579, "type": "multiple_choice", "question": "Nosotros ___ comido en un restaurante italiano.", "options": ["hemos", "habemos", "han", "habéis"], "correct_answer": "hemos", "explanation": "'Nosotros hemos'.", "xp": 15},
                            {"id": 1580, "type": "fill_in_the_blank", "question": "¿Vosotros ___ (haber) visto las noticias hoy?", "options": None, "correct_answer": "habéis", "explanation": "'Vosotros habéis'.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_participios_regulares_1",
                        "title": "Formation des participes passés réguliers (-ADO / -IDO)",
                        "questions": [
                            {"id": 1581, "type": "multiple_choice", "question": "Quel est le participe passé du verbe 'hablar' ?", "options": ["hablado", "hablido", "hablante", "hablar"], "correct_answer": "hablado", "explanation": "Verbes en -AR -> terminaison -ado.", "xp": 15},
                            {"id": 1582, "type": "fill_in_the_blank", "question": "Complétez : Hoy he ___ (comer) paella de marisco.", "options": None, "correct_answer": "comido", "explanation": "Verbes en -ER -> terminaison -ido.", "xp": 15},
                            {"id": 1583, "type": "multiple_choice", "question": "Quel est le participe passé du verbe 'vivir' ?", "options": ["vivido", "vivado", "viviendo", "vivito"], "correct_answer": "vivido", "explanation": "Verbes en -IR -> terminaison -ido.", "xp": 15},
                            {"id": 1584, "type": "fill_in_the_blank", "question": "Nosotros hemos ___ (estudiar) tres horas seguidas.", "options": None, "correct_answer": "estudiado", "explanation": "Estudiar -> estudiado.", "xp": 15},
                            {"id": 1585, "type": "multiple_choice", "question": "¿El participe passé s'accorde-t-il avec le sujet en espagnol avec l'auxiliaire HABER ?", "options": ["Non, il reste strictement invariable en -o", "Oui, toujours", "Seulement au pluriel", "Seulement avec nosotros"], "correct_answer": "Non, il reste strictement invariable en -o", "explanation": "Le participe passé composé avec haber ne s'accorde jamais.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_participios_irregulares_1",
                        "title": "Participes passés irréguliers essentiels (Hacer, Escribir, Ver)",
                        "questions": [
                            {"id": 1586, "type": "multiple_choice", "question": "Quel est le participe passé du verbe 'hacer' ?", "options": ["hecho", "hacido", "hacado", "harto"], "correct_answer": "hecho", "explanation": "Hacer -> hecho.", "xp": 15},
                            {"id": 1587, "type": "fill_in_the_blank", "question": "Hoy he ___ (escribir) un correo a mi jefa.", "options": None, "correct_answer": "escrito", "explanation": "Escribir -> escrito.", "xp": 15},
                            {"id": 1588, "type": "multiple_choice", "question": "Quel est le participe passé du verbe 'ver' ?", "options": ["visto", "veído", "vido", "vedo"], "correct_answer": "visto", "explanation": "Ver -> visto.", "xp": 15},
                            {"id": 1589, "type": "fill_in_the_blank", "question": "¿Qué habéis ___ (hacer) este fin de semana?", "options": None, "correct_answer": "hecho", "explanation": "Participe : hecho.", "xp": 15},
                            {"id": 1590, "type": "multiple_choice", "question": "Nosotros hemos ___ una exposición magnífica en el museo.", "options": ["visto", "veído", "mirado", "vidi"], "correct_answer": "visto", "explanation": "Participe de ver : visto.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_participios_irregulares_2",
                        "title": "Participes passés irréguliers essentiels (Poner, Abrir, Decir, Volver)",
                        "questions": [
                            {"id": 1591, "type": "multiple_choice", "question": "Quel est le participe passé du verbe 'poner' ?", "options": ["puesto", "ponido", "ponesto", "posto"], "correct_answer": "puesto", "explanation": "Poner -> puesto.", "xp": 15},
                            {"id": 1592, "type": "fill_in_the_blank", "question": "La tienda ha ___ (abrir) sus puertas a las nueve.", "options": None, "correct_answer": "abierto", "explanation": "Abrir -> abierto.", "xp": 15},
                            {"id": 1593, "type": "multiple_choice", "question": "Quel est le participe passé du verbe 'decir' ?", "options": ["dicho", "decido", "dictado", "decho"], "correct_answer": "dicho", "explanation": "Decir -> dicho.", "xp": 15},
                            {"id": 1594, "type": "fill_in_the_blank", "question": "Mis padres han ___ (volver) de sus vacaciones hoy.", "options": None, "correct_answer": "vuelto", "explanation": "Volver -> vuelto.", "xp": 15},
                            {"id": 1595, "type": "multiple_choice", "question": "¿Quién ha ___ la mesa para cenar?", "options": ["puesto", "ponido", "pueste", "puesta"], "correct_answer": "puesto", "explanation": "Participe invariable : puesto.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_marcadores_temporales_uso",
                        "title": "Concordance temporelle et marqueurs du passé récent",
                        "questions": [
                            {"id": 1596, "type": "multiple_choice", "question": "Quel marqueur déclenche l'emploi du Pretérito Perfecto en espagnol d'Espagne ?", "options": ["Hoy (Aujourd'hui)", "Ayer (Hier)", "El año pasado", "Hace cinco años"], "correct_answer": "Hoy (Aujourd'hui)", "explanation": "'Hoy' désigne une unité de temps non révolue.", "xp": 15},
                            {"id": 1597, "type": "fill_in_the_blank", "question": "Complétez : Esta ___ me he levantado muy temprano (matin).", "options": None, "correct_answer": "mañana", "explanation": "'Esta mañana' = Ce matin.", "xp": 15},
                            {"id": 1598, "type": "multiple_choice", "question": "Complétez : ___ semana hemos tenido mucho trabajo.", "options": ["Esta", "Esa", "Aquel", "Pasada"], "correct_answer": "Esta", "explanation": "'Esta semana' (période en cours).", "xp": 15},
                            {"id": 1599, "type": "fill_in_the_blank", "question": "Complétez : Este ___ hemos viajado dos veces en tren (mois).", "options": None, "correct_answer": "mes", "explanation": "'Este mes' = Ce mois-ci.", "xp": 15},
                            {"id": 1600, "type": "multiple_choice", "question": "Les adverbes 'ya' (déjà) et 'todavía no' (pas encore) s'associent naturellement à :", "options": ["Pretérito Perfecto", "Futur simple", "Impératif", "Gérondif seul"], "correct_answer": "Pretérito Perfecto", "explanation": "Bilan de l'expérience accomplie ou non.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_experiencias_vida_perfecto",
                        "title": "Exprimer ses expériences passées (Alguna vez, Ya, Nunca)",
                        "questions": [
                            {"id": 1601, "type": "multiple_choice", "question": "- ¿Has estado ___ en Barcelona? (déjà / une fois)", "options": ["alguna vez", "siempre", "ayer", "mañana"], "correct_answer": "alguna vez", "explanation": "'¿Has estado alguna vez...?' = Es-tu déjà allé... ?", "xp": 15},
                            {"id": 1602, "type": "fill_in_the_blank", "question": "Complétez : Sí, ___ he visitado Barcelona dos veces (déjà).", "options": None, "correct_answer": "ya", "explanation": "'Ya' = Déjà.", "xp": 15},
                            {"id": 1603, "type": "multiple_choice", "question": "- ¿Has probado la paella valenciana? - No, ___ no la he probado.", "options": ["todavía", "ya", "siempre", "nunca"], "correct_answer": "todavía", "explanation": "'Todavía no' = Pas encore.", "xp": 15},
                            {"id": 1604, "type": "fill_in_the_blank", "question": "Complétez : Yo ___ he montado en globo (jamais).", "options": None, "correct_answer": "nunca", "explanation": "'Nunca he + participe' = Je n'ai jamais...", "xp": 15},
                            {"id": 1605, "type": "multiple_choice", "question": "- ¿Has terminado los deberes? - Sí, ___ los he terminado.", "options": ["ya", "todavía", "nunca", "tampoco"], "correct_answer": "ya", "explanation": "'Ya he terminado' = J'ai déjà fini.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_pronombres_orden_perfecto",
                        "title": "Placement des pronoms réfléchis avec les verbes composés",
                        "questions": [
                            {"id": 1606, "type": "multiple_choice", "question": "Quelle est la position correcte du pronom réfléchi avec le passé composé ?", "options": ["Devant l'auxiliaire HABER (me he levantado)", "Entre l'auxiliaire et le participe (he me levantado)", "Attaché au participe (he levantadome)", "À la fin de la phrase"], "correct_answer": "Devant l'auxiliaire HABER (me he levantado)", "explanation": "Le pronom précède obligatoirement l'auxiliaire haber conjugué.", "xp": 15},
                            {"id": 1607, "type": "fill_in_the_blank", "question": "Complétez : Esta mañana yo ___ he levantado a las seis (pronom réfléchi).", "options": None, "correct_answer": "me", "explanation": "'Yo me he levantado'.", "xp": 15},
                            {"id": 1608, "type": "multiple_choice", "question": "¿A qué hora os ___ acostado anoche?", "options": ["habéis", "habidos", "habiendo", "han"], "correct_answer": "habéis", "explanation": "Vosotros os habéis acostado.", "xp": 15},
                            {"id": 1609, "type": "fill_in_the_blank", "question": "Carlos ___ ha lavado los dientes después de comer (pronom).", "options": None, "correct_answer": "se", "explanation": "Él se ha lavado.", "xp": 15},
                            {"id": 1610, "type": "multiple_choice", "question": "Nosotros ___ hemos preparado para salir a cenar.", "options": ["nos", "os", "se", "les"], "correct_answer": "nos", "explanation": "Nosotros nos hemos preparado.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_recato_jornada_hoy",
                        "title": "Récit d'actions successives accomplies aujourd'hui",
                        "questions": [
                            {"id": 1611, "type": "multiple_choice", "question": "- ¿Qué has hecho hoy? - Primero me he levantado temprano y luego ___", "options": ["he ido a trabajar a la oficina", "iré al cine mañana", "trabajo todos los días", "me levantaba a las siete"], "correct_answer": "he ido a trabajar a la oficina", "explanation": "Poursuite du récit chronologique au passé.", "xp": 15},
                            {"id": 1612, "type": "fill_in_the_blank", "question": "Complétez : A las dos ___ (comer) con un compañero de trabajo (Pretérito Perfecto - yo).", "options": None, "correct_answer": "he comido", "explanation": "Yo he comido.", "xp": 15},
                            {"id": 1613, "type": "multiple_choice", "question": "Por la tarde he vuelto a casa y ___ un rato en el sofá.", "options": ["he descansado", "descansaré", "descansar", "habré descansado"], "correct_answer": "he descansado", "explanation": "Action accomplie dans la journée.", "xp": 15},
                            {"id": 1614, "type": "fill_in_the_blank", "question": "Complétez : Al final del día ___ (hacer) la cena para mi familia (yo).", "options": None, "correct_answer": "he hecho", "explanation": "Yo he hecho.", "xp": 15},
                            {"id": 1615, "type": "multiple_choice", "question": "Ha sido un día muy productivo porque ___ todas mis tareas.", "options": ["he terminado", "termino", "terminaré", "terminaba"], "correct_answer": "he terminado", "explanation": "Bilan d'accomplissement de journée.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_recato_fin_de_semana",
                        "title": "Raconter les actions de son week-end récent",
                        "questions": [
                            {"id": 1616, "type": "multiple_choice", "question": "- ¿Qué tal el fin de semana? - ___", "options": ["Muy bien, he estado en la sierra con unos amigos", "Me gusta el campo", "Voy a descansar el sábado", "Trabajo los lunes"], "correct_answer": "Muy bien, he estado en la sierra con unos amigos", "explanation": "Récit global sur le week-end écoulé.", "xp": 15},
                            {"id": 1617, "type": "fill_in_the_blank", "question": "Complétez : El sábado por la noche ___ (ir - nosotros) a un concierto genial.", "options": None, "correct_answer": "hemos ido", "explanation": "Nosotros hemos ido.", "xp": 15},
                            {"id": 1618, "type": "multiple_choice", "question": "El domingo nos hemos levantado tarde y ___ una comida familiar.", "options": ["hemos preparado", "preparamos mañana", "preparando", "habríamos preparado"], "correct_answer": "hemos preparado", "explanation": "Hemos preparado.", "xp": 15},
                            {"id": 1619, "type": "fill_in_the_blank", "question": "Complétez : ¡Nos lo ___ pasado fenomenal! (verbe pasarse - nosotros)", "options": None, "correct_answer": "hemos", "explanation": "'Nos lo hemos pasado bien/fenomenal' = Nous nous sommes bien amusés.", "xp": 15},
                            {"id": 1620, "type": "multiple_choice", "question": "- ¿Has descansado? - Sí, ___ muchas horas.", "options": ["he dormido", "dormiré", "duermo siempre", "estoy durmiendo"], "correct_answer": "he dormido", "explanation": "Récit d'un état accompli : he dormido.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_recato_viajes_vacaciones",
                        "title": "Conjugaison en contexte de voyage récent",
                        "questions": [
                            {"id": 1621, "type": "multiple_choice", "question": "- ¿Adónde has viajado en tus últimas vacaciones? - ___", "options": ["He viajado a Andalucía y he visitado Sevilla y Granada", "Viajo en tren", "Quiero ir a Italia", "Andalucía es bonita"], "correct_answer": "He viajado a Andalucía y he visitado Sevilla y Granada", "explanation": "Récit de voyage avec mention des étapes.", "xp": 15},
                            {"id": 1622, "type": "fill_in_the_blank", "question": "Complétez : Durante el viaje ___ (hacer - yo) cientos de fotos preciosas.", "options": None, "correct_answer": "he hecho", "explanation": "Yo he hecho fotos.", "xp": 15},
                            {"id": 1623, "type": "multiple_choice", "question": "En Granada ___ la Alhambra, que es impresionante.", "options": ["hemos visitado", "visitaremos", "visitando", "visitas"], "correct_answer": "hemos visitado", "explanation": "Hemos visitado.", "xp": 15},
                            {"id": 1624, "type": "fill_in_the_blank", "question": "Complétez : La comida andaluza me ___ encantado (haber - singulier).", "options": None, "correct_answer": "ha", "explanation": "'Me ha encantado' = J'ai adoré.", "xp": 15},
                            {"id": 1625, "type": "multiple_choice", "question": "- ¿Ha hecho buen tiempo durante el viaje? - Sí, ___", "options": ["ha hecho mucho sol todos los días", "hace frío en invierno", "lloverá mañana", "hacía viento"], "correct_answer": "ha hecho mucho sol todos los días", "explanation": "Bilan météo : ha hecho sol.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_recato_anecdotas_imprevistos",
                        "title": "Raconter un contretemps ou une anecdote passée",
                        "questions": [
                            {"id": 1626, "type": "multiple_choice", "question": "¡No te imaginas lo que me ha pasado hoy! ___", "options": ["He perdido el autobús y he tenido que correr", "Mañana voy al médico", "Tengo dos hermanos", "El autobús es rojo"], "correct_answer": "He perdido el autobús y he tenido que correr", "explanation": "Narration d'un imprévu.", "xp": 15},
                            {"id": 1627, "type": "fill_in_the_blank", "question": "Complétez : Al salir de casa me ___ dado cuenta de que no tenía las llaves (haber - yo).", "options": None, "correct_answer": "he", "explanation": "'Me he dado cuenta'.", "xp": 15},
                            {"id": 1628, "type": "multiple_choice", "question": "Por suerte mi vecina me ___ y me ha ayudado.", "options": ["ha visto", "ha veído", "ve", "verá"], "correct_answer": "ha visto", "explanation": "Action ponctuelle : ha visto.", "xp": 15},
                            {"id": 1629, "type": "fill_in_the_blank", "question": "Complétez : Al final todo se ___ solucionado rápidamente (haber - 3e personne).", "options": None, "correct_answer": "ha", "explanation": "'Se ha solucionado'.", "xp": 15},
                            {"id": 1630, "type": "multiple_choice", "question": "- ¿Quién te ha llevado al trabajo? - Un compañero me ___ en su coche.", "options": ["ha recogido", "recogerá", "recoge", "recogiendo"], "correct_answer": "ha recogido", "explanation": "Ha recogido.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_recato_celebraciones_fiestas",
                        "title": "Conjuguer les récits de fêtes et réceptions",
                        "questions": [
                            {"id": 1631, "type": "multiple_choice", "question": "- ¿Cómo has celebrado tu cumpleaños? - ___", "options": ["He invitado a mis amigos a cenar a casa", "Cumplo treinta años el mes que viene", "Me gusta la tarta", "Tengo muchos regalos"], "correct_answer": "He invitado a mis amigos a cenar a casa", "explanation": "Récit d'un événement festif.", "xp": 15},
                            {"id": 1632, "type": "fill_in_the_blank", "question": "Complétez : Mi madre me ___ preparado una tarta de chocolate deliciosa (haber).", "options": None, "correct_answer": "ha", "explanation": "Ella me ha preparado.", "xp": 15},
                            {"id": 1633, "type": "multiple_choice", "question": "Mis amigos me ___ unos regalos increíbles.", "options": ["han traído", "han traendo", "traerán", "traían"], "correct_answer": "han traído", "explanation": "Participe de traer : traído.", "xp": 15},
                            {"id": 1634, "type": "fill_in_the_blank", "question": "Complétez : Hemos bailado y ___ (cantar) hasta medianoche.", "options": None, "correct_answer": "cantado", "explanation": "Participe de cantar : cantado.", "xp": 15},
                            {"id": 1635, "type": "multiple_choice", "question": "Ha sido una fiesta inolvidable y todos ___ muy contentos.", "options": ["se han ido", "se van", "se irán", "se fueron mañana"], "correct_answer": "se han ido", "explanation": "Se han ido.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_recato_salidas_gastronomicas",
                        "title": "Raconter une expérience au restaurant au passé",
                        "questions": [
                            {"id": 1636, "type": "multiple_choice", "question": "- ¿Qué tal la cena en el restaurante nuevo? - ___", "options": ["Ha estado todo riquísimo y el servicio ha sido excelente", "La carta tiene muchos platos", "Ceno a las nueve", "El restaurante abre mañana"], "correct_answer": "Ha estado todo riquísimo y el servicio ha sido excelente", "explanation": "Évaluation globale d'une sortie au restaurant.", "xp": 15},
                            {"id": 1637, "type": "fill_in_the_blank", "question": "Complétez : De primero hemos ___ gazpacho andaluz (pedir).", "options": None, "correct_answer": "pedido", "explanation": "Participe de pedir : pedido.", "xp": 15},
                            {"id": 1638, "type": "multiple_choice", "question": "De segundo plato el camarero nos ___ pescado a la plancha.", "options": ["ha servido", "ha sirvido", "servirá", "sirve"], "correct_answer": "ha servido", "explanation": "Participe régulier de servir : servido.", "xp": 15},
                            {"id": 1639, "type": "fill_in_the_blank", "question": "Complétez : Para terminar yo me ___ tomado un café cortado (haber).", "options": None, "correct_answer": "he", "explanation": "Yo me he tomado.", "xp": 15},
                            {"id": 1640, "type": "multiple_choice", "question": "- ¿Ha sido caro? - No, la cuenta ___ muy razonable.", "options": ["ha sido", "ha estado", "es", "será"], "correct_answer": "ha sido", "explanation": "Appréciation rétrospective : ha sido razonable.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_contraste_presente_perfecto",
                        "title": "Articuler le Présent (habitudes) et le Passé composé (actions récentes)",
                        "questions": [
                            {"id": 1641, "type": "multiple_choice", "question": "Normalmente yo ___ (comer - habitude) en casa, pero hoy ___ (comer - fait récent) fuera.", "options": ["como / he comido", "he comido / como", "como / comí", "como / comeré"], "correct_answer": "como / he comido", "explanation": "Présent pour l'habitude (como) vs Pretérito Perfecto pour l'exception du jour (he comido).", "xp": 15},
                            {"id": 1642, "type": "fill_in_the_blank", "question": "Todos los días salgo a las ocho, pero esta mañana ___ (salir - yo) a las nueve.", "options": None, "correct_answer": "he salido", "explanation": "Événement ponctuel aujourd'hui : he salido.", "xp": 15},
                            {"id": 1643, "type": "multiple_choice", "question": "Siempre ___ la verdad, pero hoy me ___ una mentira. (decir)", "options": ["dice / ha dicho", "ha dicho / dice", "dices / dices", "dice / dice"], "correct_answer": "dice / ha dicho", "explanation": "Él dice siempre / hoy ha dicho.", "xp": 15},
                            {"id": 1644, "type": "fill_in_the_blank", "question": "Mis padres viven en el campo, pero esta semana ___ (venir) a la ciudad de visita.", "options": None, "correct_answer": "han venido", "explanation": "Action accomplie cette semaine : han venido.", "xp": 15},
                            {"id": 1645, "type": "multiple_choice", "question": "No suelo ver la televisión, pero esta tarde ___ una película muy bonita.", "options": ["he visto", "veo", "veré", "veía"], "correct_answer": "he visto", "explanation": "Fait accompli cet après-midi : he visto.", "xp": 15}
                        ]
                    },
                    {
                        "id": "a1_conj_evaluacion_final_recatos",
                        "title": "Bilan de conjugaison : Récit complet d'une expérience",
                        "questions": [
                            {"id": 1646, "type": "multiple_choice", "question": "Yo ___ (ser) estudiante, ___ (vivir) en Sevilla y este fin de semana ___ (viajar) a Córdoba.", "options": ["soy / vivo / he viajado", "estoy / vivo / viajo", "soy / he vivido / viajo", "soy / vivo / viajaré"], "correct_answer": "soy / vivo / he viajado", "explanation": "Profil permanent au présent + action accomplie ce week-end au passé.", "xp": 15},
                            {"id": 1647, "type": "fill_in_the_blank", "question": "Complétez : En Córdoba nosotros hemos ___ (visitar) la Mezquita Catedral.", "options": None, "correct_answer": "visitado", "explanation": "Participe : visitado.", "xp": 15},
                            {"id": 1648, "type": "multiple_choice", "question": "¿Tú ___ alguna vez platos típicos andaluces?", "options": ["has probado", "has probando", "has pruebo", "has probaste"], "correct_answer": "has probado", "explanation": "Expérience vécue : has probado.", "xp": 15},
                            {"id": 1649, "type": "fill_in_the_blank", "question": "Complétez : Esta tarde yo ___ (volver) a casa cansado pero muy feliz (haber + volver).", "options": None, "correct_answer": "he vuelto", "explanation": "Yo he vuelto.", "xp": 15},
                            {"id": 1650, "type": "multiple_choice", "question": "- ¿Ha sido una buena experiencia? - Sí, ___ una experiencia maravillosa que nunca olvidaré.", "options": ["ha sido", "ha estado", "es", "será"], "correct_answer": "ha sido", "explanation": "Bilan rétrospectif : ha sido una experiencia maravillosa.", "xp": 15}
                        ]
                    }


                ]},
                "ecoute": {"title": "Écoute", "exercises": []}
        }},

    "B1": {
        "title": "Niveau B1 - Intermédiaire",
        "categories": {
            "vocabulaire": {"title": "Vocabulaire", "exercises": []},
            "conjugaison": {"title": "Conjugaison", "exercises": []},
            "ecoute": {"title": "Écoute", "exercises": []}
        }
    },
    "B2": {
        "title": "Niveau B2 - Avancé",
        "categories": {
            "vocabulaire": {"title": "Vocabulaire", "exercises": []},
            "conjugaison": {"title": "Conjugaison", "exercises": []},
            "ecoute": {"title": "Écoute", "exercises": []}
        }
    },
    "C1": {
        "title": "Niveau C1 - Autonome",
        "categories": {
            "vocabulaire": {"title": "Vocabulaire", "exercises": []},
            "conjugaison": {"title": "Conjugaison", "exercises": []},
            "ecoute": {"title": "Écoute", "exercises": []}
        }
    },
    "C2": {
        "title": "Niveau C2 - Maîtrise",
        "categories": {
            "vocabulaire": {"title": "Vocabulaire", "exercises": []},
            "conjugaison": {"title": "Conjugaison", "exercises": []},
            "ecoute": {"title": "Écoute", "exercises": []}
        }
    }
}

# Extraction plate des questions pour validation
QUESTIONS_DB = [
    q
    for level in CURRICULUM_DB.values()
    for cat in level.get("categories", {}).values()
    for ex in cat.get("exercises", [])
    for q in ex.get("questions", [])
]