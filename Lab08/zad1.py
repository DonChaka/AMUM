import matplotlib.pyplot as plt
import numpy as np


def f(x1, x2): return 0.5 * np.sin(x1 ** 3) + 0.25 * np.sin((x2 + np.pi) ** 2)


n = 100
x = np.linspace(-np.pi / 2, np.pi / 2, n)
y = np.linspace(-np.pi, np.pi / 2, n)

XX, YY = np.meshgrid(x, y)
mesh_data = np.c_[XX.ravel(), YY.ravel()]
Z = f(mesh_data[:, 0], mesh_data[:, 1]).reshape(XX.shape)

plt.figure(figsize=(20, 10))
plt.contourf(XX, YY, Z, alpha=1, levels=10)
plt.contour(XX, YY, Z, alpha=1, levels=10, colors='black')
plt.colorbar()
plt.xlim(-np.pi / 2, np.pi / 2)
plt.ylim(-np.pi, np.pi / 2)
plt.show()
