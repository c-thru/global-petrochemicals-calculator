from floweaver import (
    ProcessGroup,
    Waypoint,
    Bundle,
    Partition,
    Elsewhere,
    SankeyDefinition,
)

polymerisation_processes = [
    "PolymerisationOfHDPE",
    "PolymerisationOfLDPE",
    "PolymerisationOfLLDPE",
    "PolymerisationOfPP",
    "PolymerisationOfPolystyrene",
    "PolymerisationOfPVC",
    "PolymerisationOfPET",
    # "PolymerisationOfPolyurethane",
    "PolymerisationOfPUR",
    "PolymerisationOfStyreneButadiene",
    "PolymerisationOfFibrePPA",
    "PolymerisationOfOtherPolymers",
]

polymer_objects = [
    "HDPEPolyethylene",
    "LDPEPolyethylene",
    "LLDPE",
    "PPPolypropylene",
    "PSPolystyrene",
    "PVCPolyvinylChloride",
    "PETPolyethyleneTerephthalatePolyesters",
    "Polyurethane",
    "SyntheticRubbers",
    "FibrePPA",
    "OtherPolymers",
]

polymer_objects_short = [
    "HDPE",
    "LDPE",
    "LLDPE",
    "PP",
    "PS",
    "PVC",
    "PET",
    "PUR",
    "Rubber",
    "FibrePPA",
    "Other",
]

production_processes = [
    "ProductionOfPackagingProducts",
    "ProductionOfTransportationProducts",
    "ProductionOfBuildingsAndConstructionProducts",
    "ProductionOfElectricalAndElectronicProducts",
    "ProductionOfConsumerAndInstitutionalProducts",
    "ProductionOfIndustrialMachinery",
    "ProductionOfTextileProducts",
    "ProductionOfOtherProducts",
]

product_objects = [
    "PackagingProducts",
    "TransportationProducts",
    "BuildingsAndConstructionProducts",
    "ElectricalAndElectronicProducts",
    "ConsumerAndInstitutionalProducts",
    "IndustrialMachinery",
    "TextileProducts",
    "OtherProducts",
]
product_short = [
    "Packaging",
    "Transportation",
    "Buildings / construction",
    "Electrical / electronic",
    "Consumer / institutional",
    "Industrial machinery",
    "Textiles",
    "Other",
]

eol_product_objects = [f"EOL{p}" for p in product_objects]

use_processes = [
    "UseOfPackagingProducts",
    "UseOfTransportationProducts",
    "UseOfBuildingsAndConstructionProducts",
    "UseOfElectricalAndElectronicProducts",
    "UseOfConsumerAndInstitutionalProducts",
    "UseOfIndustrialMachinery",
    "UseOfTextileProducts",
    "UseOfOtherProducts",
]

eol_processes = [p.replace("UseOf", "EOLProcessing") for p in use_processes]

eol_polymer_objects = [f"{polymer}AtEOL" for polymer in polymer_objects]

organic_chemicals = [
    "EthyleneGlycol",
    "VinylChloride",
    "Styrene",
    "AdipicAcid",
    "Hexamethylenediamine",
    "HydrogenCyanide",
    "IsophthalicAcid",
    "AceticAcid",
    # "Diisocyanates",
    "TolueneDiisocyanate",
    "OtherIntermediateOrganicChemicals",
    # "DimethylTerephthalateOrIsophthalicAcid",
    "Cyclohexane",
    "TerephthalicAcidPhthalicAnhydrideDioctylPhthalate",
    # "Formaldehyde",
    # "Aniline",
    # "Adiponitrile",
    "Polyols",
    "PropyleneOxide",
    "EthyleneOxide",
    "Acrylonitrile",
]

organic_chemicals_synthesis1 = [
    "HydrogenCyanideSynthesis",
    "AceticAcidSynthesis",
    "PropyleneOxideSynthesis",
    "EthyleneOxideSynthesis",
    "CyclohexaneSynthesis",
    "OtherOrganicChemicalsSynthesis",
]
organic_chemicals_synthesis2 = [
    "StyreneSynthesis",
    "VinylChlorideSynthesis",
    "IsophthalicAcidSynthesis",
    "TolueneDiisocyanateSynthesis",
    "EthyleneGlycolSynthesis",
    "TerephthalicAcidSynthesis",
    "HexamethylenediamineSynthesisFromButadiene",
    "AdipicAcidSynthesis",
    "AcrylonitrileSynthesis",
    "PolyolsSynthesis",
]
organic_chemicals_synthesis = (
    organic_chemicals_synthesis1 + organic_chemicals_synthesis2
)

steam_cracking = [
    "SteamCrackingOfNaphtha",
    "SteamCrackingOfEthane",
]

ethyl_alcohol_synthesis = [
    "EthylAlcoholSynthesisFromSugarcane",
    "EthylAlcoholSynthesisFromSugarcaneBagasse",
    "EthylAlcoholSynthesisFromMaize",
    "EthylAlcoholSynthesisFromCornStover",
    "EthylAlcoholSynthesisFromWheatStraw",
    "EthylAlcoholSynthesisFromRiceStraw",
]

chemical_recycling = [
    "ChemicalRecyclingOfMixedPolymersAtEOL",
]

primary_chemicals = [
    "Ethylene",
    "Propylene",
    "Butadiene",
    "Butylenes",
    "Ammonia",
]

BTX = [
    "Benzene",
    "Toluene",
    "Xylenes",
]

primary_chemicals_partition = Partition.Simple(
    "material",
    [
        ("Methyl alcohol", ["MethylAlcohol"]),
        ("Natural gas", ["NaturalGas"]),
        ("Hydrogen", ["PureHydrogen"]),
        "Ethylene",
        "Propylene",
        "Butadiene",
        "Butylenes",
        "Benzene",
        "Toluene",
        "Xylenes",
        "Ammonia",
    ],
)

inorganic_chemicals = [
    "SodiumHydroxide",
    "NitricAcid",
    "InorganicAcids",
    "PureOxygen",
    "Chlorine",
    "OtherIndustrialGases",
    "OtherInorganicPrimaryChemicals",
    "Water",
]

inorganic_chemicals_production = [
    "SodiumChlorideElectrolysisForChlorine",
    "ProducingNitricAcid",
    "MakingInorganicAcids",
    "AirSeparation",
    "MakingOtherInorganicPrimaryChemicals",
]

parafins = [
    "Ethane",
    "Propane",
    "Butane",
    "Naphtha",
]

syngas_production = [
    "NaturalGasSteamMethaneReformingToSyngas",
    "CoalGasificationToSyngas",
    "SugarCaneBagasseGasificationToSyngas",
    "CornStoverGasificationToSyngas",
    "WheatStrawGasificationToSyngas",
    "RiceStrawGasificationToSyngas",
]

pyrolysis_gasoline = [
    "PyrolysisGasoline",
]

natural_gas = [
    "NaturalGas",
]

natural_gas_extraction = [
    "NaturalGasExtraction",
]

mining_products = [
    "ChemicalAndFertiliserMinerals",
    "Salt",
]

mining = [
    "ChemFertMinMining",
    "SaltMining",
]

final_treatment = ["Landfilling", "Incineration", "Mismanagement"]

flow_partition = Partition.Simple(
    "material",
    [
        (
            "Biomass",
            [
                "SugarCane",
                "SugarCaneBagasse",
                "CornStover",
                "WheatStraw",
                "RiceStraw",
                "Maize",
            ],
        ),
        ("Fossil feedstocks", parafins + ["NaturalGas", "Coal"]),
        ("Syngas / methyl alcohol", ["Syngas", "MethylAlcohol"]),
        ("Ethyl alcohol", ["EthylAlcohol"]),
        "Ethylene",
        "Propylene",
        ("BTX", ["Benzene", "Toluene", "Xylenes"]),
        (
            "Organic chemicals",
            organic_chemicals + ["Butadiene", "Butylenes", "PyrolysisGasoline"],
        ),
        ("Inorganic chemicals", ["Ammonia"]),
        (
            "Other",
            [
                "Waste",
                "WasteOtherChemicals",
                "Nitrogen",
                "OtherIndustrialGases",
                "Water",
                "MiscRefineryProducts",
                "PureOxygen",
                "OtherInorganicPrimaryChemicals",
            ],
        ),
        (
            "Polyethylenes",
            [
                "HDPEPolyethylene",
                "LDPEPolyethylene",
                "LLDPE",
            ],
        ),
        (
            "Polypropylene",
            [
                "PPPolypropylene",
            ],
        ),
        (
            "Other polymers",
            [
                "PSPolystyrene",
                "PVCPolyvinylChloride",
                "PETPolyethyleneTerephthalatePolyesters",
                "Polyurethane",
                "SyntheticRubbers",
                "FibrePPA",
                "OtherPolymers",
            ],
        ),
        ("Products", product_objects + eol_product_objects),
    ],
)


colours = {
    "1": {"50": "#d7ccfe", "100": "#a689f1", "200": "#9c59d3", "Origin": "#6929c4"},
    "2": {"50": "#bbdcf6", "100": "#87c1f4", "200": "#58aaef", "Origin": "#1792e7"},
    "3": {"50": "#86d8d7", "100": "#58b1b0", "200": "#1b8f8e", "Origin": "#005d5d"},
    "4": {"50": "#feacc3", "100": "#ea7098", "200": "#cb3b73", "Origin": "#9f1853"},
    "5": {"50": "#fdc9c6", "100": "#f99e9a", "200": "#f77171", "Origin": "#fa4d56"},
    "6": {"50": "#a5f0b0", "100": "#7ee490", "200": "#5acd73", "Origin": "#198038"},
    "7": {"50": "#a5cafb", "100": "#6e93ed", "200": "#5273dd", "Origin": "#002d9c"},
    "8": {"50": "#ead5ab", "100": "#dbb76a", "200": "#c29a3b", "Origin": "#b28600"},
    "9": {"50": "#e1bfaf", "100": "#c89278", "200": "#b06845", "Origin": "#8a3800"},
}

