import matplotlib.pyplot as plt
import time
import numpy as np


def draw(matrix: list) -> None:
    """
    Draws graph changes
    :param matrix: matrix with data
    :return: none
    """
    a, b = np.shape(matrix)
    x = np.linspace(0, 1, b)
    plt.ion()
    fig = plt.figure()
    ax = fig.add_subplot(111)

    for i in range(0, a):
        plt.clf()
        plt.plot(x, matrix[i, :])
        plt.draw()
        plt.gcf().canvas.flush_events()
        time.sleep(0.00001)

    plt.ioff()
    plt.show()
