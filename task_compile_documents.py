import pytask
from pathlib import Path


ROOT = Path(__file__).parent
BLD = ROOT / "bld"
DEPENDENCIES = [ROOT / "paper" / "paper.tex", ROOT / "references.bib"]
DEPENDENCIES += list(ROOT.joinpath("paper").rglob("*.tex"))


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
@pytask.mark.depends_on(DEPENDENCIES)
@pytask.mark.produces(BLD / "paper.pdf")
def task_compile_documents():
    pass
