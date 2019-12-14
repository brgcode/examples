import compas
from compas.datastructures import Mesh
from compas.datastructures import mesh_quads_to_triangles
from compas.datastructures import trimesh_collapse_edge
from compas_plotters import MeshPlotter


mesh = Mesh.from_obj(compas.get('faces.obj'))

u = [key for key in mesh.vertices() if mesh.vertex_degree(key) == 2][0]

plotter = MeshPlotter(mesh, figsize=(10, 7))

plotter.defaults['face.facecolor'] = '#eeeeee'
plotter.defaults['face.edgecolor'] = '#cccccc'

plotter.draw_vertices()
plotter.draw_faces()
plotter.draw_edges()

mesh_quads_to_triangles(mesh)

while True:
    nbrs = mesh.vertex_neighbors(u, ordered=True)

    if not nbrs:
        break

    for v in nbrs:
        if mesh.vertex_degree(u):
            if trimesh_collapse_edge(mesh, u, v, t=0.0, allow_boundary=True):
                plotter.update_vertices()
                plotter.update_faces()
                plotter.update_edges()
                plotter.update(0.1)

plotter.show()
