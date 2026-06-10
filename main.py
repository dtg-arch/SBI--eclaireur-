# main.py
# Script d'orchestration pour tester le module FARS.

from fars_acquirer import WikipediaAcquirer
from fars_refiner import SignalRefiner

if __name__ == "__main__":
    # 1. Initialiser les modules
    acquirer = WikipediaAcquirer()
    refiner = SignalRefiner()

    # 2. Définir la cible
    topic_to_fetch = "Code Napoléon"

    # 3. Acquérir le signal brut
    raw_signal_data = acquirer.fetch(topic_to_fetch)

    # 4. Raffiner le signal brut en signal F1
    if raw_signal_data:
        refined_signal = refiner.refine(raw_signal_data, vector="wikipedia")

        # 5. Afficher le résultat F1 final
        if refined_signal:
            print("\n--- SIGNAL F1 FINAL ---")
            # .model_dump_json() est une méthode Pydantic pour une sortie JSON propre.
            print(refined_signal.model_dump_json(indent=2))
            print("--- FIN DU SIGNAL ---")
