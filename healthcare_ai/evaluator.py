import argparse
from pathlib import Path
import pandas as pd

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "healthcare_metrics.csv"

DRIVER_KEYWORDS = {
    "utilization_increase": ["utilization", "admission", "volume", "er visit", "higher use"],
    "unit_cost_inflation": ["unit cost", "cost per admission", "price", "inflation", "higher paid"],
    "pharmacy_mix_shift": ["specialty", "pharmacy mix", "generic", "brand", "formulary"],
    "site_of_care_shift": ["site of care", "outpatient", "hospital outpatient", "setting shift", "infusion"],
    "post_acute_spike": ["post-acute", "snf", "skilled nursing", "rehab", "post acute"],
    "leakage_network": ["leakage", "out of network", "network", "capture", "referral pattern"],
}


def load_data(path: Path = DATA_PATH) -> pd.DataFrame:
    return pd.read_csv(path)


def infer_expected_driver(row: pd.Series) -> str:
    """Simple transparent logic to infer the most likely PMPM driver."""
    if row["Specialty_Rx_Spend_PMPM"] >= 110 and row["Generic_Dispensing_Rate"] <= 0.78:
        return "pharmacy_mix_shift"
    if row["Outpatient_Site_of_Care_Index"] >= 1.12:
        return "site_of_care_shift"
    if row["SNF_Days_per_1000"] >= 28:
        return "post_acute_spike"
    if row["Leakage_Rate"] >= 0.11:
        return "leakage_network"
    if row["Avg_Cost_per_Admission"] >= 20500:
        return "unit_cost_inflation"
    if row["Admissions_per_1000"] >= 50 or row["ER_Visits_per_1000"] >= 165:
        return "utilization_increase"
    return row.get("Expected_Driver", "unknown")


def score_response(response_text: str, expected_driver: str) -> dict:
    response = response_text.lower()
    keywords = DRIVER_KEYWORDS.get(expected_driver, [])
    matched = [kw for kw in keywords if kw in response]
    return {
        "expected_driver": expected_driver,
        "matched_keywords": matched,
        "is_correct": len(matched) > 0,
    }


def build_case_summary(row: pd.Series) -> str:
    return (
        f"Month={row['Month']}, Region={row['Region']}, Provider={row['Provider_Group']}, "
        f"Category={row['Service_Category']}, PMPM={row['PMPM']}, ER/1000={row['ER_Visits_per_1000']}, "
        f"Adm/1000={row['Admissions_per_1000']}, AvgCostAdm={row['Avg_Cost_per_Admission']}, "
        f"SpecRxPMPM={row['Specialty_Rx_Spend_PMPM']}, GenericRate={row['Generic_Dispensing_Rate']}, "
        f"SNFDays/1000={row['SNF_Days_per_1000']}, SOCIndex={row['Outpatient_Site_of_Care_Index']}, "
        f"Leakage={row['Leakage_Rate']}"
    )


def main(sample: int) -> None:
    df = load_data()
    demo = df.sample(sample, random_state=7).copy()
    for _, row in demo.iterrows():
        expected = infer_expected_driver(row)
        case_summary = build_case_summary(row)

        # Example placeholder response. Replace with actual model output later.
        placeholder_response = f"The likely driver is {expected.replace('_', ' ')}."

        result = score_response(placeholder_response, expected)
        print("-" * 100)
        print(case_summary)
        print("Expected driver:", expected)
        print("Scored correct:", result["is_correct"])
        print("Matched keywords:", result["matched_keywords"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate AI reasoning on healthcare cost drivers.")
    parser.add_argument("--sample", type=int, default=5, help="Number of random rows to display.")
    args = parser.parse_args()
    main(args.sample)
