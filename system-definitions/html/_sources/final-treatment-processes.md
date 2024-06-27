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

Final treatment processes
=========

Polymers at end-of-life that do not get recycled can to any of these:


```{system:process} FinalTreatment
:become_parent: true
```


```{system:process} Landfilling
---
consumes: |
    MixedPolymersAtEOL                         = 1 kg
---
```

```{system:process} Incineration
---
consumes: |
    MixedPolymersAtEOL                         = 1 kg
---
```

```{system:process} Mismanagement
---
consumes: |
    MixedPolymersAtEOL                         = 1 kg
---
```



```{end-sub-processes}
```


