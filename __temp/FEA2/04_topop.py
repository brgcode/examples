from matplotlib import pyplot as plt
from compas.numerical import topop_numpy

nelx = 400
nely = 40

plt.figure(figsize=(8, 5))
plt.axis([0, nelx, 0, nely])


def callback(x):
    plt.imshow(1 - x, cmap='gray', origin='lower')
    plt.pause(0.001)


loads = {'200-40': [0, -1]}
supports = {'0-0': [1, 1], '400-0': [0, 1]}

x = topop_numpy(nelx=nelx, nely=nely, loads=loads, supports=supports, volfrac=0.5, callback=callback)

plt.show()
