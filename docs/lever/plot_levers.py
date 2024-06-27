#!/usr/bin/env python3

from IPython.display import Markdown, display
import pandas as pd
import matplotlib.pyplot as plt

import sys
sys.path.append("../../model")
import load_levers

levers = load_levers.read_levers("../../model/levers.xlsx")
levers_by_id = {lever.lever_id: lever for lever in levers.levers}
param_units = {param.symbol: param.units for param in levers.params}

def plot_recycling_rates(subset=None, param_descriptions=None, **kwargs):
    if param_descriptions is None:
        param_descriptions = {}

    lever = levers_by_id["recycling"]

    # Re-group by parameter
    RR = {
        j: {
            level.level_id: {
                "Chemical": level.params[f"RR_C__{j}"],
                "Mechanical": level.params[f"RR_M__{j}"],
            }
            for level in lever.levels
        }
        for j in range(11)
    }

    items = list(RR.items())
    if subset is None:
        subset = range(len(items))
    for param, data in [items[i] for i in subset]:
        fig, ax = plt.subplots(1, len(lever.levels), figsize=(6.5, 1.2),
                               sharey=True, sharex=True)
        for i, (level_id, values) in enumerate(data.items()):
            df = pd.DataFrame.from_records(
                values,
                index=list(range(2020, 2051, 5)),
            )
            # from IPython.display import display
            df.columns.name = "Level"
            # display(df)
            # title = (
            #     f"{param}\n({param_descriptions[param]})"
            #     if param in param_descriptions
            #     else param
            # )
            # units = param_units.get(param, "")
            df.plot.area(ax=ax[i], stacked=True, title=f"Level {level_id}",
                         color=["#444", "#999"], legend=(i == 0), **kwargs)
        ax[0].legend(loc="upper left") #(0, 1))
        ax[0].set_ylim(0, 1)
        # ax[0].set_yticks([0, 0.25, 0.50, 0.75, 1])
        # ax[0].set_yticklabels(["0%", "25%", "50%", "75%", "100%"])


def plot_lever(lever_id, subset=None, param_descriptions=None, **kwargs):
    if param_descriptions is None:
        param_descriptions = {}

    lever = levers_by_id[lever_id]

    # Re-group by parameter
    param_data = {}
    for level in lever.levels:
        for k, v in level.params.items():
            if k not in param_data:
                param_data[k] = {}
            param_data[k][level.level_id] = v

    items = list(param_data.items())
    if subset is None:
        subset = range(len(items))
    for param, values in [items[i] for i in subset]:
        df = pd.DataFrame.from_records(
            values,
            index=list(range(2020, 2051, 5)),
        )
        df.columns.name = "Level"
        title = (
            f"{param}\n({param_descriptions[param]})"
            if param in param_descriptions
            else param
        )
        units = param_units.get(param, "")
        df.plot(marker="o", xlabel="Year", ylabel=units, title=title, **kwargs)


def describe_lever_levels(lever_id):
    lever = levers_by_id[lever_id]

    level_markdown = "\n - ".join(
        f"_Level {level.level_id}:_ {level.description if not pd.isnull(level.description) else '—'}"
        for level in lever.levels
    )
    display(Markdown(f"""
Lever ID
: {lever.lever_id}

Description
: {lever.description}

Levels
: - {level_markdown}
    """))