palette = {
    "Biomass": colours["6"]["200"],
    "Fossil feedstocks": colours["8"]["200"],
    # Need to adjust to show biomass inputs separately
    "Syngas / methyl alcohol": colours["3"]["100"],
    "Ethyl alcohol": colours["3"]["200"],
    "Ethylene": colours["1"]["200"],
    "Propylene": colours["1"]["100"],
    "BTX": colours["4"]["200"],
    "Organic chemicals": colours["4"]["100"],
    "Inorganic chemicals": colours["5"]["100"],
    "Polyethylenes": colours["7"]["200"],
    "Polypropylene": colours["7"]["100"],
    "Other polymers": colours["7"]["50"],
    "Products": colours["2"]["200"],
    "Other": "#AAAAAA",
    "Waste": colours["9"]["50"],
}


def define_overall_sdd():
    """High-level diagram that includes everything."""

    nodes = {
        "Feedstocks": Waypoint(
            Partition.Simple(
                "source",
                [
                    (
                        "Biomass",
                        [
                            "SugarCane",
                            "SugarCaneBagasse",
                            "CornStover",
                            "WheatStraw",
                            "RiceStraw",
                            "Maize",
                            "SugarCaneBagasseGasificationToSyngas",
                            "CornStoverGasificationToSyngas",
                            "WheatStrawGasificationToSyngas",
                            "RiceStrawGasificationToSyngas",
                            "EthylAlcoholSynthesisFromCornStover",
                            "EthylAlcoholSynthesisFromMaize",
                            "EthylAlcoholSynthesisFromRiceStraw",
                            "EthylAlcoholSynthesisFromSugarcane",
                            "EthylAlcoholSynthesisFromSugarcaneBagasse",
                            "EthylAlcoholSynthesisFromWheatStraw",
                        ],
                    ),
                    "CrudeOil",
                    (
                        "Natural gas",
                        [
                            "NaturalGas",  # use downstream
                            "NaturalGasSteamMethaneReformingToSyngas",
                            "NaturalGasSteamMethaneReformingToHydrogen",
                            "NaturalGasSteamMethaneReformingWithCCSToHydrogen",
                        ],
                    ),
                    ("Coal", ["CoalGasificationToSyngas"]),
                    ("Water", ["WaterElectrolysisForHydrogen"]),
                    ("CO2", ["CapturedCarbonDioxide"]),
                    ("H2", [
                        "CarbonDioxideHydrogenationToMethylAlcohol",
                        "PureHydrogen",
                    ]),
                    (
                        "Oil refining",
                        [
                            "OilRefiningEthane",
                            "OilRefiningNaphtha",
                            "OilRefiningPropane",
                            "OilRefiningButane",
                        ],
                    ),
                ],
            )
        ),
        # Outputs to elsewhere
        "OtherOutputs": Waypoint(title="Other outputs"),
        # Group these together to save space, since almost all of the syngas becomes
        # methyl alcohol
        "SyngasMethylAlcohol": ProcessGroup(
            ["Syngas", "MethylAlcoholSynthesis", "MethylAlcohol"],
            title="Syngas / methyl alcohol",
        ),
        # "CarbonDioxideHydrogenationToMethylAlcohol": ProcessGroup(
        #     ["CarbonDioxideHydrogenationToMethylAlcohol"], title="CO2 hydrogenation"
        # ),
        "EthylAlcohol": ProcessGroup(["EthylAlcohol"], title="Ethyl alcohol"),
        # Main processes
        "Paraffins": ProcessGroup(
            ["Ethane", "Propane", "Butane", "Naphtha"],
            # Partition.Simple("process", ["Ethane", "Naphtha", "Propane", "Butane"]),
            title="Paraffins",
        ),
        "DehydrationOfEthylAlcohol": ProcessGroup(
            ["DehydrationOfEthylAlcohol"], title="Dehydration"
        ),
        "PrimaryChemicalsSynthesis": ProcessGroup(
            steam_cracking
            + ["FluidCatalyticCrackingOfGasOil"]
            + [
                "DehydrogenationOfButaneForButadiene",
                "DehydrogenationOfPropane",
            ]
            + [
                "DistillationOfPyrolysisGasolineForBTX",
                "DistillationOfButylenesForButadiene",
            ]
            + pyrolysis_gasoline
            + [
                "CatalyticReformingOfNaphthaForXylenes",
                "CatalyticReformingOfNaphthaForToluene",
                "DisproportionationOfTolueneForXylenes",
                "DealkylationOfTolueneForBenzene",
            ],
            title="from paraffins",
        ),
        "MTX": ProcessGroup(
            [
                "MethylAlcoholToOlefins",
                "MethylAlcoholToPropylene",
                "MethylAlcoholToAromatics",
            ],
            title="MTX",
        ),
        "AmmoniaProduction": ProcessGroup(
            ["SyngasToAmmoniaProduction"], title="Ammonia production"
        ),
        "PrimaryChemicals": ProcessGroup(
            primary_chemicals + BTX,
            # primary_chemicals_partition,
        ),
        # "BTX": ProcessGroup(
        #     BTX,
        #     primary_chemicals_partition,
        #     title="BTX",
        # ),
        # These are just to improve the layout of the diagram
        "wpt_OtherInputs1": Waypoint(title="Other inputs"),
        "wpt_OtherInputs2": Waypoint(title=""),
        "wpt_OtherInputs3": Waypoint(title=""),
        "wpt_OtherInputs4": Waypoint(title=""),
        "wpt_OtherInputs5": Waypoint(title=""),
        "wpt_OtherInputs6": Waypoint(title=""),
        "wpt_OtherInputs7": Waypoint(title=""),
        # Production processes
        "OtherDemand": Waypoint(title="Other demand"),
        "OrganicChemicals": ProcessGroup(
            organic_chemicals_synthesis + organic_chemicals, title="Organic chemicals"
        ),
        "Polymerisation": ProcessGroup(
            polymerisation_processes,
            title="Polymerisation",
        ),
        # Use phase (including the first steps of end-of-life processing, so
        # polymers rather than just products emerge)
        "StockInUse": ProcessGroup(
            polymer_objects
            + production_processes
            + product_objects
            + use_processes
            + eol_product_objects
            + eol_processes
            + [f"{polymer}AtEOL" for polymer in polymer_objects]
            + [f"Mixing{polymer}AtEOL" for polymer in polymer_objects]
            + ["MixedPolymersAtEOL"]
        ),
        # End of life processing
        "ChemicalRecycling": ProcessGroup(chemical_recycling),
        "MechanicalRecycling": ProcessGroup(
            [f"MechanicalRecyclingOf{polymer}AtEOL" for polymer in polymer_objects]
        ),
        "FinalTreatment": ProcessGroup(final_treatment),
        # Waypoints
        "wpt3": Waypoint(title="", direction="L"),
        "wpt4": Waypoint(title="", direction="L"),
        "wpt_OtherOutputs": Waypoint(title=""),
        "wpt_OtherOutputs2": Waypoint(title=""),
        "wpt_OtherOutputs3": Waypoint(title=""),
        "wpt_ChemicalRecycling1": Waypoint(title="", direction="L"),
        "wpt_ChemicalRecycling2": Waypoint(title="", direction="L"),
        "wpt_ChemicalRecycling3": Waypoint(title="", direction="L"),
        "wpt_ChemicalRecycling4": Waypoint(title="", direction="L"),
        "wpt_ChemicalRecycling5": Waypoint(title="", direction="L"),
        "wpt_ChemicalRecycling6": Waypoint(title="", direction="L"),
        "wpt_ChemicalRecycling7": Waypoint(title="", direction="L"),
        "wpt_primary_loop1": Waypoint(title="", direction="L"),
        "wpt_primary_loop2": Waypoint(title="", direction="L"),
        "wpt_Bypass1": Waypoint(title=""),
        "wpt_Bypass2": Waypoint(title=""),
        "wpt_Bypass3": Waypoint(title=""),
    }
    bundles = [
        Bundle(Elsewhere, "MTX", waypoints=["wpt_OtherInputs1", "wpt_OtherInputs2"]),
        # Bundle(
        #     Elsewhere,
        #     "CarbonDioxideHydrogenationToMethylAlcohol",
        #     waypoints=["wpt_OtherInputs1", "wpt_OtherInputs2"],
        # ),
        Bundle(
            Elsewhere,
            "Paraffins",
            flow_selection='source in ["OilRefiningEthane", "OilRefiningNaphtha", "OilRefiningPropane", "OilRefiningButane"]',
            waypoints=["Feedstocks"],
        ),
        Bundle(
            "ChemicalRecycling",
            "Paraffins",
            waypoints=[f"wpt_ChemicalRecycling{i}" for i in range(1, 8)],
        ),
        Bundle(
            "AmmoniaProduction",
            Elsewhere,
            waypoints=[
                "wpt_OtherOutputs",
                "wpt_OtherOutputs2",
                "wpt_OtherOutputs3",
                "OtherOutputs",
            ],
        ),
        Bundle(
            Elsewhere,
            "SyngasMethylAlcohol",
            waypoints=["wpt_OtherInputs1"],
            flow_selection='material == "OtherInorganicPrimaryChemicals"',
        ),
        Bundle("SyngasMethylAlcohol", "AmmoniaProduction"),
        Bundle("SyngasMethylAlcohol", "MTX"),
        Bundle("EthylAlcohol", "DehydrationOfEthylAlcohol"),
        Bundle("Paraffins", "PrimaryChemicalsSynthesis"),
        Bundle("Paraffins", "AmmoniaProduction"),
        # Bundle("SyngasProduction", "Syngas"),
        Bundle(
            Elsewhere,
            "SyngasMethylAlcohol",
            flow_selection=f"material == ['Syngas', 'MethylAlcohol']",
            waypoints=["Feedstocks"],
        ),
        Bundle(
            Elsewhere,
            "EthylAlcohol",
            waypoints=["Feedstocks"],
        ),
        Bundle(
            Elsewhere,
            "PrimaryChemicalsSynthesis",
            waypoints=["Feedstocks", "wpt_Bypass1"],
            flow_selection='material in ["PureHydrogen"]',
        ),
        # Bundle(
        #     Elsewhere, "OrganicChemicals", waypoints=["wpt_Bypass2", "wpt_Bypass3"],
        # ),
        # Bundle("BTX", "PrimaryChemicalsSynthesis"),
        Bundle(
            "DehydrationOfEthylAlcohol",
            Elsewhere,
            waypoints=[
                "wpt_OtherOutputs",
                "wpt_OtherOutputs2",
                "wpt_OtherOutputs3",
                "OtherOutputs",
            ],
            flow_selection="material in ['NaturalGas']",
        ),
        Bundle(
            "MTX",
            Elsewhere,
            waypoints=[
                "wpt_OtherOutputs",
                "wpt_OtherOutputs2",
                "wpt_OtherOutputs3",
                "OtherOutputs",
            ],
            flow_selection="material in ['NaturalGas', 'MiscRefineryProducts', 'OtherIndustrialGases', 'WasteOtherChemicals']",
        ),
        Bundle(
            "MTX",
            "Paraffins",
            waypoints=["wpt_ChemicalRecycling6", "wpt_ChemicalRecycling7"],
        ),
        Bundle(
            "PrimaryChemicalsSynthesis",
            Elsewhere,
            waypoints=[
                "wpt_OtherOutputs",
                "wpt_OtherOutputs2",
                "wpt_OtherOutputs3",
                "OtherOutputs",
            ],
            flow_selection="material in ['MiscRefineryProducts', 'NaturalGas', 'OtherIndustrialGases', 'WasteOtherChemicals']",
        ),
        Bundle("DehydrationOfEthylAlcohol", "PrimaryChemicals"),
        Bundle("MTX", "PrimaryChemicals"),
        Bundle("PrimaryChemicalsSynthesis", "PrimaryChemicals"),
        Bundle(
            "PrimaryChemicals",
            "PrimaryChemicalsSynthesis",
            waypoints=["wpt_primary_loop1", "wpt_primary_loop2"],
        ),  # loop
        Bundle("AmmoniaProduction", "PrimaryChemicals"),
        # Other demand
        Bundle(
            "PrimaryChemicals",
            Elsewhere,
            waypoints=["OtherDemand"],
            flow_selection='target in ["OtherConsumptionOfBenzene", "OtherConsumptionOfToluene", "OtherConsumptionOfXylenes", "OtherConsumptionOfMethylAlcohol", "EthylAlcoholSynthesisFromCornStover", "EthylAlcoholSynthesisFromMaize", "ProducingNitricAcid"]',
        ),
        Bundle(
            "SyngasMethylAlcohol",
            Elsewhere,
            waypoints=["OtherDemand"],
            flow_selection='material in ["MethylAlcohol"]',
        ),
        # Inputs
        Bundle(
            Elsewhere,
            "OrganicChemicals",
            waypoints=[f"wpt_OtherInputs{i}" for i in range(1, 5)],
            flow_selection='material in ["PureOxygen", "OtherInorganicPrimaryChemicals", "InorganicAcids", "Chlorine", "NitricAcid", "Water", "OtherIndustrialGases"]',
        ),
        Bundle(
            Elsewhere,
            "Polymerisation",
            waypoints=[f"wpt_OtherInputs{i}" for i in range(1, 6)],
            flow_selection='material in ["PureOxygen", "OtherInorganicPrimaryChemicals", "InorganicAcids", "Chlorine", "NitricAcid", "Water"]',
        ),
        Bundle(
            Elsewhere,
            "OrganicChemicals",
            waypoints=["Feedstocks", "wpt_Bypass1", "wpt_Bypass2", "wpt_Bypass3"],
            flow_selection='material in ["NaturalGas", "PureHydrogen"]',
        ),
        Bundle(
            "SyngasMethylAlcohol",
            "OrganicChemicals",
            waypoints=["wpt_Bypass2", "wpt_Bypass3"],
        ),
        Bundle(
            "PrimaryChemicals",
            "OrganicChemicals",
        ),
        Bundle(
            "OrganicChemicals",
            Elsewhere,
            waypoints=["wpt_OtherOutputs3", "OtherOutputs"],
            flow_selection='material in ["Air", "InorganicAcids", "WasteOtherChemicals", "OtherIndustrialGases", "Water"]',
        ),
        Bundle(
            "Polymerisation",
            Elsewhere,
            waypoints=["OtherOutputs"],
            flow_selection='material in ["WasteOtherChemicals", "Water"]',
        ),
        Bundle("PrimaryChemicals", "Polymerisation"),
        # Bundle("OrganicChemicalsSynthesis", "OrganicChemicals"),
        Bundle("OrganicChemicals", "Polymerisation"),
        Bundle("Polymerisation", "StockInUse"),
        Bundle("StockInUse", "FinalTreatment"),
        Bundle("StockInUse", "ChemicalRecycling"),
        Bundle("StockInUse", "MechanicalRecycling"),
        Bundle(
            "MechanicalRecycling",
            "StockInUse",
            waypoints=["wpt4", "wpt3"],
        ),
        Bundle(
            Elsewhere,
            "MechanicalRecycling",
            waypoints=[f"wpt_OtherInputs{i}" for i in range(1, 8)],
        ),
        Bundle(
            Elsewhere,
            "ChemicalRecycling",
            waypoints=[f"wpt_OtherInputs{i}" for i in range(1, 8)],
        ),
    ]
    order = [
        [
            ["wpt_OtherInputs1"],
            [],
            ["Feedstocks"],
            [],
        ],
        [
            ["wpt_OtherInputs2"],
            ["wpt_Bypass1"],
            [
                "EthylAlcohol",
                "SyngasMethylAlcohol",
                "Paraffins",
            ],
            [],
            ["wpt_ChemicalRecycling7"],
        ],
        [
            ["wpt_OtherInputs3"],
            ["wpt_Bypass2"],
            [
                "DehydrationOfEthylAlcohol",
                "MTX",
                "AmmoniaProduction",
                "PrimaryChemicalsSynthesis",
            ],
            ["wpt_primary_loop2"],
            ["wpt_ChemicalRecycling6"],
        ],
        [
            ["wpt_OtherInputs4"],
            ["wpt_Bypass3"],
            ["PrimaryChemicals"],
            ["wpt_primary_loop1"],
            ["wpt_ChemicalRecycling5"],
            ["wpt_OtherOutputs"],
        ],
        [
            ["wpt_OtherInputs5"],
            [],
            ["OrganicChemicals", "OtherDemand"],
            [],
            ["wpt_ChemicalRecycling4"],
            ["wpt_OtherOutputs2"],
            [],
        ],
        [
            ["wpt_OtherInputs6"],
            [],
            ["Polymerisation"],
            [],
            ["wpt_ChemicalRecycling3"],
            ["wpt_OtherOutputs3"],
            [],
        ],
        [
            ["wpt_OtherInputs7"],
            [],
            ["StockInUse"],
            ["wpt3"],
            ["wpt_ChemicalRecycling2"],
            ["OtherOutputs"],
        ],
        [
            [],
            [],
            ["FinalTreatment", "ChemicalRecycling", "MechanicalRecycling"],
            ["wpt4"],
            ["wpt_ChemicalRecycling1"],
            [],
        ],
    ]
    sdd = SankeyDefinition(nodes, bundles, order, flow_partition=flow_partition)

    return sdd


