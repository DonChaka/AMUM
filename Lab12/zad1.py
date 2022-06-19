from numpy import array
import matplotlib.pyplot as plt

A = array([[1.2, 1.4],
           [0.8, -1.3],
           [-0.9, -1.1],
           [-1.2, 1]])

plt.fill(A[:, 0], A[:, 1])
plt.xlim([-5, 5])
plt.ylim([-5, 5])

plt.show()
