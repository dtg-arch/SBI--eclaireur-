# SBI-Éclaireur

**SBI-Éclaireur** est la version publique des modules d’acquisition et de raffinage de signaux, développés grâce au moteur souverain **SBI-REC TITAN**.

### Intention du projet

Grâce à la Forge, le rôle de SBI-Éclaireur est de **trier les informations en masse** et d’**extraire la structure essentielle** sans détour ni bruit inutile.  
Priorité absolue à la **vérité factuelle**.

### Modules inclus

- `fars_acquirer.py` → Acquisition Wikipedia
- `fars_acquirer_duckduckgo_news.py` → Acquisition actualités DuckDuckGo
- `fars_models.py` → Modèles de structuration Pydantic
- `fars_refiner.py` → Raffineur de signal
- `api.py` → Micro-service FastAPI
- `main.py` → Exemple d’utilisation

### Installation

```bash
pip install wikipedia-api duckduckgo-search pydantic langchain-google-genai python-dotenv fastapi uvicorn
Crée un fichier .env à la racine :
.env _ GOOGLE_API_KEY=ta_cle_google_api_ici
Lancement
Mode simple :
Bashpython main.py
Mode API (recommandé) :
Bashuvicorn api:app --reload --host 127.0.0.1 --port 5000
Puis ouvre http://127.0.0.1:5000 dans ton navigateur.
Licence
Modules publics → MIT
Cœur SBI-REC TITAN → BSL 1.1 (protégé, non inclus)
Dons & Contributions
N’hésitez pas à tester, donner votre feedback ou contribuer.
Tout retour est bon à prendre pour améliorer le projet.
Si cela vous est utile, les dons serviront uniquement à améliorer la qualité technique des prochains modules.



### Soutenir le développement

Si **SBI-Éclaireur** vous est utile et que votre conscience vous le permet, vous pouvez soutenir le projet via PayPal :

**[💰 Faire un don](https://www.paypal.com/donate/?hosted_button_id=96P77EMM2C6RL)**

**Message pour les donateurs :**

> Merci du fond du cœur.  
> Ce projet est né dans la fatigue, la solitude et la volonté de créer quelque chose de vrai.  
> Chaque euro reçu sert uniquement à améliorer la qualité technique des modules et à continuer le combat pour une IA plus factuelle et souveraine.  
> Même un petit don fait une vraie différence.
Contact : contact.alex@lascribeforge.fr
