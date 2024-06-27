Upstream processes
==================

These processes produce the basic input chemicals such as syngas, ethyl alcohol, methyl alcohol, hydrogen, used subsequently in the {doc}`primary-chemicals` processes.

Most of the main chemicals are already defined from the UK FIRES production system map {cite}`lupton_ukproductionsystem_2024`, but a few additional "objects" need to be defined here.

## Upstream refining

These processes represent upstream production of other chemicals not modelled in more detail.

```{system:process} ukf:OilRefiningButane
---
consumes: |
  ukf:CrudeOil                                 = 1.0 kg
produces: |
  ukf:Butane                                   = 1.0 kg
---
```

```{system:process} ukf:OilRefiningEthane
---
consumes: |
  ukf:CrudeOil                                 = 1.0 kg
produces: |
  ukf:Ethane                                   = 1.0 kg
---
```

```{system:process} ukf:OilRefiningPropane
---
consumes: |
  ukf:CrudeOil                                 = 1.0 kg
produces: |
  ukf:Propane                                  = 1.0 kg
---
```

```{system:process} ukf:OilRefiningNaphtha
---
consumes: |
  ukf:CrudeOil                                 = 1.0 kg
produces: |
  ukf:Naphtha                                  = 1.0 kg
---
```

Products:

```{system:object} ukf:Butane
``` 

```{system:object} ukf:Ethane
``` 

```{system:object} ukf:Propane
```

```{system:object} ukf:Naphtha
```

Fossil feedstocks:

```{system:object} ukf:NaturalGas
```

```{system:object} ukf:Coal
```

```{system:object} ukf:CrudeOil
```

## Syngas

The following processes are for the production of syngas from fossil fuels (natural gas and coal).

```{system:process} NaturalGasSteamMethaneReformingToSyngas
---
consumes: |
  ukf:NaturalGas                               = 0.566 kg
  ukf:PureOxygen                               = 0.329 kg {comment: 'Oxygen, according to the recipe of Zhao et al. (2021)'}
  ukf:Water                                    = 0.132 kg {comment: 'Steam, according to the recipe of Zhao et al. (2021)'}
produces: |
  ukf:Syngas                                   = 1 kg  
---
Recipe based on {cite:t}`zhao_economic_2021`. Note there is an imbalance of 0.027 kg (outputs not included in recipe).
```

```{system:process} CoalGasificationToSyngas
---
consumes: |
  ukf:Coal                                     = 1.006 kg
  ukf:PureOxygen                               = 0.956 kg {comment: 'Oxygen, according to the recipe of Zhao et al. (2021)'}
produces: |
  ukf:Syngas                                   = 1 kg
---
Recipe based on {cite:t}`zhao_economic_2021`. Methyl alcohol at 0.09 kg per kg syngas is also consumed as solvent for the acid gas removal, but this was assumed to be recycled.  Note there is an imbalance of 1.05 kg (outputs not included in recipe).
```

From biomass, syngas can be produced by gasification:

```{system:process} BiomassGasificationToSyngas
:become_parent: true
```

```{system:process} SugarCaneBagasseGasificationToSyngas
---
consumes: |
  SugarCaneBagasse                             = 1.674 kg
  ukf:PureOxygen                               = 0.670 kg {comment: 'Oxygen, according to the recipe of Zhao et al. (2021)'}
produces: |
  ukf:Syngas                                   = 1 kg
---
Recipe based on {cite:t}`zhao_economic_2021`. Methyl alcohol at 0.04 kg per kg syngas is also consumed as solvent for the acid gas removal, but this was assumed to be recycled.  Note there is an imbalance of 1.38 kg (outputs not included in recipe).
```


```{system:process} CornStoverGasificationToSyngas
---
consumes: |
  CornStover                                   = 1.674 kg
  ukf:PureOxygen                               = 0.670 kg {comment: 'Oxygen, according to the recipe of Zhao et al. (2021)'}
produces: |
  ukf:Syngas                                   = 1 kg
---
Gasification of corn stover is assumed to be equivalent to {system:ref}`SugarCaneBagasseGasificationToSyngas`.
```


```{system:process} WheatStrawGasificationToSyngas
---
consumes: |
  WheatStraw                                   = 1.674 kg
  ukf:PureOxygen                               = 0.670 kg {comment: 'Oxygen, according to the recipe of Zhao et al. (2021)'}
produces: |
  ukf:Syngas                                   = 1 kg
---
Gasification of wheat straw is assumed to be equivalent to {system:ref}`SugarCaneBagasseGasificationToSyngas`.

```


