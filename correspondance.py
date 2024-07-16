##correspondance
import os
import csv

true_pos = "true_positives.txt"
queries = "queries_correspondance.txt"
targets = "targets__correspondance.txt"
cor = "correspondance_complexes_to_queries_and_targets"
output_dir = "correspondance"

queries_correspondance = {}
with open(queries, "r") as qc_file:
    for line in qc_file:
        parts = line.strip().split()
        queries_correspondance[parts[0]] = parts[1]

targets_correspondance = {}
with open(targets, "r") as tc_file:
    for line in tc_file:
        parts = line.strip().split()
        targets_correspondance[parts[0]] = parts[1]

correspondance_complexes = {}
with open(cor, "r") as cc_file:
    reader = csv.DictReader(cc_file)
    for row in reader:
        correspondance_complexes[(row["PDB ID 1"], row["PDB ID 2"])] = row["Complex"]

for dir_name in os.listdir(output_dir):
    X, Y = dir_name.split("_")
        pdbidx = queries_correspondance.get(X)
    pdbidy = targets_correspondance.get(Y)
        complex = correspondance_complexes.get((pdbidx, pdbidy))

    print(f"For true positive {dir_name}, the corresponding complex is: {complex}")
