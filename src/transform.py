import pandas as pd


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [c.lower() for c in df.columns]
    df['data'] = pd.to_datetime(df['data'], errors="coerce")
    df['valor'] = pd.to_numeric(df['valor'], errors="coerce")

    if df['valor'].isnull().any():
        raise ValueError('Valores inválidos encontrado na coluna VALOR')

    if (df['valor'] <= 0).any():
        raise ValueError('Encontrado Valores menores ou igual a 0')

    if df['data'].isnull().any():
        raise ValueError('Valores inválidos encontrados na coluna DATA')

    return df