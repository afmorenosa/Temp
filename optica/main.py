"""Simulacion de un rayo incidente en una interfaz."""
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import pyplot as plt
from matplotlib import animation
import math

"""
Este codigo simula un rayo incidiendo en una interfaz, plana, con un alguno
inicial de treinta grados (30°).

Andŕes Felipe Moreno Sarria
"""

"""Cofigurar las figuras, los ejes y los entornos donde se animará."""
fig = plt.figure()
ax = p3.Axes3D(fig)
ax.grid()
ax.plot([-5, 5], [0, 0], [0, 0], lw=1)
ax.plot([0, 0], [-5, 5], [0, 0], lw=1)
ax.plot([0, 0], [0, 0], [-5, 5], lw=1)
line, = ax.plot([], [], [], lw=3)
line2, = ax.plot([], [], [], lw=3)
line3, = ax.plot([], [], [], lw=3)
line4, = ax.plot([], [], [], lw=3)


"""Variables importantes."""
E = 2
n1 = 1
n2 = 1.5
lo = 500
k = 2 * math.pi / lo
w = 2 * math.pi / 60
sxi = math.sin(math.pi / 6)
syi = - math.cos(math.pi / 6)
syr = math.cos(math.pi / 6)
theta_t = math.asin(n1 * math.sin(math.pi / 6) / n2)
sxt = math.sin(theta_t)
syt = - math.cos(theta_t)
er = 2 * syi * k
et = (-n2 * syt + syi) * k
r_par = (-n2 * syi + n1 * syt)/(-n2 * syi - n1 * syt)
r_per = (-n1 * syi + n2 * syt)/(-n1 * syi - n2 * syt)
t_par = (-2 * n1 * syi)/(-n2 * syi - n1 * syt)
t_per = (-2 * n1 * syi)/(-n1 * syi - n2 * syt)


def Exi(x, y, z, t):
    """Campo electrico incidente, componente x."""
    Ex = E * math.cos(k * n1 * (x * sxi + y * syi) - w
                        * t) * math.cos(math.pi / 6) / math.sqrt(2)
    return Ex


def Eyi(x, y, z, t):
    """Campo electrico incidente, componente y."""
    Ey = E * math.cos(k * n1 * (x * sxi + y * syi) - w
                        * t) * math.sin(math.pi / 6) / math.sqrt(2)
    return Ey


def Ezi(x, y, z, t):
    """Campo electrico incidente, componente z."""
    Ez = - E * math.sin(k * n1 * (x * sxi + y * syi) - w
                          * t) / math.sqrt(2)
    return Ez


def Exr(x, y, z, t):
    """Campo electrico reflejado, componente x."""
    Ex = r_par * E * math.cos(k * n1 * (x * sxi + y * syr + er) - w
                                * t) * math.cos(math.pi / 6) / math.sqrt(2)
    return Ex


def Eyr(x, y, z, t):
    """Campo electrico reflejado, componente y."""
    Ey = r_par * E * math.cos(k * n1 * (x * sxi + y * syr + er) - w
                                * t) * math.sin(math.pi / 6) / math.sqrt(2)
    return Ey


def Ezr(x, y, z, t):
    """Campo electrico reflejado, componente z."""
    Ez = - r_per * E * math.sin(k * n1 * (x * sxi + y * syr + er) - w
                                  * t) / math.sqrt(2)
    return Ez


def Ext(x, y, z, t):
    """Campo electrico transmitido, componente x."""
    Ex = t_par * E * math.cos(k * n1 * (x * sxt + y * syt + et) - w
                                * t) * math.cos(math.pi / 6) / math.sqrt(2)
    return Ex


def Eyt(x, y, z, t):
    """Campo electrico transmitido, componente y."""
    Ey = t_par * E * math.cos(k * n1 * (x * sxt + y * syt + et) - w
                                * t) * math.sin(math.pi / 6) / math.sqrt(2)
    return Ey


def Ezt(x, y, z, t):
    """Campo electrico transmitido, componente z."""
    Ez = - t_per * E * math.sin(k * n1 * (x * sxt + y * syt + et) - w
                                  * t) / math.sqrt(2)
    return Ez


