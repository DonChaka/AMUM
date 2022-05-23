import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def f(x1, x2, t): return 0.5 * np.sin(x1 ** 3) + 0.25 * np.sin((x2 - t * 0.05) ** 2)


n = 100
x = np.linspace(-np.pi / 2, np.pi / 2, n)
y = np.linspace(-np.pi, np.pi / 2, n)

XX, YY = np.meshgrid(x, y)
mesh_data = np.c_[XX.ravel(), YY.ravel()]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlim3d([-np.pi / 2, np.pi / 2])
ax.set_ylim3d([-np.pi, np.pi / 2])


def animate(i):
    ax.clear()
    Z = f(mesh_data[:, 0], mesh_data[:, 1], i).reshape(XX.shape)
    ax.plot_surface(XX, YY, Z, cmap='jet')
    plt.draw()


ani = FuncAnimation(fig, animate, frames=1000, interval=1000/60, repeat=True)
plt.show()
plt.show()
