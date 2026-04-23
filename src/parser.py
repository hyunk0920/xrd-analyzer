from pathlib import Path
import pandas as pd
def load_xrd_csv(filepath: str | Path ) -> pd.DataFrame:
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"CSV not found : {filepath}")
    df = pd.read_csv(filepath)
    expected_cols = {"two_theta", "intensity"}
    if not expected_cols.issubset(df.columns):
        raise ValueError(
            f"CSV must have columns {expected_cols}, got {set(df.columns)}"
        )
    df = df[["two_theta", "intensity"]].copy()
    df = df.sort_values("two_theta").reset_index(drop=True)
    return df