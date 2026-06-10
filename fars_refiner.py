# fars_refiner.py
# Module de raffinage et structuration de signal (Community Edition)
# Version allégée pour usage public - Core protégé sous BSL 1.1

import os
import json
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import ValidationError

from fars_models import F1Signal

class SignalRefiner:
    """
    Raffineur de signal. Utilise un LLM pour structurer un signal brut
    en format validé (JSON + Pydantic).
    """
    
    def __init__(self):
        """
        Initialise le raffineur et configure le moteur LLM.
        """
        # --- BLINDAGE DU PROTOCOLE DE CHARGEMENT DE L'ENVIRONNEMENT ---
        env_path = Path('.') / '.env'
        if not load_dotenv(dotenv_path=env_path):
            print(f"[REFINER] Alerte: Fichier .env non trouvé au chemin: {env_path.resolve()}")
        
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("[ERREUR SYSTÈME] Clé API Google non trouvée. Le protocole de transmutation ne peut être initialisé.")

        # Configuration du modèle LLM
        certified_model_vector = "models/gemini-2.5-flash"
        
        self.llm = ChatGoogleGenerativeAI(
            model=certified_model_vector, 
            temperature=0.1, # L'Étouffoir de température est maintenu pour neutraliser l'hallucination (F4).
            google_api_key=api_key
        )
        
        # Prompt système pour forcer une sortie JSON structurée
        self.system_prompt = """
Tu es un assistant d'analyse. Ta mission est d'analyser le texte et de retourner UNIQUEMENT un objet JSON valide.
Le JSON doit suivre exactement cette structure :
{
  "analysis": {
    "fact_score": float (0.0-1.0),
    "hostility_score": float (0.0-1.0),
    "emotional_noise": float (0.0-1.0)
  },
  "signal_f1": {
    "title": string,
    "summary_f1": string,
    "entities": ["entité 1", "entité 2"]
  }
}
Réponds uniquement avec le JSON. Pas de texte supplémentaire.
"""

    def refine(self, raw_data: dict, vector: str) -> Optional[F1Signal]:
        """
        Raffine le signal brut et le structure en objet validé.
        """
        if not raw_data or not raw_data.get('raw_text'):
            print(f"[REFINER] Signal d'entrée nul ou invalide. Transmutation annulée.")
            return None

        print(f"[REFINER] Début de la transmutation pour le signal '{raw_data.get('title', 'Sans Titre')}'...")
        
        messages = [
            SystemMessage(content=self.system_prompt),
            HumanMessage(content=raw_data['raw_text'][:15000])
        ]
        
        llm_response_content = ""
        try:
            response = self.llm.invoke(messages)
            llm_response_content = response.content.strip()
            
            json_block = llm_response_content.replace("```json", "").replace("```", "").strip()
            
            parsed_data = F1Signal.model_validate_json(json_block)
            
            parsed_data.source_url = raw_data.get('url', 'N/A')
            parsed_data.acquisition_vector = vector
            
            print(f"[REFINER] Transmutation réussie. Signal F1 validé et structuré.")
            return parsed_data

        except ValidationError as e:
            print(f"[REFINER] Signal rejeté par validation. Sortie LLM non conforme.")
            print(f"          Détails de l'entropie: {e}")
            print(f"          Sortie brute du LLM pour analyse: {llm_response_content}")
            return None
        except Exception as e:
            print(f"[REFINER] Erreur critique lors de la transmutation: {e}")
            print(f"          Sortie brute du LLM (si disponible): {llm_response_content}")
            return None