"""."""
c = 1
m = 1
g = 9.8


def set_parameters(C=1, M=1, G=9.8):
    """."""
    global c, m, g
    c = C
    m = M
    g = G


def get_parameters(C=False, M=False, G=False):
    """."""
    if(C):
        if(M):
            if(G):
                return [c, m, g]
            else:
                return [c, m]
        else:
            if(G):
                return [c, g]
            else:
                return [c]
    else:
        if(M):
            if(G):
                return [m, g]
            else:
                return [m]
        else:
            if(G):
                return [g]
            else:
                return []


def dx(vx):
    """."""
    return vx


def dy(vy):
    """."""
    return vy


def dvx(vx, vy):
    """."""
    return 0


def dvy(vx, vy):
    """."""
    return -g
