Primary chemicals
=================

These processes produce primary chemicals such as ethylene and BTX.

## Primary chemicals

Most of the main chemicals are already defined from the UK FIRES production system map {cite}`lupton_ukproductionsystem_2024`, reproduced here for completeness:

```{system:object} ukf:Ethylene
```

```{system:object} ukf:Propylene
```

```{system:object} ukf:Benzene
```

```{system:object} ukf:Toluene
```

```{system:object} ukf:Xylenes
```

```{system:object} ukf:Butylenes
```

```{system:object} ukf:Butadiene
```

```{system:object} ukf:Ammonia
```

```{system:object} ukf:MethylAlcohol
:label: Methyl alcohol
```

```{system:object} ukf:Syngas
```

A few additional "objects" need to be defined here.

## Fossil feedstocks

Steam cracking produces olefins (ethylene, propylene) from a range of fossil feedstocks.  Two feedstocks are modelled, ethane (which also represents other lighter feeds such as LPG) and naphtha (which also represents other heavier feeds). 

```{system:process} SteamCrackingOfNaphtha
---
consumes: |
  ukf:Naphtha                                  = 2.68 kg
produces: |
  ukf:Ethylene                                 = 1 kg
  ukf:Propylene                                = 0.48 kg
  ukf:Butylenes                                = 0.21 kg {comment: 'C4 fraction'}
  PyrolysisGasoline                            = 0.46 kg
  ukf:NaturalGas                               = 0.50 kg {comment: 'Fuel gas'}
  ukf:MiscRefineryProducts                     = 0.03 kg {comment: 'Fuel oil'}
---
This recipe represents a generic steam cracking process from naphtha.

Note that the output of fuel gas is categorised as "natural gas", so it can in principle displace natural gas for combustion as utility.
```


```{system:process} SteamCrackingOfEthane
---
consumes: |
  ukf:Ethane                                   = 1.25 kg
produces: |
  ukf:Ethylene                                 = 1 kg
  ukf:Propylene                                = 0.03 kg
  ukf:Butadiene                                = 0.04 kg
  ukf:NaturalGas                               = 0.18 kg {comment: 'Fuel gas'}
---
This recipe represents a generic steam cracking process from ethane.

Note that the output of fuel gas is categorised as "natural gas", so it can in principle displace natural gas for combustion as utility.
```

```{system:object} GasOil
GasOil from crude oil refining is consumed for propylene production via fluid catalytic cracking
```

```{system:process} FluidCatalyticCrackingOfGasOil
---
consumes: |
  GasOil                                       = 4.4 kg
produces: |
  ukf:Propylene                                = 1 kg
  ukf:Ethylene                                 = 0.1 kg
  ukf:Butylenes                                = 0.9 kg 
  ukf:Propane                                  = 0.1 kg 
  ukf:NaturalGas                               = 0.3 kg {comment: 'Fuel gas'}
  ukf:MiscRefineryProducts                     = 1.6 kg {comment: 'gasoline, oil, column bottoms'}
---
This recipe represents a generic catalytic cracking process producing mainly propylene from gas oil.

Note that the output of fuel gas is categorised as "natural gas", so it can in principle displace natural gas for combustion as utility.
```


```{system:process} CatalyticReformingOfNaphthaForToluene
---
consumes: |
  ukf:Naphtha                                  = 6.75 kg
produces: |
  ukf:Toluene                                  = 1 kg
  ukf:Benzene                                  = 0.25 kg
  ukf:NaturalGas                               = 0.1 kg {comment: 'Fuel gas'}
  ukf:OtherIndustrialGases                     = 0.3 kg {comment: 'Hydrogen and LPG'}
  ukf:MiscRefineryProducts                     = 4.2 kg {comment: 'C8+ aromatics and prefrac bottoms'}
  ukf:WasteOtherChemicals                      = 0.5 kg {comment: 'BTX extraction raffinate'}
---
This recipe represents generic catalytic reforming of naphtha for toluene. 

Note that the output of fuel gas is categorised as "natural gas", so it can in principle displace natural gas for combustion as utility.
```


