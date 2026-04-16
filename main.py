import os

from src.ingestion.data_loader import load_data, merge_data
from src.validation.data_validation import validate_data
from src.preprocessing.data_cleaning import clean_data
from src.anomaly_detection.zscore_detector import detect_zscore_anomalies
from src.anomaly_detection.isolation_forest import detect_iforest_anomalies
from src.rca.rca_engine import generate_rca
from src.reporting.report_generator import generate_report


def main():
    train_path = "data/raw/train.csv"
    store_path = "data/raw/store.csv"

    # Step 1: Load
    df_train, df_store = load_data(train_path, store_path)

    # Step 2: Merge
    df = merge_data(df_train, df_store)
    print("Data Loaded Successfully\n")

    # Step 3: Validate
    report = validate_data(df)
    print("Validation Report:")
    for key, value in report.items():
        print(f"{key}: \n{value}\n")

    # Step 4: Clean
    df = clean_data(df)
    print("Data Cleaned Successfully\n")

    # Step 5: Anomaly Detection
    df = detect_zscore_anomalies(df)
    df = detect_iforest_anomalies(df)

    print("Anomaly Detection Done\n")
    print("Z-score anomalies:", df['is_anomaly'].sum())
    print("Isolation Forest anomalies:", df['iforest_anomaly'].sum())

    # Save final dataset
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv("data/processed/cleaned_retail_data.csv", index=False)

    # Step 6: RCA
    rca_results = generate_rca(df)

    print("\nSample RCA Results:\n")
    for r in rca_results[:5]:
        print(r)

    # Step 7: Report
    report_df = generate_report(rca_results)

    print("\nReport Generated Successfully")
    print(report_df.head())


if __name__ == "__main__":
    main()