import matplotlib.image
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import AnnotationBbox, OffsetImage

with open('animals.npz', 'rb') as f:
    animals = np.load(f)['animals']

fig, ax = plt.subplots()

f1 = animals[:, 2].astype(float)
f2 = animals[:, 3].astype(float)

points = plt.scatter(f1, f2)

imagebox = OffsetImage(matplotlib.image.imread(animals[0][4]), zoom=0.3)
imagebox.image.axes = ax
image = AnnotationBbox(imagebox, (0, 0),
                       xybox=(120, -80),
                       boxcoords="offset points",
                       )
ax.add_artist(image)
image.set_visible(False)
w, h = fig.get_size_inches() * fig.dpi
images = [matplotlib.image.imread(animals[ind, 4]) for ind in range(len(animals))]


def hover(event):
    if points.contains(event)[0]:
        ind, = points.contains(event)[1]["ind"]
        ws = (event.x > w / 2.) * -1 + (event.x <= w / 2.)
        hs = (event.y > h / 2.) * -1 + (event.y <= h / 2.)
        image.xybox = (ws, hs)
        image.set_visible(True)
        image.xy = (f1[ind], f2[ind])
        imagebox.set_data(images[ind])
    else:
        image.set_visible(False)
    fig.canvas.draw_idle()


fig.canvas.mpl_connect('motion_notify_event', hover)
plt.show()
