"""."""
from imports import runge_kutta_4 as rk4
import mpl_toolkits.mplot3d.axes3d as p3
from scipy.integrate import odeint
from imports import lorentz as lr
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
"""
Andŕes Felipe Moreno Sarria
"""

sigma = 9
rho = 35
beta = 8/4
tf = 40
N = 5000
h = tf/N
x = [1]
y = [1]
z = [1]
px = [1]
py = [1]
pz = [1]

lr.set_parameters(sigma, rho, beta)

"""Cofigurar las figuras, los ejes y los entornos donde se animará."""
fig = plt.figure()
ax = p3.Axes3D(fig)
ax.set_xlim(-20, 20)
ax.set_ylim(-30, 30)
ax.set_zlim(0, 50)
ax.grid()
line, = ax.plot([], [], [], lw=1, c="magenta")
line2, = ax.plot([], [], [], ".", ms=5, c="purple")
ax.set_title(r"$\sigma={}, \rho={}, \beta={}$".format(sigma, rho, beta))


def init():
    """Establecer los datos de la grafica a animar."""
    line.set_data([], [])
    line.set_3d_properties([])
    line2.set_data([], [])
    line2.set_3d_properties([])

    return line, line2


def animate(i):
    """Actualización de la animación."""
    global x, y, z, px, py, pz

    if((i+1)/N*100 == 20):
        print("{:.2f}% Analizando Datos".format((i+1)/N*100))
    elif((i+1)/N*100 == 40):
        print("{:.2f}% Configurando figuras".format((i+1)/N*100))
    elif((i+1)/N*100 == 50):
        print("{:.2f}% Dibujando Trayectoria".format((i+1)/N*100))
    elif((i+1)/N*100 == 60):
        print("{:.2f}% Colocando colores".format((i+1)/N*100))
    elif((i+1)/N*100 == 80):
        print("{:.2f}% Ultimos detalles".format((i+1)/N*100))
    elif((i+1)/N*100 == 100):
        print("{:.2f}% Finalizado".format((i+1)/N*100))

    refresh = rk4.rk4(lr.dx, lr.dy, lr.dz, x[-1], y[-1], z[-1], h)
    x.append(refresh[0])
    y.append(refresh[1])
    z.append(refresh[2])

    px = [x[-1]]
    py = [y[-1]]
    pz = [z[-1]]

    line.set_data(x, y)
    line.set_3d_properties(z)
    line2.set_data(px, py)
    line2.set_3d_properties(pz)

    return line, line2


"""Animación."""
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=N, interval=20, blit=True)

"""Guardar animaciones."""
anim.save('lorentz.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

sigma = 10
rho = 29
beta = 8/3
lr.set_parameters(sigma, rho, beta)


def f(state, t):
    """."""
    x, y, z = state  # Unpack the state vector
    return lr.dx(x, y, z), lr.dy(x, y, z), lr.dz(x, y, z)  # Derivatives


state0 = [1.0, 1.0, 1.0]
t = np.arange(0.0, 40.0, 0.01)

states = odeint(f, state0, t)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(states[:, 0], states[:, 1], states[:, 2], lw=1, c="r")
ax.set_title(r"$\sigma={}, \rho={}, beta={}$".format(sigma, rho, beta))
fig.savefig("lorentz.pdf")
