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
    with open(produces, "w") as f:
        f.write(df.to_latex(na_rep=""))
