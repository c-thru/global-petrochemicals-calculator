Organic chemicals
=================

These processes synthesise downstream organic chemicals.

From UK FIRES production system model {cite}`lupton_ukproductionsystem_2024`, reproduced here:

````{system:process} ukf:AdipicAcidSynthesis
---
consumes: |
  ukf:Cyclohexane                              = 0.72 kg {comment: 'cyclohexane (C6H12)'}
  ukf:PureOxygen                               = 0.27 kg {comment: 'oxygen(O2)'}
  ukf:InorganicAcids                           = 0.40 kg {comment: 'nitrous (HNO2) acid'}
  ukf:NitricAcid                               = 0.54 kg {comment: 'nitric (HNO3) acid'}
  ukf:Water                                    = 0.15 kg
produces: |
  ukf:AdipicAcid                               = 1.00 kg {comment: 'adipic acid (C6H10O4)'}
  ukf:OtherIndustrialGases                     = 0.30 kg {comment: 'Dinitrogen oxide (N2O); this was classified as OtherInorganicPrimaryChemicals'}
  ukf:Water                                    = 0.40 kg
  ukf:WasteOtherChemicals                      = 0.33 kg {comment: 'waste cyclohexane (C6H12)+ waste nitrous (HNO2) acid + waste nitric (HNO3) acid'}
  ukf:Air                                      = 0.05 kg {comment: 'wasted O2'}  
---

The calculations behind this recipe are in {download}`an accompanying spreadsheet <BasicChemicalsAndPlasticsProduction_recipe.xlsx>`.

Process yield of 80% is calculated based on average tonnages of inputs required directly reported in {cite}`OrbiChem2016`.

This recipe is from {cite}`levi_mapping_2018`. This is the global average of capacity for 2013.
````

````{system:process} ukf:AceticAcidSynthesis
---
consumes: |
  ukf:MethylAlcohol                            = 0.54 kg
  ukf:OtherIndustrialGases                     = 0.47 kg {comment: 'carbon monoxide (CO)'}
