# Healthcare Cost Driver Evaluator

## Overview

This project analyzes healthcare cost trends to identify key drivers of PMPM (Per Member Per Month) changes using a structured analytics and evaluation framework.

The goal is to demonstrate how data science and AI-driven reasoning can identify actionable cost drivers that influence total cost of care.

---

## Business Problem

Healthcare organizations must understand what is driving cost increases in order to manage financial performance and improve outcomes.

Key cost drivers often include:

- Utilization (visits, admissions)
- Unit cost per service
- Pharmacy mix (specialty vs generic)
- Site-of-care differences
- Network leakage

This project simulates those scenarios and evaluates whether an AI system can correctly identify the underlying drivers of cost change.

---

## Analysis Approach

The evaluator framework:

- Generates synthetic healthcare cost scenarios  
- Identifies expected primary cost drivers  
- Compares AI reasoning against known drivers  
- Validates whether models correctly explain PMPM changes  

---

## Results (Example)

The waterfall analysis below illustrates how different service categories contribute to PMPM cost change.

<img width="1086" height="592" alt="image" src="https://github.com/user-attachments/assets/dacb0c43-ab01-4f90-9c66-3104c32a5b82" />

---

## Key Findings

- Specialty pharmacy and inpatient utilization are the largest contributors to rising PMPM costs  
- Cost increases are driven more by utilization intensity than demographic factors  
- Declines in emergency department utilization do not offset growth in high-cost categories  
- Cost driver patterns align with real-world healthcare spending dynamics  

---

## Business Impact

These insights enable healthcare organizations to:

- Prioritize specialty drug management programs  
- Reduce inpatient utilization through care coordination  
- Focus on high-cost member segments  
- Improve PMPM forecasting and financial planning  

---

## Dataset

A synthetic healthcare dataset was generated to reflect real-world analytics metrics.

### Key Fields

- Month  
- Region  
- Provider Group  
- Service Category  
- PMPM  
- ER visits per 1000  
- Admissions per 1000  
- Average Cost per Admission  
- Specialty Rx PMPM  
- Generic Dispensing Rate  
- SNF Days per 1000  
- Site-of-Care Index  
- Network Leakage  

Each record includes an expected primary cost driver.

---

## Repository Structure


healthcare-cost-driver-evaluator
│
├── data/
│ └── healthcare_metrics.csv
│
├── healthcare_ai/
│ ├── evaluator.py
│ └── prompt_tests.py
│
├── notebooks/
│ └── demo_analysis.ipynb
│
├── images/
│ └── pmpm_cost_drivers.png
│
├── README.md
├── requirements.txt
└── .gitignore


---

## Key Takeaway

This project demonstrates how healthcare cost drivers can be systematically identified and validated, enabling more effective cost management and decision-making in value-based care environments.
