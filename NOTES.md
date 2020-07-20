# Notes

## Example Template

1. **Title**
2. **Summary**
3. **Requirements**
4. **Base code snippet**
5. **Visualization with viewer**
6. **Rhino and/or GH variant**
7. **Blender variant**

## Wishlist of Examples

### Slicing a Mesh

Compute the intersection polylines between a mesh and a series of planes.
Ideally, the planes are oriented along the tangents of a spatial curve
to illustrate the most generic case possible.

* compas
* compas_cgal

### Cutting data of a (foam) block

Define the cutting polylines for wire-cutting a block out of a blank.
Use the geometry of a 3D block from HiLo.
The block data is defined in a JSON file or as Rhino geometry.
In the latter case, polylines have to be added to identify the components of the block.

* compas

### Equilibrium geometry of a cablenet

Compute the equilibrium shape of a cable net with the force density method.
Materialize the cable net and analyse behaviour under additional loads.
Use the texas shell as example.

* compas

### Ray-Mesh intersections

Shoot rays from a moving source in all directions of a hemi-sphere.
Compute intersections with surrounding structure represented by a mesh.
Move source along planar spline over ground.

* compas
* compas_libigl

### Low-poly mesh modeling

Use a low-poly mesh as control mechansim to model a high-res, smooth subdivision surface.
Potentially demonstrate control over subd patches.
Use a 3D "Swiss Cross" as base geometry?

* compas
* compas_cage?

### Stereotomy of a masonry vault

Use the dual of a form diagram to create a base voussoir layout.
Potentialy optimise interfaces to align perpendicularly with the force flow.
Generate 3D block geometries with planar side cuts.

* compas
* compas_tna?

### Discrete Element Assembly data structure

Use a combination of network and mesh to define the relations
between different elements of a DEA and their individual geometry.

* compas
* compas_assembly

### Skeleton modeling

Use a skeleton to model a smooth high-res mesh surface.
Use a skeleton to model a spatial branching tree and its nodes.
Use mycotree as case study?

* compas
* compas_skeleton

### Pattern design

Design a structural pattern by choosing singularities in a coarse quad-mesh.

* compas
* compas_singular

### FEA of a shell

FEA of a concrete shell.
Use HiLo roof?

* compas
* compas_fea2

### Pointcloud registration

Match point cloud of measured 3d printed vault to digital model.
Visualize collapse sequence using matched 3D model.

* compas

### Surface reconstruction

Convert xyz format to ply.
Downsample data and reduce noise.
Estimate normals.
Use poisson reconstruction.
Cut reconstructed mesh to remove artifacts.
Remesh to create smooth surface reconstruction.
Use scan of HiLo from before winter.

* compas
* compas_cgal
* open3d

### Constructive Solid Geometry

Use CSG to construct volumetric COMPAS letters from primitives and shapes.
Compute booleans using boundary representations provided by GMSH.

* compas
* compas_gmsh
