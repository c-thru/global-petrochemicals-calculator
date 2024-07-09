# Introduction

The goal of the Petrochemicals Calculator model is to give a consistent account of demand, recycling, production of key chemicals, and feedstocks. It ensures mass balance and clearly represents physical process characteristics (e.g. stoichiometry of reactions and yields, and utility requirements), as a basis for calculating lifecycle GHG emissions. The model aims to be able to represent today's state of the system, and as wide a range of future configurations as are feasible. The system scope covers detailed demand-driven modelling of plastics and nitrogen fertilisers, with other chemical demand accounted for in a simplified way, so that total production of primary chemicals is correctly captured. The scope of emissions modelled covers upstream production of feedstocks, indirect emissions from electricity use, emissions from utility combustion and reactions during production of chemicals, nitrogen fertiliser use-phase emissions, and emissions from end-of-life management of waste polymers.

To do this, the model has three main elements, which are described in the following sections of this documentation:

1. The *structure* of the system and the bottom-up processes and objects that it consists of [@sec-system-definitions];
2. The *model logic*, which determines how demand and supply are balanced, and which process routes are selected when multiple options are available [@sec-model-logic]; and
3. The *levers* that determine how the model configurations evolve over time, aiming to represent scenarios spanning “business as usual” to “maximum possible" (remaining sections of the documentation).
