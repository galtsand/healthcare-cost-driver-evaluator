# Healthcare Cost Driver Evaluator

This project analyzes healthcare cost trends to identify key drivers of PMPM (Per Member Per Month) changes using Python analytics models.

The framework evaluates factors such as:
- Specialty drug utilization
- Service utilization trends
- Cost category shifts
- Predictive modeling of healthcare spend

<img width="1086" height="592" alt="image" src="https://github.com/user-attachments/assets/dacb0c43-ab01-4f90-9c66-3104c32a5b82" />


The goal is to demonstrate how data science can identify actionable cost drivers in healthcare


This project explores how AI models reason about healthcare cost drivers that influence PMPM (Per Member Per Month) cost trends.

Healthcare organizations routinely analyze utilization, unit cost, pharmacy mix, site-of-care, and network leakage to understand total cost of care. This repository demonstrates a simple evaluation framework that simulates those scenarios and tests whether an AI system correctly identifies the underlying driver.

---

## Project Objective

Create an analytics framework that evaluates whether AI models correctly interpret healthcare economics scenarios.

Common cost drivers simulated in the dataset include:

- Utilization increases
- Unit cost inflation
- Pharmacy mix shifts (specialty vs generic)
- Site-of-care shifts
- Post-acute utilization spikes
- Network leakage

The evaluator compares AI reasoning to the expected cost driver.

---

## Dataset

A synthetic healthcare analytics dataset was generated to represent metrics commonly used in healthcare cost analysis.

Key fields include:

- Month
- Region
- Provider Group
- Service Category
- PMPM (Per Member Per Month)
- ER visits per 1000
- Admissions per 1000
- Average Cost per Admission
- Specialty Rx PMPM
- Generic Dispensing Rate
- SNF Days per 1000
- Site-of-Care Index
- Network Leakage

Each record contains an **expected primary cost driver**.

---

## Repository Structure

```
healthcare-cost-driver-evaluator
│
├── data/
│   └── healthcare_metrics.csv
│
├── healthcare_ai/
│   ├── __init__.py
│   ├── evaluator.py
│   └── prompt_tests.py
│
├── notebooks/
│   └── demo_analysis.ipynb
│
├── README.md
├── requirements.txt
└── .gitignore
```














