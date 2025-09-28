import pandas as pd
from src.transform import transform_data

def test_transform_data():
    df = pd.DataFrame({
        "id_venda": [1, 2],
        "produto": ["Camiseta", "Tênis"],
        "valor": ["79.9", "199.0"],
        "data": ["2025-01-01", "2025-01-02"]
    })

    df_transformed = transform_data(df)

    assert df_transformed["valor"].dtype == float

    assert str(df_transformed["data"].dtype).startswith("datetime")

    assert len(df_transformed) == 2
