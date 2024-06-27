Fertilisers
===========

This model is based on data and scenarios from {cite:t}`gao_greenhouse_2023`.

Because they have already developed a self-contained analysis of the impacts of fertiliser production and use, for the initial model these processes are treated as "black boxes": they are not further integrated into explicit mass-flow models of the upstream supply chain.

These are the fertiliser types considered:

```{system:object} NitrogenFertiliser
:become_parent: true
```

```{system:object} AmmoniaFertiliser
Note that this is modelled separately from the ammonia used as part of the main petrochemicals model, because for fertilisers we are using emissions factors directly from {cite:t}`gao_greenhouse_2023`.
```
```{system:object} AmmoniumSulphate
```
```{system:object} AmmoniumNitrate
```
```{system:object} CalciumAmmoniumNitrate
```
```{system:object} AmmoniumPhosphate
```
```{system:object} NKCompound
```
```{system:object} NPKCompound
```
```{system:object} UreaAmmoniumNitrate
```
```{system:object} OtherFertiliserN
```
```{system:object} OtherFertiliserNP
```
```{system:object} Urea
```

```{end-sub-objects}
```

These are the processes that produce and use them:

```{system:process} ProductionOfNitrogenFertiliser
:become_parent: true
```

```{system:process} ProductionOfAmmoniaFertiliser
:produces: "{object: AmmoniaFertiliser, amount: 1, unit: kg}"
```
```{system:process} ProductionOfAmmoniumSulphate
:produces: "{object: AmmoniumSulphate, amount: 1, unit: kg}"
```
```{system:process} ProductionOfAmmoniumNitrate
:produces: "{object: AmmoniumNitrate, amount: 1, unit: kg}"
```
```{system:process} ProductionOfCalciumAmmoniumNitrate
:produces: "{object: CalciumAmmoniumNitrate, amount: 1, unit: kg}"
```
```{system:process} ProductionOfAmmoniumPhosphate
:produces: "{object: AmmoniumPhosphate, amount: 1, unit: kg}"
```
```{system:process} ProductionOfNKCompound
:produces: "{object: NKCompound, amount: 1, unit: kg}"
```
```{system:process} ProductionOfNPKCompound
:produces: "{object: NPKCompound, amount: 1, unit: kg}"
```
```{system:process} ProductionOfUreaAmmoniumNitrate
:produces: "{object: UreaAmmoniumNitrate, amount: 1, unit: kg}"
```
```{system:process} ProductionOfOtherFertiliserN
:produces: "{object: OtherFertiliserN, amount: 1, unit: kg}"
```
```{system:process} ProductionOfOtherFertiliserNP
:produces: "{object: OtherFertiliserNP, amount: 1, unit: kg}"
```
```{system:process} ProductionOfUrea
:produces: "{object: Urea, amount: 1, unit: kg}"
```

```{end-sub-processes}
```

These are the processes that represent use (application) of each type of fertiliser:

```{system:process} UseOfNitrogenFertiliser
:become_parent: true
```

```{system:process} UseOfAmmoniaFertiliser
:consumes: "{object: AmmoniaFertiliser, amount: 1, unit: kg}"
```
```{system:process} UseOfAmmoniumSulphateFertiliser
:consumes: "{object: AmmoniumSulphate, amount: 1, unit: kg}"
```
```{system:process} UseOfAmmoniumNitrateFertiliser
:consumes: "{object: AmmoniumNitrate, amount: 1, unit: kg}"
```
```{system:process} UseOfCalciumAmmoniumNitrateFertiliser
:consumes: "{object: CalciumAmmoniumNitrate, amount: 1, unit: kg}"
```
```{system:process} UseOfAmmoniumPhosphateFertiliser
:consumes: "{object: AmmoniumPhosphate, amount: 1, unit: kg}"
```
```{system:process} UseOfNKCompoundFertiliser
:consumes: "{object: NKCompound, amount: 1, unit: kg}"
```
```{system:process} UseOfNPKCompoundFertiliser
:consumes: "{object: NPKCompound, amount: 1, unit: kg}"
```
```{system:process} UseOfUreaAmmoniumNitrateFertiliser
:consumes: "{object: UreaAmmoniumNitrate, amount: 1, unit: kg}"
```
```{system:process} UseOfOtherFertiliserN
:consumes: "{object: OtherFertiliserN, amount: 1, unit: kg}"
```
```{system:process} UseOfOtherFertiliserNP
:consumes: "{object: OtherFertiliserNP, amount: 1, unit: kg}"
```
```{system:process} UseOfUreaFertiliser
:consumes: "{object: Urea, amount: 1, unit: kg}"
```

```{end-sub-processes}
```


