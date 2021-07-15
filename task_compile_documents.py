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
@pytask.mark.depends_on([SRC / "science" / "paper.tex", *_DEPENDENCIES])
@pytask.mark.produces(BLD / "science" / "paper.pdf")
def task_compile_science_report():
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
@pytask.mark.depends_on([SRC / "science" / "cover_letter.tex", *_DEPENDENCIES])
@pytask.mark.produces(BLD / "cover_letter.pdf")
def task_compile_cover_letter():
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


@pytask.mark.depends_on(
    {
        "paper": SRC / "science" / "paper.tex",
        "scicite": SRC / "science" / "scicite.sty",
        "model_graph_top_left": SRC / "figures" / "model-graph-top-left.pdf",
        "model_graph_top_right": SRC / "figures" / "model-graph-top-right.pdf",
        "model_graph_bottom_left": SRC / "figures" / "model-graph-bottom-left.pdf",
        "model_graph_bottom_right": SRC / "figures" / "model-graph-bottom-right.pdf",
        "full_new_known_case": SRC
        / "figures"
        / "results"
        / "figures"
        / "scenario_comparisons"
        / "combined_fit"
        / "full_new_known_case.pdf",
        "stringency2_with_seasonality": SRC
        / "figures"
        / "results"
        / "figures"
        / "data"
        / "stringency2_with_seasonality.pdf",
        "full_share_b117": SRC
        / "figures"
        / "results"
        / "figures"
        / "scenario_comparisons"
        / "combined_fit"
        / "full_share_b117.pdf",
        "full_share_rapid_test_in_last_week_and_vaccinated": SRC
        / "figures"
        / "results"
        / "figures"
        / "scenario_comparisons"
        / "combined_fit"
        / "full_share_rapid_test_in_last_week_and_vaccinated.pdf",
        "full_new_known_case_": SRC
        / "figures"
        / "results"
        / "figures"
        / "scenario_comparisons"
        / "effect_of_channels_on_pessimistic_scenario"
        / "full_new_known_case.pdf",
        "full_newly_infected_": SRC
        / "figures"
        / "results"
        / "figures"
        / "scenario_comparisons"
        / "effect_of_channels_on_pessimistic_scenario"
        / "full_newly_infected.pdf",
        "full_decomposition_channels_area": SRC
        / "figures"
        / "results"
        / "figures"
        / "full_decomposition_channels_area.pdf",
        "full_decomposition_rapid_tests_area": SRC
        / "figures"
        / "results"
        / "figures"
        / "full_decomposition_rapid_tests_area.pdf",
    }
)
@pytask.mark.produces(
    {
        "paper": BLD / "science" / "paper.tex",
        "scicite": BLD / "science" / "scicite.sty",
        "model_graph_top_left": BLD
        / "science"
        / "figures"
        / "model-graph-top-left.pdf",
        "model_graph_top_right": BLD
        / "science"
        / "figures"
        / "model-graph-top-right.pdf",
        "model_graph_bottom_left": BLD
        / "science"
        / "figures"
        / "model-graph-bottom-left.pdf",
        "model_graph_bottom_right": BLD
        / "science"
        / "figures"
        / "model-graph-bottom-right.pdf",
        "full_new_known_case": BLD / "science"
        / "figures"
        / "results"
        / "figures"
        / "scenario_comparisons"
        / "combined_fit"
        / "full_new_known_case.pdf",
        "stringency2_with_seasonality": BLD / "science"
        / "figures"
        / "results"
        / "figures"
        / "data"
        / "stringency2_with_seasonality.pdf",
        "full_share_b117": BLD / "science"
        / "figures"
        / "results"
        / "figures"
        / "scenario_comparisons"
        / "combined_fit"
        / "full_share_b117.pdf",
        "full_share_rapid_test_in_last_week_and_vaccinated": BLD
        / "science"
        / "figures"
        / "results"
        / "figures"
        / "scenario_comparisons"
        / "combined_fit"
        / "full_share_rapid_test_in_last_week_and_vaccinated.pdf",
        "full_new_known_case_": BLD
        / "science"
        / "figures"
        / "results"
        / "figures"
        / "scenario_comparisons"
        / "effect_of_channels_on_pessimistic_scenario"
        / "full_new_known_case.pdf",
        "full_newly_infected_": BLD
        / "science"
        / "figures"
        / "results"
        / "figures"
        / "scenario_comparisons"
        / "effect_of_channels_on_pessimistic_scenario"
        / "full_newly_infected.pdf",
        "full_decomposition_channels_area": BLD
        / "science"
        / "figures"
        / "results"
        / "figures"
        / "full_decomposition_channels_area.pdf",
        "full_decomposition_rapid_tests_area": BLD
        / "science"
        / "figures"
        / "results"
        / "figures"
        / "full_decomposition_rapid_tests_area.pdf",
    }
)
def task_prepare_submission_material(depends_on, produces):
    for name in depends_on:
        if name == "paper":
            text = depends_on[name].read_text()
            # Fix figure paths
            text = text.replace("../figures", "figures")
            produces[name].write_text(text)
        else:
            shutil.copy(depends_on[name], produces[name])
