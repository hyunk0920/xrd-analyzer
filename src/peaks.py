import pandas as pd
from scipy.signal import find_peaks

def detect_peaks(
        df : pd.DataFrame,
        height : float | None=None,
        distance : int=1,
) -> pd.DataFrame:
    
    if height is None:
        height = df["intensity"].max() * 0.1
    
    peak_indices, _ = find_peaks(
        df["intensity"].values,
        height=height,
        distance=distance,
    )
    peaks_df = df.iloc[peak_indices].copy().reset_index(drop=True)
    return peaks_df