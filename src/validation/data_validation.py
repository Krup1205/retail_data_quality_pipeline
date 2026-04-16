def validate_data(df):
    report = {}

    report['missing_values'] = df.isnull().sum()
    report['duplicates'] = df.duplicated().sum()
    report['negative_sales'] = (df['Sales'] < 0).sum()

    report['zero_sales_open_store'] = df[
        (df['Open'] == 1) & (df['Sales'] == 0)
    ]

    return report