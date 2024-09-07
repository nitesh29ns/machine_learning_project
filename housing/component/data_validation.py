import re
from tkinter import E
from turtle import home
from urllib.request import HTTPPasswordMgrWithPriorAuth
from evidently.dashboard import tabs
from matplotlib.pyplot import table
from evidently.model_profile.sections import DataDriftProfileSection
from sklearn.metrics import rand_score
from housing.logger import lg
from housing.exception import HousingException
from housing.entity.config_entity import datavalidationconfig
from housing.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact
import os, sys
import pandas as pd
import json
from evidently.model_profile import Profile
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab
from housing.util.util import read_yaml_file
from housing import constant


class DataValidation:


    def __init__(self, data_validation_config: datavalidationconfig,
        data_ingestion_artifact: DataIngestionArtifact)-> None:
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_train_test_df(self):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)

            return train_df, test_df
        except Exception as e:
            raise HousingException(e, sys) from e

    def is_train_test_file_exist(self):
        try:
            lg.info("checking is train and test file is available.")
            is_train_file_exist = False
            is_test_file_exist = False

            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            is_train_file_exist = os.path.exists(train_file_path)
            is_test_file_exist = os.path.exists(test_file_path)

            is_available = is_train_file_exist and is_test_file_exist
            lg.info(f"Is train and test file exists? -> {is_available}")

            if not is_available:
                training_file = self.data_ingestion_artifact.train_file_path
                testing_file = self.data_ingestion_artifact.test_file_path

                message = f"training file: {training_file} or testing file: {testing_file} is not present."


            return is_available

        except Exception as e:
            raise HousingException(e, sys) from e

    def validate_dataset_schema(self):
        try:
            validation_status = False
            schema = read_yaml_file(constant.SCHEMA_FILE_PATH)
            train_df, test_df = self.get_train_test_df()
            if True:
                len(train_df.columns) == len(schema["columns"].keys())
                train_df.columns == list(schema['columns'].keys())
                df_values = list(train_df['ocean_proximity'].unique())
                values = list(schema['domain_value'].values())[0]
                for i in df_values:
                    if i in values:
                        pass
                    else:
                        raise HousingException(Exception, sys)
                validation_status = True
            else:
                validation_status = False
            return validation_status
        except Exception as e:
            raise HousingException(e, sys) from e

    def get_and_save_data_drift_report(self):
        try:
            profile = Profile(sections=[DataDriftProfileSection()])

            train_df, test_df = self.get_train_test_df()

            profile.calculate(train_df, test_df)

            report = json.loads(profile.json())

            report_file_path = self.data_validation_config.report_file_path
            report_dir = os.path.dirname(report_file_path)
            os.makedirs(report_dir,exist_ok=True)

            with open(report_file_path, "w") as report_file:
                json.dump(report, report_file, indent=6) 
            return report
        except Exception as e:
            raise HousingException(e, sys) from e

    def save_data_drift_report_page(self):
        try:
            dashboard = Dashboard(tabs=[DataDriftTab()])
            train_df ,test_df = self.get_train_test_df()
            dashboard.calculate(train_df, test_df)

            report_page_file_path = self.data_validation_config.report_page_file_path
            report_page_dir = os.path.dirname(report_page_file_path)
            os.makedirs(report_page_dir,exist_ok=True)

            dashboard.save(report_page_file_path)
        except Exception as e :
            raise HousingException(e, sys) from e
    def is_data_drift_found(self)->bool:
        try:
            report = self.get_and_save_data_drift_report()
            self.save_data_drift_report_page()

            return True
        except Exception as e:
            raise HousingException(e, sys) from e
    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            self.is_train_test_file_exist()
            self.validate_dataset_schema()
            self.is_data_drift_found()

            data_validation_artifact = DataValidationArtifact(
                schema_file_path=self.data_validation_config.schema_file_path,
                report_file_path=self.data_validation_config.report_file_path,
                report_page_file_path=self.data_validation_config.report_page_file_path,
                is_validated= True,
                message="Data validation performed successfully."
            )
            lg.info(f"data_validation_artifact: {data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise HousingException(e, sys) from e
