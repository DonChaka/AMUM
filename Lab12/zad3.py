import numpy as np
from numpy import array, sin, cos, radians, c_
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rcParams["figure.figsize"] = (20, 10)

A = array([[1.2, 1.4], [0.8, -1.3], [-0.9, -1.1], [-1.2, 1]])

fig = plt.figure()


def animate(i):
    transformationMatrix = array([[cos(radians(i)), -sin(radians(i)), i * 0.05],
                                  [sin(radians(i)), cos(radians(i)), i * 0.05],
                                  [0, 0, 1]])

    extendedMatrix = c_[A, np.ones((A.shape[0], 1))]

    transformedMatrix = extendedMatrix@transformationMatrix
    title = 'Przeksztalcenie afiniczne'

    plt.cla()
    plt.fill(transformedMatrix[:, 0], transformedMatrix[:, 1])
    plt.title(title)
    plt.xlim([0, 20])
    plt.ylim([0, 20])
    # plt.gca.set_aspect('equal', adjustable='box')
    plt.draw()


ani = FuncAnimation(fig, animate, frames=360, interval=16, repeat=True)
plt.show()
