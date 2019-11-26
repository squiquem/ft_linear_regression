import pandas as pd
import matplotlib.pyplot as plt
import argparse
import sys

def error_exit(string):
    """
    Print + quit
    """
    print(string)
    sys.exit(0)

def file_check(file):
    """
    Checking if file is correct
    """
    try:
        with open(file, 'r') as f:
            fl = f.readlines()
            for l in fl[1:]:
                L = l[:-1].split(',')
                if not L[0].isnumeric() or not L[1].isnumeric():
                    return 0
            return 1
    except:
        error_exit('No data')

def cost(X, Y, th):
    """
    MSE
    """
    return ((th[1] * X + th[0] - Y) ** 2).sum() / len(X)

def new_theta(lr, X, Y, th):
    """
    Updating theta with output
    """
    new = [0, 0]
    pred = X * th[1] + th[0]
    new[0] = th[0] - 2 * lr * (pred - Y).sum() / len(X)
    new[1] = th[1] - 2 * lr * (pred - Y).dot(X).sum() / len(X)
    return new

def normalisation(s):
    """
    Normalisation
    """
    if s.empty:
        error_exit("No data")
    return (s - min(s)) / (max(s) - min(s))

def unnormalization(th, P, K):
    """
    Reversed Normalisation
    """
    DP = max(P) - min(P)
    DK = max(K) - min(K)
    return [
        min(P) + DP * (th[0] - th[1] * min(K) / DK),
        th[1] * DP / DK
    ]

if __name__ == '__main__':
    # Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--epochs', type=int,
            help='number of iterations', default=500)
    parser.add_argument('-lr', '--learningrate', type=float,
            help='learning rate', default=0.1)
    parser.add_argument('file', type=str,
            help='train from data in file')
    parser.add_argument('-o', '--output', type=str,
            help='output file', default='theta.txt')
    args = parser.parse_args()
    lr, epochs = args.learningrate, args.epochs

    # Arguments check
    if epochs <= 0:
        error_exit('Enter positive number of epochs')
    if lr <= 0:
        error_exit('Enter positive learning rate')

    # File check
    if not file_check(args.file):
        error_exit('Wrong data')

    # From file to dataframe
    df = pd.read_csv(args.file, sep=',')
    price = df.columns[1]
    km = df.columns[0]
    df['X'] = normalisation(df[km])
    df['Y'] = normalisation(df[price])
    theta = [0, 0]
    E, C = [i for i in range(epochs)], []

    # Plotting
    plt.figure(figsize=(10, 5))
    plt.subplot(121)
    axes = plt.gca()
    xdata, ydata = df[km], [0] * len(df)
    line, = axes.plot(xdata, ydata, 'r-')
    line.set_xdata(xdata)
    plt.scatter(df[km], df[price])
    plt.ylabel(price)
    plt.xlabel(km)
    plt.title(price + ' = f(' + km + ')')

    for e in range(epochs):
        theta = new_theta(lr, df.X, df.Y, theta)
        alpha = unnormalization(theta, df[price], df[km])
        C.append(cost(df.X, df.Y, theta))
        line.set_ydata(alpha[1] * xdata + alpha[0])
        plt.title('Epoch {}'.format(str(e)))
        plt.draw()
        plt.pause(1e-17)

    # Accuracy
    print("Précision de l'algorithme:")
    print("RMSE =", 100 * (1 - C[-1] ** 0.5), "%")
    print("MSE =", 100 * (1 - C[-1]), "%")

    # Theta file
    try:
        with open(args.output, "w+") as f:
            f.write('{}\n{}\n'.format(alpha[0], alpha[1]))
    except:
        error_exit('Wrong file')

    # Plot cost = f(epoch)
    plt.subplot(122)
    plt.ylabel('Cost')
    plt.xlabel('Epochs')
    plt.title('Cost = f(epoch)')
    plt.plot(E, C)
    plt.show()
