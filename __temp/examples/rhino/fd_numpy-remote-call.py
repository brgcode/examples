import compas
from compas.datastructures import Mesh
from compas.remote import Proxy
import time

numerical = Proxy('compas.numerical')

mesh = Mesh.from_obj(compas.get('faces.obj'))

mesh.update_default_vertex_attributes({'is_anchor': False, 'px': 0.0, 'py': 0.0, 'pz': 0.0})
mesh.update_default_edge_attributes({'q': 1.0})

for key, attr in mesh.vertices(True):
    attr['is_anchor'] = mesh.vertex_degree(key) == 2
    if key in (18, 35):
        attr['z'] = 5.0

k_i   = mesh.key_index()
xyz   = mesh.get_vertices_attributes(('x', 'y', 'z'))
loads = mesh.get_vertices_attributes(('px', 'py', 'pz'))
q     = mesh.get_edges_attribute('q')
fixed = mesh.vertices_where({'is_anchor': True})
fixed = [k_i[k] for k in fixed]
edges = [(k_i[u], k_i[v]) for u, v in mesh.edges()]

xyz, q, f, l, r = numerical.fd_numpy(xyz, edges, fixed, q, loads)

print(xyz)
