import os
import sys
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
import pandas as pd
from dataclasses import dataclass

@dataclass

class DataIngestionConfig:
    train_path: str=os.path.join("artifacts","train.csv")
    test_path: str=os.path.join("artifacts","test.csv")
    raw_path: str=os.path.join("artifacts","raw.csv")
    
class Dataingestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        
    def dataingestionmethod(self):
        logging.info("Entering into train and test split region")
        try:
            df=pd.read_csv("notebook\data\insurance.csv")
            logging.info("Reading that csv")
            os.makedirs(os.path.dirname(self.ingestion_config.train_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_path,index=False,header=True)
            logging.info("Splitting the dataset")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=10)
            train_set.to_csv(self.ingestion_config.train_path,index=True,header=True)
            logging.info("saving it as train data")
            test_set.to_csv(self.ingestion_config.test_path,index=True,header=True)
            logging.info("Ingestion of dataset is completed")
            
            return (
                self.ingestion_config.train_path,
                self.ingestion_config.test_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        
        
if __name__=="__main__":
    obj=Dataingestion()
    obj.dataingestionmethod()