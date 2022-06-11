from numpy import array, sin, cos, radians
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.rcParams["figure.figsize"] = (20, 10)

A = array([[1.2, 1.4], [0.8, -1.3], [-0.9, -1.1], [-1.2, 1]])

fig, ax = plt.subplots(1, 3)


def animate(i):
    rotMatrix = array([[cos(radians(i)), -sin(radians(i))], [sin(radians(i)), cos(radians(i))]])
    stretchXmatrix = array([[1 + 0.01*i, 0], [0, 1]])
    leanMatrix = array([[1, 0], [i*0.01, 1]])

    transformedMatrixes = [A@rotMatrix, A@stretchXmatrix, A@leanMatrix]
    titles = ['Obracanie figury', 'Rozciaganie figury', 'Pochylanie figury']

    for axis, matrix, title in zip(ax, transformedMatrixes, titles):
        axis.clear()
        axis.fill(matrix[:, 0], matrix[:, 1])
        axis.set_title(title)
        axis.set_xlim([-5, 5])
        axis.set_ylim([-5, 5])
        axis.set_aspect('equal', adjustable='box')
    plt.draw()


ani = FuncAnimation(fig, animate, frames=360, interval=50, repeat=True)
plt.show()
