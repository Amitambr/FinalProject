from Bio import SeqIO
import csv

# === Config ===
fasta_file = "idmapping_2025_06_29.fasta"   # <- your input FASTA file
output_csv = "peptides.csv"                 # <- MHCflurry input
mhc_allele = "HLA-A*02:01"                  # <- change as needed
min_len = 8
max_len = 11

# === Extract peptides ===
unique_peptides = set()

for record in SeqIO.parse(fasta_file, "fasta"):
    seq = str(record.seq)
    for length in range(min_len, max_len + 1):
        for i in range(len(seq) - length + 1):
            peptide = seq[i:i+length]
            if "X" not in peptide and "U" not in peptide and "B" not in peptide:
                unique_peptides.add(peptide)

# === Write CSV for MHCflurry ===
with open(output_csv, mode="w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["peptide", "allele"])
    for pep in sorted(unique_peptides):
        writer.writerow([pep, mhc_allele])

print(f"Saved {len(unique_peptides)} peptides to {output_csv}")