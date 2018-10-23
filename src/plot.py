import os, numpy as np
from matplotlib import pyplot as plt


def accuracy(output_dir):
    X = import_data(output_dir + "/accuracy.csv")
    data, titles = X[0], X[1]
    for i in range(len(data.T)):
        plt.plot((data.T)[0], (data.T)[i])
        plt.savefig(output_dir + "/" + titles[i])
        plt.clf()


def import_data(input_file):

    assert (os.path.isfile(input_file))

    print("Importing data, assuming that first line has titles and using a .csv file\n")

    with open(input_file, 'r') as input:
        lines = input.readlines()
        titles = lines[0].split(",")
        piece = titles[-1].split("\n")
        titles[-1] = piece[0]
        num_features = len(titles)  # columns
        num_instances = len(lines) - 1  # rows, not counting title row
        data = np.empty((num_instances, num_features))

        for i in range(0, num_instances):
            row = lines[i + 1].split(",", num_features)
            piece = row[-1].split("\n")
            row[-1] = piece[0]
            data[i] = row

    # print_data(data, titles)
    return data, titles

def gen_avg_data(data):
    # TODO: finish and put in larger scheme
    # given many reps of same sim, avg features who are at the same iteration
    avg_data = [[None for i in range(len(data)-1)] for j in range(len(data[0]))] #may need to reverse
    for j in range(len(data)):
        for i in range(len(data[0])):
            avg_data[data[0][i]][j] += data[i][j] #i think