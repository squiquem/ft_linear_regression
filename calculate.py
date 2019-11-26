import pandas as pd
import matplotlib.pyplot as plt
import argparse
import numpy as np
from train import file_check, error_exit

if __name__ == '__main__':
    # Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str,
            help='train from data in file')
    parser.add_argument('-o', '--output', type=str,
            help='output file', default='theta.txt')
    args = parser.parse_args()

    # File check
    if not file_check(args.file):
        error_exit('Wrong data')

    # From file to dataframe
    df = pd.read_csv(args.file, sep=',')
    if df.empty or len(df) < 2:
        error_exit("No data")
    km = df.columns[0]
    price = df.columns[1]

    # Theta exact calculation
    X = np.matrix([np.ones(df.shape[0]), np.stack(df[km].values)]).T
    y = np.matrix(df[price]).T
    theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

    # Plotting
    plt.ylabel(price)
    plt.xlabel(km)
    plt.title(price + ' = f(' + km + ')')
    plt.scatter(df[km], df[price])
    plt.plot(df[km], theta.item(1) * df[km] + theta.item(0), color='red')
    plt.show()

    # Theta file
    try:
        with open(args.output,"w+") as f:
            f.write('{}\n{}\n'.format(theta.item(0), theta.item(1)))
    except:
        error_exit('Wrong file')
