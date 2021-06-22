import shutil
from pathlib import Path

import pytask


ROOT = Path(__file__).parent
BLD = ROOT / "bld"
SRC = ROOT / "src"
_DEPENDENCIES = SRC.rglob("*.tex")


@pytask.mark.latex(
    [
        "--pdf",
        "--interaction=nonstopmode",
        "--synctex=1",
        "--cd",
        "--shell-escape",
        "-f",
    ]
)
@pytask.mark.depends_on([SRC / "paper.tex", *_DEPENDENCIES])
@pytask.mark.produces(BLD / "paper.pdf")
def task_compile_documents():
    pass


@pytask.mark.depends_on(BLD / "paper.pdf")
@pytask.mark.produces(ROOT / "paper.pdf")
def task_copy_pdf_to_root(depends_on, produces):
    shutil.copy(depends_on, produces)