```{system:process} CatalyticReformingOfNaphthaForXylenes
---
consumes: |
  ukf:Naphtha                                  = 1.85 kg
  PureHydrogen                                 = 0.05 kg
produces: |
  ukf:Xylenes                                  = 1 kg
  ukf:Benzene                                  = 0.22 kg
  ukf:NaturalGas                               = 0.03 kg {comment: 'Fuel gas'}
  ukf:OtherIndustrialGases                     = 0.17 kg {comment: 'Hydrogen and LPG'}
  ukf:MiscRefineryProducts                     = 0.03 kg {comment: 'Heavy aromatics bottom'}
  ukf:WasteOtherChemicals                      = 0.24 kg {comment: 'BTX extraction raffinate'}
---
This recipe represents generic catalytic reforming of naphtha for p-xylene. 

Note that the output of fuel gas is categorised as "natural gas", so it can in principle displace natural gas for combustion as utility.
```

To balance remaining demand not supplied by co-production of other processes, "on-purpose" production from propane and butane can be used.

```{system:process} DehydrogenationOfPropane
---
consumes: |
  ukf:Propane                                  = 1.2 kg
produces: |
  ukf:Propylene                                = 1 kg
  ukf:NaturalGas                               = 0.16 kg {comment: 'Fuel gas'}
---
This recipe represents generic dehydrogenation of propane for propylene. 
```

```{system:process} DehydrogenationOfButaneForButadiene
---
consumes: |
  ukf:Butane                                   = 1.7 kg
produces: |
  ukf:Butadiene                                = 1 kg
---
This recipe represents generic dehydrogenation of butane for butadiene. 
```

## From methyl alcohol

Collectively, these processes are known as methanol-to-X (MTX).  Methanol production processes are defined in {ref}`methyl-alcohol`.

Methanol-to-olefins (MTO) is already used to produce ethylene and other olefines.  Methanol-to-propylene (MTP) increases the fraction of propylene in the output.

```{system:process} MethylAlcoholToOlefins
---
consumes: |
  ukf:MethylAlcohol                             = 4.3 kg
  ukf:OtherInorganicPrimaryChemicals            = 0.1 kg {comment: 'Caustic soda'}
produces: |
  ukf:Ethylene                                  = 1 kg
  ukf:Propylene                                 = 0.5 kg
  ukf:Butylenes                                 = 0.23 kg {comment: 'C4 fraction'}
  ukf:NaturalGas                                = 0.03 kg {comment: 'Methane'}
  ukf:Ethane                                    = 0.04 kg
  ukf:Propane                                   = 0.03 kg
---
This process represents a generic methanol-to-olefin process.
```

```{system:process} MethylAlcoholToPropylene
---
consumes: |
  ukf:MethylAlcohol                            = 3.46 kg
produces: |
  ukf:Propylene                                = 1 kg
  ukf:Ethylene                                 = 0.05 kg
  ukf:MiscRefineryProducts                     = 0.32 kg {comment: 'Gasoline and LPG'}
---
This process represents a generic methanol-to-propylene process.
```

Methanol-to-aromatics (MTA) is an earlier-stage technology but is being developed:

```{system:process} MethylAlcoholToAromatics
---
consumes: |
  ukf:MethylAlcohol                            = 9.93 kg
produces: |
  ukf:Xylenes                                  = 1 kg
  ukf:Benzene                                  = 0.15 kg
  ukf:Toluene                                  = 0.49 kg
  ukf:OtherIndustrialGases                     = 2.44 kg {comment: 'Dry gas and LPG'}
  ukf:MiscRefineryProducts                     = 0.67 kg {comment: 'Pentane and C9+'}
  ukf:WasteOtherChemicals                      = 5.18 kg {comment: 'Water'}
---
This recipe is from the work of {cite:t}`jiang_comparative_2020`. The `WasteOtherChemicals` is largely water.
```

## From ethyl alcohol

Ethyl alcohol (ethanol) production processes are defined in {ref}`ethyl-alcohol`.

Ethyl alcohol can be used to produce ethylene:

```{system:process} DehydrationOfEthylAlcohol
---
consumes: |
  EthylAlcohol                                 = 1.77 kg
produces: |
  ukf:Ethylene                                 = 1 kg
  ukf:NaturalGas                               = 0.02 kg {comment: 'Fuel gas'}
---
This recipe represents ethylene production from ethyl alcohol by dehydration.

Note that the output of fuel gas is categorised as "natural gas", so it can in principle displace natural gas for combustion as utility.
```

