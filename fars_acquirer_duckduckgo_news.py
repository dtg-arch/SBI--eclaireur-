# fars_acquirer_duckduckgo_news.py
# Module d'acquisition de signaux d'actualité via DuckDuckGo.
# STATUT : Vecteur d'ingestion spécialisé.

from fars_acquirer import BaseAcquirer
from duckduckgo_search import DDGS

class DuckDuckGoNewsAcquirer(BaseAcquirer):
    """
    Acquéreur spécialisé pour les signaux bruts d'actualités de DuckDuckGo.
    """
    def __init__(self):
        self.ddgs = DDGS()

    def fetch(self, query: str) -> str:
        """
        Récupère les 5 principaux articles d'actualité de DuckDuckGo.
        """
        print(f"[ACQUIRER:DuckDuckGoNews] Tentative d'acquisition pour '{query}'.")
        try:
            # Effectue une recherche d'actualités
            results = self.ddgs.news(keywords=query, max_results=15)
            
            if results:
                # Concatène les résultats en un seul signal brut structuré
                formatted_results = []
                for result in results:
                    title = result.get('title', 'N/A')
                    body = result.get('body', 'N/A')
                    source = result.get('source', 'N/A')
                    date = result.get('date', 'N/A')
                    url = result.get('url', 'N/A')
                    
                    formatted_results.append(
                        f"Titre: {title}\n"
                        f"Source: {source}\n"
                        f"Date: {date}\n"
                        f"Contenu: {body}\n"
                        f"URL: {url}\n"
                        f"--------------------\n"
                    )
                
                print(f"[ACQUIRER:DuckDuckGoNews] {len(results)} signaux bruts acquis pour '{query}'.")
                return "\n".join(formatted_results)
            else:
                print(f"[ACQUIRER:DuckDuckGoNews] Aucun signal brut trouvé pour '{query}'.")
                return ""
        except Exception as e:
            print(f"[ACQUIRER:DuckDuckGoNews] Erreur lors de l'acquisition pour '{query}': {e}")
            return ""