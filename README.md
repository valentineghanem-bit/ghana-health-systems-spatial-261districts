# Spatial Analysis of Health System Performance and Geographic Equity — Ghana 261 Districts

[![CI](https://github.com/valentineghanem-bit/ghana-health-systems-spatial-261districts/actions/workflows/ci.yml/badge.svg)](https://github.com/valentineghanem-bit/ghana-health-systems-spatial-261districts/actions) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/) [![R 4.3+](https://img.shields.io/badge/R-4.3+-blue.svg)](https://www.r-project.org/) [![ORCID](https://img.shields.io/badge/ORCID-0009--0002--8332--0220-green.svg)](https://orcid.org/0009-0002-8332-0220)

**Author:** Valentine Golden Ghanem | Ghana COCOBOD Cocoa Clinic, Accra, Ghana
**ORCID:** [0009-0002-8332-0220](https://orcid.org/0009-0002-8332-0220)
**Affiliation:** Ghana COCOBOD Cocoa Clinic, Accra, Ghana
**Reporting standard:** STROBE · RECORD-Spatial · TRIPOD+AI
**Date:** 2026
**Status:** Manuscript in preparation

## 1. Abstract

This study provides a district-level spatial analysis of health system performance across Ghana's 261 districts and 16 administrative regions. A composite performance index (0–100) integrating facility density, service coverage, workforce ratios, geographic accessibility, quality indicators, and health equity metrics was constructed and mapped. Spatial autocorrelation analysis (Moran's I = 0.62, p < 0.001) reveals strong geographic clustering, with high-burden districts concentrated in the Northern, Savannah, and Upper regions. The North–South performance gap spans 47.2 points (Greater Accra: 78.4 vs Upper West: 29.8). XGBoost modelling (LOROCV AUC = 0.91) identifies poverty rate as the dominant driver of performance deficits (SHAP contribution: 28.4%). These findings provide an evidence base for geographically targeted health system strengthening interventions.

## 2. Research Question & Aims

1. How is health system performance spatially distributed across Ghana's 261 districts?
2. What are the socioeconomic and geographic determinants of performance deficits?
3. Can a validated ML model identify high-priority under-served districts for intervention targeting?

## 3. Methods Summary

| Method | Tool | Purpose |
|--------|------|---------|
| Composite Index (PCA + equal-weight) | Python / NumPy | Multi-domain performance aggregate (0–100) |
| 2-Step Floating Catchment Area (2SFCA) | geopandas / shapely | Spatial accessibility to health facilities |
| Global Moran's I / LISA | esda / libpysal | Spatial autocorrelation & cluster detection |
| Getis-Ord Gi* | esda | District-level hot-spot analysis |
| GWR | mgwr (Python / R) | Spatially varying coefficient estimation |
| XGBoost + SHAP | xgboost / shap | Predictive modelling & feature attribution |
| LOROCV | scikit-learn | Leave-one-region-out cross-validation |

## 4. Data Sources

| Source | Variables | Year | Access |
|--------|-----------|------|--------|
| DHIMS2 (Ghana Health Service) | Facility census, service utilisation, workforce | 2020–2023 | Open |
| NHIS (National Health Insurance Authority) | Coverage rates, claims data | 2022–2023 | Open |
| Ghana Statistical Service (GSS) | Population (2021 PHC), poverty headcount | 2021 | Open |
| GADM v4.1 | Administrative boundaries (261 districts) | 2023 | Open |

## 5. Key Findings

| Metric | Value |
|--------|-------|
| National mean composite performance index | 49.6 / 100 |
| North–South performance gap | Δ47.2 points |
| Global Moran's I | 0.62 (p < 0.001) |
| HH cluster districts (high-burden, under-served) | n = 47 |
| Top XGBoost predictor (SHAP) | Poverty rate (28.4% variance) |
| GWR coefficient β — facility density | 0.18–0.74 |
| XGBoost LOROCV AUC | 0.91 (95% CI: 0.87–0.94) |
| Spatial Gini coefficient | 0.31 (moderate inequity) |

## 6. Repository Structure

```
ghana-health-systems-spatial-261districts/
├── dashboard/
│   └── Ghana_HealthSystems_Spatial_Dashboard.html
├── poster/
│   └── Ghana_HealthSystems_Spatial_Poster.html
├── scripts/
│   ├── analysis_pipeline.py
│   ├── spatial_utils.py
│   └── spatial_diagnostics.R
├── data/                  # processed datasets (no raw PII)
├── figures/               # publication figures (PNG, 300 DPI)
├── tests/
├── .github/workflows/ci.yml
├── app.py
├── analysis.R
├── requirements.txt
├── Dockerfile
├── CITATION.cff
└── LICENSE
```

## 7. Reproducibility

### 7.1 Requirements

- Python 3.12+, R 4.3+, Docker (optional)

### 7.2 Clone & install

```bash
git clone https://github.com/valentineghanem-bit/ghana-health-systems-spatial-261districts.git
cd ghana-health-systems-spatial-261districts
pip install -r requirements.txt
```

### 7.3 Run the analytical pipeline

```bash
python scripts/analysis_pipeline.py
```

### 7.4 Run the test suite

```bash
pytest tests/ -v
```

### 7.5 Launch the interactive Dash application

```bash
python app.py
```

### 7.6 Open the static HTML dashboard

```bash
# macOS
open dashboard/Ghana_HealthSystems_Spatial_Dashboard.html
# Windows
start dashboard/Ghana_HealthSystems_Spatial_Dashboard.html
# Linux
xdg-open dashboard/Ghana_HealthSystems_Spatial_Dashboard.html
```

## 8. Outputs

| Output | Description |
|--------|-------------|
| dashboard/Ghana_HealthSystems_Spatial_Dashboard.html | Interactive vanilla-JS dashboard |
| poster/Ghana_HealthSystems_Spatial_Poster.html | A0 conference poster (print-ready) |
| figures/ | Publication-quality PNG figures (300 DPI) |

## 8a. Downloadable Artefacts (HTML)

| Artefact | View on GitHub | Live preview | Direct download (raw HTML) |
|----------|---------------|--------------|---------------------------|
| Interactive dashboard | [View](https://github.com/valentineghanem-bit/ghana-health-systems-spatial-261districts/blob/main/dashboard/Ghana_HealthSystems_Spatial_Dashboard.html) | [Preview](https://htmlpreview.github.io/?https://github.com/valentineghanem-bit/ghana-health-systems-spatial-261districts/blob/main/dashboard/Ghana_HealthSystems_Spatial_Dashboard.html) | [Download](https://raw.githubusercontent.com/valentineghanem-bit/ghana-health-systems-spatial-261districts/main/dashboard/Ghana_HealthSystems_Spatial_Dashboard.html) |
| Conference poster | [View](https://github.com/valentineghanem-bit/ghana-health-systems-spatial-261districts/blob/main/poster/Ghana_HealthSystems_Spatial_Poster.html) | [Preview](https://htmlpreview.github.io/?https://github.com/valentineghanem-bit/ghana-health-systems-spatial-261districts/blob/main/poster/Ghana_HealthSystems_Spatial_Poster.html) | [Download](https://raw.githubusercontent.com/valentineghanem-bit/ghana-health-systems-spatial-261districts/main/poster/Ghana_HealthSystems_Spatial_Poster.html) |

> **Tip:** The dashboard works fully offline once downloaded. The poster is print-ready at A0 (841 × 1189 mm).

## 9. Reporting Standard

This study follows the **STROBE** (Strengthening the Reporting of Observational Studies in Epidemiology) reporting guideline for observational ecological studies. Spatial components follow **RECORD-Spatial**. Machine learning components follow **TRIPOD+AI**.

## 10. Ethical Statement

This study uses aggregated administrative and national survey data. No individual-level or identifiable data were used. Data were obtained from publicly available national repositories. Ethical review was not required under Ghana Health Service guidelines for aggregate spatial analyses.

## 11. Citation

**APA:**
Ghanem, V. G. (2026). *Spatial Analysis of Health System Performance and Geographic Equity — Ghana 261 Districts.* GitHub. https://github.com/valentineghanem-bit/ghana-health-systems-spatial-261districts

**BibTeX:**
```bibtex
@misc{ghanem2026healthsystems,
  author = {Ghanem, Valentine Golden},
  title  = {Spatial Analysis of Health System Performance and Geographic Equity -- Ghana 261 Districts},
  year   = {2026},
  url    = {https://github.com/valentineghanem-bit/ghana-health-systems-spatial-261districts}
}
```
A machine-readable citation is provided in `CITATION.cff`.

## 12. License

Code is released under the **MIT License** — see [LICENSE](LICENSE) for details.
Outputs and figures: **CC BY 4.0**.

## 13. Author & Contact

**Valentine Golden Ghanem**
Ghana COCOBOD Cocoa Clinic, Accra, Ghana
Email: valentineghanem@gmail.com
ORCID: [0009-0002-8332-0220](https://orcid.org/0009-0002-8332-0220)

## 14. Acknowledgements

The author acknowledges the Ghana Health Service, the National Health Insurance Authority, and the Ghana Statistical Service for providing the data underpinning this analysis. This work was conducted independently and does not represent the official position of any affiliated institution.
