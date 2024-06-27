---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.13.8
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
--- 

Other demand for chemicals
========

This model mostly focuses on polymer demand, but there are other uses of BTX in particular that are missed without this. These are included explicitly here in aggregated form.

```{system:process} OtherConsumptionOfBenzene
---
consumes: |
  ukf:Benzene = 1 kg
---
```

```{system:process} OtherConsumptionOfToluene
---
consumes: |
  ukf:Toluene = 1 kg
---
```

```{system:process} OtherConsumptionOfXylenes
---
consumes: |
  ukf:Xylenes = 1 kg
---
```

```{system:process} OtherConsumptionOfMethylAlcohol
---
consumes: |
  ukf:MethylAlcohol = 1 kg
---
```
