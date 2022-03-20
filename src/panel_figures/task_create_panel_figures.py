"""Create single figures from multi-panel figures.

For publications multi-panel figures are usually not allowed since necessary packages
are not supported, etc..

https://texblog.org/2015/10/07/combining-sub-figures-to-a-single-figure-for-submission-to-journal/

"""

import pytask
from pathlib import Path


BLD = Path(__file__).parents[2].joinpath("bld").resolve()
SRC = Path(__file__).parents[1].resolve()


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
@pytask.mark.parametrize(
    "depends_on, produces",
    [
        (
            SRC / "panel_figures" / "model_description.tex",
            BLD / "panel_figures" / "fig-model-description.pdf",
        ),
        (
            SRC / "panel_figures" / "evolution_pandemic.tex",
            BLD / "panel_figures" / "fig-evolution-pandemic.pdf",
        ),
        (
            SRC / "panel_figures" / "2021_scenarios.tex",
            BLD / "panel_figures" / "fig-2021-scenarios.pdf",
        ),
        (
            SRC / "panel_figures" / "school_workplace_scenarios.tex",
            BLD / "panel_figures" / "fig-school-workplace-scenarios.pdf",
        ),
    ],
)
def task_create_panel_figures():
    pass