def define_lifecycle_sdd():
    nodes = {
        # Inputs
        "PrimaryChemicals": Waypoint(primary_chemicals_partition),
        "OtherInputs": Waypoint(title="Other inputs"),
        # Production processes
        "OrganicChemicals": ProcessGroup(
            organic_chemicals_synthesis + organic_chemicals, title="Organic chemicals"
        ),
        "Polymerisation": ProcessGroup(
            polymerisation_processes,
            Partition.Simple(
                "process",
                [(" " * (i + 1), [v]) for i, v in enumerate(polymerisation_processes)],
            ),
            title="Polymerisation",
        ),
        "Polymers": ProcessGroup(
            polymer_objects,
            Partition.Simple(
                "process",
                [
                    (short, [full])
                    for short, full in zip(polymer_objects_short, polymer_objects)
                ],
            ),
        ),
        "Production": ProcessGroup(
            production_processes,
            Partition.Simple(
                "process",
                [
                    (short, [full])
                    for short, full in zip(product_short, production_processes)
                ],
            ),
        ),
        # Use phase (including the first steps of end-of-life processing, so
        # polymers rather than just products emerge)
        "StockInUse": ProcessGroup(
            product_objects
            + use_processes
            + eol_product_objects
            + eol_processes
            + [f"{polymer}AtEOL" for polymer in polymer_objects]
            + [f"Mixing{polymer}AtEOL" for polymer in polymer_objects]
            + ["MixedPolymersAtEOL"]
        ),
        # End of life processing
        "ChemicalRecycling": ProcessGroup(chemical_recycling),
        "MechanicalRecycling": ProcessGroup(
            [f"MechanicalRecyclingOf{polymer}AtEOL" for polymer in polymer_objects]
        ),
        "FinalTreatment": ProcessGroup(final_treatment),
        # Waypoints
        "wpt1": Waypoint(title="", direction="L"),
        "wpt2": Waypoint(title="", direction="L"),
        "wpt3": Waypoint(title="", direction="L"),
        "wpt4": Waypoint(title="", direction="L"),
        "wpt5": Waypoint(title=""),
        "OtherOutputs": Waypoint(title="Other outputs"),
        "PrimaryWpt": Waypoint(
            Partition.Simple(
                "material",
                [
                    (" ", ["Ethylene"]),
                    ("  ", ["Propylene"]),
                    ("   ", ["Butadiene", "Butylenes", "BTX"]),
                ],
            )
        ),
        "Waste": Waypoint(),
    }
    bundles = [
        Bundle(
            Elsewhere,
            "OrganicChemicals",
            waypoints=["OtherInputs"],
            flow_selection='material in ["PureOxygen", "OtherInorganicPrimaryChemicals", "InorganicAcids", "Chlorine", "NitricAcid", "Water", "Ammonia", "OtherIndustrialGases"]',
        ),
        Bundle(
            Elsewhere,
            "Polymerisation",
            waypoints=["OtherInputs", "wpt5"],
            flow_selection='material in ["PureOxygen", "OtherInorganicPrimaryChemicals", "InorganicAcids", "Chlorine", "NitricAcid", "Water", "Ammonia"]',
        ),
        Bundle(
            Elsewhere,
            "OrganicChemicals",
            waypoints=["PrimaryChemicals"],
        ),
        Bundle(
            "OrganicChemicals",
            Elsewhere,
            waypoints=["OtherOutputs"],
            flow_selection='material in ["Air", "InorganicAcids", "WasteOtherChemicals", "OtherIndustrialGases", "Water"]',
        ),
        Bundle(
            "Polymerisation",
            Elsewhere,
            waypoints=["Waste"],
            flow_selection='material in ["WasteOtherChemicals", "Water"]',
        ),
        Bundle(
            Elsewhere, "Polymerisation", waypoints=["PrimaryChemicals", "PrimaryWpt"]
        ),
        # Bundle("OrganicChemicalsSynthesis", "OrganicChemicals"),
        Bundle("OrganicChemicals", "Polymerisation"),
        Bundle("Polymerisation", "Polymers"),
        Bundle("Polymers", "Production"),
        Bundle("Production", "StockInUse"),
        Bundle("StockInUse", "FinalTreatment"),
        Bundle("StockInUse", "ChemicalRecycling"),
        Bundle("StockInUse", "MechanicalRecycling"),
        Bundle(
            "MechanicalRecycling",
            "Polymers",
            waypoints=["wpt4", "wpt3", "wpt2", "wpt1"],
        ),
    ]
    order = [
        [[], ["OtherInputs", "PrimaryChemicals"], [], []],
        [[], ["OrganicChemicals", "PrimaryWpt", "wpt5"], [], []],
        [["OtherOutputs"], ["Polymerisation"], [], []],
        [["wpt1"], ["Polymers"], ["Waste"], []],
        [["wpt2"], ["Production"], [], []],
        [["wpt3"], ["StockInUse"], [], []],
        [
            ["wpt4"],
            ["MechanicalRecycling", "ChemicalRecycling", "FinalTreatment"],
            [],
            [],
        ],
    ]
    sdd = SankeyDefinition(nodes, bundles, order, flow_partition=flow_partition)

    return sdd


