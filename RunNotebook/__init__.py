from . import notebook_sphinxext
from . import notebookcell_sphinxext


def setup(app):
    notebook_sphinxext.setup(app)
    notebookcell_sphinxext.setup(app)
