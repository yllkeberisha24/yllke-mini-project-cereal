# yllke-mini-project-cereal
# Cereal Mini Project

## Description
Simple reproducible analysis of cereal nutrition data.

## Data
- `data/raw/cereal.csv`: raw dataset

## Folder Structure
- `code/`: scripts
- `data/raw/`: raw dataset
- `output/figures/`: generated plots
- `environment.yml`: Conda environment
Running `python code/analysis.py` will generate the figure `output/sugar_histogram.png` showing the distribution of sugar content in cereals.

## Environment
```bash
conda env create -f environment.yml
conda activate cereal-env
