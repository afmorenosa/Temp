"""."""
from scipy.special import ellipj
import matplotlib.pyplot as plt
import numpy as np
import math as mt

g = 9.8
l = 10
omega = mt.sqrt(g / l)
k = mt.sin(20*mt.pi/180/2)
t = np.arange(0, 50, 0.01)
x = 2*np.arcsin(k * ellipj(omega*t, k)[0])
h = 0.00001

# for i in range(3):
#     plt.plot(t, 2*np.arcsin(k * ellipj(omega*t, k)[i]))
plt.plot(t, x, label="Nonlinear")

plt.plot(t, np.sin(omega*t)*2*np.arcsin(k), label="Linear")
plt.legend()
plt.grid()
plt.title("Angle")
plt.xlabel(r"$t$")
plt.ylabel(r"$\theta(t)$")
plt.savefig("t_x.pdf")


def D(f, x, h):
    """."""
    return (f(x + h / 2) - f(x - h / 2)) / h


def DR(f, x, h):
    """."""
    res = 4 * D(f, x, h/2) - D(f, x, h)
    return res / 3


def F(x):
    """."""
    return 2*np.arcsin(k * ellipj(omega*x, k)[0])


v = []

for i in range(len(t)):
    v.append(DR(F, t[i], h))

plt.clf()
plt.plot(t, v, label="Nonlinear")
plt.plot(t, omega*np.cos(omega*t)*2*np.arcsin(k), label="Linear")
plt.legend()
plt.grid()
plt.title("Angular velocity")
plt.xlabel(r"$t$")
plt.ylabel(r"$\omega(t)$")
plt.savefig("t_v.pdf")

plt.clf()
plt.plot(x, v, label="Nonlinear")
plt.plot(np.sin(omega*t)*2*np.arcsin(k), omega*np.cos(omega*t)*2*np.arcsin(k),
         label="Linear")
plt.legend()
plt.grid()
plt.title("Phase Space")
plt.xlabel(r"$\theta(t)$")
plt.ylabel(r"$\omega(t)$")
plt.savefig("x_v.pdf")
