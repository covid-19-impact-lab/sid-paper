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
@pytask.mark.produces(BLD / "paper-with-appendix.pdf")
def task_compile_documents():
    pass

@pytask.mark.skipif(shutil.which("qpdf") is None, reason="Extraction needs qpdf.")
@pytask.mark.depends_on(BLD / "paper-with-appendix.pdf")
@pytask.mark.produces(ROOT / "paper.pdf")
def task_extract_paper(depends_on, produces):
    subprocess.run(
        [
            "qpdf",
            "--empty",
            "--pages",
            depends_on.as_posix(),
            "1-14",
            "--",
            produces.as_posix(),
        ]
    )


@pytask.mark.skipif(shutil.which("qpdf") is None, reason="Extraction needs qpdf.")
@pytask.mark.depends_on(BLD / "paper-with-appendix.pdf")
@pytask.mark.produces("supplementary-material.pdf")
def task_extract_supplementary_material(depends_on, produces):
    subprocess.run(
        [
            "qpdf",
            "--empty",
            "--pages",
            depends_on.as_posix(),
            "15-77",
            "--",
            produces.as_posix(),
        ]
    )
