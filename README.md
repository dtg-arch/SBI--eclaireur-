# FARS - Modules Publics (Community Edition)

**FARS** (Forge Acquisition & Refinement System) est une collection de modules d’acquisition et de structuration de signaux, développés grâce au moteur souverain **SBI-REC TITAN**.

### Nouvelle direction du projet

Après plusieurs mois de développement en mode souverain et air-gapped, je passe en **modèle hybride** :

- Le **cœur du moteur SBI-REC TITAN** reste protégé (licence BSL 1.1).  
- Les **modules périphériques** (acquisition, raffinage, outils) sont ouverts à la communauté sous licence MIT.

L’objectif est de partager des outils utiles, de recevoir des retours et des contributions, tout en protégeant la valeur stratégique du cœur déterministe.

### Modules inclus dans cette version publique

- `fars_acquirer.py` → Interface d’acquisition (Wikipedia)
- `fars_acquirer_duckduckgo_news.py` → Acquisition d’actualités via DuckDuckGo
- `fars_models.py` → Modèles Pydantic de structuration
- `fars_refiner.py` → Raffineur de signal (version allégée)
- `main.py` → Exemple d’orchestration

### Installation

```bash
pip install wikipedia-api duckduckgo-search pydantic langchain-google-genai python-dotenv
Crée un fichier .env à la racine avec ta clé :
envGOOGLE_API_KEY=ta_cle_ici
Utilisation rapide
Bashpython main.py