### More detailed view of end-of-life
###


def define_eol_sdd():
    nodes_eol = {
        "Production": ProcessGroup(
            production_processes,
            Partition.Simple(
                "process",
                [
                    (short, [full])
                    for short, full in zip(product_short, production_processes)
                ],
            ),
            title="Production",
        ),
        "Products": ProcessGroup(
            product_objects + use_processes + eol_product_objects + eol_processes,
            Partition.Simple(
                "process",
                [
                    (short, [a, b, c, d])
                    for short, a, b, c, d in zip(
                        product_short,
                        product_objects,
                        use_processes,
                        eol_product_objects,
                        eol_processes,
                    )
                ],
            ),
            title="Stock in use",
        ),
        "EOLProcessing": ProcessGroup(
            eol_polymer_objects,
            Partition.Simple(
                "process",
                [
                    (short, [a])
                    for short, a in zip(polymer_objects_short, eol_polymer_objects)
                ],
            ),
            title="EOL polymers",
        ),
        "EOLMixing": ProcessGroup(
            [f"Mixing{polymer}AtEOL" for polymer in polymer_objects]
            + ["MixedPolymersAtEOL"]
        ),
        "MechanicalRecycling": ProcessGroup(
            [f"MechanicalRecyclingOf{polymer}AtEOL" for polymer in polymer_objects]
        ),
        "ChemicalRecycling": ProcessGroup(chemical_recycling),
        "FinalTreatment": ProcessGroup(
            final_treatment,
            Partition.Simple("process", final_treatment),
            title="Final treatment",
        ),
        "OtherInputs": Waypoint(title="Other inputs"),
        "Naphtha": Waypoint(),
        "wpt3": Waypoint(title="", direction="L"),
        "wpt4": Waypoint(title="", direction="L"),
        "wpt5": Waypoint(title=""),
        "OtherOutputs": Waypoint(title="Other outputs"),
        "Waste": Waypoint(),
        "RecycledPolymers": Waypoint(title="Recycled polymers"),
    }
    bundles_eol = [
        Bundle("Production", "Products"),
        Bundle("Products", "EOLProcessing"),
        # Bundle("EOLProcessing", "Polymers", waypoints=["wpt4", "wpt3", "wpt2", "wpt1"]),
        Bundle("EOLProcessing", "MechanicalRecycling"),
        Bundle("EOLProcessing", "EOLMixing"),
        Bundle("EOLMixing", "ChemicalRecycling"),
        Bundle("EOLMixing", "FinalTreatment"),
        # Bundle(Elsewhere, "FinalTreatment", waypoints=["OtherInputs"]),
        Bundle(Elsewhere, "ChemicalRecycling", waypoints=["OtherInputs"]),
        Bundle(
            "ChemicalRecycling",
            Elsewhere,
            waypoints=["Naphtha"],
            flow_selection="material == 'Naphtha'",
        ),
        Bundle(
            "ChemicalRecycling",
            Elsewhere,
            waypoints=["Waste"],
            flow_selection="material in ['PyrolysisResidue', 'MiscRefineryProducts', 'WasteOtherChemicals']",
        ),
        Bundle(
            "MechanicalRecycling",
            Elsewhere,
            waypoints=["RecycledPolymers"],
            flow_selection="material not in ['Waste']",
        ),
        Bundle(
            "MechanicalRecycling",
            Elsewhere,
            waypoints=["Waste"],
            flow_selection="material in ['Waste']",
        ),
    ]
    order_eol = [
        [[], ["Production"], [], []],
        [[], ["Products"], [], ["wpt3"]],
        [[], ["EOLProcessing"], [], ["wpt4"]],
        [["OtherInputs"], ["EOLMixing"], [], []],
        [[], ["ChemicalRecycling", "MechanicalRecycling", "FinalTreatment"], [], []],
        [["Waste"], ["Naphtha", "RecycledPolymers"], [], [], []],
    ]
    sdd_eol = SankeyDefinition(
        nodes_eol, bundles_eol, order_eol, flow_partition=flow_partition
    )
    return sdd_eol


### More detailed view of chemical synthesis


