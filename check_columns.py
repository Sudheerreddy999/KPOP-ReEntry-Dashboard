import pandas as pd

files = [
    "reentry_frequency.csv",
    "momentum_score.csv",
    "retention_days.csv",
    "rank_recovery_speed.csv",
    "album_comeback_advantage.csv",
    "fandom_intensity_score.csv"
]

for f in files:
    df = pd.read_csv(f"dashboard_data/{f}")
    print("\n", f)
    print(df.columns.tolist())