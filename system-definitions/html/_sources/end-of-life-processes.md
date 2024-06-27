End-of-life processes
=====================

At the end-of-life of the end-use sector products, some of the polymers can be recovered.  The processes that split end-of-life products into end-of-life polymers are generated from the product model, and generated recipes are included in {doc}`products`.

## End-of-life polymer streams

The following objects are defined to represent polymer streams recovered from end-of-life processes:

```{system:object} PolymersAtEOL
:become_parent: true
```

```{system:object} LDPEPolyethyleneAtEOL
LDPEPolyethylene recovered at the end-of-life products.
```

```{system:object} LLDPEAtEOL
LLDPE recovered at the end-of-life products.
```

```{system:object} HDPEPolyethyleneAtEOL
HDPEPolyethylene recovered at the end-of-life products.
```

```{system:object} PPPolypropyleneAtEOL
PPPolypropylene recovered at the end-of-life products.
```

```{system:object} PSPolystyreneAtEOL
PSPolystyrene recovered at the end-of-life products.
```

```{system:object} PVCPolyvinylChlorideAtEOL
PVCPolyvinylChloride recovered at the end-of-life products.
```

```{system:object} PETPolyethyleneTerephthalatePolyestersAtEOL
PETPolyethyleneTerephthalatePolyesters recovered at the end-of-life products.
```

```{system:object} PolyurethaneAtEOL
Polyurethane recovered at the end-of-life products.
```

```{system:object} SyntheticRubbersAtEOL
SyntheticRubbers recovered at the end-of-life products.
```

```{system:object} OtherPolymersAtEOL
OtherPolymers recovered at the end-of-life products.
```

```{system:object} FibrePPAAtEOL
FibrePPA recovered at the end-of-life products.
```

```{end-sub-objects}
```

## Mixed polymer streams

Polymers-at-end-of-life can end up mixed together, that can subsequently go to chemical recycling or their final treatment. Below are the representation of these mixing processes: 

```{system:process} MixingWastePolymerStreams
:become_parent: true
```

```{system:process} MixingLDPEPolyethyleneAtEOL
---
consumes: |
    LDPEPolyethyleneAtEOL                           = 1 kg
produces: |
    MixedPolymersAtEOL          = 1 kg
---
```

```{system:process} MixingLLDPEAtEOL
---
consumes: |
    LLDPEAtEOL                           = 1 kg
produces: |
    MixedPolymersAtEOL          = 1 kg
---
```

```{system:process} MixingHDPEPolyethyleneAtEOL
---
consumes: |
    HDPEPolyethyleneAtEOL                           = 1 kg
produces: |
    MixedPolymersAtEOL          = 1 kg
---
```

```{system:process} MixingPPPolypropyleneAtEOL
---
consumes: |
    PPPolypropyleneAtEOL                           = 1 kg
produces: |
    MixedPolymersAtEOL          = 1 kg
---
```

```{system:process} MixingPSPolystyreneAtEOL
---
consumes: |
    PSPolystyreneAtEOL                           = 1 kg
produces: |
    MixedPolymersAtEOL          = 1 kg
---
```

```{system:process} MixingPVCPolyvinylChlorideAtEOL
---
consumes: |
    PVCPolyvinylChlorideAtEOL                           = 1 kg
produces: |
    MixedPolymersAtEOL          = 1 kg
---
```

```{system:process} MixingPETPolyethyleneTerephthalatePolyestersAtEOL
---
consumes: |
    PETPolyethyleneTerephthalatePolyestersAtEOL                           = 1 kg
produces: |
    MixedPolymersAtEOL          = 1 kg
---
```

```{system:process} MixingPolyurethaneAtEOL
---
consumes: |
    PolyurethaneAtEOL                           = 1 kg
produces: |
    MixedPolymersAtEOL          = 1 kg
---
```

```{system:process} MixingSyntheticRubbersAtEOL
---
consumes: |
    SyntheticRubbersAtEOL                           = 1 kg
produces: |
    MixedPolymersAtEOL          = 1 kg
---
```

```{system:process} MixingFibrePPAAtEOL
---
consumes: |
    FibrePPAAtEOL                           = 1 kg
produces: |
    MixedPolymersAtEOL          = 1 kg
---
```

```{system:process} MixingOtherPolymersAtEOL
---
consumes: |
    OtherPolymersAtEOL                           = 1 kg
produces: |
    MixedPolymersAtEOL          = 1 kg
---
```

```{end-sub-processes}
```

The following objects are defined to represent polymer streams recovered from end-of-life processes:

```{system:object} MixedPolymersAtEOL
MixedPolymersAtEOL goes to chemical recycling or final treatment.
```

```{system:object} Waste
```