def define_chemical_synthesis_sdd():
    primary_inputs = (
        primary_chemicals + BTX + ["PureHydrogen", "MethylAlcohol", "NaturalGas"]
    )
    organic_chemicals1 = {
        x: x.replace("Synthesis", "") for x in organic_chemicals_synthesis1
    }
    organic_chemicals2 = {
        x: x.replace("Synthesis", "") for x in organic_chemicals_synthesis2
    }
    organic_chemicals1["OtherOrganicChemicalsSynthesis"] = (
        "OtherIntermediateOrganicChemicals"
    )
    organic_chemicals2["TerephthalicAcidSynthesis"] = (
        "TerephthalicAcidPhthalicAnhydrideDioctylPhthalate"
    )
    organic_chemicals2["HexamethylenediamineSynthesisFromButadiene"] = (
        "Hexamethylenediamine"
    )
    other_outputs = [
        "Air",
        "InorganicAcids",
        "OtherIndustrialGases",
        "WasteOtherChemicals",
        "Water",
    ]
    nodes2 = {
        "PrimaryChemicals": Waypoint(Partition.Simple("material", primary_inputs)),
        "InorganicChemicals": Waypoint(
            Partition.Simple(
                "material",
                [
                    "SodiumHydroxide",
                    "NitricAcid",
                    "InorganicAcids",
                    "PureOxygen",
                    "Chlorine",
                    (
                        "Other",
                        [
                            "OtherInorganicPrimaryChemicals",
                            "OtherIndustrialGases",
                            "Water",
                        ],
                    ),
                ],
            ),
        ),
        "OrganicChemicalsSynthesis1": ProcessGroup(
            organic_chemicals_synthesis1 + list(organic_chemicals1.values()),
            Partition.Simple(
                "process",
                [
                    (chemical, [synthesis_process, chemical])
                    for chemical, synthesis_process in (
                        (organic_chemicals1[synthesis_process], synthesis_process)
                        for synthesis_process in organic_chemicals_synthesis1
                    )
                ],
            ),
        ),
        # Grouped version
        "OrganicChemicalsSynthesis2": ProcessGroup(
            organic_chemicals_synthesis2 + list(organic_chemicals2.values()),
            Partition.Simple(
                "process",
                [
                    (chemical, [synthesis_process, chemical])
                    for chemical, synthesis_process in (
                        (organic_chemicals2[synthesis_process], synthesis_process)
                        for synthesis_process in organic_chemicals_synthesis2
                    )
                ],
            ),
        ),
        # # Ungrouped version
        # "OrganicChemicalsSynthesis2": ProcessGroup(
        #     organic_chemicals_synthesis2,
        #     Partition.Simple("process", organic_chemicals_synthesis2),
        # ),
        # "OrganicChemicals2": ProcessGroup(
        #     organic_chemicals2,
        #     Partition.Simple(
        #         "material",
        #         [
        #             "Styrene",
        #             "VinylChloride",
        #             "AdipicAcid",
        #             "Hexamethylenediamine",
        #             "IsophthalicAcid",
        #             "TerephthalicAcidPhthalicAnhydrideDioctylPhthalate",
        #             "Polyols",
        #             "EthyleneGlycol",
        #             "TolueneDiisocyanate",
        #             "OtherIntermediateOrganicChemicals",
        #             "Acrylonitrile",
        #         ],
        #     ),
        # ),
        "Polymerisation": ProcessGroup(
            polymerisation_processes,
            Partition.Simple(
                "process",
                [
                    (short, [full])
                    for short, full in zip(
                        polymer_objects_short, polymerisation_processes
                    )
                ],
            ),
            title="Polymerisation",
        ),
        "OtherInputs": Waypoint(),
        "OtherOutputs": Waypoint(),
        "wpt_OtherOutputs": Waypoint(title=""),
        "wpt1": Waypoint(title=""),
        "wpt2": Waypoint(title=""),
    }
    bundles2 = [
        Bundle(
            Elsewhere,
            "OrganicChemicalsSynthesis1",
            waypoints=["PrimaryChemicals"],
            flow_selection="material in %r" % primary_inputs,
        ),
        Bundle(
            Elsewhere,
            "OrganicChemicalsSynthesis2",
            waypoints=["PrimaryChemicals", "wpt1"],
            flow_selection="material in %r" % primary_inputs,
        ),
        Bundle(
            Elsewhere,
            "OrganicChemicalsSynthesis1",
            waypoints=["InorganicChemicals"],
            flow_selection="material in %r" % inorganic_chemicals,
        ),
        Bundle(
            Elsewhere,
            "OrganicChemicalsSynthesis2",
            waypoints=["InorganicChemicals"],
            flow_selection="material in %r" % inorganic_chemicals,
        ),
        # OrganicChemicalsSynthesis1 includes the output chemicals
        Bundle("OrganicChemicalsSynthesis1", "OrganicChemicalsSynthesis2"),
        # Bundle("OrganicChemicalsSynthesis2", "OrganicChemicals2"),
        Bundle(
            "OrganicChemicalsSynthesis2", "OrganicChemicalsSynthesis1"
        ),  # HydrogenCyanide
        Bundle(
            Elsewhere,
            "Polymerisation",
            waypoints=["PrimaryChemicals", "wpt1", "wpt2"],
            flow_selection="material in %r" % primary_inputs,
        ),
        Bundle(
            Elsewhere,
            "Polymerisation",
            waypoints=["OtherInputs"],
            flow_selection='material in ["Water", "OtherInorganicPrimaryChemicals"]',
        ),
        Bundle("OrganicChemicalsSynthesis1", "Polymerisation"),
        Bundle("OrganicChemicalsSynthesis2", "Polymerisation"),
        # Bundle("OrganicChemicals2", "Polymerisation"),
        Bundle(
            "OrganicChemicalsSynthesis1",
            Elsewhere,
            waypoints=["wpt_OtherOutputs", "OtherOutputs"],
            flow_selection="material in %r" % other_outputs,
        ),
        Bundle(
            "OrganicChemicalsSynthesis2",
            Elsewhere,
            waypoints=["OtherOutputs"],
            flow_selection="material in %r" % other_outputs,
        ),
    ]
    order2 = [
        [["PrimaryChemicals"], [], ["InorganicChemicals"], []],
        [["wpt1"], ["OrganicChemicalsSynthesis1"], []],
        [["wpt2"], ["OrganicChemicalsSynthesis2"], ["OtherInputs", "wpt_OtherOutputs"]],
        [[], ["Polymerisation"], ["OtherOutputs"]],
    ]
    sdd_chemical_synthesis = SankeyDefinition(
        nodes2, bundles2, order2, flow_partition=flow_partition
    )

    return sdd_chemical_synthesis


# # Focus just on upstream part
# #
# nodes3 = {
#     # Inputs
#     "Feedstocks": Waypoint(
#         Partition.Simple(
#             "source",
#             [
#                 (
#                     "Biomass",
#                     [
#                         "SugarCane",
#                         "SugarCaneBagasse",
#                         "CornStover",
#                         "WheatStraw",
#                         "RiceStraw",
#                         "Maize",
#                         "SugarCaneBagasseGasificationToSyngas",
#                         "CornStoverGasificationToSyngas",
#                         "WheatStrawGasificationToSyngas",
#                         "RiceStrawGasificationToSyngas",
#                         "EthylAlcoholSynthesisFromCornStover",
#                         "EthylAlcoholSynthesisFromMaize",
#                         "EthylAlcoholSynthesisFromRiceStraw",
#                         "EthylAlcoholSynthesisFromSugarcane",
#                         "EthylAlcoholSynthesisFromSugarcaneBagasse",
#                         "EthylAlcoholSynthesisFromWheatStraw",
#                     ],
#                 ),
#                 "CrudeOil",
#                 ("NaturalGas", ["NaturalGasSteamMethaneReformingToSyngas"]),
#                 ("Coal", ["CoalGasificationToSyngas"]),
#             ],
#         )
#     ),
#     "OtherInputs": Waypoint(title="Other inputs"),
#     "OtherInputs2": Waypoint(title="Other inputs"),
#     "FromChemicalRecycling": Waypoint(title="from chemical recycling"),
#     # Outputs to elsewhere
#     "OtherOutputs": Waypoint(title="Other outputs"),
#     "Waste": Waypoint(),
#     # Group these together to save space, since almost all of the syngas becomes
#     # methyl alcohol
#     "SyngasMethylAlcohol": ProcessGroup(
#         ["Syngas", "MethylAlcoholSynthesis", "MethylAlcohol"],
#         title="Syngas / methyl alcohol",
#     ),
#     "Hydrogen": ProcessGroup(
#         ["PureHydrogen"],
#     ),
#     "EthylAlcohol": ProcessGroup(["EthylAlcohol"], title="Ethyl alcohol"),
#     # Main processes
#     "Paraffins": ProcessGroup(
#         ["Ethane", "Propane", "Butane", "Naphtha"], title="Paraffins"
#     ),
#     "Distillation": ProcessGroup(
#         [
#             "DistillationOfPyrolysisGasolineForBTX",
#             "DistillationOfButylenesForButadiene",
#         ],
#     ),
#     "PyrolysisGasoline": ProcessGroup(pyrolysis_gasoline, direction="L", title=" "),
#     "DehydrationOfEthylAlcohol": ProcessGroup(
#         ["DehydrationOfEthylAlcohol"], title="Dehydration"
#     ),
#     "SteamCracking": ProcessGroup(steam_cracking, title="Steam cracking"),
#     "MTO": ProcessGroup(
#         ["MethylAlcoholToOlefins", "MethylAlcoholToPropylene"], title="MTO"
#     ),
#     "AmmoniaProduction": ProcessGroup(
#         ["SyngasToAmmoniaProduction"], title="Ammonia production"
#     ),
#     # "FischerTropschSynthesisOfOlefinsFromSyngas",
#     "Dehydrogenation": ProcessGroup(
#         [
#             "DehydrogenationOfButaneForButadiene",
#             "DehydrogenationOfPropane",
#         ]
#     ),
#     "PrimaryChemicals": ProcessGroup(
#         primary_chemicals + BTX,
#         primary_chemicals_partition,
#     ),
#     # "PrimaryChemicalsConsumption": Waypoint(),
#     # These are just to improve the layout of the diagram
#     "wpt1": Waypoint(
#         title="",  # partition=Partition.Simple("material", ["NaturalGas", "Coal"])
#     ),
# }
# bundles3 = [
#     # Bundle(Elsewhere, "MethylAlcoholSynthesis", waypoints=["Feedstocks", "wpt1"]),
#     Bundle(Elsewhere, "MTO", waypoints=["OtherInputs2"]),
#     Bundle("AmmoniaProduction", Elsewhere, waypoints=["OtherOutputs"]),
#     Bundle("SyngasMethylAlcohol", "AmmoniaProduction"),
#     Bundle("SyngasMethylAlcohol", "MTO"),
#     Bundle("EthylAlcohol", "DehydrationOfEthylAlcohol"),
#     Bundle("Paraffins", "SteamCracking", waypoints=["wpt1"]),
#     Bundle("Paraffins", "AmmoniaProduction", waypoints=["wpt1"]),
#     Bundle("Paraffins", "Dehydrogenation", waypoints=["wpt1"]),
#     # Bundle("SyngasProduction", "Syngas"),
#     Bundle(
#         Elsewhere,
#         "SyngasMethylAlcohol",
#         flow_selection=f"material == 'Syngas'",
#         waypoints=["Feedstocks"],
#     ),
#     Bundle(
#         Elsewhere,
#         "EthylAlcohol",
#         waypoints=["Feedstocks"],
#     ),
#     Bundle("PyrolysisGasoline", "Distillation"),
#     Bundle("Distillation", "PrimaryChemicals"),
#     Bundle(
#         "Distillation",
#         Elsewhere,
#         waypoints=["Waste"],
#         flow_selection="material == 'WasteOtherChemicals'",
#     ),
#     Bundle(
#         "DehydrationOfEthylAlcohol",
#         Elsewhere,
#         waypoints=["OtherOutputs"],
#         flow_selection="material in ['NaturalGas']",
#     ),
#     Bundle(
#         "MTO",
#         Elsewhere,
#         waypoints=["OtherOutputs"],
#         flow_selection="material in ['Ethane', 'Propane', 'NaturalGas']",
#     ),
#     Bundle(
#         "SteamCracking",
#         Elsewhere,
#         waypoints=["OtherOutputs"],
#         flow_selection="material in ['WasteOtherChemicals', 'MiscRefineryProducts', 'NaturalGas', 'OtherIndustrialGases']",
#     ),
#     Bundle(
#         "Dehydrogenation",
#         Elsewhere,
#         waypoints=["Waste"],
#         flow_selection="material in ['WasteOtherChemicals', 'NaturalGas']",
#     ),
#     Bundle("DehydrationOfEthylAlcohol", "PrimaryChemicals"),
#     Bundle("MTO", "PrimaryChemicals"),
#     Bundle("SteamCracking", "PrimaryChemicals"),
#     Bundle("AmmoniaProduction", "PrimaryChemicals"),
#     Bundle("Dehydrogenation", "PrimaryChemicals"),
#     Bundle("PrimaryChemicals", "Distillation"),  # loop
#     Bundle("SteamCracking", "PyrolysisGasoline"),
#     # Bundle("PrimaryChemicals", Elsewhere, waypoints=["PrimaryChemicalsConsumption"]),
#     Bundle(
#         Elsewhere,
#         "PrimaryChemicals",
#         waypoints=["FromChemicalRecycling"],
#         flow_selection="source == 'ChemicalPolyolefinRecycling'",
#     ),
# ]
# order3 = [
#     [[], ["Feedstocks", "Paraffins", "OtherInputs"], []],
#     [
#         ["OtherInputs2"],
#         ["EthylAlcohol", "SyngasMethylAlcohol", "Hydrogen", "wpt1"],
#         [],
#     ],
#     [
#         ["FromChemicalRecycling"],
#         [
#             "DehydrationOfEthylAlcohol",
#             "MTO",
#             "AmmoniaProduction",
#             "SteamCracking",
#             "Dehydrogenation",
#             "PyrolysisGasoline",
#             "Distillation",
#         ],
#         [],
#     ],
#     [["OtherOutputs"], ["PrimaryChemicals"], ["Waste"]],
#     # [[], ["PrimaryChemicalsConsumption"]],
# ]
# sdd_primary = SankeyDefinition(nodes3, bundles3, order3, flow_partition=flow_partition)


