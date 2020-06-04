from random import randint
from math import radians

from compas.geometry import Point
from compas.geometry import Vector
from compas.geometry import Plane
from compas.geometry import Frame
from compas.geometry import Translation
from compas.geometry import Rotation
from compas.geometry import Box
from compas.datastructures import Mesh

from compas_viewers.multimeshviewer import MeshObject
from compas_viewers.multimeshviewer import MultiMeshViewer


def cutting_plane(mesh, ry=10, rz=-50):
    plane = Plane(mesh.centroid(), Vector(1, 0, 0))
    Ry = Rotation.from_axis_and_angle(Vector(0, 1, 0), radians(ry), plane.point)
    Rz = Rotation.from_axis_and_angle(Vector(0, 0, 1), radians(rz), plane.point)
    plane.transform(Rz * Ry)
    return plane


# ==============================================================================
# Input
# ==============================================================================

frame = Frame.worldXY()
box = Box(frame, 10, 3, 5)

mesh = Mesh.from_shape(box)

# ==============================================================================
# Parts
# ==============================================================================

red = []
blue = []

plane = cutting_plane(mesh, ry=0, rz=0)
A, B = mesh.cut(plane)

for _ in range(0, 7):
    plane = cutting_plane(A, ry=-40, rz=0)
    A, b = A.cut(plane)
    red.append(b)
    vector = plane.normal.scaled(0.1)
    T = Translation(vector)
    A.transform(T)
red.append(A)

for _ in range(0, 7):
    plane = cutting_plane(B, ry=40, rz=0)
    a, B = B.cut(plane)
    blue.append(a)
    vector = plane.normal.scaled(-0.1)
    T = Translation(vector)
    B.transform(T)
blue.append(B)

# ==============================================================================
# Visualize
# ==============================================================================

meshes = [MeshObject(mesh, color='#0000ff') for mesh in blue]
meshes += [MeshObject(mesh, color='#ff0000') for mesh in red]

viewer = MultiMeshViewer()
viewer.meshes = meshes
viewer.show()

