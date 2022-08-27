"""Sphinx configuration."""
project = "Marvel Snap Simulator"
author = "Jonathan Reyes"
copyright = "2022, Jonathan Reyes"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
