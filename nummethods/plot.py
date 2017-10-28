import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D

def plot(data):
    """
    Plot one function
    """
    plt.plot(data[0], data[1])
    plt.show()


def plot_all(z, x, S, p):
    """
    Plot 4 functions, z, x, S in one plot
    """
    plt.figure(1)
    plt.subplot(121)
    zplot = plt.plot(z[0], z[1], 'b-', label="z(t)")
    xplot = plt.plot(x[0], x[1], 'r-', label="x(t)")
    Splot = plt.plot(S[0], S[1], label="S(t)")
    plt.legend()

    pplot = plt.subplot(122)
    pplot.set_title("p(w)")
    plt.plot(p[0], p[1], 'r-')
    plt.show()
