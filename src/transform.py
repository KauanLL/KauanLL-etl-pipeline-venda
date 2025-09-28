import pandas as pd


def transform_data(df):
    df.collumns = [c.lower() for c in df.collumns]
    df['data'] = pd.to_datetime(df['data'])
    df['valor'] = df['valor'].astype(float)
    return df