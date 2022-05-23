import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation


def f(x1, x2, t): return 0.5 * np.sin(x1 ** 3) + 0.25 * np.sin((x2 - t) ** 2)


n = 100
x = np.linspace(-np.pi / 2, np.pi / 2, n)
y = np.linspace(0, np.pi * 1.5, n)

XX, YY = np.meshgrid(x, y)
mesh_data = np.c_[XX.ravel(), YY.ravel()]

fig, ax = plt.subplots(figsize=(10, 7))

ax.set_xlim(-np.pi / 2, np.pi / 2)
ax.set_ylim(0, np.pi * 1.5)


# uzupełnij (wyświetl obraz za pomocą `contourf` i `contour`).

def animate(i):
    ax.clear()
    Z = f(mesh_data[:, 0], mesh_data[:, 1], i).reshape(XX.shape)
    ax.contourf(XX, YY, Z, alpha=1, levels=10)
    ax.contour(XX, YY, Z, alpha=1, levels=10, colors='black')
    plt.draw()


ani = FuncAnimation(fig, animate, frames=1000, interval=10, repeat=True)
plt.show()
