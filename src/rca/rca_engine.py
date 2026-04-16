def generate_rca(df):

    results = []
    anomalies = df[df['iforest_anomaly'] == 1]

    for _, row in anomalies.iterrows():

        reasons = []

        if row['z_score'] > 3:
            anomaly_type = "Spike"
        elif row['z_score'] < -3:
            anomaly_type = "Drop"
        else:
            anomaly_type = "General"

        if row['Customers'] == 0:
            reasons.append("No customers → possible issue")

        if row['Promo'] == 1 and anomaly_type == "Spike":
            reasons.append("Promotion increased sales")

        if row['Promo'] == 0 and anomaly_type == "Drop":
            reasons.append("No promotion → sales drop")

        if row['Sales'] > 10000:
            reasons.append("High demand spike")

        if row['Sales'] < 100:
            reasons.append("Very low sales")

        results.append({
            "Store": row['Store'],
            "Date": row['Date'],
            "Sales": row['Sales'],
            "AnomalyType": anomaly_type,
            "Reasons": reasons
        })

    return results