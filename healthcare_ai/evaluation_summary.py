
import pandas as pd
from pathlib import Path

from evaluator import load_data, infer_expected_driver, score_response


def run_evaluation(path: Path = Path("./data/healthcare_metrics.csv")) -> pd.DataFrame:
    df = load_data(path)

    results = []

    for _, row in df.iterrows():
        expected = infer_expected_driver(row)

        # Placeholder response for version 1.
        # Later this can be replaced with a real LLM response.
        placeholder_response = f"The likely driver is {expected.replace('_', ' ')}."

        scored = score_response(placeholder_response, expected)

        results.append(
            {
                "Month": row["Month"],
                "Region": row["Region"],
                "Provider_Group": row["Provider_Group"],
                "Service_Category": row["Service_Category"],
                "expected_driver": expected,
                "matched_keywords": ", ".join(scored["matched_keywords"]),
                "is_correct": scored["is_correct"],
            }
        )

    results_df = pd.DataFrame(results)
    accuracy = results_df["is_correct"].mean()

    print("Evaluation Summary")
    print("------------------")
    print(f"Rows evaluated: {len(results_df)}")
    print(f"Correct predictions: {results_df['is_correct'].sum()}")
    print(f"Accuracy: {accuracy:.2%}")

    return results_df


if __name__ == "__main__":
    run_evaluation()