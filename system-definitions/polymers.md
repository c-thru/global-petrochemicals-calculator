Polymers
========

```{system:object} Polymers
:become_parent: true
:composed_of: ukf:LDPEPolyethylene ukf:HDPEPolyethylene ukf:PPPolypropylene ukf:PSPolystyrene ukf:PVCPolyvinylChloride ukf:PETPolyethyleneTerephthalatePolyesters ukf:Polyurethane ukf:SyntheticRubbers ukf:OtherPolymers
```

Most of the polymers are already defined in the UK FIRES production system structure {cite}`lupton_ukproductionsystem_2024`:

```{system:object} ukf:LDPEPolyethylene
:label: LDPE, Polyethylene
```

```{system:object} ukf:HDPEPolyethylene
:label: HDPE, Polyethylene
```

```{system:object} ukf:PPPolypropylene
:label: PP, Polypropylene
```

```{system:object} ukf:PSPolystyrene
:label: PS, Polystyrene
```

```{system:object} ukf:PVCPolyvinylChloride
:label: PVC, Polyvinyl chloride
```

```{system:object} ukf:PETPolyethyleneTerephthalatePolyesters
:label: PET, Polyethylene terephthalate, polyesters
```

```{system:object} ukf:Polyurethane
:label: Polyurethane
```

```{system:object} ukf:SyntheticRubbers
:label: Synthetic rubbers
```

```{system:object} ukf:OtherPolymers
:label: Other polymers
```

But LLDPE and PPA need to be defined in addition here:

```{system:object} LLDPE
"Linear low density PE"
```

```{system:object} FibrePPA
"Polyphthalamide"
```

```{end-sub-objects}
```

```{system:process} ProductionOfPolymers
:become_parent: true
:composed_of: ukf:PolymerisationOfLDPE ukf:PolymerisationOfHDPE ukf:PolymerisationOfPP ukf:PolymerisationOfPolystyrene ukf:PolymerisationOfPVC ukf:PolymerisationOfPET ukf:PolymerisationOfPolyurethane ukf:PolymerisationOfStyreneButadiene ukf:PolymerisationOfOtherPolymers
```

Most of the polymerisation processes are already defined:

````{system:process} ukf:PolymerisationOfLDPE
---
consumes: |
  ukf:Ethylene                                 = 1.03 kg
produces: |
  ukf:LDPEPolyethylene                         = 1.0 kg
  ukf:WasteOtherChemicals                      = 0.03 kg {comment: 'Assume 3% polymerisation loss'}  
---

The calculations behind this recipe are in {download}`an accompanying spreadsheet <BasicChemicalsAndPlasticsProduction_recipe.xlsx>`.

Process yield of 97.1% is calculated based on average tonnages of inputs required directly reported in {cite}`OrbiChem2016`. 

This recipe is from {cite}`levi_mapping_2018`. This is the global average of capacity for 2013. The polymerisation of LDPE in the UK might have a different recipe.
````

````{system:process} ukf:PolymerisationOfHDPE
---
consumes: |
  ukf:Ethylene                                 = 1.05 kg
produces: |
  ukf:HDPEPolyethylene                         = 1.0 kg
  ukf:WasteOtherChemicals                      = 0.03 kg {comment: 'Assume 5% polymerisation loss'}  
  
---

The calculations behind this recipe are in {download}`an accompanying spreadsheet <BasicChemicalsAndPlasticsProduction_recipe.xlsx>`.

Process yield of 95.2% is calculated based on average tonnages of inputs required directly reported in {cite}`OrbiChem2016`. 

This recipe is from {cite}`levi_mapping_2018`. This is the global average of capacity for 2013. The polymerisation of HDPE in the UK might have a different recipe.
````

````{system:process} ukf:PolymerisationOfPP
---
consumes: |
  ukf:Propylene                                = 1.02 kg
produces: |
  ukf:PPPolypropylene                          = 1.0 kg
  ukf:WasteOtherChemicals                      = 0.02 kg {comment: 'Assume 2% polymerisation loss'}
---

The calculations behind this recipe are in {download}`an accompanying spreadsheet <BasicChemicalsAndPlasticsProduction_recipe.xlsx>`.

Process yield of 98% is calculated based on average tonnages of inputs required directly reported in {cite}`OrbiChem2016`. 

This recipe is from {cite}`levi_mapping_2018`. This is the global average of capacity for 2013. The polymerisation of PP in the UK might have a different recipe.
````

````{system:process} ukf:PolymerisationOfPolystyrene
---
consumes: |
  ukf:Styrene                                  = 1.02 kg {comment: 'styrene n(C8H8)'}
produces: |
  ukf:PSPolystyrene                            = 1.0 kg
  ukf:WasteOtherChemicals                      = 0.02 kg {comment: 'Assume 2% polymerisation loss'}    
---

The calculations behind this recipe are in {download}`an accompanying spreadsheet <BasicChemicalsAndPlasticsProduction_recipe.xlsx>`.

Process yield of 98% is calculated based on average tonnages of inputs required directly reported in {cite}`OrbiChem2016` but assume 2% polymerisation loss. 

