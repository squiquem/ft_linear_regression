import matplotlib.pyplot as plt
import pandas as pd
from train import file_check, error_exit
import argparse
import numpy as np

def check_number(f, n):
    """
    Check if number is correct
    """
    try:
        n = f(n)
    except:
        error_exit("Value error")
    return n

if __name__ == '__main__':
    # Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='text file for input')
    parser.add_argument('-sc', '--scatter', help='data scatter plot', type=str)
    args = parser.parse_args()

    # Check if theta is here
    try:
        with open(args.file, 'r') as f:
            if f.mode == 'r':
                theta = []
                fl = f.readlines()
                for x in fl:
                    theta.append(check_number(float, x))
    except:
        theta = [0, 0]
    print('Theta:', theta)

    # km input and calculation
    print('Veuillez entrer un kilométrage: ')
    d = input()
    d = check_number(float, d)
    p = theta[0] + theta[1] * d
    print('Le prix estimé est:', p, 'euros')

    # Check if scatter argument is here
    if args.scatter:
        if not file_check(args.scatter):
            error_exit('Wrong data')
        df = pd.read_csv(args.scatter)
        km = df.columns[0]
        price = df.columns[1]
        plt.scatter(df[km], df[price])
        X, Y = df[km], df[price]
    else:
        X = np.linspace(0, 250000, num=25)
        price = None
        km = None

    # Plotting
    plt.plot(d, p, '*', markersize=12, color='red')
    plt.plot(X, theta[0] + theta[1] * X, color='green')
    if price and km:
        plt.ylabel(price)
        plt.xlabel(km)
        plt.title(price + ' = f(' + km + ')')
    plt.show()
