import compas_rhino

from compas.datastructures import Mesh
from compas.geometry import smooth_area

from compas_rhino.geometry import RhinoMesh
from compas_rhino.geometry import RhinoSurface
from compas_rhino.artists import MeshArtist


# define a callback for updating the conduit
# and for pulling the free vertices back to the surface
# at every iteration

def callback(k, args):
    for index in range(len(vertices)):
        if index in fixed:
            continue
        x, y, z = surf.closest_point(vertices[index])
        vertices[index][0] = x
        vertices[index][1] = y
        vertices[index][2] = z

# make a mesh datastructure from a Rhino mesh object
# and select a target surface

guid = compas_rhino.select_mesh()
rmesh = RhinoMesh.from_guid(guid)
vertices = rmesh.vertices
faces = [face[:-1] for face in rmesh.faces]
mesh = Mesh.from_vertices_and_faces(vertices, faces)

guid = compas_rhino.select_surface()
surf = RhinoSurface.from_guid(guid)

# extract the input for the smoothing algorithm from the mesh
# and identify the boundary as fixed

vertices  = mesh.vertices_attributes('xyz')
faces     = [mesh.face_vertices(fkey) for fkey in mesh.faces()]
adjacency = [mesh.vertex_faces(key, ordered=True) for key in mesh.vertices()]
fixed     = set(mesh.vertices_on_boundary())

# run the smoothing algorithm

smooth_area(
    vertices,
    faces,
    adjacency,
    fixed=fixed,
    kmax=50,
    callback=callback)

# update the mesh

for key, attr in mesh.vertices(True):
    attr['x'] = vertices[key][0]
    attr['y'] = vertices[key][1]
    attr['z'] = vertices[key][2]

# visualize

artist = MeshArtist(mesh, layer='mesh-out')
artist.draw_faces(join_faces=True)
