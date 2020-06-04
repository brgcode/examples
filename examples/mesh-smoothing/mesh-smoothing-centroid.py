from random import choice
from numpy import array

import compas

from compas.datastructures import Mesh
from compas.datastructures import mesh_smooth_centroid
from compas.geometry import add_vectors

from compas_plotters import MeshPlotter


mesh = Mesh.from_obj(compas.get('faces.obj'))

key = choice(list(set(mesh.vertices()) - set(mesh.vertices_on_boundary())))

mesh.vertex[key]['x'] += 0.3
mesh.vertex[key]['y'] += 0.3


mesh_smooth_centroid(mesh, fixed=list(mesh.vertices_on_boundary()))


plotter = MeshPlotter(mesh, figsize=(8, 5), tight=True)

plotter.draw_vertices()
plotter.draw_edges()
plotter.draw_faces()

plotter.show()