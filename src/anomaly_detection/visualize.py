import matplotlib.pyplot as plt

def plot_anomalies(df, store_id=1):
    
    # Filter one store (important for clarity)
    store_df = df[df['Store'] == store_id]

    plt.figure(figsize=(12,6))

    # Plot normal sales
    plt.plot(store_df['Date'], store_df['Sales'], label='Sales')

    # Plot anomalies
    anomalies = store_df[store_df['is_anomaly'] == True]
    plt.scatter(anomalies['Date'], anomalies['Sales'], label='Anomalies')

    plt.title(f"Sales Anomalies for Store {store_id}")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.legend()

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()