```{system:process} RiceStrawGasificationToSyngas
---
consumes: |
  RiceStraw                                    = 1.674 kg
  ukf:PureOxygen                               = 0.670 kg {comment: 'Oxygen, according to the recipe of Zhao et al. (2021)'}
produces: |
  ukf:Syngas                                   = 1 kg
---
Gasification of wheat straw is assumed to be equivalent to {system:ref}`SugarCaneBagasseGasificationToSyngas`.
```

```{end-sub-processes}
```

These object types need to be defined for these biomass feedstocks:

```{system:object} SugarCaneBagasse
SugarCaneBagasse is consumed to produce ethyl alcohol
```

```{system:object} CornStover
CornStover is consumed to produce ethyl alcohol
```

```{system:object} WheatStraw
WheatStraw is consumed to produce ethyl alcohol
```

```{system:object} RiceStraw
RiceStraw is consumed to produce ethyl alcohol
```

And other inputs:

```{system:object} Nutrients
Nutrients is consumed to produce ethyl alcohol
```

## Hydrogen

These processes represent production of "grey", "blue" and "green" hydrogen respectively:

```{system:object} PureHydrogen
PureHydrogen is produced from steam methane reforming and electrolysis.
```

```{system:process} HydrogenSynthesis
:become_parent: true
```

```{system:process} NaturalGasSteamMethaneReformingToHydrogen
---
consumes: |
  ukf:NaturalGas                               = 2.30 kg
produces: |
  PureHydrogen                                 = 1 kg
---
Recipe based on {cite:t}`oni_comparative_2022`.
Note that the indirect and process emissions of this process totals to 9.54 kgCO2eq. Note there is an imbalance of 1.30 kg (output emissions not included in recipe).
```

```{system:process} NaturalGasSteamMethaneReformingWithCCSToHydrogen
---
consumes: |
  ukf:NaturalGas                               = 2.30 kg
produces: |
  PureHydrogen                                 = 1 kg
---
Recipe based on {cite:t}`oni_comparative_2022`.
Note that the indirect and process emissions of this process totals to 3.68 kgCO2eq. Note there is an imbalance of 1.30 kg (output emissions not included in recipe).
```

```{system:process} WaterElectrolysisForHydrogen
---
consumes: |
  ukf:Water                                    = 9 kg
produces: |
  PureHydrogen                                 = 1 kg
---
Recipe based on {cite:t}`iea_world_2021`.
Note there is an imbalance of 8 kg (output emissions not included in recipe).
```


```{end-sub-processes}
```

(ethyl-alcohol)=
## Ethyl alcohol

Ethyl alcohol, an intermediate for ethylene production, is produced from biomass by fermentation.

```{system:object} EthylAlcohol
```

The feedstock materials are defined already in the UK FIRES production system map {cite}`lupton_ukproductionsystem_2024`, reproduced here for completeness:

```{system:object} ukf:Maize
```

```{system:object} ukf:SugarCane
```

Production processes:

```{system:process} EthylAlcoholSynthesisFromBiomass
:become_parent: true
```

```{system:process} EthylAlcoholSynthesisFromSugarcane
---
consumes: |
  ukf:SugarCane                                = 35 kg
  ukf:OtherInorganicPrimaryChemicals           = 0.12 kg  
produces: |
  EthylAlcohol                                 = 1 kg
  ukf:WasteBiomass                             = 2.5 kg {comment: 'Sugarcane (raw)'}
---
{cite:t}`shelar_net_2023` report a yield of 0.06 kg ethanol per kg sugar cane, but this is higher than other recipes checked so a somewhat lower yield was assumed here to be representative.
Other inputs are mostly phosphate, with some calcium oxide. Note there is an imbalance of 31.7 kg (additional output flows not included in recipe).
```


```{system:process} EthylAlcoholSynthesisFromSugarcaneBagasse
---
consumes: |
  SugarCaneBagasse                             = 4.5 kg
  Nutrients                                    = 0.07 kg
  ukf:OtherInorganicPrimaryChemicals           = 0.53 kg {comment: 'Diammonium phosphate, gypsum disposal, and lime'}
  ukf:InorganicAcids                           = 0.18 kg {comment: 'Sulfuric acid'}
produces: |
  EthylAlcohol                                 = 1 kg
---
{cite:t}`zabed_fuel_2016` report a yield range of 0.2043 to 0.3914 kg ethanol per kg crop residue, with this recipe falling towards the lower end.
Other inputs include diammonium phosphate, gypsum disposal, and lime. Note there is an imbalance of 4.3 kg (additional output flows not included in recipe).
```

