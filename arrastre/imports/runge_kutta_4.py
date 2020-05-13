"""."""


def rk4(dx, dy, dvx, dvy, x, y, vx, vy, h):
    """."""
    kx1 = h * dx(vx)
    ky1 = h * dy(vy)
    lx1 = h * dvx(vx, vy)
    ly1 = h * dvy(vx, vy)

    kx2 = h * dx(vx + 0.5 * lx1)
    ky2 = h * dy(vy + 0.5 * ly1)
    lx2 = h * dvx(vx + 0.5 * lx1, vy + 0.5 * ly1)
    ly2 = h * dvy(vx + 0.5 * lx1, vy + 0.5 * ly1)

    kx3 = h * dx(vx + 0.5 * lx2)
    ky3 = h * dy(vy + 0.5 * ly2)
    lx3 = h * dvx(vx + 0.5 * lx2, vy + 0.5 * ly2)
    ly3 = h * dvy(vx + 0.5 * lx2, vy + 0.5 * ly2)

    kx4 = h * dx(vx + lx3)
    ky4 = h * dy(vy + ly3)
    lx4 = h * dvx(vx + lx3, vy + ly3)
    ly4 = h * dvy(vx + lx3, vy + ly3)

    X = x + (kx1 + 2 * kx2 + 2 * kx3 + kx4) / 6
    Y = y + (ky1 + 2 * ky2 + 2 * ky3 + ky4) / 6
    VX = vx + (lx1 + 2 * lx2 + 2 * lx3 + lx4) / 6
    VY = vy + (ly1 + 2 * ly2 + 2 * ly3 + ly4) / 6

    return [X, Y, VX, VY]
