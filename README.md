# FinalProject: Immunogenic Peptide Discovery Pipeline

This repository contains scripts for analyzing TMT-labeled proteomics data and identifying immunogenic peptides using **MSstatsTMT**, **MHCflurry**, and validation against **IEDB** and **Cancer Peptide Atlas** datasets.

---

## MSstatsTMT Analysis

**File:** `MSstatsTMT_pipeline1.Rmd`

This script performs TMT-based proteomics analysis using the **MSstatsTMT** package. It:
- Converts FragPipe `protein.tsv` files into the MSstatsTMT format
- Applies normalization and imputation
- Runs group comparisons across biological conditions
- Identifies significant proteins using `log2FC` and `p-value` thresholds
- Visualizes results using volcano plots

**Output includes:**
- Annotation files (`*_annotation.tsv`)
- Converted intensity files (`*_converted.tsv`)
- Differential abundance results (`*_DA_proteins.csv`)
- Volcano plots and significant protein tables

---

## IEDB Epitope Matching

**File:** `IEDB_search.py`

This script matches predicted strong-binding peptides (`strong_peptides.csv`) from **MHCflurry** with known epitopes in the **IEDB** database (`epitope_full_v3.csv`).

**Output:**
- `iedb_matches_clean.csv` with:
  - Binding scores
  - Epitope metadata (organism, source molecule, start/end positions, etc.)

---

## Cancer Peptide Atlas Search

**File:** `caAtlas_search.py`

This script cross-checks strong-binding peptides against known tumor-associated peptides in the **Cancer Peptide Atlas** (`caAtlas_non_mod_peptides.csv`).

**Output:**
- `caAtlas_matches.csv` with microbial peptides already observed in tumor samples

---

## Peptide Generation from FASTA

**File:** `generate_peptides_for_mhcflurry.py`

This script extracts all possible **8–11mer peptides** from a FASTA file of protein sequences (`idmapping_2025_06_29.fasta`). It excludes non-standard amino acids (X, U, B) and formats the output for **MHCflurry** input.

**Output:**
- `peptides.csv` containing peptide sequences and MHC allele assignments

---

## Strong Binder Filtering

**File:** `strong_peptides_filter.py`

This script filters MHCflurry prediction results (`predictions.csv`) to identify **strong-binding peptides** using either of the following criteria:
- Affinity < 500 nM
- Percentile rank < 2%

**Output:**
- `strong_peptides.csv` — used for downstream IEDB and Cancer Atlas validation

---

## Summary

Each script contributes to identifying microbial peptides with potential immunogenicity in cancer:
- **MSstatsTMT** identifies differentially expressed proteins
- **MHCflurry** predicts peptide-MHC binding
- **IEDB** and **Cancer Peptide Atlas** provide external validation

Use this pipeline to trace bacterial peptides through tumor proteomics and assess their immune relevance.
