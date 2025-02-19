import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', "train.csv")
    test_data_path: str = os.path.join('artifacts', "test.csv")
    raw_data_path: str = os.path.join('artifacts', "data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # ✅ Check if dataset path is correct
            dataset_path = r'notebook/data/StudentsPerformance.csv'
            if not os.path.exists(dataset_path):
                raise FileNotFoundError(f"Dataset not found at: {dataset_path}")

            df = pd.read_csv(dataset_path)
            logging.info('Read the dataset as dataframe')

            # ✅ Ensure "artifacts" directory exists
            artifacts_dir = "artifacts"
            if not os.path.exists(artifacts_dir):
                logging.info(f"Creating directory: {artifacts_dir}")
                os.makedirs(artifacts_dir, exist_ok=True)
            else:
                logging.info(f"Directory already exists: {artifacts_dir}")

            # ✅ Check if folder is created successfully
            assert os.path.exists(artifacts_dir), "Failed to create 'artifacts' directory"

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            logging.info(f"Raw data saved at: {self.ingestion_config.raw_data_path}")

            logging.info("Train-test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info(f"Train data saved at: {self.ingestion_config.train_data_path}")
            logging.info(f"Test data saved at: {self.ingestion_config.test_data_path}")

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
