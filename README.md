# COMPAS examples

This repo collects examples of COMPAS usage for solving various problems related to AE(F)C research or praxis.

## Run an example locally

Each example can use any combination of COMPAS and non-COMPAS packages
and defines these dependencies in an environment file
that can be used to create a conda environment in which the example is guaranteed to run.

The environment file can be downloaded from the example page in the documentation.
To create an environment with the conda and the file, do

```bash
conda env create -n example -f path/to/example/env.yml
```

Activate before using

```bash
conda activate example
```

What it means to run the example code, will depend on the example.
Examples written for Rhino will probably have to be run in Rhino,
those for Blender in Blender, and so on.

Standalone examples can be run from an editor or the command line.

If an example is meant for a CAD environment,
make sure to install the example environment in the CAD software.

## Contribute an example

1. Create a virtual environment
2. Set up a development repo using the cookiecutter template
3. Develop the example
4. Configure the environment file
5. Run the example in a test environment created from the environment file
6. Fork the main example repo and clone the fork
7. Add a branch for your example
8. Add your example as a submodule
9. Submit a PR at the main example repo
