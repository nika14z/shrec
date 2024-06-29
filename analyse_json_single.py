import json

scores_of_interest = ['ics', 'ips', 'lddt', 'tm_score', 'dockq']

with open('out.json') as json_file:
    data = json.load(json_file)

with open('selected_scores.txt', 'w') as score_file:
    for score_name in scores_of_interest:
        if score_name in data:
            score_file.write(f"{score_name}: {data[score_name]}\n")
        else:
            print(f"Score '{score_name}' not found in the data.")



### example of ost command: ./ost compare-structures -m cluster1_1.pbd -r 2I25_N_L.pdb --lddt --dockq --ics --ips --tm-score
