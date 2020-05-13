"""."""
sigma = 1
rho = 1
beta = 1


def set_parameters(S=1, R=1, B=1):
    """."""
    global sigma, rho, beta
    sigma = S
    rho = R
    beta = B


def dx(x, y, z):
    """."""
    return sigma * (y-x)


def dy(x, y, z):
    """."""
    return x * (rho - z) - y


def dz(x, y, z):
    """."""
    return x * y - beta * z
