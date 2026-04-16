from sklearn.ensemble import IsolationForest

def detect_iforest_anomalies(df):

    df = df.copy()

    features = df[['Sales', 'Customers', 'Promo', 'CompetitionDistance']]

    model = IsolationForest(
        n_estimators=100,
        contamination=0.01,
        random_state=42
    )

    df['iforest_score'] = model.fit_predict(features)
    df['iforest_anomaly'] = df['iforest_score'].apply(lambda x: 1 if x == -1 else 0)

    return df