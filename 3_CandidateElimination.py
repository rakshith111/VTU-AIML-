""" For a given set of training data examples stored in a .CSV file, implement and demonstrate the
candidate-Elimination algorithm output a description of the set of all hypotheses consistent with the training
examples """

import csv

with open("CandidateElimination.csv") as f:
    csv_file = csv.reader(f)
    data = list(csv_file)

    specific_hyp = data[1][:-1]
    row_size=len(specific_hyp)
    general_hyp = [['?' for i in range(row_size)] for j in range(row_size)]

    for row in data:
        if row[-1] == "Yes":
            for item in range(row_size):
                if row[item] != specific_hyp[item]:
                    specific_hyp[item] = '?'
                    general_hyp[item][item] = '?'

        elif row[-1] == "No":
            for item in range(row_size):
                if row[item] != specific_hyp[item]:
                    general_hyp[item][item] = specific_hyp[item]
                else:
                    general_hyp[item][item] = "?"
        print("\nSteps of Candidate Elimination Algorithm", data.index(row) + 1)
        print(specific_hyp)
        print(general_hyp)
    t=['?', '?', '?', '?', '?', '?']
    while t in general_hyp:
        general_hyp.remove(t)

    print("\nFinal specific hypothesis:\n", specific_hyp)

    print("\nFinal general hypothesis:\n", general_hyp)