# Upstream feedstock detail. These are not shown in the "primary" Sankey because
# the conversion losses are large so it messes up the scale.
#
def define_feedstock_sdd():

    nodes = {
        # Inputs
        "Feedstocks": Waypoint(
            Partition.Simple(
                "source",
                [
                    (
                        "Biomass",
                        [
                            "SugarCane",
                            "SugarCaneBagasse",
                            "CornStover",
                            "WheatStraw",
                            "RiceStraw",
                            "Maize",
                        ],
                    ),
                    "CrudeOil",
                    (
                        "Natural gas",
                        [
                            "NaturalGas",
                        ],
                    ),
                    "Coal",
                    "Water",
                    ("CO2", ["CapturedCarbonDioxide"]),
                    ("H2", ["PureHydrogen"]),
                ],
            )
        ),
        "OtherInputs": Waypoint(title="Other inputs"),
        "OtherInputs2": Waypoint(title="Other inputs"),
        # Outputs to elsewhere
        "OtherOutputs": Waypoint(title="Other outputs"),
        "Waste": Waypoint(),
        # Main processes
        "Gasification": ProcessGroup([
            "SugarCaneBagasseGasificationToSyngas",
            "CornStoverGasificationToSyngas",
            "WheatStrawGasificationToSyngas",
            "RiceStrawGasificationToSyngas",
            "CoalGasificationToSyngas",
        ]),
        "Reforming": ProcessGroup([
            "NaturalGasSteamMethaneReformingToSyngas",
            "NaturalGasSteamMethaneReformingToHydrogen",
            "NaturalGasSteamMethaneReformingWithCCSToHydrogen",
        ]),
        "Electrolysis": ProcessGroup([
            "WaterElectrolysisForHydrogen",
        ]),
        "EthylAlcoholSynthesis": ProcessGroup([
            "EthylAlcoholSynthesisFromCornStover",
            "EthylAlcoholSynthesisFromMaize",
            "EthylAlcoholSynthesisFromRiceStraw",
            "EthylAlcoholSynthesisFromSugarcane",
            "EthylAlcoholSynthesisFromSugarcaneBagasse",
            "EthylAlcoholSynthesisFromWheatStraw",
        ]),
        "Syngas": ProcessGroup(["Syngas"]),
        "MethylAlcohol": ProcessGroup(
            ["MethylAlcoholSynthesis", "MethylAlcohol"],
            title="Methyl alcohol synthesis",
        ),
        "Hydrogen": ProcessGroup(
            ["PureHydrogen"],
        ),
        "CarbonDioxideHydrogenationToMethylAlcohol": ProcessGroup(
            ["CarbonDioxideHydrogenationToMethylAlcohol"], title="CO2 hydrogenation"
        ),
        "EthylAlcohol": ProcessGroup(["EthylAlcohol"], title="Ethyl alcohol"),
        # "DehydrationOfEthylAlcohol": ProcessGroup(
        #     ["DehydrationOfEthylAlcohol"], title="Dehydration"
        # ),
        "Products": Waypoint(
            Partition.Simple(
                "target",
                [
                    (
                        "Primary production",
                        [
                            "MethylAlcoholToOlefins",
                            "MethylAlcoholToAromatics",
                            "DehydrationOfEthylAlcohol",
                            "CatalyticReformingOfNaphthaForXylenes",
                            "DealkylationOfTolueneForBenzene",
                            "DisproportionationOfTolueneForXylenes",
                        ]
                    ),
                    (
                        "Organic chemical synthesis",
                        [
                            "EthyleneOxideSynthesis",
                            "PolymerisationOfLLDPE",
                            "EthyleneGlycolSynthesis",
                            "OtherOrganicChemicalsSynthesis",
                            "PolymerisationOfHDPE",
                            "PolymerisationOfLDPE",
                            "PolymerisationOfOtherPolymers",
                            "StyreneSynthesis",
                            "VinylChlorideSynthesis",
                            "PropyleneOxideSynthesis",
                            "PolymerisationOfPP",
                            "HexamethylenediamineSynthesisFromButadiene",
                            "PolymerisationOfStyreneButadiene",
                            "CyclohexaneSynthesis",
                            "HydrogenCyanideSynthesis",
                            "TolueneDiisocyanateSynthesis",
                            "IsophthalicAcidSynthesis",
                            "TerephthalicAcidSynthesis",
                            "AcrylonitrileSynthesis",
                        ],
                    ),
                    (
                        "Misc",
                        [
                            "EthylAlcoholSynthesisFromCornStover",
                            "EthylAlcoholSynthesisFromMaize",
                            "ProducingNitricAcid",
                            "AceticAcidSynthesis",
                            "SyngasToAmmoniaProduction",
                        ],
                    ),
                    (
                        "Other demand",
                        [
                            "OtherConsumptionOfBenzene",
                            "OtherConsumptionOfToluene",
                            "OtherConsumptionOfXylenes",
                            "OtherConsumptionOfMethylAlcohol",
                        ],
                    ),
                ],
            )
        ),
        # These are just to improve the layout of the diagram
        "FossilParaffins": Waypoint(
            Partition.Simple("material", ["Ethane", "Naphtha", "Propane", "Butane"]),
            title="Fossil paraffins",  # partition=Partition.Simple("material", ["NaturalGas", "Coal"])
        ),
        "wpt_loop_paraffins_1": Waypoint(title="", direction="L"),
        "wpt_loop_paraffins_2": Waypoint(title="", direction="L"),
    }
    bundles = [
        # Bundle(Elsewhere, "MethylAlcoholSynthesis", waypoints=["Feedstocks", "wpt1"]),
        # Bundle(
        #     Elsewhere,
        #     "CarbonDioxideHydrogenationToMethylAlcohol",
        #     waypoints=["OtherInputs2"],
        # ),
        # Bundle("AmmoniaProduction", Elsewhere, waypoints=["OtherOutputs"]),
        # Bundle("SyngasMethylAlcohol", "AmmoniaProduction"),
        # Bundle("SyngasMethylAlcohol", "MTX"),
        # Bundle("EthylAlcohol", "DehydrationOfEthylAlcohol"),
        # Bundle("SyngasProduction", "Syngas"),
        # Bundle(
        #     Elsewhere,
        #     "MethylAlcohol",
        #     flow_selection=f"material in ['Syngas', 'MethylAlcohol']",
        #     waypoints=["Feedstocks"],
        # ),
        Bundle(
            Elsewhere,
            "MethylAlcohol",
            flow_selection=f"material in ['OtherInorganicPrimaryChemicals']",
            waypoints=["OtherInputs"],
        ),
        Bundle(
            Elsewhere,
            "EthylAlcoholSynthesis",
            flow_selection=f"material in ['OtherInorganicPrimaryChemicals', 'Enzymes', 'InorganicAcids', 'VegetableOil', 'Yeast', 'Nutrients', 'Ammonia']",
            waypoints=["OtherInputs"],
        ),
        Bundle(
            Elsewhere,
            "Gasification",
            flow_selection=f"material in ['PureOxygen']",
            waypoints=["OtherInputs"],
        ),
        Bundle(
            Elsewhere,
            "Reforming",
            flow_selection=f"material in ['PureOxygen']",
            waypoints=["OtherInputs"],
        ),
        Bundle(
            Elsewhere,
            "EthylAlcoholSynthesis",
            waypoints=["Feedstocks"],
        ),
        Bundle(
            Elsewhere,
            "Gasification",
            waypoints=["Feedstocks"],
        ),
        Bundle(
            Elsewhere,
            "Reforming",
            waypoints=["Feedstocks"],
        ),
        Bundle(
            Elsewhere,
            "Electrolysis",
            waypoints=["Feedstocks"],
        ),
        # Bundle(Elsewhere, "Hydrogen", waypoints=["Feedstocks"]),

        Bundle("Electrolysis", "Hydrogen"),
        Bundle("Reforming", "Hydrogen"),
        Bundle("Reforming", "Syngas"),
        Bundle("Gasification", "Syngas"),
        Bundle("EthylAlcoholSynthesis", "EthylAlcohol"),
        Bundle("Syngas", "MethylAlcohol"),

        Bundle("Hydrogen",                 "CarbonDioxideHydrogenationToMethylAlcohol"),
        Bundle(                "CarbonDioxideHydrogenationToMethylAlcohol", "MethylAlcohol"),

        Bundle("EthylAlcohol", Elsewhere, waypoints=["Products"]),
        Bundle("MethylAlcohol", Elsewhere, waypoints=["Products"]),
        Bundle("Syngas", Elsewhere, waypoints=["Products"]),
        Bundle("Hydrogen", Elsewhere, waypoints=["Products"]),

        # Bundle(
        #     Elsewhere,
        #     "CarbonDioxideHydrogenationToMethylAlcohol",
        #     waypoints=["Feedstocks"],
        # ),
        # Bundle("Hydrogen", "CarbonDioxideHydrogenationToMethylAlcohol"),
        # Bundle("CarbonDioxideHydrogenationToMethylAlcohol", "SyngasMethylAlcohol"),
        # Bundle(
        #     "CarbonDioxideHydrogenationToMethylAlcohol",
        #     Elsewhere,
        #     waypoints=["OtherOutputs"],
        #     flow_selection="material in ['MiscRefineryProducts', 'NaturalGas', 'OtherIndustrialGases']",
        # ),
        Bundle(
            "EthylAlcoholSynthesis",
            Elsewhere,
            waypoints=["Waste"],
            flow_selection="material in ['WasteBiomass']",
        ),
        Bundle(
            "CarbonDioxideHydrogenationToMethylAlcohol",
            Elsewhere,
            waypoints=["Waste"],
            flow_selection="material in ['WasteOtherChemicals']",
        ),
        # Bundle("DehydrationOfEthylAlcohol", "PrimaryChemicals"),
        # Bundle("Hydrogen", Elsewhere, waypoints=["PrimaryChemicalsConsumption"]),
        # Bundle(
        #     "SyngasMethylAlcohol", Elsewhere, waypoints=["PrimaryChemicalsConsumption"]
        # ),
    ]
    order = [
        [
            [],
            ["Feedstocks", "OtherInputs"],
            [],
        ],
        [
            [],
            ["EthylAlcoholSynthesis", "Gasification", "Reforming", "Electrolysis"],
            [],
        ],
        [
            ["OtherInputs2"],
            ["EthylAlcohol", "Syngas", "Hydrogen"],
            []
        ],
        [
            [],
            ["CarbonDioxideHydrogenationToMethylAlcohol"],
            []
        ],
        [
            [],
            [
                "MethylAlcohol",
            ],
            [],
        ],
        [["OtherOutputs"], ["Products"], ["Waste"]],
    ]
    sdd_feedstocks = SankeyDefinition(
        nodes, bundles, order, flow_partition=flow_partition
    )
    return sdd_feedstocks


