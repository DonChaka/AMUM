import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt
import numpy as np


def f(x1, x2): return 0.5 * np.sin(x1 ** 3) + 0.25 * np.sin((x2 + np.pi) ** 2)


n = 100
x = np.linspace(-np.pi / 2, np.pi / 2, n)
y = np.linspace(-np.pi, np.pi / 2, n)

XX, YY = np.meshgrid(x, y)
mesh_data = np.c_[XX.ravel(), YY.ravel()]
Z = f(mesh_data[:, 0], mesh_data[:, 1]).reshape(XX.shape)

fig = plt.figure(figsize=(20, 10))

ax = p3.Axes3D(fig)
ax.set_xlim3d([-np.pi / 2, np.pi / 2])
ax.set_ylim3d([-np.pi, np.pi / 2])

ax.plot_surface(XX, YY, Z, cmap="gist_ncar")

plt.show()


