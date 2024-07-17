#!/bin/bash

true_positives_file="true_positives_complexes.txt"
reference_dir="/media/nikatchou/One Touch/shrek2024/ground_truth/filtered_PDB/queries"
output_dir="OUTPUTS_ref"

while IFS= read -r complex_name; do
    reference_pdb="$reference_dir/$complex_name.pdb"
    if [ -f "$reference_pdb" ]; then
        output_pdb="$output_dir/$complex_name.pdb"

        if [ -f "$output_pdb" ]; then
            ./stage/bin/ost compare-structures -m "$reference_pdb" -r "$output_pdb" --lddt --dockq --ics --ips --tm-score
        else
            echo "Output PDB file $output_pdb not found."
        fi
    else
        echo "Reference PDB file $reference_pdb not found."
    fi
done < "$true_positives_file"
