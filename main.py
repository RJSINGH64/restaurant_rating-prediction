from src.pipeline.training_pipeline import initiate_training_pipeline
from src.excepton import SrcException
import os, sys
if __name__=="__main__":

    try:
        initiate_training_pipeline()

    except Exception as e:
        raise SrcException(e ,sys)