This recipe is from {cite}`levi_mapping_2018`. This is the global average of capacity for 2013. The polymerisation of polystyrene in the UK might have a different recipe.
````

````{system:process} ukf:PolymerisationOfPVC
---
consumes: |
  ukf:VinylChloride                            = 1.03 kg
produces: |
  ukf:PVCPolyvinylChloride                     = 1.0 kg {comment: '(C2H3Cl)n'}
  ukf:WasteOtherChemicals                      = 0.03 kg {comment: 'Assume 3% polymerisation loss'} 
---

The calculations behind this recipe are in {download}`an accompanying spreadsheet <BasicChemicalsAndPlasticsProduction_recipe.xlsx>`.

Process yield of 97.1% is calculated based on average tonnages of inputs required directly reported in {cite}`OrbiChem2016`. 

This recipe is from {cite}`levi_mapping_2018`. This is the global average of capacity for 2013. The polymerisation of PVC in the UK might have a different recipe.
````

````{system:process} ukf:PolymerisationOfPET
---
consumes: |
  ukf:EthyleneGlycol                           = 0.34 kg {comment: 'ethylene glycol n(C2H6O2)'}
  ukf:TerephthalicAcidPhthalicAnhydrideDioctylPhthalate= 0.87 kg {comment: 'terephthalate acid (C8H6O4)'}
produces: |
  ukf:PETPolyethyleneTerephthalatePolyesters   = 1.0 kg
  ukf:Water                                    = 0.19 kg
  ukf:WasteOtherChemicals                      = 0.02 kg  
---

The calculations behind this recipe are in {download}`an accompanying spreadsheet <BasicChemicalsAndPlasticsProduction_recipe.xlsx>`.

Process yield of 99.4% for terephthalic acid is calculated based on average tonnages of inputs required directly reported in {cite}`OrbiChem2016` and 95% for ethylene glycol is calcuated based on {cite}`ASIACHEM2011`. 

This recipe is from {cite}`levi_mapping_2018`. This is the global average of capacity for 2013. The polymerisation of PET in the UK might have a different recipe.
````

````{system:process} ukf:PolymerisationOfStyreneButadiene
---
consumes: |
  ukf:Butadiene                                = 0.77 kg
  ukf:Styrene                                  = 0.25 kg
produces: |
  ukf:SyntheticRubbers                         = 1.0 kg
  ukf:WasteOtherChemicals                      = 0.02 kg {comment: 'Assume 2% polymerisation loss'}    
---

The calculations behind this recipe are in {download}`an accompanying spreadsheet <BasicChemicalsAndPlasticsProduction_recipe.xlsx>`.

Process yield of 95.2% is calculated assuming an average composition: 25% Styrene, 75% butadiene. Assume 2% polymerisation loss reported in {cite}`Lide2016`. 

This recipe is from {cite}`levi_mapping_2018`. This is the global average of capacity for 2013. The polymerisation of styrene butadiene in the UK might have a different recipe.
````

However, these do not cover every polymer we are using here, so here are the two new production processes required:

```{system:process} PolymerisationOfLLDPE
---
consumes: |
  ukf:Ethylene                             = 0.97 kg
  ukf:Butylenes                            = 0.08 kg
produces: |
  LLDPE                                    = 1.0 kg
---
```

```{system:process} PolymerisationOfFibrePPA
---
consumes: |
  ukf:Hexamethylenediamine                               = 0.48 kg 
  ukf:Water                                              = 0.46 kg
  ukf:TerephthalicAcidPhthalicAnhydrideDioctylPhthalate  = 0.44 kg
  IsophthalicAcid                                        = 0.17 kg
  ukf:AdipicAcid                                         = 0.06 kg
  ukf:OtherIntermediateOrganicChemicals                  = 0.005 kg
  ukf:OtherInorganicPrimaryChemicals                     = 0.002 kg
produces: |
  FibrePPA                                               = 1.00 kg
---
```

```{system:process} PolymerisationOfPUR
---
consumes: |
  TolueneDiisocyanate                                    = 0.39 kg 
  Polyols                                                = 0.66 kg
  ukf:OtherIntermediateOrganicChemicals                  = 0.01 kg
produces: |
  ukf:Polyurethane                                       = 1.00 kg
---

In general polyurethane is made from a combination of TDI (toluene diisocyanate) and MDI (methylene diphenyl diisocyanate), but for simplicity we represent both as "TDI" here.
```

Similarly for polymerisation of "other polymers":

```{system:process} PolymerisationOfOtherPolymers
---
consumes: |
  ukf:Acrylonitrile                            = 0.25 kg
  ukf:Butadiene                                = 0.20 kg
  ukf:Styrene                                  = 0.57 kg
produces: |
  ukf:OtherPolymers                            = 1 kg
---
Based on the data of Yunhu et al., 80% of the other polymers produced in 2020 are thermoplastic, for which 40% (or about half) is ABS. Hence, the process recipe to for production of `OtherPolymers` is based on ABS production. 
```


```{end-sub-processes}
```