```{system:process} EthylAlcoholSynthesisFromMaize
---
consumes: |
  ukf:Maize                                    = 4.0 kg
  ukf:Ammonia                                  = 0.008 kg
  ukf:OtherInorganicPrimaryChemicals           = 0.005 kg {comment: 'Lime'}
  ukf:InorganicAcids                           = 0.008 kg {comment: 'Sulfuric acid'}
produces: |
  EthylAlcohol                                 = 1 kg
  ukf:WasteBiomass                             = 1.1 kg
---
{cite:t}`dees_cost_2023` report a yield of 0.33 kg ethanol per kg maize, but this is higher than other recipes checked so a somewhat lower yield was assumed here to be representative.
Note there is an imbalance of 1.9 kg (additional output flows not included in recipe).
```

```{system:process} EthylAlcoholSynthesisFromCornStover
---
consumes: |
  CornStover                                   = 5.5 kg
  ukf:Ammonia                                  = 0.17 kg
  ukf:OtherInorganicPrimaryChemicals           = 0.0051 kg {comment: 'Diammonium phosphate'}
  ukf:InorganicAcids                           = 0.057 kg {comment: 'Sulfuric acid'}
produces: |
  EthylAlcohol                                 = 1 kg
  ukf:WasteBiomass                             = 1.5 kg {comment: 'Lignin residues'}
---
{cite:t}`zabed_fuel_2016` report a yield range of 0.2043 to 0.3914 kg ethanol per kg crop residue, but this is higher than other recipes checked so a somewhat lower yield was assumed here to be representative.
Other inputs include diammonium phosphate. Note there is an imbalance of 3.3 kg (additional output flows not included in recipe).
```


```{system:process} EthylAlcoholSynthesisFromWheatStraw
---
consumes: |
  WheatStraw                                   = 5.6 kg
  Nutrients                                    = 0.10 kg
  ukf:OtherInorganicPrimaryChemicals           = 0.19 kg {comment: 'Diammonium phosphate and lime'}
  ukf:InorganicAcids                           = 0.19 kg {comment: 'Sulfuric acid'}
produces: |
  EthylAlcohol                                 = 1 kg
---
{cite:t}`zabed_fuel_2016` report a yield range of 0.2043 to 0.3914 kg ethanol per kg crop residue, but this is higher than other recipes checked so a somewhat lower yield was assumed here to be representative.
Other inputs include diammonium phosphate and lime. Note there is an imbalance of 5.1 kg (additional output flows not included in recipe).
```


```{system:process} EthylAlcoholSynthesisFromRiceStraw
---
consumes: |
  RiceStraw                                    = 6.038362102 kg
  Nutrients                                    = 0.10 kg
  ukf:OtherInorganicPrimaryChemicals           = 0.20 kg {comment: 'Diammonium phosphate and lime'}
  ukf:InorganicAcids                           = 0.20 kg {comment: 'Sulfuric acid'}
produces: |
  EthylAlcohol                                 = 1 kg
---
Because wheat straw and rice straw have little to no difference in composition {cite}`bakker_rice_2013`, this recipe is similar to {system:ref}`EthylAlcoholSynthesisFromWheatStraw`, but adjusted by the ratio of the cellulose & hemicellulose composition of wheat straw that of rice straw. 
```

```{end-sub-processes}
```

(methyl-alcohol)=
## Methyl alcohol

Methyl alcohol can be produced from syngas or from hydrogen:

```{system:object} CapturedCarbonDioxide
CapturedCarbonDioxide is captured carbon dioxide from point sources and is consumed for methyl alcohol production
```

```{system:process} CarbonDioxideHydrogenationToMethylAlcohol
---
consumes: |
  CapturedCarbonDioxide                        = 1.441 kg
  PureHydrogen                                 = 0.203 kg
  ukf:OtherInorganicPrimaryChemicals           = 0.00183 kg {comment: 'Catalyst'}
produces: |
  ukf:MethylAlcohol                            = 1 kg
  ukf:OtherIndustrialGases                     = 0.066 kg {comment: 'Carbon dioxide'}
  ukf:WasteOtherChemicals                      = 0.578 kg {comment: 'Water'}
---
This recipe was based from from the work of {cite:t}`rosental_life_2020`. Note that the `OtherIndustrialGases` includes carbon dioxide.
```

```{system:process} MethylAlcoholSynthesis
---
consumes: |
  ukf:Syngas                                    = 1.5 kg
produces: |
  ukf:MethylAlcohol                             = 1.0 kg
---
```
