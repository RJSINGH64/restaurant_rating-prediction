from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.entity.config_entity import TrainingPipelineConfig , DataIngestionConfig , DataValidationConfig , DataTransformationConfig
from src.excepton import SrcException
from src.logger import logging
import os,sys

def initiate_training_pipeline():

    try:
        #pipeline test
        training_pipeline_config = TrainingPipelineConfig()
        
        #Data Ingestion
        data_ingestion_config= DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact=data_ingestion.initiate_data_ingestion()
        print(f' {">"*20} Data Ingestion Pipeline Completed {"<"*20}')
        logging.info(f' {">"*20} Data Ingestion Pipeline Completed {"<"*20}')

        #Data Validation 
        data_validation_config=DataValidationConfig(training_pipeline_config=training_pipeline_config)
        data_validation=DataValidation(data_validation_config , data_ingestion_artifact)
        data_validation_artifact=data_validation.initiate_data_validation()
        print(f' {">"*20} Data Validation Pipeline Completed {"<"*20}')
        logging.info(f' {">"*20} Data Validation Pipeline Completed {"<"*20}')

        #Data Transformation 
        data_transformation_config=DataTransformationConfig(training_pipeline_config=training_pipeline_config)
        data_transfomation=DataTransformation(data_transformation_config , data_ingestion_artifact)
        data_transformation_artifact=data_transfomation.initiate_data_transformation()
        print(f' {">"*20} Data Transformation Pipeline Completed {"<"*20}')
        logging.info(f' {">"*20} Data Transformation Pipeline Completed {"<"*20}')
   
    except Exception as e:
        raise SrcException(e,sys)
