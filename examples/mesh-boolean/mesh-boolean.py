from compas.geometry import Box
from compas.geometry import Sphere
from compas.geometry import Cylinder
from compas.geometry import Circle
from compas.geometry import Translation
from compas.datastructures import Mesh
from compas.datastructures import mesh_quads_to_triangles

from compas_viewers.multimeshviewer import MultiMeshViewer
from compas_viewers.multimeshviewer import MeshObject

import compas_libigl as igl

# ==============================================================================
# Input Geometry
# ==============================================================================

R = 1.4

point = [0.0, 0.0, 0.0]
cube = Box.from_width_height_depth(2 * R, 2 * R, 2 * R)
sphere = Sphere(point, R * 1.25)

a = Mesh.from_shape(cube)
b = Mesh.from_shape(sphere, u=30, v=30)

mesh_quads_to_triangles(a)
mesh_quads_to_triangles(b)

A = a.to_vertices_and_faces()
B = b.to_vertices_and_faces()

# ==============================================================================
# Booleans
# ==============================================================================

D = igl.mesh_intersection(A, B)

for n in ([1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]):
    circle = Circle((point, n), 0.6 * R)
    cylinder = Cylinder(circle, 2.1 * R)
    mesh = Mesh.from_shape(cylinder, u=30)
    mesh_quads_to_triangles(mesh)
    C = mesh.to_vertices_and_faces()
    D = igl.mesh_difference(D, C)

mesh = Mesh.from_vertices_and_faces(*D)

# ==============================================================================
# Visualization
# ==============================================================================

# c_union.transform(Translation([7.5, 0, 0]))
# c_intersection.transform(Translation([15, 0, 0]))
# c_diff.transform(Translation([22.5, 0, 0]))

viewer = MultiMeshViewer()

meshes = [
    # MeshObject(a, color='#ff0000'),
    # MeshObject(b, color='#0000ff'),
    # MeshObject(c_union, color='#ff00ff'),
    # MeshObject(c_intersection, color='#00ff00'),
    MeshObject(mesh, color='#00ff00'),
]

viewer.meshes = meshes
viewer.show()
