import math


def initial(x: float) -> float:
    """
    Initial conditions
    :param x: coordinates
    :return: value in coordinates x
    """
    return 50 * math.exp(-(x - 0.5) ** 2 / 0.02) - 20 * x + 30
