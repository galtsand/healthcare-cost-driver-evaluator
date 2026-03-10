import argparse
from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "healthcare_metrics.csv"


def load_data() -> pd.DataFrame:
    return pd.read_csv(DATA_PATH)


def build_prompt(row: pd.Series) -> str:
    return f"""
You are reviewing healthcare performance data.

Scenario:
- Month: {row['Month']}
- Region: {row['Region']}
- Provider Group: {row['Provider_Group']}
- Service Category: {row['Service_Category']}
- PMPM: {row['PMPM']}
- ER visits per 1000: {row['ER_Visits_per_1000']}
- Admissions per 1000: {row['Admissions_per_1000']}
- Average cost per admission: {row['Avg_Cost_per_Admission']}
- Specialty Rx spend PMPM: {row['Specialty_Rx_Spend_PMPM']}
- Generic dispensing rate: {row['Generic_Dispensing_Rate']}
- Mail order rate: {row['Mail_Order_Rate']}
- Imaging utilization per 1000: {row['Imaging_Util_per_1000']}
- SNF days per 1000: {row['SNF_Days_per_1000']}
- Site-of-care index: {row['Outpatient_Site_of_Care_Index']}
- Leakage rate: {row['Leakage_Rate']}

Question:
What is the most likely primary driver of PMPM movement in this scenario?
Explain your reasoning in 2-3 sentences.
""".strip()


def main(sample: int) -> None:
    df = load_data()
    demo = df.sample(sample, random_state=11)
    for i, (_, row) in enumerate(demo.iterrows(), start=1):
        print("=" * 100)
        print(f"Prompt {i}")
        print(build_prompt(row))
        print(f"\nExpected driver label: {row['Expected_Driver']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate test prompts for healthcare AI evaluation.")
    parser.add_argument("--sample", type=int, default=3, help="Number of prompts to print.")
    args = parser.parse_args()
    main(args.sample)
