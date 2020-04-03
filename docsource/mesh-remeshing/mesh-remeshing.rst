**************
Mesh Remeshing
**************

.. figure:: mesh-remeshing.png
    :figclass: figure
    :class: figure-img img-fluid


COMPAS includes a simple, pure-Python algorithm for remeshing triangle meshes.
The algorithm splits, collapses and swaps edges of a triangle mesh to balance
the valency (degree) of the mesh vertices, and until the edges reach a
specified target length.


Basic imports
=============

.. code-block:: python

    from compas.datastructures import Mesh
    from compas.datastructures import trimesh_remesh


Make a starting mesh
====================

.. code-block:: python

    vertices = [(0.0, 0.0, 0.0), (10.0, 0.0, 0.0), (6.0, 10.0, 0.0), (0.0, 10.0, 0.0)]
    faces = [[0, 1, 2, 3]]

    mesh = Mesh.from_vertices_and_faces(vertices, faces)


Triangulate
===========

.. code-block:: python

    mesh.insert_vertex(0)


Remesh
======

.. code-block:: python

    trimesh_remesh(
        mesh,
        0.5,
        kmax=200,
        allow_boundary_split=True,
        allow_boundary_swap=True,
        allow_boundary_collapse=True)


Visualize
=========

With a plotter, we can visualize the remeshing process.
To update the plotter, we define a callback function to pass
to the remeshing algorithm.

.. code-block:: python

    def callback(mesh, k, args):
        print(k)
        plotter.update_edges()
        plotter.update()


