# fars_acquirer.py
# Module d'acquisition de signaux bruts.
# STATUT : Interface d'acquisition de données brutes.

from abc import ABC, abstractmethod
import wikipediaapi

class BaseAcquirer(ABC):
    """
    Interface abstraite pour tous les modules d'acquisition de signaux.
    Garantit une méthode 'fetch' uniforme.
    """
    @abstractmethod
    def fetch(self, query: str) -> str:
        """
        Récupère le signal brut à partir de la source spécifiée.
        Doit être implémentée par chaque acquéreur concret.
        """
        pass

class WikipediaAcquirer(BaseAcquirer):
    """
    Acquéreur spécifique pour les signaux bruts de Wikipedia.
    """
    def __init__(self, language='fr'):
        # --- CORRECTION APPLIQUÉE ICI ---
        # Utilisation d'arguments nommés pour éviter toute collision.
        self.wiki = wikipediaapi.Wikipedia(
            language=language, 
            user_agent='SBI-REC_TITAN/6.1 (contact.alex@lascribeforge.fr)'
        )

    def fetch(self, query: str) -> str:
        """
        Récupère le contenu d'une page Wikipedia.
        """
        page = self.wiki.page(query)
        if page.exists():
            print(f"[ACQUIRER:Wikipedia] Signal brut acquis pour '{query}'.")
            return page.text
        else:
            print(f"[ACQUIRER:Wikipedia] Aucun signal brut trouvé pour '{query}'.")
            return ""