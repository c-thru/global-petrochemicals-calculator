# Global petrochemicals calculator

This model was developed as part of the [C-THRU project](https://www.c-thru.org/) by Rick Lupton and Stephen Doliente, with input from many colleagues.

It calculates the mass-flows of chemicals and plastics throughout the whole lifecycle at a global scale, and estimates the greenhouse gas emissions linked to this.  By changing the setting of various "levers" you can explore the effect of different future configurations of the petrochemical system: for example, switching to biomass sources of carbon, increasing plastics recycling, or reducing demand for plastic-containing products.

An interactive version of the model is available at https://go.ricklupton.name/H6cWV1

## Repository structure

The structure of the process-model system is defined in `system-definitions/`.  Here all the processes and their "recipes" are defined, together with the object types (i.e. materials, chemicals and products) that flow between them.

The logic of the chemicals calculator itself is defined in `model/`.

There are two separate parts of the model: one for fertilisers, one for plastics.

For each model:

- `model/model_{XXX}.ttl` defines the *structure* of the model -- what processes are included, and which objects must be balanced by "markets" within the system boundary. This is a Turtle RDF file, which uniquely identifies the processes and objects using URIs which can be looked up against existing definitions from the UK FIRES production system map (`ukf:` prefix), and from new definitions defined in `system-definitions/` folder here (`sys:` prefix).

- `model/load_model_{XXX}.py` defines the *logic* of the model -- the user-defined input parameters, and how specifying a parameter in one part of the model should propagate through the structure.

  - `load_model_fertilisers.py` is very simple, since most of the work has already been done in modelling the fertiliser production scenarios by Gao et al elsewhere.
  - `load_model_polymers.py` is more complex, because it deals with stock modelling of demand and end-of-life recycling; varying recycling rates; chains of chemical production processes; multi-functional process outputs.

- `model/levers.xlsx` defines user-facing "levers" which together define specific values for the model parameters.

The various other Jupyter notebooks in `model/` can be used to set up the models and test them using interactive Sankey diagrams and graphs.

Documentation for the levers is in the `docs/` folder.

## Setting up the development environment

Install the conda environment with `conda env create` and then `conda activate cthru-calculator`.

Once the conda environment is installed and activated, run `jupyter lab` to open the Jupyter notebooks.

## Developing the models

### Adding a new process to the model

First, the process needs to be *defined*. Many processes have already been defined as part of the UK FIRES production system map. If new processes or object types are needed, they should be defined by adding `{system:process}` and `{system:object}` blocks in the relevant subsection of the documents in `system-definitions/`. If the process has a well-defined fixed recipe, this can be defined at the same time and will be automatically used when solving the model equations; in more complex cases, the process recipes can be defined dynamically as part of the model logic.

Second, the process/object needs to be included in the model *structure* by adding to the `model/model_{XXX}.ttl` file.

Third, the model *logic* may need to be updated (but, depending on the change, this may not be necessary).

If changes to the logic have introduced any new parameters, then fourthly, the user-facing *levers* may need to be updated to specify specific values for any new parameters based on the setting of the levers.

### Updating the system definitions

The "system definitions" in the `system-definitions/` are where the vocabulary of the model is defined (the process names and object/material types), together with the quantitative "recipes" for the processes.

The `.md` Markdown files are processed using Jupyter Book to generate both human-readable HTML documentation, and human-readable RDF data.

After making changes to the input Markdown files, make sure to re-run `jupyter-book build system-definitions` to re-generate the documentation and RDF data, so that changes can be picked up when running the model.

(Specifically, if you are running jupyter lab in a terminal as described above, you can do this by: (1) Suspending jupyter lab by typing `Ctrl-Z`; (2) Run jupyter-book: `jupyter-book build system-definitions`; (3) Restarting jupyter lab: `fg`.)

#### Imported UK FIRES definitions

Terms defined in the UK FIRES production system map are referred to in the model's system definitions using the `ukf:` prefix.

To ensure this project is self-contained, until the UK FIRES production system map is formally published, the relevant definitions are reproduced within the `system-definitions/` as needed.

### Updating the interactive calculator code

Run the notebook `model/Convert to JS.ipynb` to generate output used by the interactive calculator webapp:

- Model logic as a Javascript function
- Sankey diagram data
- Lever data


## Lever definitions

### levels.xlsx format

- The levers are read from the sheet called LEVERS. The first column is used as the lever id. Columns `label` and `description` are associated with the lever. Then, labels and descriptions for the 4 levels are read from columns `level_label_{i}` and `level_description_{i}` (i = 1 to 4).

- For each lever defined, the specific data is read from sheets called after each *lever_id*. These should have columns `level`, `param` and a column for each year

### Lever documentation and graphs

The data from the spreadsheet is graphed and documented using [Quarto](https://quarto.org/) documents in the folder `docs/`.

To preview the docs, run `quarto preview docs`.

To render a complete set of HTML files, run `quarto render docs`.

The results are cached, so if the underlying data in `levers.xlsx` changes, you may need to add the `--cache-refresh` option to Quarto.