def init():
    """Establecer los datos de la grafica a animar."""
    line.set_data([], [])  # gráifca
    line2.set_data([], [])  # gráifca
    line.set_3d_properties([])
    line2.set_3d_properties([])

    return line, line2


"""Condiciones iniciales."""
xi = -4 * math.sin(math.pi / 6)
yi = 4 * math.cos(math.pi / 6)
zi = 0
x1 = [xi + Exi(xi, yi, zi, 0)]
y1 = [yi + Eyi(xi, yi, zi, 0)]
z1 = [zi + Eyi(xi, yi, zi, 0)]
x2 = [0]
y2 = [0]
z2 = [0]
x3 = [xi]
y3 = [yi]
z3 = [0]
x4 = [0]
y4 = [0]
z4 = [0]


def init_cond():
    """Funcion de Condiciones iniciales."""
    global xi, yi, zi, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4
    xi = -4 * math.sin(math.pi / 6)
    yi = 4 * math.cos(math.pi / 6)
    zi = 0
    x1 = [xi + Exi(xi, yi, zi, 0)]
    y1 = [yi + Eyi(xi, yi, zi, 0)]
    z1 = [zi + Eyi(xi, yi, zi, 0)]
    x2 = [0]
    y2 = [0]
    z2 = [0]
    x3 = [xi]
    y3 = [yi]
    z3 = [0]
    x4 = [0]
    y4 = [0]
    z4 = [0]


n_frames = 1000
points = 40


