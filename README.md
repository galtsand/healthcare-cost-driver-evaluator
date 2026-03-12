# Healthcare Cost Driver Evaluator

This project analyzes healthcare cost trends to identify key drivers of PMPM (Per Member Per Month) changes using Python analytics models.

The framework evaluates factors such as:
- Specialty drug utilization
- Service utilization trends
- Cost category shifts
- Predictive modeling of healthcare spend

## Example Output

<img width="1086" height="592" alt="image" src="https://github.com/user-attachments/assets/dacb0c43-ab01-4f90-9c66-3104c32a5b82" />


## Business Insight

The waterfall analysis illustrates how different healthcare service categories contribute to PMPM cost change.

In this example scenario, specialty pharmacy and inpatient utilization are the largest contributors to rising costs. While emergency department utilization shows a slight decline, it does not offset the growth driven by specialty medications and inpatient services.

This type of analysis helps healthcare organizations prioritize cost containment strategies, such as specialty drug management programs, care coordination to reduce inpatient admissions, and targeted utilization review.


---

## Project Objective

The goal of this project is to demonstrate how data science can identify actionable cost drivers in healthcare.

This project explores how AI models reason about healthcare cost drivers that influence PMPM (Per Member Per Month) cost trends.

Healthcare organizations routinely analyze factors such as utilization, unit cost, pharmacy mix, site-of-care, and network leakage to understand total cost of care. This repository demonstrates a simplified evaluation framework that simulates those scenarios and tests whether an AI system correctly identifies the underlying drivers of cost change.

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
├── images/
│   └── pmpm_cost_drivers.png
│
├── README.md
├── requirements.txt
└── .gitignore
```














