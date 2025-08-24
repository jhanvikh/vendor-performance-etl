import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

# Ensure log directory exists
os.makedirs("logs", exist_ok=True)

# Explicit logger setup (works in Jupyter)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/injestion_db.log", mode="a")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

engine = create_engine('sqlite:///inventory.db')

def ingest_db(df, table_name, engine):
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)

def load_raw_data():
    '''this will load CSV in dataframe and ingest into db'''
    start = time.time()
    for file in os.listdir('data'):
        if file.lower().endswith(".csv"):
            df = pd.read_csv(os.path.join("data", file))
            logger.info(f'Ingesting {file} in db')
            ingest_db(df, file[:-4], engine)
    logger.info("Ingestion Complete")
    end = time.time()
    total_time = (end - start) / 60
    logger.info("-----------------------Ingestion Complete--------------------------")
    logger.info(f'Total time taken : {total_time:.2f} minutes')

if __name__ == '__main__':
    load_raw_data()
    logging.shutdown()   # flush logs to file
