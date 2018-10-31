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

def gamma_run(output_dir, set_title, gammas, gamma_acc, gamma_convg, control_acc, control_convg, max_iters):
    plt.plot(gammas, gamma_acc, color="red", label='Alternative')
    plt.plot(gammas, [control_acc for i in range(len(gammas))], color='blue', label='Control', linestyle = '-.', alpha=.7)
    plt.title("Accuracy for " + str(set_title))
    plt.legend()
    plt.xlabel("Gamma")
    plt.ylabel("Percent Correct")
    plt.savefig(output_dir + "/"  + str(set_title) + "_accuracy")
    plt.clf()

    plt.plot(gammas, gamma_convg, color="red", label='Alternative')
    plt.plot(gammas, [control_convg for i in range(len(gammas))], color='blue', label='Control', linestyle = '-.', alpha=.7)
    plt.plot(gammas, [max_iters for i in range(len(gammas))], color='grey', linestyle='--', alpha=.5, label='Max Iterations allowed')

    plt.title("Convergence Time for " + str(set_title))
    plt.legend()
    plt.xlabel("Gamma")
    plt.ylabel("Average Iterations to Convergence") #note that NOT converging counts as Max Iters
    plt.savefig(output_dir + "/"  + str(set_title) + "_convergence")
    plt.clf()


def gen_avg_data(data):
    # TODO: finish and put in larger scheme
    # given many reps of same sim, avg features who are at the same iteration
    avg_data = [[None for i in range(len(data)-1)] for j in range(len(data[0]))] #may need to reverse
    for j in range(len(data)):
        for i in range(len(data[0])):
            avg_data[data[0][i]][j] += data[i][j] #i think