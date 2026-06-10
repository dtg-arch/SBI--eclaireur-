# fars_models.py
# Modèles de données Pydantic pour la structuration déterministe du signal F1.
# STATUT : Alignement du bouclier sur la logique de pipeline.

from pydantic import BaseModel, Field
from typing import List, Optional

class AnalysisOutput(BaseModel):
    """
    Structure pour l'analyse des fréquences informationnelles.
    """
    fact_score: float = Field(..., ge=0.0, le=1.0, description="Score d'objectivité pure (densité F1).")
    hostility_score: float = Field(..., ge=0.0, le=1.0, description="Score de détection de propagande/attaque (densité F3).")
    emotional_noise: float = Field(..., ge=0.0, le=1.0, description="Score de détection de surcharge émotionnelle (densité F2).")

class SignalF1Output(BaseModel):
    """
    Structure pour le signal F1 purifié.
    """
    title: str = Field(..., description="Le titre original du signal.")
    summary_f1: str = Field(..., description="Résumé de 3 phrases maximum, 100% factuel, sans interprétation.")
    entities: List[str] = Field(..., description="Liste des entités clés extraites du signal.")

class F1Signal(BaseModel):
    """
    Modèle global pour un signal F1 entièrement structuré et validé.
    """
    analysis: AnalysisOutput
    signal_f1: SignalF1Output
    source_url: Optional[str] = Field(None, description="URL de la source du signal brut.")
    acquisition_vector: Optional[str] = Field(None, description="Vecteur d'acquisition du signal (e.g., 'wikipedia', 'local_file').")