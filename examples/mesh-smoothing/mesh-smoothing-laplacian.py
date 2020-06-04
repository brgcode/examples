from random import choice
from numpy import array

import compas

from compas.datastructures import Mesh
from compas.datastructures import mesh_laplacian_matrix
from compas.geometry import add_vectors

from compas_plotters import MeshPlotter


mesh = Mesh.from_obj(compas.get('faces.obj'))

key = choice(list(set(mesh.vertices()) - set(mesh.vertices_on_boundary())))

mesh.vertex[key]['x'] += 0.3
mesh.vertex[key]['y'] += 0.3

fixed = list(mesh.vertices_on_boundary())

for k in range(10):
    V = array(mesh.vertices_attributes('xyz'))
    L = mesh_laplacian_matrix(mesh)
    d = L.dot(V)
    V = V + d

    for key, attr in mesh.vertices(True):
        if key in fixed:
            continue
        attr['x'] = V[key][0]
        attr['y'] = V[key][1]
        attr['z'] = V[key][2]

plotter = MeshPlotter(mesh, figsize=(8, 5), tight=True)
plotter.draw_vertices()
plotter.draw_edges()
plotter.draw_faces()

# arrows = []
# for start, vector in zip(V, d):
#     arrows.append({
#         'start' : start,
#         'end'   : add_vectors(start, vector),
#         'color' : '#ff0000'
#     })
# plotter.draw_arrows(arrows)

plotter.show()
