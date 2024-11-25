import pandas as pd
import numpy as np 
from src.config import mongo_client
from src.excepton import SrcException
import dill
import yaml
from src.logger import logging
import os,sys

def get_collection_as_dataframe(database_name , collection_name):
    """
    ===================================================================
    ThisFuntion is used to export Data from MongoDB and Convert it into Dataframe
    
    database_nameb :str = name of database inside MongoDB Atlas
    
    collection :str  = collection name inside MongoDB Atlas
    
    In case of error make sure to create .env file with mongo url 
    
    return dataframe as df
    ====================================================================
    """
    try:
        logging.info(f'collecting Data from Database {database_name} Collection {collection_name}')
        df=pd.DataFrame(mongo_client[database_name][collection_name].find())
        logging.info(f'Dataframe columns Available Rows {df.shape[0]} columns {df.shape[1]}')
        if '_id' in df.columns:
            df=df.drop("_id" , axis=1)
        df.to_csv("dataset/zomato.csv" ,index=False)    
        return df 
    except Exception as e:
        print(e,sys)


def write_yaml_file(file_path,data:dict):
    try:
        file_dir = os.path.dirname(file_path)
        os.makedirs(file_dir,exist_ok=True)
        with open(file_path,"w") as file_writer:
            yaml.dump(data,file_writer)
    except Exception as e:
        raise SrcException(e, sys)
    

def convert_columns_float(df: pd.DataFrame, exclude_columns: list) -> pd.DataFrame:
    try:
        for column in df.columns:
            if column not in exclude_columns:
                if df[column].dtype == 'object':  # Check if it's a string
                    logging.info(f"Skipping conversion for non-numeric column: {column}")
                    continue  # Skip non-numeric columns

                try:
                    df[column] = df[column].astype('float')
                except ValueError as e:
                    logging.warning(f"Column '{column}' could not be converted to float: {e}")
        return df
    except Exception as e:
        raise e

