import pandas as pd

# Load predictions
df = pd.read_csv("predictions.csv")

# Filter for strong binders
strong = df[
    (df["mhcflurry_affinity"] < 500) |
    (df["mhcflurry_affinity_percentile"] < 2)
]

# Save filtered results
strong.to_csv("strong_peptides.csv", index=False)

print(f"Found {len(strong)} strong-binding peptides saved to 'strong_peptides.csv'")
