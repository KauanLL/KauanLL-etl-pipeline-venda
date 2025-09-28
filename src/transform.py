import pandas as pd


def transform_data(df):
    df.columns = [c.lower() for c in df.columns]
    df['data'] = pd.to_datetime(df['data'])
    df['valor'] = df['valor'].astype(float)
    return df