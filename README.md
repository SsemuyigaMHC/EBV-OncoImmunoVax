# EBV-OncoImmunoVax

## Systems-level immunoinformatics framework for the design and evaluation of multi-epitope therapeutic vaccines targeting EBV-associated malignancies

![EBV Vaccine Design](https://img.shields.io/badge/Focus-EBV%20Therapeutic%20Vaccine-blue)
![Computational Biology](https://img.shields.io/badge/Field-Immunoinformatics-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Overview

**EBV-OncoImmunoVax** is an immunoinformatics-driven repository supporting the rational design and computational evaluation of multi-epitope vaccine candidates targeting oncogenic Epstein–Barr virus (EBV).

The pipeline integrates epitope discovery, antigen processing prediction, vaccine construction, structural refinement, immune simulation, molecular docking, molecular dynamics simulations, and expression-readiness assessment to identify promising therapeutic vaccine candidates against EBV-associated malignancies.

This repository accompanies a research manuscript and is intended to promote **reproducibility, transparency, and downstream experimental translation**.

---

# Scientific Scope

The workflow integrates multiple computational vaccinology approaches:

- EBV oncogenic and latency-associated antigen selection
- MHC class I epitope prediction
- MHC class II epitope prediction
- Antigen processing analysis
  - Proteasomal cleavage prediction
  - TAP transport prediction
- B-cell epitope prioritization
- HLA population coverage analysis
- Epitope conservancy analysis
- Multi-epitope vaccine construction
- Structural prediction and refinement
- Antigenicity evaluation
- Allergenicity and toxicity screening
- Solubility and aggregation assessment
- Junction epitope analysis
- Agent-based immune simulation
- Protein–protein docking
- Molecular dynamics simulation
- Codon optimization and mRNA stability assessment

---

# Computational Workflow

---

# Target Antigens

The vaccine design framework incorporates both structural and latency-associated EBV proteins.

## Latency-associated targets

- EBNA1
- LMP1
- LMP2
- BZLF1

## Structural targets

- gp350
- gB
- gH/gL
- gp42

This combined strategy aims to target both viral persistence mechanisms and immune-recognizable structural components.

---

# Repository Structure




---

# Vaccine Construction Strategy

Sixteen multi-epitope vaccine candidates were generated using:

- MHC class I epitopes
- MHC class II epitopes
- B-cell epitopes

Epitope assembly was performed using:

- **EAAAK linker** for structural separation
- **GPGPG linker** for immune epitope organization

Constructs were evaluated through sequence, structural, immunological, and expression-oriented analyses.

---

# Structural and Immunological Evaluation

The framework includes:

### Structural analysis

- ColabFold / AlphaFold-based modelling
- Rosetta refinement
- MolProbity validation

### Immune evaluation

- VaxiJen antigenicity prediction
- Vaxign2 reverse vaccinology analysis
- AllergenFP and AllerCatPro allergenicity assessment
- ToxinPred2 toxicity prediction
- C-ImmSim immune simulation

### Molecular interaction analysis

Docking and simulation against immune-associated receptors:

- TLR4
- NKG2D
- PD-1

Molecular dynamics simulations were performed using GROMACS to evaluate:

- RMSD
- RMSF
- Radius of gyration
- SASA
- Hydrogen bonding
- Interaction energies

---

# Expression Readiness Assessment

Selected vaccine candidates were evaluated through:

- Mammalian codon optimization
- GC-content optimization
- Restriction site removal
- Back-translation validation
- mRNA secondary structure prediction

---

# Main Computational Outputs

The repository provides:

- Predicted epitope datasets
- Vaccine construct sequences
- Structural models
- Refined protein structures
- Docking results
- Molecular dynamics outputs
- Expression optimization results
- Analysis scripts

---

# Key Findings

Integrated computational evaluation identified the most promising vaccine candidates based on combined:

- Immunogenicity
- Antigenicity
- Safety profile
- Structural stability
- Immune simulation performance
- Expression suitability

Leading candidates:

| Candidate | Overall assessment |
|---|---|
| Construct 4 | Most balanced immunological and structural profile |
| Construct 7 | Strong cellular immune-response profile |
| Construct 10 | Strong immune durability profile |
| Construct 8 | Favorable developability characteristics |
| Construct 12 | Strong antigenicity and solubility profile |

---

# Reproducibility

The pipeline uses publicly available computational resources including:

- IEDB analysis tools
- NetMHCpan
- NetMHCIIpan
- ColabFold
- Rosetta
- VaxiJen
- Vaxign2
- ToxinPred2
- AllergenFP
- C-ImmSim
- LightDock
- GROMACS

---

# Citation

If this repository contributes to your research, please cite:

**Ssemuyiga Charles et al.**  
*Systems-Level Design of a Multi-Epitope Immunotherapeutic Vaccine Targeting EBV-Associated Oncogenesis.*

---

# License

MIT License