produces: |
  ukf:AceticAcid                               = 1.00 kg
  ukf:OtherIndustrialGases                     = 0.01 kg {comment: 'carbon monoxide (CO)''}
  ukf:WasteOtherChemicals                      = 0.01 kg {comment: 'waste methyalcohol'}
---

The calculations behind this recipe are in {download}`an accompanying spreadsheet <BasicChemicalsAndPlasticsProduction_recipe.xlsx>`.

Process yield of 98.5% is Monsanto process about 98% yield on methanol, Cativa 99%+ in {cite}`levi_mapping_2018`.

This recipe is from {cite}`levi_mapping_2018`. This is the global average of capacity for 2013.
````

````{system:process} ukf:StyreneSynthesis
---
consumes: |
  ukf:Ethylene                                 = 0.28 kg {comment: 'ethylene (C2H4)'}
  ukf:Benzene                                  = 0.79 kg {comment: 'benzene (C6H6)'}
produces: |
  ukf:Styrene                                  = 1.0 kg  {comment: 'Styrene (C8H8)'}
  ukf:OtherIndustrialGases                     = 0.02 kg {comment: 'Hydrogen (H2)'}
  ukf:WasteOtherChemicals                      = 0.05 kg {comment: 'waste ethylene (C2H4)+waste benzene (C6H6)'}
---

The calculations behind this recipe are in {download}`an accompanying spreadsheet <BasicChemicalsAndPlasticsProduction_recipe.xlsx>`.

Process yield of 95.2% is calculated based on process yield of 99% for ethylbenzene in {cite}`Wells1999` and process yield of 96.2 % for average tonnages of inputs required directly reported for styrene conversion in {cite}`OrbiChem2016`. 

This recipe is from {cite}`levi_mapping_2018`. This is the global average of capacity for 2013. 
````

````{system:process} ukf:VinylChlorideSynthesis
---
consumes: |
  ukf:Ethylene                                 = 0.49 kg {comment: 'C2H4'}
  ukf:Chlorine                                 = 0.62 kg {comment: 'direct chlorination (Cl2)'}
  ukf:InorganicAcids                           = 0.64 kg {comment: 'hydrogen chloride (HCl)'}
  ukf:PureOxygen                               = 0.14 kg
produces: |
  ukf:VinylChloride                            = 1 kg
  ukf:InorganicAcids                           = 0.64 kg {comment: 'hydrogen chloride (HCl)'}
  ukf:Water                                    = 0.14 kg
  ukf:WasteOtherChemicals                      = 0.04 kg {comment: 'waste ethylene (C2H4)'}
  ukf:OtherIndustrialGases                     = 0.09 kg {comment: 'wasted chlorine'}
  ukf:Air                                      = 0.01 kg {comment: 'wasted O2'}
---

The calculations behind this recipe are in {download}`an accompanying spreadsheet <BasicChemicalsAndPlasticsProduction_recipe.xlsx>`.

Process yield of 91.6% is calculated based on average tonnages of inputs required directly reported in {cite}`OrbiChem2016`. 

This recipe is from {cite}`levi_mapping_2018`. This is the global average of capacity for 2013. 
````

````{system:process} ukf:EthyleneGlycolSynthesis
---
consumes: |
  ukf:Ethylene                                 = 0.60 kg {comment: 'ethylene (C2H4).'}
  ukf:PureOxygen                               = 0.34 kg
  ukf:Water                                    = 0.39 kg
produces: |
  ukf:EthyleneGlycol                           = 1 kg {comment: 'C2H6O2'}
  ukf:Air                                      = 0.08 kg {comment: 'wasted O2'}
  ukf:WasteOtherChemicals                      = 0.15 kg {comment: 'ethylene (C2H4)'}
  ukf:Water                                    = 0.10 kg
---

This recipe is from {cite}`levi_mapping_2018`. This is the global average of capacity for 2013.

`Air` and `Water` in the outputs represent unreacted oxygen and water that are wasted, `WasteOtherChemicals` represents unreacted ethylene. The quantities of these outputs were calculated based on a process yield of 75.3%, reported by {cite}`OrbiChem2016`. This yield is the ratio of actual `Ethylene` required to produce `EthyleneGlycol` and the theoretical quantity.

The calculations behind this recipe are in {download}`an accompanying spreadsheet <BasicChemicalsAndPlasticsProduction_recipe.xlsx>`.
````

````{system:process} ukf:TerephthalicAcidSynthesis
---
consumes: |
  ukf:Xylenes                                  = 0.67 kg
  ukf:PureOxygen                               = 0.61 kg
produces: |
  ukf:TerephthalicAcidPhthalicAnhydrideDioctylPhthalate = 1 kg
  ukf:Water                                    = 0.22 kg
  ukf:WasteOtherChemicals                      = 0.03 kg {comment: 'waste xylene (C8H10)'}
  ukf:Air                                      = 0.08 kg {comment: 'wasted O2'}
---

The calculations behind this recipe are in {download}`an accompanying spreadsheet <BasicChemicalsAndPlasticsProduction_recipe.xlsx>`.

Process yield of 95.4% is calculated based on average tonnages of inputs required directly reported in {cite}`OrbiChem2016`.

This recipe is from {cite}`levi_mapping_2018`. This is the global average of capacity for 2013.
````

````{system:process} ukf:CyclohexaneSynthesis
---
consumes: |
  ukf:Benzene                                  = 0.94 kg
  ukf:OtherIndustrialGases                     = 0.07 kg {comment: 'Hydrogen (H2)'}
produces: |
  ukf:Cyclohexane                              = 1.0 kg
  ukf:OtherIndustrialGases                     = 0.01 kg {comment: 'waste Hydrogen (H2)'}
---

The calculations behind this recipe are in {download}`an accompanying spreadsheet <BasicChemicalsAndPlasticsProduction_recipe.xlsx>`.

Process yield of 98.7% is calculated based on average tonnages of inputs required directly reported in {cite}`OrbiChem2016`.

This recipe is from {cite}`levi_mapping_2018`. This is the global average of capacity for 2013.
````

````{system:process} ukf:OtherOrganicChemicalsSynthesis
---
consumes: |
  ukf:Butylenes                                = 0.14285714285714285 kg
  ukf:Benzene                                  = 0.14285714285714285 kg
  ukf:Propylene                                = 0.14285714285714285 kg
  ukf:Toluene                                  = 0.14285714285714285 kg
  ukf:Xylenes                                  = 0.14285714285714285 kg
  ukf:Ethylene                                 = 0.14285714285714285 kg
  ukf:Butadiene                                = 0.14285714285714285 kg
produces: |
  ukf:OtherIntermediateOrganicChemicals        = 1.0 kg
---

Fall-back recipe to represent production of other intermediate organic chemicals (small quantities only, so this recipe is not critical).
````

Additional processes defined for this model:

```{system:process} HexamethylenediamineSynthesisFromButadiene
---
consumes: |
  ukf:Butadiene                                = 0.54 kg
  HydrogenCyanide                              = 0.54 kg
  ukf:OtherIndustrialGases                     = 0.07 kg {comment: 'Carbon dioxide and Hydrogen'}
  ukf:OtherInorganicPrimaryChemicals           = 0.18 kg
produces: |
  ukf:Hexamethylenediamine                     = 1 kg
  ukf:WasteOtherChemicals                      = 0.02 kg
---
This recipe represents synthesis of hexamethylenediamine, including the adiponitrile production from butadiene.
```

```{system:process} HydrogenCyanideSynthesis
---
consumes: |
  ukf:Ammonia                                  = 0.65 kg
  ukf:NaturalGas                               = 0.65 kg
produces: |
  HydrogenCyanide                              = 1 kg
---
```

```{system:process} IsophthalicAcidSynthesis
---
consumes: |
  ukf:Xylenes                                  = 0.68 kg
  ukf:Water                                    = 0.42 kg
  ukf:AceticAcid                               = 0.10 kg
produces: |
  IsophthalicAcid                              = 1 kg
---
Isophthalic acid is produced by oxidising xylenes.
```

```{system:process} TolueneDiisocyanateSynthesis
---
consumes: |
  ukf:Toluene                                  = 0.55 kg
  ukf:Chlorine                                 = 0.91 kg
  ukf:NitricAcid                               = 0.96 kg
  ukf:OtherIndustrialGases                     = 0.40 kg {comment: 'Carbon dioxide and Hydrogen'}
  ukf:OtherInorganicPrimaryChemicals           = 0.07 kg
produces: |
  TolueneDiisocyanate                          = 1 kg
  ukf:WasteOtherChemicals                      = 0.84 kg {comment: 'Hydrochloric acid'}
---
Toluene diisocyanate is produced from toluene.
```

```{system:process} PolyolsSynthesis
---
consumes: |
  PropyleneOxide                               = 0.9 kg
  EthyleneOxide                                = 0.1 kg
  ukf:OtherIntermediateOrganicChemicals        = 0.03 kg
  ukf:OtherInorganicPrimaryChemicals           = 0.04 kg
produces: |
  Polyols                                      = 1 kg
  ukf:WasteOtherChemicals                      = 0.01 kg
---
```

```{system:process} PropyleneOxideSynthesis
---
consumes: |
  ukf:Propylene                                = 0.86 kg
  ukf:PureOxygen                               = 0.8 kg
  PureHydrogen                                 = 0.07 kg
produces: |
  PropyleneOxide                               = 1 kg
---
```

```{system:process} EthyleneOxideSynthesis
---
consumes: |
  ukf:Ethylene                                 = 0.80 kg
  ukf:PureOxygen                               = 0.84 kg
produces: |
  EthyleneOxide                                = 1 kg
---
```

```{system:process} AcrylonitrileSynthesis
---
consumes: |
  ukf:Ammonia                                  = 0.44 kg
  ukf:Propylene                                = 1.09 kg
  ukf:InorganicAcids                           = 0.10 kg {comment: 'Sulfuric acid'}
produces: |
  ukf:Acrylonitrile                            = 1 kg
  HydrogenCyanide                              = 0.01 kg 
---
Note: another version of this process was already defined in the UK FIRES system.
```

Most of the main chemicals are already defined from the UK FIRES production system map {cite}`lupton_ukproductionsystem_2024`, and reproduced here for completeness:

```{system:object} ukf:OtherIntermediateOrganicChemicals
:label: Other intermediate organic chemicals
```

```{system:object} ukf:AdipicAcid
:label: Adipic acid
```

```{system:object} ukf:Hexamethylenediamine
```

```{system:object} ukf:AceticAcid
:label: Acetic acid
```

```{system:object} ukf:Styrene
```

```{system:object} ukf:VinylChloride
:label: Vinyl chloride
```

```{system:object} ukf:EthyleneGlycol
:label: Ethylene glycol
```

```{system:object} ukf:TerephthalicAcidPhthalicAnhydrideDioctylPhthalate
:label: Terephthalic acid, phthalic anhydride, dioctyl phthalate
```

```{system:object} ukf:Cyclohexane
```

```{system:object} ukf:Acrylonitrile
```


A few additional "objects" need to be defined for the calculator model:

```{system:object} HydrogenCyanide
Hydrogen cyanide is consumed to produce hexamethylenediamine
```


```{system:object} IsophthalicAcid
Isophthalic acid is consumed to produce polyphthalamide
```


```{system:object} TolueneDiisocyanate
TolueneDiisocyanate is consumed to produce polyurethane
```


```{system:object} PropyleneOxide
Propylene oxide is consumed to produce polyols
```


```{system:object} EthyleneOxide
Ethylene oxide is consumed to produce polyols
```


```{system:object} Polyols
Polyols is consumed to produce polyurethane
```

