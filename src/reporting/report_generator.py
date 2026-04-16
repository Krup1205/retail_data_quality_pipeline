import pandas as pd
import os

def generate_report(rca_results):

    os.makedirs("outputs/reports", exist_ok=True)

    df_report = pd.DataFrame(rca_results)
    df_report['Reasons'] = df_report['Reasons'].apply(lambda x: "; ".join(x))

    df_report.to_csv("outputs/reports/anomaly_report.csv", index=False)
    df_report.to_excel("outputs/reports/anomaly_report.xlsx", index=False)

    return df_report