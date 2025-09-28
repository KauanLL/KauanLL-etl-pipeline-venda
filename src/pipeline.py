from perfect import flow, task
from extract import extract_data
from transform import transform_data
from load import load_data

@task
def extract():
    return extract_data()

@task
def transform(df):
    return transform_data(df)

@task
def load(df):
    load_data(df)

@flow
def etl_pipeline():
    df = extract()
    df = transform(df)
    load(df)
    
if __name__ == "__main__":
    etl_pipeline()