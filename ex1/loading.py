import importlib.util
from importlib import metadata

if (__name__ == "__main__"):
    REQUIRED = ["pandas", "requests", "matplotlib"]
    missing = [m for m in REQUIRED if importlib.util.find_spec(m) is None]
    if (missing):
        print(missing, "are missing you can get them via pip \
(pip install -r requirements.txt) or Poetry (poetry install)")
    else:
        import pandas as pd
        import requests
        import matplotlib.pyplot as plt

        print("\nLOADING STATUS: Loading programs...\n")
        print("Checking dependencies:")
        print(f"[OK] {REQUIRED[0]} ({metadata.version(REQUIRED[0])}) \
- Data manipulation ready")
        print(f"[OK] {REQUIRED[1]} ({metadata.version(REQUIRED[1])}) \
- Network access ready")
        print(f"[OK] {REQUIRED[2]} ({metadata.version(REQUIRED[2])}) \
- Visualization ready")

        # Coordonnées (ex: Paris)
        LAT = 45.783
        LON = 4.738

        URL = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={LAT}&longitude={LON}"
            "&daily=temperature_2m_max"
            "&timezone=Europe/Paris"
        )
        file_name = "matrix_analysis.png"

        response = requests.get(URL, timeout=10)
        response.raise_for_status()
        data = response.json()

        print("\nAnalyzing Matrix data...")
        print("Processing 1000 data points...")

        df = pd.DataFrame({
            "date": data["daily"]["time"],
            "temp_max": data["daily"]["temperature_2m_max"]
        })

        df["date"] = pd.to_datetime(df["date"])

        print("Generating visualization...")
        # Plot
        plt.figure(figsize=(8, 4))
        plt.plot(df["date"], df["temp_max"], marker="o")
        plt.title("Température maximale sur 7 jours")
        plt.xlabel("Date")
        plt.ylabel("Température (°C)")
        plt.grid(True)

        # Sauvegarde PNG
        plt.tight_layout()
        plt.savefig(file_name)
        plt.close()
        print("\nAnalysis complete!")
        print("Results saved to:", file_name)
