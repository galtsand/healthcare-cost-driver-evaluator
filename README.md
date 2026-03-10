# healthcare-cost-driver-evaluator

A compact portfolio project that evaluates whether an AI model can reason correctly about common healthcare cost drivers.

## What this project demonstrates

This repo focuses on healthcare analytics reasoning, not just generic prompting. It tests whether a model can correctly identify the primary driver of PMPM movement across scenarios such as:

- utilization increase
- unit cost inflation
- pharmacy mix shift
- site-of-care shift
- post-acute spike
- leakage / network inefficiency

## Repo contents

- `data/healthcare_metrics.csv`  
  Synthetic monthly healthcare analytics dataset with provider, region, and service-category variation.

- `src/evaluator.py`  
  Rule-based evaluator that generates a baseline expected driver from the data and scores an AI response.

- `src/prompt_tests.py`  
  Builds sample prompts from the dataset and shows how to test a model response.

- `requirements.txt`  
  Minimal Python dependencies.

## Dataset grain

One row per:

- Month
- Region
- Provider Group
- Service Category

The dataset includes measures commonly used in healthcare analytics:

- PMPM
- ER visits per 1000
- admissions per 1000
- average cost per admission
- specialty Rx spend PMPM
- generic dispensing rate
- mail order rate
- imaging utilization per 1000
- SNF days per 1000
- site-of-care index
- leakage rate

## Why this matters

Healthcare AI models often get the following wrong:

1. confusing utilization with unit cost
2. missing pharmacy mix as a cost driver
3. failing to recognize site-of-care shifts
4. overlooking leakage and post-acute dynamics

This project is designed to make those reasoning failures visible and testable.

## Quick start

```bash
pip install -r requirements.txt
python src/evaluator.py --sample 5
python src/prompt_tests.py --sample 3
```

## Example use case

A model is asked to explain why PMPM increased for a provider group.  
The evaluator checks whether the response correctly points to the most likely driver based on the metrics in the scenario.

## Notes

- The data is synthetic and intended for portfolio / demonstration use.
- The logic is intentionally simple and transparent so the reasoning can be reviewed easily.
- This can be extended later with an API-based LLM call, notebook demo, or RAG workflow.
