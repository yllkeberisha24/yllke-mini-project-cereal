from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = Path("data/raw/cereal.csv")
OUTPUT_PATH = Path("output/sugar_histogram.png")

df = pd.read_csv(DATA_PATH)
df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
plt.figure(figsize=(6,4))
sns.histplot(df["sugars"], bins=10)
plt.title("Cereal Sugar Content")
plt.xlabel("Sugar (g)")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig(OUTPUT_PATH)
plt.show()
