### Main aim is to read a data set from specific data source that data source can be created by data team or cloud team
import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
#This is creating a data class known as data ingestionconfig, which will be used to store data config setting for your data ingestion step
#  
@dataclass
class DataingestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")## This is the path where ur traing data set will be stored
    test_data_path: str=os.path.join('artifacts',"test.csv")## Path where test set will be stored
    raw_data_path: str=os.path.join('artifacts',"data.csv")## path where data part will be stored

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataingestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        ## Here we are trying to read the database from anywhere
        try:
            df = pd.read_csv('notebook/data/stud.csv')  # Use forward slashes

            logging.info('Read the dataset as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data iss completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)

    # modeltrainer=ModelTrainer()
    # print(modeltrainer.initiate_model_trainer(train_arr,test_arr))
   