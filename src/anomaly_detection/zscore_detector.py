def detect_zscore_anomalies(df, threshold=3):

    df = df.copy()

    df['z_score'] = df.groupby('Store')['Sales'].transform(
        lambda x: (x - x.mean()) / x.std()
    )

    df['z_score'] = df['z_score'].fillna(0)

    df['is_anomaly'] = df['z_score'].abs() > threshold

    return df