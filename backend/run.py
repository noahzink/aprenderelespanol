"""import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)"""


import os
import uvicorn

if __name__ == "__main__":
    # Récupère le port de Render, ou utilise 8000 en local
    port = int(os.environ.get("PORT", 8000))
    # 0.0.0.0 permet d'écouter sur tout le réseau
    uvicorn.run("app.main:app", host="0.0.0.0", port=port)