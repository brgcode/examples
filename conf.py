# -*- coding: utf-8 -*-

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

import sys
import os
import m2r2

import sphinx_compas_theme

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))

# patches

current_m2r2_setup = m2r2.setup

def patched_m2r2_setup(app):
    try:
        return current_m2r2_setup(app)
    except (AttributeError):
        app.add_source_suffix(".md", "markdown")
        app.add_source_parser(m2r2.M2RParser)
    return dict(
        version=m2r2.__version__, parallel_read_safe=True, parallel_write_safe=True,
    )

m2r2.setup = patched_m2r2_setup

# -- General configuration ------------------------------------------------

project = 'COMPAS Examples'
copyright = 'Block Research Group - ETH Zurich'
author = 'Tom Van Mele'

release = '0.1.0'
version = '.'.join(release.split('.')[0:2])

master_doc       = 'index'
source_suffix    = ['.rst', ]
templates_path   = ['_templates', ]
exclude_patterns = ['_build', '**.ipynb_checkpoints', '_notebooks', '__temp', '.github', '.vscode']

pygments_style   = 'sphinx'
show_authors     = True
add_module_names = True
language         = None


# -- Extension configuration ------------------------------------------------

extensions = [
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.extlinks",
    "sphinx.ext.githubpages",
    "matplotlib.sphinxext.plot_directive",
    "m2r2",
    "nbsphinx",
]

# autodoc options

# autosummary options

# graph options

# napoleon options

# plot options

plot_template = """
{{ source_code }}

{{ only_html }}

   {% if source_link or (html_show_formats and not multi_image) %}
   (
   {%- if source_link -%}
   `Source code <{{ source_link }}>`__
   {%- endif -%}
   {%- if html_show_formats and not multi_image -%}
     {%- for img in images -%}
       {%- for fmt in img.formats -%}
         {%- if source_link or not loop.first -%}, {% endif -%}
         `{{ fmt }} <{{ dest_dir }}/{{ img.basename }}.{{ fmt }}>`__
       {%- endfor -%}
     {%- endfor -%}
   {%- endif -%}
   )
   {% endif %}

   {% for img in images %}
   {% set has_class = false %}

   .. figure:: {{ build_dir }}/{{ img.basename }}.{{ default_fmt }}
      {% for option in options -%}
      {%- if option.startswith(":class:") -%}
      {%- set has_class = true -%}
      {%- if "img-fluid" not in option -%}
      {%- set option = option + " img-fluid" -%}
      {%- endif -%}
      {%- if "figure-img" not in option -%}
      {%- set option = option + " figure-img" -%}
      {%- endif -%}
      {%- endif -%}
      {{ option }}
      {% endfor %}
      {%- if not has_class -%}
      :class: figure-img img-fluid
      {%- endif %}

      {% if html_show_formats and multi_image -%}
        (
        {%- for fmt in img.formats -%}
        {%- if not loop.first -%}, {% endif -%}
        `{{ fmt }} <{{ dest_dir }}/{{ img.basename }}.{{ fmt }}>`__
        {%- endfor -%}
        )
      {%- endif -%}

      {{ caption }}
   {% endfor %}

{{ only_latex }}

   {% for img in images %}
   {% if "pdf" in img.formats -%}
   .. figure:: {{ build_dir }}/{{ img.basename }}.pdf
      {% for option in options -%}
      {{ option }}
      {% endfor %}

      {{ caption }}
   {% endif -%}
   {% endfor %}

{{ only_texinfo }}

   {% for img in images %}
   .. image:: {{ build_dir }}/{{ img.basename }}.png
      {% for option in options -%}
      {{ option }}
      {% endfor %}

   {% endfor %}

"""

plot_html_show_source_link = False
plot_html_show_formats = False

# intersphinx options

intersphinx_mapping = {
    "python": ("https://docs.python.org/", None),
    "compas": ("https://compas.dev/compas/latest/", None),
}

# linkcode

# extlinks

extlinks = {}

# -- Options for HTML output ----------------------------------------------

html_theme = 'compas'
html_theme_path = sphinx_compas_theme.get_html_theme_path()
html_theme_options = {
    'navbar_active' : 'examples',
}
html_context = {}
html_static_path = []
html_extra_path = []
html_last_updated_fmt = ""
html_copy_source = False
html_show_sourcelink = False
html_permalinks = False
html_add_permalinks = ""
html_experimental_html5_writer = True
html_compact_lists = True
