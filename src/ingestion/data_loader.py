import pandas as pd

def load_data(train_path, store_path):
    df_train = pd.read_csv(
        train_path,
        dtype={'StateHoliday': str},
        parse_dates=['Date']
    )
    df_store = pd.read_csv(store_path)
    return df_train, df_store

def merge_data(df_train, df_store):
    return df_train.merge(df_store, on='Store', how='left')