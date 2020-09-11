'''
Plot 1D Gaussian
'''

import numpy as np
import matplotlib.pyplot as plt
import argparse

def plot_gaussian_1d(mean=0., std=1., model=False):

    plt.xlabel('x')
    plt.ylabel('Gaussian dist')

    if model:
        # generate data bet -4, 4 interval of 0.02
        x = np.arange(-4 + mean, 4 + mean, 0.02)
        y = np.exp( -(x - mean)**2 / (2 * std**2) )
        y /= (std * np.sqrt(2 * np.pi))

        plt.plot(x, y, '-', label="model=N(x; mean, std^2)")

    data = np.random.normal(mean, std, 10000)
    hist, edges = np.histogram(data, 100, density=True)
    plt.plot(edges[:-1], hist, 'o', label="1D Gaussian samples")

    plt.savefig("gaussian_1d.png")
    plt.show()
    plt.close('all')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='1D Gaussian')
    parser.add_argument('--mean',
                        type=float,
                        default=0.0,
                        help='Mean of Gaussian dist')
    parser.add_argument('--std',
                        type=float,
                        default=1.0,
                        help='Standard deviation of Gaussian dist')
    parser.add_argument('--model',
                        default=False,
                        action='store_true',
                        help='Plot using 1D Gaussian model')
    args = parser.parse_args()

    plot_gaussian_1d(args.mean, args.std, args.model)
