from math import radians

from compas.geometry import Point
from compas.geometry import Vector
from compas.geometry import Plane
from compas.geometry import Frame
from compas.geometry import Translation
from compas.geometry import Rotation
from compas.geometry import Box
from compas.geometry import intersection_segment_plane
from compas.geometry import length_vector
from compas.geometry import subtract_vectors
from compas.geometry import dot_vectors
from compas.datastructures import Mesh

from compas_rhino.artists import MeshArtist

# ==============================================================================
# Mesh geometry
# ==============================================================================

frame = Frame.worldXY()
box = Box(frame, 10, 3, 5)

mesh = Mesh.from_shape(box)

# ==============================================================================
# Move mesh to origin
# ==============================================================================

xmin = min(mesh.vertices_attribute('x'))
ymin = min(mesh.vertices_attribute('y'))
zmin = min(mesh.vertices_attribute('z'))

T = Translation([-xmin, -ymin, -zmin])

mesh.transform(T)

# ==============================================================================
# Cutting plane YZ (rotated over 30 deg)
# ==============================================================================

plane = Plane(mesh.centroid(), Vector(1, 0, 0))

Ry = Rotation.from_axis_and_angle(Vector(0, 1, 0), radians(10), plane.point)
Rz = Rotation.from_axis_and_angle(Vector(0, 0, 1), radians(-50), plane.point)

T = Translation([3, 0, 0])

plane.transform(T * Rz * Ry)

# ==============================================================================
# Compute intersections
# ==============================================================================

intersections = []

for u, v in list(mesh.edges()):
    a = mesh.vertex_attributes(u, 'xyz')
    b = mesh.vertex_attributes(v, 'xyz')
    x = intersection_segment_plane((a, b), plane)
    if not x:
        continue
    L_ax = length_vector(subtract_vectors(x, a))
    L_ab = length_vector(subtract_vectors(b, a))
    t = L_ax / L_ab
    key = mesh.split_edge(u, v, t=t, allow_boundary=True)
    intersections.append(key)

# ==============================================================================
# Split faces
# ==============================================================================

if len(intersections) > 2:
    for fkey in list(mesh.faces()):
        split = [key for key in mesh.face_vertices(fkey) if key in intersections]
        if len(split) == 2:
            u, v = split
            mesh.split_face(fkey, u, v)

# ==============================================================================
# Identify sides
# ==============================================================================

o = plane.point
n = plane.normal

positive_vertices = []
negative_vertices = []

for key in mesh.vertices():
    if key in intersections:
        continue
    a = mesh.vertex_attributes(key, 'xyz')
    oa = subtract_vectors(a, o)
    similarity = dot_vectors(n, oa)
    if similarity > 0.0:
        positive_vertices.append(key)
    elif similarity < 0.0:
        negative_vertices.append(key)

positive_faces = []
for key in positive_vertices:
    positive_faces += mesh.vertex_faces(key)
positive_faces = list(set(positive_faces))

negative_faces = []
for key in negative_vertices:
    negative_faces += mesh.vertex_faces(key)
negative_faces = list(set(negative_faces))

# ==============================================================================
# Mesh on the positive side of the cut plane
# ==============================================================================

vertices = {key: mesh.vertex_coordinates(key) for key in positive_vertices + intersections}
faces = [mesh.face_vertices(fkey) for fkey in positive_faces]

positive = Mesh.from_vertices_and_faces(vertices, faces)
positive.add_face(positive.vertices_on_boundary(True))

# ==============================================================================
# Mesh on the negative side of the cut plane
# ==============================================================================

vertices = {key: mesh.vertex_coordinates(key) for key in negative_vertices + intersections}
faces = [mesh.face_vertices(fkey) for fkey in negative_faces]

negative = Mesh.from_vertices_and_faces(vertices, faces)
negative.add_face(negative.vertices_on_boundary(True))

# ==============================================================================
# Visualize
# ==============================================================================

artist = MeshArtist(positive, layer="MeshCutting::Positive")
artist.clear_layer()
artist.draw_faces(color=(255, 0, 0), join_faces=True)

artist = MeshArtist(negative, layer="MeshCutting::Negative")
artist.clear_layer()
artist.draw_faces(color=(0, 0, 255), join_faces=True)