def animate(i):
    """Actualizacion de la animacion."""
    print("{:.2f}% Generando video".format((i+1)/10))

    tt = (i+1)/n_frames

    if(i < n_frames/2):

        if(len(x1) < points):
            x1.append(Exi(x1[-1], y1[-1], z1[-1], tt*n_frames) + (1 - tt)
                      * (-2 * math.sin(math.pi / 6)) + tt
                      * (2 * math.sin(math.pi / 6)))
            y1.append(Eyi(x1[-1], y1[-1], z1[-1], tt*n_frames) + (1 - tt)
                      * (2 * math.cos(math.pi / 6)) + tt
                      * (-2 * math.cos(math.pi / 6)))
            z1.append(Ezi(x1[-1], y1[-1], z1[-1], tt*n_frames))

            x3.append((1 - tt) * (-2 * math.sin(math.pi / 6)) + tt
                      * (2 * math.sin(math.pi / 6)))
            y3.append((1 - tt) * (2 * math.cos(math.pi / 6)) + tt
                      * (-2 * math.cos(math.pi / 6)))
            z3.append(0)

        else:
            x1.remove(x1[0])
            y1.remove(y1[0])
            z1.remove(z1[0])
            x3.remove(x3[0])
            y3.remove(y3[0])
            z3.remove(z3[0])
            x1.append(Exi(x1[-1], y1[-1], z1[-1], tt*n_frames) + (1 - tt)
                      * (-2 * math.sin(math.pi / 6)) + tt
                      * (2 * math.sin(math.pi / 6)))
            y1.append(Eyi(x1[-1], y1[-1], z1[-1], tt*n_frames) + (1 - tt)
                      * (2 * math.cos(math.pi / 6)) + tt
                      * (-2 * math.cos(math.pi / 6)))
            z1.append(Ezi(x1[-1], y1[-1], z1[-1], tt*n_frames))

            x3.append((1 - tt) * (-2 * math.sin(math.pi / 6)) + tt
                      * (2 * math.sin(math.pi / 6)))
            y3.append((1 - tt) * (2 * math.cos(math.pi / 6)) + tt
                      * (-2 * math.cos(math.pi / 6)))
            z3.append(0)

    else:
        if(len(x1) < points):
            x1.append(Ext(x1[-1], y1[-1], z1[-1], tt*n_frames) + (1 - tt)
                      * (-2 * math.sin(theta_t)) + tt
                      * (2 * math.sin(theta_t)))
            y1.append(Eyt(x1[-1], y1[-1], z1[-1], tt*n_frames) + (1 - tt)
                      * (-2 * math.cos(theta_t)) + tt
                      * (2 * math.cos(theta_t)))
            z1.append(Ezt(x1[-1], y1[-1], z1[-1], tt*n_frames))

            x3.append((1 - tt) * (-2 * math.sin(math.pi / 6)) + tt
                      * (2 * math.sin(math.pi / 6)))
            y3.append((1 - tt) * (-2 * math.cos(math.pi / 6)) + tt
                      * (2 * math.cos(math.pi / 6)))
            z3.append(0)
        else:
            x1.remove(x1[0])
            y1.remove(y1[0])
            z1.remove(z1[0])
            x3.remove(x3[0])
            y3.remove(y3[0])
            z3.remove(z3[0])
            x1.append(Ext(x1[-1], y1[-1], z1[-1], tt*n_frames) + (1 - tt)
                      * (-2 * math.sin(theta_t)) + tt
                      * (2 * math.sin(theta_t)))
            y1.append(Eyt(x1[-1], y1[-1], z1[-1], tt*n_frames) + (1 - tt)
                      * (-2 * math.cos(theta_t)) + tt
                      * (2 * math.cos(theta_t)))
            z1.append(Ezt(x1[-1], y1[-1], z1[-1], tt*n_frames))

            x3.append((1 - tt) * (-2 * math.sin(math.pi / 6)) + tt
                      * (2 * math.sin(math.pi / 6)))
            y3.append((1 - tt) * (-2 * math.cos(math.pi / 6)) + tt
                      * (2 * math.cos(math.pi / 6)))
            z3.append(0)

        if(len(x2) < points):
            x2.append(Exr(x2[-1], y2[-1], z2[-1], tt*n_frames) + (1 - tt)
                      * (-2 * math.sin(theta_t)) + tt
                      * (2 * math.sin(theta_t)))
            y2.append(Eyr(x2[-1], y2[-1], z2[-1], tt*n_frames) + (1 - tt)
                      * (2 * math.cos(theta_t)) + tt
                      * (-2 * math.cos(theta_t)))
            z2.append(Ezr(x2[-1], y2[-1], z2[-1], tt*n_frames))

            x4.append((1 - tt) * (-2 * math.sin(theta_t)) + tt
                      * (2 * math.sin(theta_t)))
            y4.append((1 - tt) * (2 * math.cos(theta_t)) + tt
                      * (-2 * math.cos(theta_t)))
            z4.append(0)
        else:
            x2.remove(x2[0])
            y2.remove(y2[0])
            z2.remove(z2[0])
            x4.remove(x4[0])
            y4.remove(y4[0])
            z4.remove(z4[0])
            x2.append(Exr(x2[-1], y2[-1], z2[-1], tt*n_frames) + (1 - tt)
                      * (-2 * math.sin(theta_t)) + tt
                      * (2 * math.sin(theta_t)))
            y2.append(Eyr(x2[-1], y2[-1], z2[-1], tt*n_frames) + (1 - tt)
                      * (2 * math.cos(theta_t)) + tt
                      * (-2 * math.cos(theta_t)))
            z2.append(Ezr(x2[-1], y2[-1], z2[-1], tt*n_frames))

            x4.append((1 - tt) * (-2 * math.sin(theta_t)) + tt
                      * (2 * math.sin(theta_t)))
            y4.append((1 - tt) * (2 * math.cos(theta_t)) + tt
                      * (-2 * math.cos(theta_t)))
            z4.append(0)

    line.set_data(x1, y1)
    line.set_3d_properties(z1)
    line2.set_data(x2, y2)
    line2.set_3d_properties(z2)
    line3.set_data(x3, y3)
    line3.set_3d_properties(z3)
    line4.set_data(x4, y4)
    line4.set_3d_properties(z4)

    return line, line2


"""Animación."""
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=n_frames, interval=20, blit=True)

"""Guardar animaciones."""
init_cond()
ax.view_init(elev=45, azim=10)
anim.save('Polarizacion.mp4', fps=30, extra_args=['-vcodec', 'libx264'])


init_cond()
ax.view_init(elev=60, azim=10)
anim.save('Polarizacion_A.mp4', fps=30, extra_args=['-vcodec', 'libx264'])


init_cond()
ax.view_init(elev=45, azim=-30)
anim.save('Polarizacion_B.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
