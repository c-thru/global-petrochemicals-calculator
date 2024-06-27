Other chemical synthesis
========================

Other processes used in the model defined by the UK FIRES production system {cite}`lupton_ukproductionsystem_2024`, reproduced here:

```{system:process} ukf:MakingInorganicAcids
---
consumes: |
  ukf:ChemicalAndFertiliserMinerals            = 1.0 kg
produces: |
  ukf:InorganicAcids                           = 1.0 kg
---

Placeholder recipe for production of the small quantities of inorganic acids used in other processes.
```

```{system:process} ukf:MakingOtherInorganicPrimaryChemicals
---
consumes: |
  ukf:ChemicalAndFertiliserMinerals            = 1.0 kg
produces: |
  ukf:OtherInorganicPrimaryChemicals           = 1.0 kg
---

Placeholder recipe for production of the small quantities of inorganic acids used in other processes.
```

```{system:object} ukf:ChemicalAndFertiliserMinerals
```

```{system:object} ukf:InorganicAcids
```

```{system:object} ukf:NitricAcid
```

```{system:object} ukf:OtherInorganicPrimaryChemicals
```

A few miscellaneous/inorganic chemical processes are defined here:

```{system:process} ProducingNitricAcid
---
consumes: |
  ukf:Ammonia                                  = 0.27 kg
  ukf:PureOxygen                               = 1.02 kg
  ukf:Water                                    = 0.14 kg
produces: |
  ukf:NitricAcid                               = 1 kg
  ukf:Water                                    = 1.22 kg
---

Rescaled version of UK FIRES process.

Recipe from {cite}`levi_mapping_2018`.
```

```{system:process} AirSeparation
---
consumes: |
  ukf:Air                                      = 5.26 kg
produces: |
  ukf:PureOxygen                               = 1 kg
  ukf:Nitrogen                                 = 4.21 kg
  ukf:OtherIndustrialGases                     = 0.05 kg
---

Assumed recipe from composition of air
```

```{system:process} SodiumChlorideElectrolysisForChlorine
---
consumes: |
  ukf:Salt                                     = 1.67 kg
  ukf:OtherInorganicPrimaryChemicals           = 0.04 kg
  ukf:InorganicAcids                           = 0.02 kg {comment: 'Hydrochloric acid and Sulfuric acid'}
produces: |
  ukf:Chlorine                                 = 1 kg
  ukf:OtherInorganicPrimaryChemicals           = 1.10 kg {comment: 'Caustic soda'}
  ukf:OtherIndustrialGases                     = 0.03 kg {comment: 'Fuel gas'}
  ukf:InorganicAcids                           = 0.01 kg
---
This recipe represents production of chlorine by electrolysis of NaCl salt.
```


## Wastes and other misc objects

```{system:object} ukf:WasteOtherChemicals
```

```{system:object} ukf:OtherIndustrialGases
```

```{system:object} ukf:WasteBiomass
```

```{system:object} ukf:Water
```

```{system:object} ukf:PureOxygen
```

```{system:object} ukf:MiscRefineryProducts
```

```{system:object} ukf:Nitrogen
```

```{system:object} ukf:Air
```

```{system:object} ukf:Salt
```

```{system:object} ukf:Chlorine
```







