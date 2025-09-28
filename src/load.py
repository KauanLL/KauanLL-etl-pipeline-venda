from sqlalchemy import create_engine

def load_data(df):
    engine = create_engine('sqlite:///../data/vendas.db')
    df.to_sql('vendas', engine, if_exists='replace', index=False)
    print("Dados carregados com sucesso!")