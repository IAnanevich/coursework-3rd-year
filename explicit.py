import numpy as np
import draw

from conditions import initial, borders


def solve(M: int, N: int, tau: float, h: float) -> list:
    """
    Create matrix with data
    :param M: numbers of columns
    :param N: numbers of lines
    :param tau: columns breaks value
    :param h: lines breaks value
    :return: matrix with data of temperature
    """
    matrix = np.zeros((M + 1, N + 1), dtype=float)

    for i in range(1, N):
        matrix[0][i] = initial.initial(i * h)

    for i in range(0, M + 1):
        matrix[i][0] = borders.border1(i * tau)
        matrix[i][N] = borders.border2(i * tau)

    for i in range(1, M + 1):
        for j in range(1, N):
            matrix[i][j] = matrix[i - 1][j] + alpha * (matrix[i - 1][j - 1] + matrix[i - 1][j + 1] - 2 * matrix[i - 1][j])

    return matrix


if __name__ == "__main__":
    a = 1.
    L = 1.
    T = 10
    alpha = 0.5
    N = 20

    h = L / N
    tau = pow(h, 2) * alpha / pow(a, 2)
    M = T / tau

    matrix = solve(int(M), N, tau, h)

    draw.draw(matrix)
