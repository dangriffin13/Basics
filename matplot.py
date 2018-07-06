
import matplotlib.pyplot as plt
import math


x = [i for i in range(1,26)]
log_x = [math.log(i) for i in x]
x_exp = [i**2 for i in x]

def plot_log_x():
    plt.plot(x, log_x)
    plt.xlabel('x')
    plt.ylabel('log base 2 of x')
    plt.title('Log of X')
    plt.show()


def fig_log_x():  #object oriented
    fig = plt.figure()
    axes = fig.add_axes() #play with this in jupyter

    axes.set_xlabel('X')
    axes.set_ylable('Log base 2 of X')
    axes.set_title('Log of X')


if __name__ == "__main__":
    print("Start plotting")
    print('Methods: plot_log_x, fig_log_x')

    