from prefect import flow, task, get_run_logger
import pandas as pd
from extract import extract_data
from transform import transform_data
from load import load_data

@task
def extract(path: str):
    logger = get_run_logger()
    logger.info(f'Lendo arquivo CSV de {path}')
    return extract_data()

@task
def transform(df: pd.DataFrame):
    logger = get_run_logger()
    logger.info(f'Iniciando transformação e validação dos dados')
    return transform_data(df)

@task
def load(df: pd.DataFrame, db_path: str):
    logger = get_run_logger()
    logger.info(f'Carregando dados em {db_path}')
    load_data(df)

@flow
def etl_pipeline(path: str, db_path: str):
    logger = get_run_logger()
    logger.info('Pipeline ETL inicializando')
    df = extract(path)
    df = transform(df)
    load(df, db_path)
    logger.info('Pipeline finalizado com sucesso')
    
if __name__ == "__main__":
    etl_pipeline("data/vendas.csv", "data/vendas.db")