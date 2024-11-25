from src.excepton import SrcException
from src.logger import logging
import os , sys
from datetime import datetime


class TrainingPipelineConfig:

    def __init__(self):
        
        try:
            self.artifact_directory= os.path.join(os.getcwd() , "artifact" ,f"{datetime.now().strftime('%m%d%y__%H%M%S')}")

        except Exception as e:
            raise SrcException(e ,sys)    
        

class DataIngestionConfig:

    def __init__(self , training_pipeline_config:TrainingPipelineConfig):
        
        self.database_name="Zomato" #name of database 
        self.collection_name= "Restaurant" #Collection name
        self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_directory , "data_ingestion") 
        self.feature_store_file_path= os.path.join(self.data_ingestion_dir , "Feature_Store" , "ZOMATO.csv")
        self.train_file_path = os.path.join(self.data_ingestion_dir , "Datasets" , "train.csv")
        self.test_file_path = os.path.join(self.data_ingestion_dir , "Datasets" , "test.csv")
        self.test_size= 0.3 #Choose Threshold value provided by Domain Experts
          

class DataValidationConfig:
      
      def __init__(self , training_pipeline_config:TrainingPipelineConfig):
          
          self.data_validation_dir=os.path.join(training_pipeline_config.artifact_directory , "data_validation")
          self.report_file_path = os.path.join(self.data_validation_dir , "report.yml")
          self.missing_threshold=0.3 #random threshold
          self.base_data_file_path =os.path.join("dataset/cleaned_zomato.csv")  #Production dataset /old data for validation