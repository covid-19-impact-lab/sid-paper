import subprocess
import shutil
from pathlib import Path

import pytask


ROOT = Path(__file__).parent
BLD = ROOT / "bld"
SRC = ROOT / "src"
_DEPENDENCIES = [*SRC.rglob("*.tex"), *(BLD / "param_tables").rglob("*.tex")]


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
@pytask.mark.depends_on([SRC / "rev1_reply_comments.tex"])
@pytask.mark.produces(BLD / "rev1_reply_comments.pdf")
def task_compile_reply():
    pass


@pytask.mark.depends_on(BLD / "paper.pdf")
@pytask.mark.produces(ROOT / "paper.pdf")
def task_copy_pdf_to_root(depends_on, produces):
    shutil.copy(depends_on, produces)


@pytask.mark.skipif(shutil.which("qpdf") is None, reason="Extraction needs qpdf.")
@pytask.mark.depends_on(BLD / "paper.pdf")
@pytask.mark.produces(BLD / "supplementary_material.pdf")
def task_extract_supplementary_material(depends_on, produces):
    subprocess.run(
        [
            "qpdf",
            "--empty",
            "--pages",
            depends_on.as_posix(),
            "12-78",
            "--",
            produces.as_posix(),
        ]
    )

