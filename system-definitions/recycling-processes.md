Recycling processes
===================

The polymers from end of life processes can be recycled. The thermoplastics polymers can be mechanically recycled. Thermoplastic and thermosetting plastics can be chemically recycled together.

## Mechanical recycling

```{system:process} MechanicalRecycling
:become_parent: true
```

```{system:process} MechanicalRecyclingOfLDPEPolyethyleneAtEOL
---
consumes: |
    LDPEPolyethyleneAtEOL                      = 1.6 kg
    CleaningAgents                             = 0.01 kg
produces: |
    ukf:LDPEPolyethylene                       = 1 kg
    Waste                                      = 0.5 kg
---
A yield of approximately 63% is assumed.
```

```{system:process} MechanicalRecyclingOfLLDPEAtEOL
---
consumes: |
    LLDPEAtEOL                                 = 1.6 kg
    CleaningAgents                             = 0.01 kg
produces: |
    LLDPE                                      = 1 kg
    Waste                                      = 0.5 kg
---
A yield of approximately 63% is assumed.
```

```{system:process} MechanicalRecyclingOfHDPEPolyethyleneAtEOL
---
consumes: |
    HDPEPolyethyleneAtEOL                      = 1.6 kg
    CleaningAgents                             = 0.01 kg
produces: |
    ukf:HDPEPolyethylene                       = 1 kg
    Waste                                      = 0.5 kg
---
A yield of approximately 63% is assumed.
```

```{system:process} MechanicalRecyclingOfPPPolypropyleneAtEOL
---
consumes: |
    PPPolypropyleneAtEOL                       = 1.6 kg
    CleaningAgents                             = 0.01 kg
produces: |
    ukf:PPPolypropylene                        = 1 kg
    Waste                                      = 0.5 kg
---
A yield of approximately 63% is assumed.
```

```{system:process} MechanicalRecyclingOfPSPolystyreneAtEOL
---
consumes: |
    PSPolystyreneAtEOL                         = 1.6 kg
    CleaningAgents                             = 0.01 kg             
produces: |
    ukf:PSPolystyrene                          = 1 kg
    Waste                                      = 0.5 kg
---
A yield of approximately 63% is assumed.
```

```{system:process} MechanicalRecyclingOfPVCPolyvinylChlorideAtEOL
---
consumes: |
    PVCPolyvinylChlorideAtEOL                  = 1.6 kg
    CleaningAgents                             = 0.01 kg             
produces: |
    ukf:PVCPolyvinylChloride                   = 1 kg
    Waste                                      = 0.5 kg
---
A yield of approximately 63% is assumed.
```

```{system:process} MechanicalRecyclingOfPETPolyethyleneTerephthalatePolyestersAtEOL
---
consumes: |
    PETPolyethyleneTerephthalatePolyestersAtEOL    = 1.6 kg
    CleaningAgents                                 = 0.01 kg
produces: |
    ukf:PETPolyethyleneTerephthalatePolyesters     = 1 kg
    Waste                                          = 0.5 kg
---
A yield of approximately 63% is assumed.
```

```{system:process} MechanicalRecyclingOfFibrePPAAtEOL
---
consumes: |
    FibrePPAAtEOL                              = 1.6 kg
    CleaningAgents                             = 0.01 kg             
produces: |
    FibrePPA                                   = 1 kg
    Waste                                      = 0.5 kg
---
A yield of approximately 63% is assumed.
```

```{end-sub-processes}
```

## Chemical recycling

Chemical recycling is assumed for simplicity to be a single process taking a mixed-plastic waste stream and producing a liquid hydrocarbon product, which is modelled as substituting "naphtha" in the model.

```{system:process} ChemicalRecyclingOfMixedPolymersAtEOL
---
consumes: |
  MixedPolymersAtEOL                                 = 1.7 kg
  ukf:OtherInorganicPrimaryChemicals                 = 0.1 kg
produces: |
  ukf:Naphtha                                        = 1 kg {comment: 'Liquid hydrocarbons'}
  ukf:MiscRefineryProducts                           = 0.4 kg {comment: 'Gas oil, kerosene'}
  ukf:WasteOtherChemicals                            = 0.6 kg
  PyrolysisResidue                                   = 0.1 kg
---
```

The following objects are defined in relation to the processes above:

```{system:object} CleaningAgents
Cleaning agents are used to clean and remove contaminants on the polymers.
```

```{system:object} PyrolysisResidue
PyrolysisResidue is the solid by-products produced after the pyrolysis of the polymers.
```