# Detailed primary SDD
#


def define_primary_sdd():
    nodes4 = {
        # Inputs
        "Feedstocks": Waypoint(
            Partition.Simple(
                "source",
                [
                    (
                        "Biomass",
                        [
                            "SugarCaneBagasseGasificationToSyngas",
                            "CornStoverGasificationToSyngas",
                            "WheatStrawGasificationToSyngas",
                            "RiceStrawGasificationToSyngas",
                            "EthylAlcoholSynthesisFromCornStover",
                            "EthylAlcoholSynthesisFromMaize",
                            "EthylAlcoholSynthesisFromRiceStraw",
                            "EthylAlcoholSynthesisFromSugarcane",
                            "EthylAlcoholSynthesisFromSugarcaneBagasse",
                            "EthylAlcoholSynthesisFromWheatStraw",
                        ],
                    ),
                    "CrudeOil",
                    (
                        "NaturalGas",
                        [
                            "NaturalGasSteamMethaneReformingToSyngas",
                            "NaturalGasSteamMethaneReformingToHydrogen",
                            "NaturalGasSteamMethaneReformingWithCCSToHydrogen",
                        ],
                    ),
                    ("Coal", ["CoalGasificationToSyngas"]),
                    ("Water", ["WaterElectrolysisForHydrogen"]),
                    ("CO2", ["CapturedCarbonDioxide"]),
                    ("H2", ["CarbonDioxideHydrogenationToMethylAlcohol"]),
                ],
            )
        ),
        "OtherInputs": Waypoint(title="Other inputs"),
        "OtherInputs2": Waypoint(title="Other inputs"),
        "FromChemicalRecycling": Waypoint(title="from chemical recycling"),
        # Outputs to elsewhere
        "OtherOutputs": Waypoint(title="Other outputs"),
        "Waste": Waypoint(),
        # Group these together to save space, since almost all of the syngas becomes
        # methyl alcohol
        "SyngasMethylAlcohol": ProcessGroup(
            ["Syngas", "MethylAlcoholSynthesis", "MethylAlcohol"],
            title="Syngas / methyl alcohol",
        ),
        # "CarbonDioxideHydrogenationToMethylAlcohol": ProcessGroup(
        #     ["CarbonDioxideHydrogenationToMethylAlcohol"], title="CO2 hydrogenation"
        # ),
        "EthylAlcohol": ProcessGroup(["EthylAlcohol"], title="Ethyl alcohol"),
        # Main processes
        "Paraffins": ProcessGroup(
            ["Ethane", "Propane", "Butane", "Naphtha"],
            Partition.Simple("process", ["Ethane", "Naphtha", "Propane", "Butane"]),
            title="Paraffins",
        ),
        "Distillation": ProcessGroup(
            [
                "DistillationOfButylenesForButadiene",
            ],
        ),
        "DehydrationOfEthylAlcohol": ProcessGroup(
            ["DehydrationOfEthylAlcohol"], title="Dehydration"
        ),
        "SteamCracking": ProcessGroup(
            steam_cracking
            + ["DistillationOfPyrolysisGasolineForBTX", "PyrolysisGasoline"],
            title="Steam cracking",
        ),
        "FCC": ProcessGroup(["FluidCatalyticCrackingOfGasOil"], title="FCC"),
        "MTX": ProcessGroup(
            [
                "MethylAlcoholToOlefins",
                "MethylAlcoholToPropylene",
                "MethylAlcoholToAromatics",
            ],
            Partition.Simple(
                "process",
                [
                    "MethylAlcoholToOlefins",
                    "MethylAlcoholToPropylene",
                    "MethylAlcoholToAromatics",
                ],
            ),
            title="MTX",
        ),
        "AmmoniaProduction": ProcessGroup(
            ["SyngasToAmmoniaProduction"], title="Ammonia production"
        ),
        # "FischerTropschSynthesisOfOlefinsFromSyngas",
        "Dehydrogenation": ProcessGroup(
            [
                "DehydrogenationOfButaneForButadiene",
                "DehydrogenationOfPropane",
            ]
        ),
        "ReformingToBTX": ProcessGroup(
            [
                "CatalyticReformingOfNaphthaForXylenes",
                "CatalyticReformingOfNaphthaForToluene",
                "DisproportionationOfTolueneForXylenes",
                "DealkylationOfTolueneForBenzene",
            ],
            Partition.Simple(
                "process",
                [
                    ("to benzene", ["DealkylationOfTolueneForBenzene"]),
                    ("to toluene", ["CatalyticReformingOfNaphthaForToluene"]),
                    (
                        "to xylenes",
                        [
                            "CatalyticReformingOfNaphthaForXylenes",
                            "DisproportionationOfTolueneForXylenes",
                        ],
                    ),
                ],
            ),
            title="Reforming to BTX",
        ),
        "PrimaryChemicals": ProcessGroup(
            primary_chemicals,
            primary_chemicals_partition,
        ),
        "BTX": ProcessGroup(
            BTX,
            primary_chemicals_partition,
            title="BTX",
        ),
        "PrimaryChemicalsConsumption": Waypoint(
            Partition.Simple(
                "target",
                [
                    (
                        "Organic chemical synthesis",
                        [
                            "EthyleneOxideSynthesis",
                            "PolymerisationOfLLDPE",
                            "EthyleneGlycolSynthesis",
                            "OtherOrganicChemicalsSynthesis",
                            "PolymerisationOfHDPE",
                            "PolymerisationOfLDPE",
                            "PolymerisationOfOtherPolymers",
                            "StyreneSynthesis",
                            "VinylChlorideSynthesis",
                            "PropyleneOxideSynthesis",
                            "PolymerisationOfPP",
                            "HexamethylenediamineSynthesisFromButadiene",
                            "PolymerisationOfStyreneButadiene",
                            "CyclohexaneSynthesis",
                            "HydrogenCyanideSynthesis",
                            "TolueneDiisocyanateSynthesis",
                            "IsophthalicAcidSynthesis",
                            "TerephthalicAcidSynthesis",
                            "AcrylonitrileSynthesis",
                        ],
                    ),
                    (
                        "Misc",
                        [
                            "EthylAlcoholSynthesisFromCornStover",
                            "EthylAlcoholSynthesisFromMaize",
                            "ProducingNitricAcid",
                            "AceticAcidSynthesis",
                        ],
                    ),
                    (
                        "Other demand",
                        [
                            "OtherConsumptionOfBenzene",
                            "OtherConsumptionOfToluene",
                            "OtherConsumptionOfXylenes",
                            "OtherConsumptionOfMethylAlcohol",
                        ],
                    ),
                ],
            )
        ),
        # These are just to improve the layout of the diagram
        "FossilParaffins": Waypoint(
            Partition.Simple("material", ["Ethane", "Naphtha", "Propane", "Butane"]),
            title="Fossil paraffins",  # partition=Partition.Simple("material", ["NaturalGas", "Coal"])
        ),
        "wpt_loop_paraffins_1": Waypoint(title="", direction="L"),
        "wpt_loop_paraffins_2": Waypoint(title="", direction="L"),
    }
    bundles4 = [
        # Bundle(Elsewhere, "MethylAlcoholSynthesis", waypoints=["Feedstocks", "wpt1"]),
        Bundle(Elsewhere, "MTX", waypoints=["OtherInputs2"]),
        Bundle(Elsewhere, "ReformingToBTX", waypoints=["OtherInputs2"]),
        # Bundle(
        #     Elsewhere,
        #     "CarbonDioxideHydrogenationToMethylAlcohol",
        #     waypoints=["OtherInputs2"],
        # ),
        Bundle(
            Elsewhere,
            "Paraffins",
            flow_selection='source in ["OilRefiningEthane", "OilRefiningNaphtha", "OilRefiningPropane", "OilRefiningButane"]',
            waypoints=["FossilParaffins"],
        ),
        Bundle(
            Elsewhere,
            "Paraffins",
            flow_selection='source in ["ChemicalRecyclingOfMixedPolymersAtEOL"]',
            waypoints=["FromChemicalRecycling"],
        ),
        Bundle("AmmoniaProduction", Elsewhere, waypoints=["OtherOutputs"]),
        Bundle("SyngasMethylAlcohol", "AmmoniaProduction"),
        Bundle("SyngasMethylAlcohol", "MTX"),
        Bundle("EthylAlcohol", "DehydrationOfEthylAlcohol"),
        Bundle("Paraffins", "SteamCracking"),
        Bundle("Paraffins", "FCC"),
        Bundle("Paraffins", "AmmoniaProduction"),
        Bundle("Paraffins", "Dehydrogenation"),
        Bundle("Paraffins", "ReformingToBTX"),
        # Bundle("SyngasProduction", "Syngas"),
        Bundle(
            Elsewhere,
            "SyngasMethylAlcohol",
            flow_selection=f"material in ['Syngas', 'MethylAlcohol']",
            waypoints=["Feedstocks"],
        ),
        Bundle(
            Elsewhere,
            "EthylAlcohol",
            waypoints=["Feedstocks"],
        ),
        # Bundle(Elsewhere, "Hydrogen", waypoints=["Feedstocks"]),
        # Bundle(
        #     Elsewhere,
        #     "CarbonDioxideHydrogenationToMethylAlcohol",
        #     waypoints=["Feedstocks"],
        # ),
        # Bundle("Hydrogen", "CarbonDioxideHydrogenationToMethylAlcohol"),
        # Bundle("Hydrogen", "ReformingToBTX"),
        Bundle("BTX", "ReformingToBTX"),
        # Bundle("CarbonDioxideHydrogenationToMethylAlcohol", "SyngasMethylAlcohol"),
        Bundle("Distillation", "BTX"),
        Bundle("Distillation", "PrimaryChemicals"),
        Bundle(
            "Distillation",
            Elsewhere,
            waypoints=["Waste"],
            flow_selection="material == 'WasteOtherChemicals'",
        ),
        Bundle(
            "SteamCracking",
            Elsewhere,
            waypoints=["Waste"],
            flow_selection="material == 'WasteOtherChemicals'",
        ),
        Bundle(
            "DehydrationOfEthylAlcohol",
            Elsewhere,
            waypoints=["OtherOutputs"],
            flow_selection="material in ['NaturalGas']",
        ),
        Bundle(
            "Dehydrogenation",
            Elsewhere,
            waypoints=["OtherOutputs"],
            flow_selection="material in ['NaturalGas']",
        ),
        Bundle(
            "MTX",
            Elsewhere,
            waypoints=["OtherOutputs"],
            flow_selection="material in ['NaturalGas', 'MiscRefineryProducts', 'OtherIndustrialGases']",
        ),
        Bundle(
            "MTX",
            "Paraffins",
            waypoints=["wpt_loop_paraffins_1", "wpt_loop_paraffins_2"],
        ),
        Bundle(
            "SteamCracking",
            Elsewhere,
            waypoints=["OtherOutputs"],
            flow_selection="material in ['MiscRefineryProducts', 'NaturalGas', 'OtherIndustrialGases']",
        ),
        Bundle(
            "FCC",
            Elsewhere,
            waypoints=["OtherOutputs"],
            flow_selection="material in ['MiscRefineryProducts', 'NaturalGas', 'OtherIndustrialGases']",
        ),
        Bundle(
            "ReformingToBTX",
            Elsewhere,
            waypoints=["OtherOutputs"],
            flow_selection="material in ['MiscRefineryProducts', 'NaturalGas', 'OtherIndustrialGases']",
        ),
        # Bundle(
        #     "CarbonDioxideHydrogenationToMethylAlcohol",
        #     Elsewhere,
        #     waypoints=["OtherOutputs"],
        #     flow_selection="material in ['MiscRefineryProducts', 'NaturalGas', 'OtherIndustrialGases']",
        # ),
        # Bundle(
        #     "CarbonDioxideHydrogenationToMethylAlcohol",
        #     Elsewhere,
        #     waypoints=["Waste"],
        #     flow_selection="material in ['WasteOtherChemicals']",
        # ),
        Bundle(
            "Dehydrogenation",
            Elsewhere,
            waypoints=["Waste"],
            flow_selection="material in ['WasteOtherChemicals']",
        ),
        Bundle(
            "MTX",
            Elsewhere,
            waypoints=["Waste"],
            flow_selection="material in ['WasteOtherChemicals']",
        ),
        Bundle(
            "ReformingToBTX",
            Elsewhere,
            waypoints=["Waste"],
            flow_selection="material in ['WasteOtherChemicals']",
        ),
        Bundle("DehydrationOfEthylAlcohol", "PrimaryChemicals"),
        Bundle("MTX", "PrimaryChemicals"),
        Bundle("MTX", "BTX"),
        Bundle("ReformingToBTX", "BTX"),
        Bundle("SteamCracking", "PrimaryChemicals"),
        Bundle("SteamCracking", "BTX"),
        Bundle("FCC", "PrimaryChemicals"),
        Bundle("AmmoniaProduction", "PrimaryChemicals"),
        Bundle("Dehydrogenation", "PrimaryChemicals"),
        Bundle("PrimaryChemicals", "Distillation"),  # loop
        Bundle(
            "PrimaryChemicals", Elsewhere, waypoints=["PrimaryChemicalsConsumption"]
        ),
        Bundle("BTX", Elsewhere, waypoints=["PrimaryChemicalsConsumption"]),
        # Bundle("Hydrogen", Elsewhere, waypoints=["PrimaryChemicalsConsumption"]),
        Bundle(
            "SyngasMethylAlcohol", Elsewhere, waypoints=["PrimaryChemicalsConsumption"]
        ),
        Bundle(
            Elsewhere,
            "PrimaryChemicals",
            waypoints=["FromChemicalRecycling"],
            flow_selection="source == 'ChemicalPolyolefinRecycling'",
        ),
    ]
    order4 = [
        [
            ["OtherInputs"],
            ["Feedstocks", "FossilParaffins", "FromChemicalRecycling"],
            [],
        ],
        [
            ["OtherInputs2"],
            ["EthylAlcohol", "SyngasMethylAlcohol", "Paraffins"],
            ["wpt_loop_paraffins_2"],
        ],
        [
            [],
            [
                "DehydrationOfEthylAlcohol",
                "MTX",
                "AmmoniaProduction",
                # "CarbonDioxideHydrogenationToMethylAlcohol",
                "SteamCracking",
                "FCC",
                "Dehydrogenation",
                "Distillation",
                "ReformingToBTX",
            ],
            ["wpt_loop_paraffins_1"],
        ],
        [["OtherOutputs"], ["PrimaryChemicals", "BTX"], ["Waste"]],
        [[], ["PrimaryChemicalsConsumption"]],
    ]
    sdd_primary_detailed = SankeyDefinition(
        nodes4, bundles4, order4, flow_partition=flow_partition
    )
    return sdd_primary_detailed


sdd_overall = define_overall_sdd()
sdd_lifecycle = define_lifecycle_sdd()
sdd_eol = define_eol_sdd()
sdd_chemical_synthesis = define_chemical_synthesis_sdd()
sdd_primary = define_primary_sdd()
sdd_feedstock = define_feedstock_sdd()
