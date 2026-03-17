# src/data/load.py
from pathlib import Path
import pandas as pd

def load_dataset(file_path: Path) -> pd.DataFrame:
    """
    Charge le dataset depuis le chemin spécifié.
    
    Args:
        file_path (Path): Chemin vers le fichier CSV à charger.
        
    Returns:
        pd.DataFrame: Le dataset chargé.
    """
    df = pd.read_csv(file_path)
    return df