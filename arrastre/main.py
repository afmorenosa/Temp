"""."""
from imports import drag_cuadratic as dc
from imports import runge_kutta_4 as rk4
from imports import drag_lineal as dl
import matplotlib.pyplot as plt
from imports import free_fall as ff
from matplotlib import animation
"""
Andŕes Felipe Moreno Sarria
"""

vx = 6
vy = 4
vx_dl = vx
vy_dl = vy
vx_dc = vx
vy_dc = vy
vx_ff = vx
vy_ff = vy
x_dl = [0]
y_dl = [0]
x_dc = [0]
y_dc = [0]
x_ff = [0]
y_ff = [0]
g = 9.8
m = 1.4
c = 0.3
tf = 2 * vy / g
N = 500
h = tf / N

dl.set_parameters(c, m, g)
dc.set_parameters(c, m, g)
ff.set_parameters(c, m, g)

"""Cofigurar las figuras, los ejes y los entornos donde se animará."""
fig = plt.figure()
ax = plt.axes(xlim=(0, 2*vx*vy/g), ylim=(0, vy*vy/(2*g)*(1.1)))
ax.grid()
line, = ax.plot([], [], lw=3)
line2, = ax.plot([], [], lw=3)
line3, = ax.plot([], [], lw=3)


def init():
    """Establecer los datos de la grafica a animar."""
    line.set_data([], [])
    line2.set_data([], [])
    line3.set_data([], [])

    return line, line2, line3


def animate(i):
    """Actualización de la animación."""
    global vx_dl, vy_dl, vx_dc, vy_dc, vx_ff, vy_ff

    refresh_dl = rk4.rk4(dl.dx, dl.dy, dl.dvx, dl.dvy, x_dl[-1], y_dl[-1],
                         vx_dl, vy_dl, h)
    refresh_dc = rk4.rk4(dc.dx, dc.dy, dc.dvx, dc.dvy, x_dc[-1], y_dc[-1],
                         vx_dc, vy_dc, h)
    refresh_ff = rk4.rk4(ff.dx, ff.dy, ff.dvx, ff.dvy, x_ff[-1], y_ff[-1],
                         vx_ff, vy_ff, h)

    if(len(x_dc) <= 40):

        x_dl.append(refresh_dl[0])
        y_dl.append(refresh_dl[1])
        x_dc.append(refresh_dc[0])
        y_dc.append(refresh_dc[1])
        x_ff.append(refresh_ff[0])
        y_ff.append(refresh_ff[1])

        vx_dl = refresh_dl[2]
        vy_dl = refresh_dl[3]
        vx_dc = refresh_dc[2]
        vy_dc = refresh_dc[3]
        vx_ff = refresh_ff[2]
        vy_ff = refresh_ff[3]

    else:

        x_dl.append(refresh_dl[0])
        y_dl.append(refresh_dl[1])
        x_dc.append(refresh_dc[0])
        y_dc.append(refresh_dc[1])
        x_ff.append(refresh_ff[0])
        y_ff.append(refresh_ff[1])

        x_dl.remove(x_dl[0])
        y_dl.remove(y_dl[0])
        x_dc.remove(x_dc[0])
        y_dc.remove(y_dc[0])
        x_ff.remove(x_ff[0])
        y_ff.remove(y_ff[0])

        vx_dl = refresh_dl[2]
        vy_dl = refresh_dl[3]
        vx_dc = refresh_dc[2]
        vy_dc = refresh_dc[3]
        vx_ff = refresh_ff[2]
        vy_ff = refresh_ff[3]

    line.set_data(x_dl, y_dl)
    line2.set_data(x_dc, y_dc)
    line3.set_data(x_ff, y_ff)

    return line, line2, line3


"""Animación."""
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=N, interval=20, blit=True)

"""Guardar animaciones."""
anim.save('Free_Fall.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
