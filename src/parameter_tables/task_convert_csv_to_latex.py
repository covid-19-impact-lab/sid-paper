import pytask
import pandas as pd
from pathlib import Path

PARAM_TABLE_PATH = Path(__file__).parent
BLD = PARAM_TABLE_PATH.parent.parent / "bld"
SRC = PARAM_TABLE_PATH / "csv"

PARAMETRIZATION = [(p, BLD / "param_tables" / f"{p.stem}.tex") for p in SRC.iterdir()]


@pytask.mark.parametrize("depends_on, produces", PARAMETRIZATION)
def task_convert_csv_to_tex(depends_on, produces):
    df = pd.read_csv(depends_on)
    df = df.dropna(axis=0, how="all")  # drop empty rows
    if len(df.columns) == 5:
        col_format = r"p{4cm}p{2cm}p{2cm}p{2cm}p{9cm}"
        float_format = "%.0f"
    elif len(df.columns) == 3:
        col_format = r"p{3cm}p{1.5cm}p{9cm}"
        float_format = "%.3f"
    else:
        raise ValueError(f"Unexpected number of columns: {len(df.columns)}")
    with open(produces, "w") as f:
        with pd.option_context("max_colwidth", 10000):
            table = df.to_latex(
                na_rep="",
                escape=False,
                longtable=False,
                index=False,
                column_format=col_format,
                float_format=float_format,
            )
        table = table.replace(r"\begin{tabular}", r"\begin{tabular*}{\textwidth}")
        table = table.replace(r"\end{tabular}", r"\end{tabular*}")
        f.write(table)
