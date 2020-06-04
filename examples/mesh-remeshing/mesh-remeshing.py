from compas.datastructures import Mesh
from compas.datastructures import trimesh_remesh

from compas_plotters import MeshPlotter


vertices = [(0.0, 0.0, 0.0), (10.0, 0.0, 0.0), (6.0, 10.0, 0.0), (0.0, 10.0, 0.0)]
faces = [[0, 1, 2, 3]]

mesh = Mesh.from_vertices_and_faces(vertices, faces)
mesh.insert_vertex(0)

plotter = MeshPlotter(mesh, figsize=(8, 5))

def callback(mesh, k, args):
    print(k)
    plotter.update_edges()
    plotter.update()

plotter.draw_edges(width=0.5)

trimesh_remesh(
    mesh,
    0.5,
    kmax=200,
    allow_boundary_split=True,
    allow_boundary_swap=True,
    allow_boundary_collapse=True,
    callback=callback)

plotter.update_edges()
plotter.update(pause=2.0)
plotter.show()
