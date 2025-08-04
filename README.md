# FinalProject

This script performs TMT-based proteomics analysis using the MSstatsTMT package. It manually converts FragPipe protein.tsv files into the MSstatsTMT format, applies normalization, and runs group comparisons across biological conditions. Significant proteins are identified based on log2FC and p-value thresholds, and visualized using volcano plots. The output includes annotation files, converted data, statistical results, and lists of differentially abundant proteins.


This script matches predicted strong-binding peptides from MHCflurry (strong_peptides.csv) with known epitopes in the IEDB database (epitope_full_v3.csv). It merges the datasets by peptide sequence and exports a cleaned, annotated list of overlapping peptides to iedb_matches_clean.csv. The output includes MHC binding scores and metadata like source organism, epitope position, and parent protein.

This script cross-checks strong-binding peptides predicted by MHCflurry (strong_peptides.csv) against known tumor-associated peptides from the Cancer Peptide Atlas (caAtlas_non_mod_peptides.csv).
Peptides that appear in both datasets are saved to caAtlas_matches.csv, allowing identification of microbial peptides already observed in tumor samples.
