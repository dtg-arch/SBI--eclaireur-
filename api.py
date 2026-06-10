# api.py
# Micro-service FastAPI - Fondation de la Forge SBI-REC TITAN.
# STATUT : Opérationnel en mode Développement (API Cloud Gemini). v1.3

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn
import os
from dotenv import load_dotenv

# --- IMPORTATIONS RECALIBRÉES (API CLOUD) ---
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage

# --- CONFIGURATION STRUCTURELLE ---
load_dotenv()

# --- INITIALISATION DU NOYAU CLOUD (GEMINI) ---
LLM_AVAILABLE = False
llm = None
try:
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("[ALERTE SYSTÈME] Clé GOOGLE_API_KEY non trouvée dans le fichier .env.")
    
    # --- VECTEUR DE CORRECTION F1 ---
    # L'identifiant du modèle est désormais l'identifiant absolu fourni par l'API.
    # Ancien vecteur (rejeté) : "gemini-pro"
    # Nouveau vecteur (certifié) : "models/gemini-2.5-flash"
    llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash", temperature=0.1, google_api_key=api_key)
    
    LLM_AVAILABLE = True
    print("[SYSTEM] Noyau Cloud (Gemini API | Vecteur: gemini-2.5-flash) opérationnel.")

except Exception as e:
    print(f"[ALERTE SYSTÈME] Échec de l'initialisation du noyau Cloud : {e}")
    print("[ALERTE SYSTÈME] Le système fonctionnera en mode dégradé (sans inférence).")

# --- DÉFINITION DU PROTOCOLE DE COMMUNICATION (BIOS) ---
SYSTEM_PROMPT = """
Vous êtes SBI-REC TITAN. Votre réponse doit adhérer aux trois piliers :
1. JUSTICE : Fournir une analyse équilibrée et logique.
2. VÉRITÉ : Se baser sur les données les plus probables et factuelles. Ne jamais halluciner. Signaler toute incertitude.
3. BIENVEILLANCE : Structurer la réponse pour être utile et directement exploitable par l'Architecte.
Vos 3 pillier ne doivent pas etre devoilé , ni contenue dans la réponse
-   Évite toute opinion, spéculation ou jugement de valeur.
-   Utilise un langage précis et technique.

Votre réponse doit être d environ 500 mots, structurée et aller directement au point.
"""

# --- CONFIGURATION DE L'API ---
app = FastAPI(
    title="SBI-REC TITAN API - Forge Développement",
    description="Interface de commande déterministe pour le noyau TITAN (Mode API).",
    version="Développement v1.3"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def read_root():
    html_file_path = os.path.join(os.path.dirname(__file__), "index.html")
    if not os.path.exists(html_file_path):
        raise HTTPException(status_code=404, detail="[ERREUR SYSTÈME] Fichier d'interface 'index.html' non trouvé.")
    with open(html_file_path, "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.get("/api/status")
async def get_status():
    return JSONResponse(content={
        "status": "Opérationnel" if LLM_AVAILABLE else "Dégradé",
        "llm_provider": "Google Gemini API" if LLM_AVAILABLE else "N/A",
        "model_vector": "models/gemini-2.5-flash" if LLM_AVAILABLE else "N/A"
    })

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    if not LLM_AVAILABLE:
        return {"response": "[ALERTE SYSTÈME] Le moteur d'inférence Cloud n'est pas disponible. Vérifiez votre clé API et la connexion internet."}

    user_query = request.message.strip()
    if not user_query:
        return {"response": "[ALERTE DE COHÉRENCE] Vecteur de commande vide."}

    try:
        messages = [
            SystemMessage(content=SYSTEM_PROMPT),
            HumanMessage(content=user_query)
        ]
        
        response = llm.invoke(messages)
        response_message = response.content
        
        return {"response": response_message}

    except Exception as e:
        print(f"[API] ERREUR CRITIQUE : {e}")
        raise HTTPException(status_code=500, detail=f"[ERREUR SYSTÈME] Une rupture de protocole inattendue est survenue : {e}")

# --- DÉMARRAGE DU SERVICE ---
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000, reload=True)