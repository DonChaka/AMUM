from numpy import array, sin, cos, radians
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

A = array([
    [1, 1, 1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, 1, 1],
    [-1, 1, -1],
    [1, 1, -1],
    [1, -1, -1],
    [-1, -1, -1],
    [-1, -1, 1],
    [-1, 1, 1],
    [1, 1, 1],
    [1, 1, -1],
    [1, -1, -1],
    [1, -1, 1],
    [-1, -1, 1],
    [-1, -1, -1],
    [-1, 1, -1]
])

fig = plt.figure()
ax = fig.add_subplot(projection='3d')


def animate(i):
    transformationMatrix = array([[cos(radians(i)), -sin(radians(i)), 0],
                                  [sin(radians(i)), cos(radians(i)), 0],
                                  [0, 0, 1]])

    transformedMatrix = A @ transformationMatrix
    title = 'Przeksztalcenie obrot 3D'

    ax.cla()
    ax.scatter(transformedMatrix[:, 0], transformedMatrix[:, 1], transformedMatrix[:, 2])
    ax.plot(transformedMatrix[:, 0], transformedMatrix[:, 1], transformedMatrix[:, 2])
    ax.set_xlim3d(-5, 5)
    ax.set_ylim3d(-5, 5)
    ax.set_zlim3d(-5, 5)
    ax.set_title(title)
    plt.draw()


ani = FuncAnimation(fig, animate, frames=360, interval=16, repeat=True)
plt.show()
