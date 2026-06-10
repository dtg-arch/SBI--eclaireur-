# diagnostic_api.py
# Script de validation pour lister les modèles GenAI autorisés pour la clé API fournie.
# Exécution : python diagnostic_api.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

print("[DIAGNOSTIC] Initialisation du protocole de validation...")

# 1. Charger les variables d'environnement (le fichier .env doit exister)
env_path = '.env'
if not load_dotenv(dotenv_path=env_path):
    print(f"[ERREUR] Fichier .env non trouvé au chemin: {os.path.abspath(env_path)}")
    exit()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("[ERREUR] Variable GOOGLE_API_KEY non trouvée dans le fichier .env.")
    exit()

# 2. Configurer le client API
try:
    genai.configure(api_key=api_key)
    print("[DIAGNOSTIC] Clé API chargée et client configuré.")
except Exception as e:
    print(f"[ERREUR CRITIQUE] La configuration du client a échoué : {e}")
    exit()

# 3. Interroger l'API pour la liste des modèles
print("\n[DIAGNOSTIC] Interrogation de l'API pour les modèles disponibles...")
print("-----------------------------------------------------------------")

found_models = False
try:
    for m in genai.list_models():
        # Nous filtrons pour ne garder que les modèles capables de générer du contenu textuel.
        if 'generateContent' in m.supported_generation_methods:
            print(f"  - Nom du Modèle : {m.name}")
            print(f"    Nom d'Affichage: {m.display_name}")
            print(f"    Description    : {m.description[:80]}...")
            print("-" * 50)
            found_models = True
    
    if not found_models:
        print("[ALERTE] Aucun modèle compatible 'generateContent' n'a été trouvé pour cette clé API.")
        print("         Vérifiez les autorisations de votre projet Google Cloud.")

except Exception as e:
    print(f"\n[ERREUR D'INTERROGATION] Une erreur est survenue lors de la communication avec l'API.")
    print(f"   Détails de l'erreur: {e}")
    print("   Causes possibles :")
    print("     1. La clé API est invalide ou révoquée.")
    print("     2. L'API 'Generative Language' n'est pas activée dans votre projet Google Cloud.")
    print("     3. Un problème de facturation est associé à votre projet.")

print("-----------------------------------------------------------------")
print("[DIAGNOSTIC] Protocole de validation terminé.")