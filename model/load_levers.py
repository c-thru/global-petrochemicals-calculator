"""Functions to read levers.xlsx"""

import re
import numpy as np
import pandas as pd

from dataclasses import dataclass, field


@dataclass
class ModelParam:
    symbol: str
    units: str
    description: str = ""
    default_value = None


@dataclass
class LeverLevel:
    level_id: str
    label: str = ""
    description: str = ""
    params: dict = field(default_factory=dict)


@dataclass
class Lever:
    lever_id: str
    label: str
    description: str = ""
    levels: list[LeverLevel] = field(default_factory=list)


@dataclass
class CalculatorLevers:
    """Logic to calculate a set of parameters from levels of levers."""

    # parameters: list[ModelParam]
    levers: list[Lever]
    params: list[ModelParam]

    def get_params(self, levels: dict[str, str], time_index: int) -> dict[str, float]:
        params = {}
        for lever in self.levers:
            if lever.lever_id in levels:
                level_dict = {level.level_id: level for level in lever.levels}
                level_id = levels[lever.lever_id]
                level_data = level_dict[level_id]
                for k, v in level_data.params.items():
                    params[k] = v
            else:
                print("Not using lever:", lever.lever_id)

        # Pick out data for the specified time period index (0 = 2020, 1 = 2025 etc)
        for k, v in params.items():
            params[k] = v[time_index]

        return collapse_vector_parameters(params)

    def to_dict(self):
        levers = [
            {
                "id": lever.lever_id,
                "label": lever.label,
                "description": lever.description,
                "levels": [
                    {
                        "id": level.level_id,
                        "label": level.label,
                        "description": level.description,
                        "params": level.params,
                    }
                    for level in lever.levels
                ],
            }
            for lever in self.levers
        ]
        params = [
            {
                "symbol": param.symbol,
                "units": param.units,
            }
            for param in self.params
        ]
        return {
            "levers": levers,
            "params": params,
        }


def collapse_vector_parameters(params):
    """Collapse parameter names like `x__0` to a single vector `x`."""
    new_params = {}
    for k, v in params.items():
        if "__" in k:
            base, _, i = k.rpartition("__")
            i = int(i)
            if base not in new_params:
                new_params[base] = []
            if i >= len(new_params[base]):
                new_params[base] += [np.nan] * (i - len(new_params[base]) + 1)
            new_params[base][i] = v
        else:
            assert k not in new_params
            new_params[k] = v
    return new_params


def parse_lever_info(wb) -> list[Lever]:
    sheet = wb.parse("LEVERS", index_col=0)
    levers = []
    for lever_id, row in sheet.iterrows():
        if pd.isnull(lever_id):
            continue  # skip blank rows
        levels = [
            LeverLevel(
                str(i), row[f"level_label_{i}"], row.get(f"level_description_{i}", "")
            )
            for i in range(1, 5)
            if not pd.isnull(row[f"level_label_{i}"])
        ]
        levers.append(
            Lever(
                lever_id,
                row["label"],
                row["description"] if not pd.isnull(row["description"]) else "",
                levels,
            )
        )
    return levers


YEARS = [2020, 2025, 2030, 2035, 2040, 2045, 2050]


def parse_level_data(wb, lever_id: str, levels: list[LeverLevel]):
    sheet = wb.parse(lever_id)
    assert sheet.columns[0] == "level", sheet.columns[0]
    assert sheet.columns[1] == "level_description", sheet.columns[1]
    assert sheet.columns[2] == "param", sheet.columns[2]
    assert (sheet.columns[3 : 3 + len(YEARS)] == YEARS).all()
    sheet["level"] = [str(int(x)) if not pd.isnull(x) else "" for x in sheet["level"]]
    param_data = sheet.iloc[:, : 3 + len(YEARS)] \
                      .set_index(["level", "param"]) \
                      .drop(columns=["level_description"])
    levels_by_id = {level.level_id: level for level in levels}
    for (level_id, param), data in param_data.iterrows():
        if not level_id:
            continue
        try:
            level = levels_by_id[level_id]
        except KeyError:
            print(
                f"Warning: level '{level_id}' is not defined in the LEVERS tab for lever {lever_id}"
            )
            continue
        # Convert array elements to individual parameters
        param = re.sub(r"^(.+)[[](.+)[]]$", r"\1__\2", param)
        level.params[param] = data.values.tolist()


def parse_param_units(wb):
    sheet = wb.parse("PARAM_UNITS")
    assert sheet.columns[0] == "param"
    assert sheet.columns[1] == "units"
    sheet = sheet[~pd.isnull(sheet["param"])]
    sheet["param"] = sheet["param"].astype(str)
    param_data = sheet.set_index(["param"])
    params = []
    for param, data in param_data.iterrows():
        # Convert array elements to individual parameters
        param = re.sub(r"^(.+)[[](.+)[]]$", r"\1__\2", param)
        params.append(ModelParam(param, data["units"]))
        # TODO: check units are as expected
    return params


def read_levers(filename):
    """Read levers.xlsx data from `filename`."""
    levers = []
    with pd.ExcelFile(filename) as levers_wb:
        levers = parse_lever_info(levers_wb)
        for lever in levers:
            parse_level_data(levers_wb, lever.lever_id, lever.levels)
        params = parse_param_units(levers_wb)

    known_params = {param.symbol for param in params}
    for lever in levers:
        for level in lever.levels:
            for k in level.params:
                if k not in known_params:
                    raise ValueError(f"Undeclared parameter {k} in lever {lever.lever_id} level {level.level_id}")

    return CalculatorLevers(levers, params)
