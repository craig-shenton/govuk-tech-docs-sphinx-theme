# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'GOV.UK Tech Docs Theme'
copyright = '2023, Craig R Shenton'
author = 'Craig R Shenton'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["govuk_tech_docs_sphinx_theme"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'python'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "govuk_tech_docs_sphinx_theme"

html_theme_options = {
    "organisation": "TEST.GOV.UK",  # replace with your organisation's abbreviation (ideally) or name - long text may not look nice
    "phase": "Building"          # replace with an Agile project phase - see https://www.gov.uk/service-manual/agile-delivery
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_context = {
    "github_url": "https://github.com/craig-shenton/govuk-tech-docs-sphinx-theme", 
    "gitlab_url": None,                  # if using GitLab, set to the URL of your repository as a string
    "conf_py_path": "docs/",             # assuming your Sphinx folder is called `docs`
    "version": "main",                   # assuming `main` is your repository's default branch
    "accessibility": "accessibility.md"  # assuming your accessibility statement is at `docs/accessibility.md`
}