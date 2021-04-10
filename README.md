# COMPAS examples

This repo collects examples of COMPAS usage for solving various problems related to AE(F)C research or praxis.

## Run an example locally

Each example can use any combination of COMPAS and non-COMPAS packages
and defines these dependencies in an environment file
that can be used to create a conda environment in which the example is guaranteed to run.

The environment file can be downloaded from the specific example page in the documentation.
To create an environment with the conda and the file, do

```bash
conda env create -n example -f path/to/example/environment.yml
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

To contribute an example you have to create a repository using the cookiecutter template
and submit the example as a submodule of the COMPAS examples repo through a PR.
This is a two-part procedure.

### Part 1: Making the example

1. Create a virtual environment with your favourite environment manager.
   For example with `conda`.

   ```bash
   conda create -n example-dev python=3.8
   ```

   Install the dependencies required by the example script.
   All dependencies should be available on PyPI or conda-forge!

2. Set up a development repo using the `cookiecutter` template

   ```bash
   conda activate example-dev
   pip install cookiecutter
   cookiecutter gh:compas-dev/tpl-example
   ```

3. Develop the example by writing the example script (`script.py`)
   and by filling in the corresponding ReStructured Text file (`doc.rst`)
   from which the entry in the online documentation will be generated.

4. Once development is finished, update the environment file with the required dependencies.
   The goal is that with this file, users can recreate an environment in which the example is guaranteed to run. The environment file is named by default as `environment.yml`, which means the example will be able to run across-platforms (windows, macos, linux), you can also create separate os-specific environment files and name them as: `environment.windows.yml`, `environment.macos.yml` and `environment.linux.yml`.

   The template file already contains the following

   ```yml
   name: example
   channels:
     - conda-forge
   dependencies:
     - python>=3.6
     - pip>=19.0
   ```

   Add a package.

   ```yml
   dependencies:
     - python>=3.6
     - pip>=19.0
     - compas
   ```

   Add a specific version of a package.

   ```yml
   dependencies:
     - python>=3.6
     - pip>=19.0
     - compas=1.0
   ```

   Add dependencies for specific operating systems using the selector syntax.

   ```yml
   dependencies:
     - python>=3.6
     - pip>=19.0
     - compas
     - python.app  # [osx]
   ```

   Use `pip` instead of `conda` to add a dependency.

   ```yml
   dependencies:
     - python>=3.6
     - pip>=19.0
     - compas
     - python.app  # [osx]
     - pip:
       - pyopengl
   ```

   Note that you can add dependencies directly from a github repo.
   However, this should be avoided.

   ```yml
   dependencies:
     - git
     - python>=3.6
     - pip>=19.0
     - compas
     - python.app  # [osx]
     - pip:
       - pyopengl
       - git+https://github.com/blockresearchgroup/compas_view2.git#egg=compas_view2
   ```

5. Run the example in a test environment created from the environment file.

   ```bash
   conda env create -n example -f environment.yml
   conda activate example
   python script.py
   ```

6. A `test.py` file is required for each example, to validate that everything will work under a non-visualized environment.

### Part 2: Submitting the pull request

1. On github, fork the COMPAS examples repo to your personal account and clone the fork onto your computer.

   ```bash
   git clone https://github.com/<username>/examples
   ```

2. Add a branch to the local clone for your example.

   ```bash
   git checkout -b title-of-my-example
   ```

3. Add the repo containing your example as a submodule of the COMPAS examples repo.

   ```bash
   git submodule add https://github.com/<username>/title-of-my-example
   git commit . -m "Adding title-of-my-example"
   git push
   ```

4. Go to github and submit a PR from your fork to the COMPAS examples repo.
