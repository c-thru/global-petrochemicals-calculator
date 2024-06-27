from flowprog import load_from_rdf
from rdflib import Namespace, Graph

rdf_data_path = "../system-definitions/_build/html/output.ttl"
ukf_data_path = "../datasources/ukfires-production-system/output.ttl"
model_def_paths = [
    "model_polymers.ttl",
    "model_fertilisers.ttl",
]

MODEL_NS = Namespace("http://c-thru.org/analyses/calculator/model/")
model_uri = MODEL_NS["Model"]


def load_model():
    print("Loading RDF data...")
    g = Graph(store="Oxigraph")
    g.open("rdf_data_store")
    try:
        g.parse(rdf_data_path, format="ttl")
        for model_def_path in model_def_paths:
            g.parse(model_def_path, format="ttl")

        model_data = load_from_rdf.query_endpoint(g, model_uri)
    finally:
        g.close()
    print(" done")

    return model_data


def build_model(model_data, **kwargs):
    return load_from_rdf.build_model(*model_data, **kwargs)


# def solution_to_flows(flows_sym, values):
#     # all_values = {**recipe_data, **values}
#     # return m.to_flows(all_values)
#     flows = flows_sym.copy()
#     for i, row in flows.iterrows():
#         row["value"] = row["value"].xreplace(values)
#     return flows

from attrs import evolve
import numpy as np


def subs_in_sankey_data(sankey_data, func, params, index=None):
    #     values = np.array(func({str(x): y for x, y in params.items()}))
    #     values[values < 1e-15] = 0
    #     if index is None:
    #         pass  # indexed by integers
    #     else:
    #         values = dict(zip(index, values))
    values = func(params)
    new_links = [
        evolve(
            link,
            data={**link.data, "value": sum(values[f] for f in link.original_flows)},
        )
        for link in sankey_data.links
    ]
    new_links_filtered = [link for link in new_links if link.data["value"] > 1e-6]
    new_sankey_data = evolve(sankey_data, links=new_links_filtered)
    return new_sankey_data


def reset_value_in_sankey_data(sankey_data, value=0):
    """Reset "value" attribute, which may not be JSON serialisable."""
    new_links = [
        evolve(
            link,
            data={**link.data, "value": value},
        )
        for link in sankey_data.links
    ]
    return evolve(sankey_data, links=new_links)


from load_model_polymers import define_polymer_model
from load_model_fertilisers import define_fertiliser_model


def define_model(model, recipe_data, levers):
    """Build the complete model and expressions for other results."""

    # Whitelist the processes with electricity requirements, to avoid
    # needing to define lots of zero-valued parameters for processes which
    # don't use electricity
    processes_with_elec_req = [
        param.symbol[len("ElecReq_") :]
        for param in levers.params
        if param.symbol.startswith("ElecReq_")
    ]
    processes_with_process_emissions = set(
        [
            param.symbol[len("DirProcEmis_CH4_") :]
            for param in levers.params
            if param.symbol.startswith("DirProcEmis_")
        ]
    )

    # Define the model logic
    other_results_polymer = define_polymer_model(
        model, recipe_data, processes_with_elec_req, processes_with_process_emissions
    )

    other_results_fertiliser = define_fertiliser_model(model)

    # Merge other results, add total stats
    other_results = {**other_results_polymer, **other_results_fertiliser}
    other_results["GHG_biomass"] = other_results["GHG_biomass_nonfertiliser"]
    other_results["GHG_production"] = (
        other_results["GHG_production_nonfertiliser"]
        + other_results["GHG_production_fertiliser"]
    )
    other_results["GHG_use"] = other_results["GHG_use_fertiliser"]
    other_results["GHG_eol"] = other_results["GHG_eol_nonfertiliser"]
    other_results["GHG_total"] = (
        other_results["GHG_biomass"]
        + other_results["GHG_production"]
        + other_results["GHG_use"]
        + other_results["GHG_eol"]
    )

    return other_results
