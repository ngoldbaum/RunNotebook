# Notebook sphinx extensions

## Installation

This package is available on pypi: https://pypi.python.org/pypi/RunNotebook

Install it using pip:

    pip install RunNotebook

Add the extension to your `conf.py`:

```python
extensions = [
    # Import both
    'RunNotebook',
    
    # or import each directive individually
    # 'RunNotebook.notebook_sphinxext',
    # 'RunNotebook.notebookcell_sphinxext',
    # ...
]
```

Optional configuration in your `conf.py`:

```python
# Run notebook configuration

# The template used when exporting from nbconvert
#   full  - Outputs the full HTML document [Default]
#   basic - Outputs a single div (with no additional resources)
run_notebook_export_template = 'basic'  # Default: 'full'

# Display the source links to the generated evaluated files
run_notebook_display_source_links = False  # Default: True
```

Take a look at the `conf.py` file in the example sphinx project to see how to 
integrate with your sphinx build.

## Code snippets in documentation

This packages two useful [Sphinx](http://sphinx-doc.org/) extensions: `notebook`
and `notebook-cell`. These extensions are useful for embedding entire
notebooks or single notebook cells, respectively, inside sphinx documentation.

In the past, it was relatively straightforward to include example scripts inside
of version controlled documentation. For example, one could include code
snippets inside of sphinx documentation using the rst `code-block` directive:

```rst
.. code-block:: python

   for i in range(5):
     print i

```

While this does produce a syntax highlighted python script embedded in a sphinx
document, it does not run the code or provide any facilities for checking whether
the code is correct.

[Jupyter](http://jupyter.org) notebooks offer a powerful environment for
literate programming, with code input, output, and explanatary text embedded
into a single document. It's tempting to include notebooks into documentation
wholesale. However, there are some issues with this approach as
well. Versioning notebooks is difficult - output can change and if the notebook
output contains large amounts of data, the diffs can easily grow quickly,
producing an inconveniently large repository. In addition, updating the 
notebook requires manually re-evaluating all the notebook cells, saving the 
notebook, and making a commit if anything changes.  Versioning evluated 
notebooks also offers no guarantee that the code in the notebook is still 
functional - a real concern with a notebook documenting an evolving codebase
with imperfect test coverage.

## Using Sphinx Extensions to Automate Notebook Running

The extensions included in this package make it easy to include unevaluated
notebooks or short python code snippets inside of documentation. Both extensions
make use of [nbconvert](http://nbconvert.readthedocs.io/) to script the
evaluation of notebooks and to convert the resulting evaluated notebooks into
HTML suitable for embedding in a Sphinx document.

## Dependencies

This extension depends on `Jupyter`.

Note that all `Jupyter` dependencies (even the optional ones) must be
installed. In particular, [pandoc](http://johnmacfarlane.net/pandoc/) and
[node.js](http://nodejs.org/) must be available since these are used by
nbconvert.

## Examples

Suppose I want to include a notebook named `example.ipynb` inline in my
documentation. To do so, add the following to any sphinx ReStructuredText
document:

```rst

.. notebook:: example.ipynb

```

During preprocessing, sphinx will evaluate the notebok, convert it to html, and
embed it into the document in the place where the `notebook` directive was
used.

If a full notebook does not make sense or if you would like to more tightly link
a script to the source of your documentation, you can use `notebook-cell` to
embed a single-cell mini notebook:

```rst

.. notebook-cell::

   for i in range(5):
     print i

```

This will convert the code snippet into a notebook, evaluate the notebook, and
then embed the result in the document. Note that notebook-cell does not
currently accept a user namespace, so all imports necessary for the code to run
must be included in the source.

See the `example` folder in the root of the repository for a full, working 
example using a basic sphinx configuration.

## Known issues

These extensions use a version of the 'full' HTML output from the nbconvert HTML
output. This includes the full notebook CSS. There's some CSS monkeypatching
that happens to reduce the impact of the notebook CSS on the document, which
might conflict with your documentation theme. If it turns out that the
monkeypatching is fragile and there are visual issues in your preferred docs
theme, please let me know by opening a github issue.
