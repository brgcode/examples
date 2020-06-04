import compas_rhino
from compas.datastructures import Mesh
from compas.geometry import delaunay_from_points
from compas.datastructures import trimesh_remesh
from compas_rhino.artists import MeshArtist

# get the boundary curve
# and divide into segments of a specific length

boundary = compas_rhino.rs.GetObject("Select Boundary Curve", 4)
length   = compas_rhino.rs.GetReal("Select Edge Target Length", 2.0)
points   = compas_rhino.rs.DivideCurve(boundary, compas_rhino.rs.CurveLength(boundary) / length)

# generate a delaunay triangulation
# from the points on the boundary

faces = delaunay_from_points(points, boundary=points)
mesh = Mesh.from_vertices_and_faces(points, faces)

# run the remeshing algorithm
# and draw the result

trimesh_remesh(
    mesh,
    target=length,
    kmax=500,
    allow_boundary_split=True,
    allow_boundary_swap=True)

artist = MeshArtist(mesh)
artist.draw_faces(join_faces=True)
artist.redraw()
