import numpy as np
from numpy import array, sin, cos, radians, c_
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


A = array([[1.2, 1.4], [0.8, -1.3], [-0.9, -1.1], [-1.2, 1]])

fig, ax = plt.subplots(1, 1)


def animate(i):
    transformationMatrix = array([[cos(radians(i)), -sin(radians(i)), i * 0.05],
                                  [sin(radians(i)), cos(radians(i)), i * 0.05],
                                  [0, 0, 1]])

    extendedMatrix = c_[A, np.ones((A.shape[0], 1))]

    transformedMatrix = extendedMatrix@transformationMatrix.T
    title = 'Przeksztalcenie afiniczne'

    ax.clear()
    ax.fill(transformedMatrix[:, 0], transformedMatrix[:, 1])
    ax.set_title(title)
    ax.set_xlim([-2, 20])
    ax.set_ylim([-2, 20])
    ax.set_aspect('equal', adjustable='box')
    plt.draw()


ani = FuncAnimation(fig, animate, frames=360, interval=16, repeat=True)
plt.show()
