#!/usr/bin/env python3

import sys
import numpy as np
import logging
import re
import pandas as pd
import json
from tqdm import tqdm

from load_levers import read_levers

levers = read_levers("levers.xlsx")


import load_model

model_data = load_model.load_model()
model, recipe_data = load_model.build_model(model_data)
other_results = load_model.define_model(model, recipe_data, levers)

flows_sym = model.to_flows(recipe_data, flow_ids=True)
func = model.lambdify(recipe_data)
func_other = model.lambdify(data=recipe_data, expressions=other_results)


def get_model_output(lever_settings, time_index):
    params = levers.get_params(lever_settings, time_index=time_index)
    # Should disable this for testing, but in some cases it's not a problem because the
    # invalid division-by-zero is in a branch of the piecewise expression which will not be reached.
    with np.errstate(invalid="ignore"):
        result = func_other(params)
    return result


def enumerate_lever_settings(levers):
    if not levers:
        yield {}
        return
    next_lever = levers[0]
    rest_levers = levers[1:]
    levels = (
        [next_lever.levels[0], next_lever.levels[-1]]
        if len(next_lever.levels) > 1
        else [next_lever.levels[0]]
    )
    for level in levels:
        for settings in enumerate_lever_settings(rest_levers):
            yield {**settings, next_lever.lever_id: level.level_id}


def task(lever_settings, time_index):
    return {**lever_settings, **get_model_output(lever_settings, time_index=time_index)}


# from multiprocessing import Pool

if __name__ == "__main__":
    # with Pool(5) as p:
    #     results = list(p.imap_unordered(
    #         task,
    #         enumerate_lever_settings(levers.levers[:3]),
    #         chunksize=20,
    #     ))

    time_index = int(sys.argv[1])
    n_combinations = np.product([min(2, len(lever.levels)) for lever in levers.levers])
    results = [
        task(x, time_index=time_index)
        for x in tqdm(enumerate_lever_settings(levers.levers), total=n_combinations)
    ]

    df = pd.DataFrame(results)
    # df.to_csv(f"enumerated_results_{time_index}.csv", index=False)
    df.set_index(list(df.columns[: len(levers.levers)])).to_parquet(
        f"enumerated_results_{time_index}.parquet"
    )
