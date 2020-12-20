import pytask
from pathlib import Path


ROOT = Path(__file__).parent
BLD = ROOT / "bld"


@pytask.mark.latex
@pytask.mark.depends_on(
    [ROOT / "paper" / "paper.tex"] + list(ROOT.joinpath("paper").rglob("*.tex"))
)
@pytask.mark.produces(BLD / "paper.pdf")
def task_compile_documents():
    pass
