import pandas as pd

df = pd.read_csv("strong_peptides.csv")
ca = pd.read_csv("caAtlas_non_mod_peptides.csv", sep='\t')  

merged = df.merge(ca, left_on="peptide", right_on="Peptide_Sequence", how="inner")

merged.to_csv("caAtlas_matches.csv", index=False)
print(f"Found {len(merged)} matching peptides in caAtlas.")