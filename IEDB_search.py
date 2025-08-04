import pandas as pd

# Load strong-binding peptide predictions
df = pd.read_csv("strong_peptides.csv")

# Load full IEDB dataset (with headers on second line)
iedb = pd.read_csv("epitope_full_v3.csv", header=1)

# Merge on peptide sequence
merged = df.merge(iedb, left_on="peptide", right_on="Name", how="inner")

# Select only useful columns
final = merged[[
    "peptide", "allele", "mhcflurry_affinity", "mhcflurry_affinity_percentile",
    "mhcflurry_processing_score", "mhcflurry_presentation_score", "mhcflurry_presentation_percentile",
    "Object Type", "Modifications", "Starting Position", "Ending Position",
    "Source Molecule", "Molecule Parent", "Source Organism", "Species", "Epitope Relation", "Synonyms"
]]

# Save final annotated matches
final.to_csv("iedb_matches_clean.csv", index=False)
print(f"Saved {len(final)} annotated matches to 'iedb_matches_clean.csv'")