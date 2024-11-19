import pandas as pd
import numpy as np 
from src.config import mongo_client
from src.logger import logging
from data_dump import database_name , collection_name
import os,sys

def get_collection_as_dataframe():
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


