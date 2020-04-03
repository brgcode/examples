from compas.datastructures import Mesh
from compas.datastructures import mesh_transform
from compas.datastructures import mesh_dual
from compas.geometry import Translation
from compas.geometry import Scale
from compas.geometry import length_vector
from compas_viewers.multimeshviewer import MultiMeshViewer

tetra = Mesh.from_polyhedron(4)
hexa = Mesh.from_polyhedron(6)
octa = Mesh.from_polyhedron(8)
dodeca = Mesh.from_polyhedron(12)
icosa = Mesh.from_polyhedron(20)

meshes = [tetra, hexa, octa, dodeca, icosa]
for i, mesh in enumerate(meshes):
    radius = length_vector(mesh.vertex_attributes(mesh.get_any_vertex(), 'xyz'))
    scale = 1 / radius
    T = Translation([2.2 * i, 0.0, 0.0])
    S = Scale([scale, scale, scale])
    X = T * S
    mesh_transform(mesh, X)

duals = []
for mesh in meshes:
    dual = mesh_dual(mesh)
    duals.append(dual)
    mesh_transform(dual, Translation([0.0, 2.2, 0.0]))

viewer = MultiMeshViewer()
viewer.meshes = meshes + duals
viewer.show()
