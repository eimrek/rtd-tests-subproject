# Configuration file for the Sphinx documentation builder.

import os
import sys

# Add your project's root directory to the sys.path to find your modules
sys.path.insert(0, os.path.abspath('../../'))

# -- Project information

project = 'rtd_tests_sub'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

# Override the default robots.txt
html_extra_path = ['robots.txt']