## Other chemicals

```{system:process} SyngasToAmmoniaProduction
---
consumes: |
  ukf:Syngas                                   = 1.61 kg
produces: |
  ukf:Ammonia                                  = 1 kg
  ukf:OtherIndustrialGases                     = 0.59 kg {comment: 'Carbon dioxide and Methane'}
  ukf:Nitrogen                                 = 0.003 kg
  ukf:Water                                    = 0.008 kg
---

This recipe was based on the work of {cite:t}`florez-orrego_ammonia_2023`. Carbon dioxide and methane are categorised as `OtherIndustrialGases`. Note that the values need to be reviewed, but this recipe is more consistent with the literature in terms of the components.
```


```{system:process} FischerTropschSynthesisOfOlefinsFromSyngas
---
consumes: |
  ukf:Syngas                                   = 28.89745333 kg
produces: |
  ukf:Propylene                                = 1 kg
  ukf:Ethylene                                 = 0.667 kg
  ukf:Butylenes                                = 0.333 kg {comment: 'C4 fraction, according to Zhao et al. (2021)'}
  ukf:MiscRefineryProducts                     = 1.944 kg {comment: 'Methane-hydrogen mixture, Refinery gas, and C5+ fraction, according to Zhao et al. (2021), were lumped together'}
---
This recipe was based on the work of {cite:t}`zhao_economic_2021`. Methane-hydrogen mixture, Refinery gas, and C5+ fraction were lumped together and assumed to be the same as MiscRefineryProducts.
```


## Conversion processes

Many primary chemicals are produced as co-products, so to reach the required mix it is necessary to further convert unwanted co-products into demanded chemicals.

```{system:process} DistillationOfButylenesForButadiene
---
consumes: |
  ukf:Butylenes                                = 2.3 kg
produces: |
  ukf:Butadiene                                = 1 kg
  ukf:WasteOtherChemicals                      = 1.3 kg {comment: 'Butadiene raffinate'}
---
This recipe represents distillation of butylenes for butadiene. 
```

Pyrolysis gasoline, a co-product of steam cracking of heavier feeds, can be distilled to produce BTX:

```{system:object} PyrolysisGasoline
PyrolysisGasoline is produced from steam cracking of naphtha, ethane, or crude oil, which is then distilled to produce BTX
```

```{system:process} DistillationOfPyrolysisGasolineForBTX
---
consumes: |
  PyrolysisGasoline                            = 2.00 kg
produces: |
  ukf:Benzene                                  = 1.00 kg
  ukf:Toluene                                  = 0.50 kg
  ukf:Xylenes                                  = 0.35 kg
  ukf:WasteOtherChemicals                      = 0.15 kg {comment: 'BTX extraction raffinate'}
---
This recipe represents distillation of pyrolysis gasoline for BTX.
```

Much of the toluene that is produced is converted to benzene and xylenes:

```{system:process} DisproportionationOfTolueneForXylenes
---
consumes: |
  ukf:Toluene                                  = 2.19 kg
  PureHydrogen                                 = 0.01 kg
produces: |
  ukf:Xylenes                                  = 1.00 kg
  ukf:Benzene                                  = 1.00 kg
  ukf:NaturalGas                               = 0.15 kg {comment: 'Fuel gas'}
  ukf:MiscRefineryProducts                     = 0.05 kg {comment: 'C9+ aromatics'}
---
This recipe represents disproportionation of toluene for p-xylene and benzene.

Note that the output of fuel gas is categorised as "natural gas", so it can in principle displace natural gas for combustion as utility.
```

```{system:process} DealkylationOfTolueneForBenzene
---
consumes: |
  ukf:Toluene                                  = 1.19 kg
  PureHydrogen                                 = 0.03 kg
produces: |
  ukf:Benzene                                  = 1.00 kg
  ukf:NaturalGas                               = 0.22 kg {comment: 'Fuel gas'}
---
This recipe represents dealkylation of toluene for benzene.

Note that the output of fuel gas is categorised as "natural gas", so it can in principle displace natural gas for combustion as utility.
```
