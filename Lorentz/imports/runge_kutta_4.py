"""."""


def rk4(dx, dy, dz, x, y, z, h):
    """."""
    k1 = h * dx(x, y, z)
    l1 = h * dy(x, y, z)
    m1 = h * dx(x, y, z)

    k2 = h * dx(x + k1 * 0.5, y + l1 * 0.5, z + m1 * 0.5)
    l2 = h * dy(x + k1 * 0.5, y + l1 * 0.5, z + m1 * 0.5)
    m2 = h * dz(x + k1 * 0.5, y + l1 * 0.5, z + m1 * 0.5)

    k3 = h * dx(x + k2 * 0.5, y + l2 * 0.5, z + m2 * 0.5)
    l3 = h * dy(x + k2 * 0.5, y + l2 * 0.5, z + m2 * 0.5)
    m3 = h * dz(x + k2 * 0.5, y + l2 * 0.5, z + m2 * 0.5)

    k4 = h * dx(x + k3, y + l3, z + m3)
    l4 = h * dy(x + k3, y + l3, z + m3)
    m4 = h * dz(x + k3, y + l3, z + m3)

    X = x + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    Y = y + (l1 + 2 * l2 + 2 * l3 + l4) / 6
    Z = z + (m1 + 2 * m2 + 2 * m3 + m4) / 6

    return [X, Y, Z]
