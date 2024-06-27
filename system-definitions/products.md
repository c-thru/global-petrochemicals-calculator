Products
========

These are the product types that we are modelling (based on sectors):

```{system:object} Products
:become_parent: true
```

```{system:object} PackagingProducts
```
```{system:object} TransportationProducts
```
```{system:object} BuildingsAndConstructionProducts
```
```{system:object} ElectricalAndElectronicProducts
```
```{system:object} ConsumerAndInstitutionalProducts
```
```{system:object} IndustrialMachinery
```
```{system:object} TextileProducts
```
```{system:object} OtherProducts
```

```{end-sub-objects}
```

And end-of-life versions:


```{system:object} EOLProducts
:become_parent: true
```

```{system:object} EOLPackagingProducts
```
```{system:object} EOLTransportationProducts
```
```{system:object} EOLBuildingsAndConstructionProducts
```
```{system:object} EOLElectricalAndElectronicProducts
```
```{system:object} EOLConsumerAndInstitutionalProducts
```
```{system:object} EOLIndustrialMachinery
```
```{system:object} EOLTextileProducts
```
```{system:object} EOLOtherProducts
```

```{end-sub-objects}
```


These are the processes that produce and use them:

```{system:process} ProductionOfProducts
:become_parent: true
```

```{include} production_recipes_generated.md
```

```{end-sub-processes}
```

The composition of different polymers used for packaging materials is estimated using the global average composition in 2020, from the study by {cite}`gao_evaluating_2024`. The same method applies for other products, such as transportation products, building and construction products, and so on.

```{system:process} UseOfProducts
:become_parent: true
```

```{system:process} UseOfPackagingProducts
:consumes: "{object: PackagingProducts, amount: 1, unit: kg}"
:produces: "{object: EOLPackagingProducts, amount: 1, unit: kg}"
```
```{system:process} UseOfTransportationProducts
:consumes: "{object: TransportationProducts, amount: 1, unit: kg}"
:produces: "{object: EOLTransportationProducts, amount: 1, unit: kg}"
```
```{system:process} UseOfBuildingsAndConstructionProducts
:consumes: "{object: BuildingsAndConstructionProducts, amount: 1, unit: kg}"
:produces: "{object: EOLBuildingsAndConstructionProducts, amount: 1, unit: kg}"
```
```{system:process} UseOfElectricalAndElectronicProducts
:consumes: "{object: ElectricalAndElectronicProducts, amount: 1, unit: kg}"
:produces: "{object: EOLElectricalAndElectronicProducts, amount: 1, unit: kg}"
```
```{system:process} UseOfConsumerAndInstitutionalProducts
:consumes: "{object: ConsumerAndInstitutionalProducts, amount: 1, unit: kg}"
:produces: "{object: EOLConsumerAndInstitutionalProducts, amount: 1, unit: kg}"
```
```{system:process} UseOfIndustrialMachinery
:consumes: "{object: IndustrialMachinery, amount: 1, unit: kg}"
:produces: "{object: EOLIndustrialMachinery, amount: 1, unit: kg}"
```
```{system:process} UseOfTextileProducts
:consumes: "{object: TextileProducts, amount: 1, unit: kg}"
:produces: "{object: EOLTextileProducts, amount: 1, unit: kg}"
```
```{system:process} UseOfOtherProducts
:consumes: "{object: OtherProducts, amount: 1, unit: kg}"
:produces: "{object: EOLOtherProducts, amount: 1, unit: kg}"
```

```{end-sub-processes}
```


