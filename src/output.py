import os

def write_confusion(true_pos, false_pos, true_neg, false_neg, iter, output_dir):
    # NOT USED

    with open(output_dir+"/accuracy.csv",'a') as file:
        file.write(str(iter) +"," + str(true_pos) + "," + str(false_pos) + "," + str(true_neg) + "," + str(false_neg) + "\n")

def init_output(output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    #with open(output_dir + "/accuracy.csv", 'w') as file:
    #    file.write("Iteration, True Positives, False Positives, True Negatives, False Negatives\n")



def print_matrices(P,D,R,L):
    print("\nPotentials: " + str(P))
    print("\nLengths: " + str(L))
    print("\nResistances: " + str(R))
    print("\nDiameter: " + str(D))

