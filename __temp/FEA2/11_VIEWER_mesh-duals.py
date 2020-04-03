from functools import partial

from compas.datastructures import Mesh
from compas.datastructures import mesh_subdivide
from compas.geometry import Box
from compas.geometry import Translation
from compas.geometry import distance_point_point

from compas_viewers.multimeshviewer import MultiMeshViewer


tri = partial(mesh_subdivide, scheme='tri')
quad = partial(mesh_subdivide, scheme='quad')
ck = partial(mesh_subdivide, scheme='catmullclark')
corner = partial(mesh_subdivide, scheme='corner')
doosabin = partial(mesh_subdivide, scheme='doosabin')


box = Box.from_corner_corner_height((0.0, 0.0, 0.0), (1.0, 1.0, 0.0), 1.0)
mesh = Mesh.from_shape(box)

bbox = mesh.bounding_box_xy()
d = distance_point_point(bbox[0], bbox[1])


k = 2

tri_mesh = tri(mesh, k=k)
quad_mesh = quad(mesh, k=k)
ck_mesh = ck(mesh, k=k)
corner_mesh = corner(mesh, k=k)
doosabin_mesh = doosabin(mesh, k=k)


quad_mesh.transform(Translation([1.5 * d, 0.0, 0.0]))
corner_mesh.transform(Translation([1.5 * 2 * d, 0.0, 0.0]))
ck_mesh.transform(Translation([1.5 * 3 * d, 0.0, 0.0]))
doosabin_mesh.transform(Translation([1.5 * 4 * d, 0.0, 0.0]))


meshes = [tri_mesh, quad_mesh, corner_mesh, ck_mesh, doosabin_mesh]
duals = []
for mesh in meshes:
    dual = mesh.dual()
    duals.append(dual)
    dual.transform(Translation([0.0, 2.0 * d, 0.0]))


viewer = MultiMeshViewer()
viewer.meshes = meshes + duals
viewer.show()
