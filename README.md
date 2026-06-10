SBI-Éclaireur

**SBI-Éclaireur** est la version publique des modules d’acquisition et de raffinage de signaux, développés grâce au moteur souverain **SBI-REC TITAN**.

### Nouvelle direction du projet

Après plusieurs mois de développement en mode souverain et air-gapped, je passe en **modèle hybride** :

- Le **cœur du moteur SBI-REC TITAN** reste protégé sous licence **BSL 1.1**.  
- Les **modules périphériques** (acquisition, raffinage, outils) sont ouverts à la communauté sous licence **MIT**.

**Intention du projet :**  
Grâce à la Forge, le rôle de SBI-Éclaireur est de **trier les informations en masse** et d’**extraire la structure** sans détour ni bruit inutile.  
Priorité absolue à la **vérité factuelle**.

### Modules inclus dans cette version publique

- `fars_acquirer.py` → Interface d’acquisition (Wikipedia)
- `fars_acquirer_duckduckgo_news.py` → Acquisition d’actualités via DuckDuckGo
- `fars_models.py` → Modèles Pydantic de structuration
- `fars_refiner.py` → Raffineur de signal (version allégée)
- `main.py` → Exemple d’orchestration simple
- `api.py` → Micro-service FastAPI (optionnel)

### Installation

```bash
pip install wikipedia-api duckduckgo-search pydantic langchain-google-genai python-dotenv fastapi uvicorn
Crée un fichier .env à la racine avec ta clé :
envGOOGLE_API_KEY=ta_cle_ici
Lancement
Version simple (script) :
Bashpython main.py
Version API (recommandée) :
Bashuvicorn api:app --reload --host 127.0.0.1 --port 5000
Puis ouvre http://127.0.0.1:5000 dans ton navigateur.
Utilisation
Les modules permettent de récupérer des signaux bruts (Wikipedia, DuckDuckGo) et de les structurer de façon claire et factuelle.
Dons
Si ce travail vous est utile et que votre conscience vous le permet, les dons serviront uniquement à améliorer la qualité technique des prochains modules et à soutenir le développement de SBI-Éclaireur.
Contact : contact@lascribeforge.fr
Licence
Les modules de cette version publique sont sous licence MIT (voir fichier LICENSE).
Le cœur du moteur SBI-REC TITAN reste sous licence BSL 1.1 et n’est pas inclus dans ce dépôt.

Créé par La Scribe Forge
Contact : contact@lascribeforge.fr
