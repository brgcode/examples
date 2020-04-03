******************
Boolean Operations
******************

.. figure:: mesh-subd-comparison.png
    :figclass: figure
    :class: figure-img img-fluid

There is currently no support for boolean operations in core COMPAS.
You have to install ``compas_libigl`` to make them available.
Install instructions for ``compas_libigl`` are available
`here <https://github.com/BlockResearchGroup/compas_libigl>`_.

In this example, we will create two boxes and apply various boolean operations
to them: union, intersection, and difference.

We use ``compas.geometry`` to create the box shapes, and ``compas.datastructures``
to convert them triangle meshes.


.. code-block:: python

    from compas.geometry import Box
    from compas.datastructures import Mesh


Input Geometry
==============

A box can be created around the origin with a chosen width, height, and depth.
We will box `a` with `width=5.0`, `height=3.0`, and `depth=1.0`,
and box `b` with `width=1.0`, `height=5.0`, and `depth=3.0`.

.. code-block:: python

    a = Box.from_width_height_depth(5.0, 3.0, 1.0)
    b = Box.from_width_height_depth(1.0, 5.0, 3.0)

.. note::

    Note that width is along the X-axis, height along Z, and depth along Y.

A ``Box`` is a ``Shape`` and any ``Shape`` can be converted to a mesh.

.. code-block:: python

    a = Mesh.from_shape(a)
    b = Mesh.from_shape(b)

The boolean operations only work on triangle meshes.
The meshes resulting from shapes are quads.
Therefore we have to convert the quads to triangles.

.. code-block:: python

    a.quads_to_triangles()
    b.quads_to_triangles()


Operations
==========

For the boolean operations we use ``compas_libigl``.

.. code-block:: python

    import compas_libigl as igl

The wrapper functions use generic representations of meshes with lists of vertices and faces
as input and output.

.. code-block:: python

    A = a.to_vertices_and_faces()
    B = b.to_vertices_and_faces()

.. code-block:: python

    C = igl.mesh_union(A, B)
    c_union = Mesh.from_vertices_and_faces(*C)

    C = igl.mesh_intersection(A, B)
    c_intersection = Mesh.from_vertices_and_faces(*C)

    C = igl.mesh_difference(A, B)
    c_diff = Mesh.from_vertices_and_faces(*C)


Viewer
=======

The result can be visualized using the ``MultiMeshViewer`` of ``compas_viewers``.
The viewers are not part of core COMPAS and have to be installed separately.
Installation instructions are available `here <https://github.com/compas-dev/compas_viewers>`_.

.. code-block:: python

    from compas_viewers.multimeshviewer import MultiMeshViewer

.. note::

    If you can't or don't want to install the viewers, you can skip to
    :ref:`Blender` or :ref:`Rhino` for visualization using CAD software.

This is the final script using the ``MutliMeshViewer`` for visualisation.

.. literalinclude:: mesh-boolean.py
    :language: python


.. _Blender:

Blender
=======

To run this example in Blender, make sure that COMPAS and ``compas_libigl`` are installed for Blender.
For detailed instructions, see `Install COMPAS for Blender <https://compas-dev.github.io/main/gettingstarted/cad/blender.html>`_.

For visualisation we import Blender artists instead of the ``MultiMeshViewer``.

.. code-block:: python

    # from compas_viewers.multimeshviewer import MultiMeshViewer
    # from compas_viewers.multimeshviewer import MeshObject

    from compas_blender.artists import MeshArtist

This is the complete script for Blender.

.. literalinclude:: mesh-boolean-blender.py
    :language: python


.. _Rhino:

Rhino
=====

To run this example in Rhino, make sure that COMPAS is installed for Rhino.
For detailed instructions, see `Install COMPAS for Rhino <https://compas-dev.github.io/main/gettingstarted/cad/rhino.html>`_.

In Rhino, the functionality from ``compas_libigl`` cannot be called directly because the wrappers
for the C++ code of `libigl` are generated using PyBind11. Instead we use Remote Procedure Calls.

The required changes to the original code are minimal, but the RPC server needs to be set up properly.
See the tutorial for more information: `Remote Procedure Calls <https://compas-dev.github.io/main/tutorial/rpc.html>`_.

Instead of importing ``compas_libigl`` directly as before, we create a ``Proxy`` for the library.

.. code-block:: python

    # import compas_libigl as igl
    from compas.rpc import Proxy

    igl = Proxy('compas_libigl')

For visualisation we import Rhino artists instead of the ``MultiMeshViewer``.

.. code-block:: python

    # from compas_viewers.multimeshviewer import MultiMeshViewer
    # from compas_viewers.multimeshviewer import MeshObject

    from compas_rhino.artists import MeshArtist

This is the complete script for Rhino.

.. literalinclude:: mesh-boolean-rhino.py
    :language: python
