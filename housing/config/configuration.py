import housing
# from housing.constant import CONFIG_FILE_NAME, CONFIG_FILE_PATH, CURRENT_TIME_STAMP, DATA_INGESTION_ARTIFACT_DIR, DATA_INGESTION_CONFIG_KEY, DATA_INGESTION_DOWNLOAD_DIR_KEY, DATA_INGESTION_INGESTED_DIR_NAME_KEY, DATA_INGESTION_RAW_DATA_DIR_KEY, DATA_INGESTION_TEST_DIR_KEY, DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY, DATA_INGESTION_TRAIN_DIR_KEY, DATA_TRANSFORMATION_ADD_BEDROOM_PER_ROOM_KEY, DATA_TRANSFORMATION_ARTIFACT_KEY, DATA_TRANSFORMATION_CONFIG_KEY, DATA_TRANSFORMATION_PREPROCESSED_OBJECT_FILE_NAME_KEY, DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY, DATA_TRANSFORMATION_TRANSFORMED_DIR_KEY, DATA_TRANSFORMATION_TRANSFORMED_TEST_DIR_KEY, DATA_TRANSFORMATION_TRANSFORMED_TRAIN_DIR_KEY, DATA_VALIDATION_ARTIFACT_DIR_NAME, DATA_VALIDATION_ARTIFACT_KEY, DATA_VALIDATION_CONFIG_KEY, DATA_VALIDATION_REPORT_FILE_NAME_KEY, DATA_VALIDATION_REPORT_PAGE_FILE_NAME, DATA_VALIDATION_SCHEMA_DIR_KEY, DATA_VALIDATION_SCHEMA_FILE_NAME_KEY, MODEL_EVALUATION_ARTIFACT_KEY, MODEL_EVALUATION_CONFIG_KEY, MODEL_EVALUATION_FILE_NAME, MODEL_PUSHER_ARTIFACT_KEY, MODEL_PUSHER_CONFIG_KEY, MODEL_PUSHER_EXPORT_KEY, MODEL_TRAINER_ARTIFACT_DIR_KEY, MODEL_TRAINER_BASE_ACCURACY, MODEL_TRAINER_CONFIG_KEY, MODEL_TRAINER_MODEL_CONFIG_DIR_KEY, MODEL_TRAINER_MODEL_CONFIG_FILE_NAME, MODEL_TRAINER_MODEL_FILE_NAME, MODEL_TRAINER_TRAINED_MODEL_DIR_KEY, ROOT_DIR, TRAINING_PIPELINE_ARTIFACT_DIR_KEY, TRAINING_PIPELINE_CONFIG_KEY, TRAINING_PIPELINE_NAME_KEY
from housing.constant import *
from housing.entity.config_entity import dataingestionconfig,datavalidationconfig, dataTransformationconfig, \
  modelTrainerconfig,  modelEvaluationconfig, modelPusherconfig, trainingPipelineconfig
from housing.util.util import read_yaml_file

import os,sys
from datetime import datetime
from housing.exception import HousingException
from housing.logger import lg

class configuration:
    
    def __init__(self,
        config_file_path:str = CONFIG_FILE_PATH,
        current_time_stamp:str =CURRENT_TIME_STAMP) -> None:
        try :
            self.config_info = read_yaml_file(file_path = config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
        except Exception as e:
            raise HousingException(e,sys) from e

    def get_data_ingestion_config(self) -> dataingestionconfig :
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir = os.path.join(
                artifact_dir,
                DATA_INGESTION_ARTIFACT_DIR,
                self.time_stamp
            )
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]

            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_DIR_KEY]
           
            tgz_download_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_TGZ_DOWNLOAD_DIR_KEY]
            )
            
            raw_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_RAW_DATA_DIR_KEY])

            ingested_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_INGESTED_DIR_NAME_KEY])
            
            ingested_train_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY])
            
            
            ingested_test_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY])

            data_ingestion_config = dataingestionconfig(
                dataset_download_url=dataset_download_url,
                tgz_download_dir=tgz_download_dir,
                raw_data_dir=raw_data_dir,
                ingested_train_dir=ingested_train_dir,
                ingested_test_dir=ingested_test_dir)


            lg.info(f"data ingestion config: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e :
            raise HousingException(e,sys) from e

    def get_data_validation_config(self) -> datavalidationconfig :
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            
            data_validation_artifact_dir = os.path.join(
                artifact_dir,
                DATA_VALIDATION_ARTIFACT_DIR_NAME,
                self.time_stamp)

            data_validation_info = self.config_info[DATA_VALIDATION_CONFIG_KEY]

            schema_file_path = os.path.join(ROOT_DIR,
            data_validation_info[DATA_VALIDATION_SCHEMA_DIR_KEY],
            data_validation_info[DATA_VALIDATION_SCHEMA_FILE_NAME_KEY]
            )

            report_file_path = os.path.join(data_validation_artifact_dir,
            data_validation_info[DATA_VALIDATION_REPORT_FILE_NAME_KEY])

            report_page_file_path = os.path.join(data_validation_artifact_dir,
            data_validation_info[DATA_VALIDATION_REPORT_PAGE_FILE_NAME_KEY])

            data_validation_config = datavalidationconfig(
                schema_file_path=schema_file_path,
                report_file_path=report_file_path,
                report_page_file_path=report_page_file_path,)
                
                
            lg.info(f"data validation config {data_validation_config}")
            return data_validation_config
        
        except Exception as e :
            raise HousingException(e,sys) from e
    
    def get_data_transformation_config(self) -> dataTransformationconfig :
        try:
            
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_transformation_artifact_dir = os.path.join(
                artifact_dir,
                DATA_TRANSFORMATION_ARTIFACT_KEY,
                self.time_stamp
            )

            data_transformation_info = self.config_info[DATA_TRANSFORMATION_CONFIG_KEY]

            add_bedroom_per_room=data_transformation_info[DATA_TRANSFORMATION_ADD_BEDROOM_PER_ROOM_KEY]

            preprocessed_object_file_path = os.path.join(
                data_transformation_artifact_dir,
                data_transformation_info[DATA_TRANSFORMATION_PREPROCESSING_DIR_KEY],
                data_transformation_info[DATA_TRANSFORMATION_PREPROCESSED_OBJECT_FILE_NAME_KEY]
            )

            
            transformed_train_dir=os.path.join(
            data_transformation_artifact_dir,
            data_transformation_info[DATA_TRANSFORMATION_TRANSFORMED_DIR_KEY],
            data_transformation_info[DATA_TRANSFORMATION_TRANSFORMED_TRAIN_DIR_KEY]
            )


            transformed_test_dir = os.path.join(
            data_transformation_artifact_dir,
            data_transformation_info[DATA_TRANSFORMATION_TRANSFORMED_DIR_KEY],
            data_transformation_info[DATA_TRANSFORMATION_TRANSFORMED_TEST_DIR_KEY]

            )
            

            data_transformation_config=dataTransformationconfig(
                add_bedroom_per_room=add_bedroom_per_room,
                preprocessed_object_file_path=preprocessed_object_file_path,
                transformed_train_dir=transformed_train_dir,
                transformed_test_dir=transformed_test_dir
            )

            
            lg.info(f"data transformation {data_transformation_config}")
            return data_transformation_config
        
        except Exception as e :
            raise HousingException(e,sys) from e

    def get_model_trainer_config(self) ->modelTrainerconfig :
        try:
            artifact_dir = self.training_pipeline_config.artifact_dir
            model_training_artifact_dir = os.path.join(
                artifact_dir,
                MODEL_TRAINER_ARTIFACT_DIR_KEY,
                self.time_stamp
            )

            model_trainer_info = self.config_info[MODEL_TRAINER_CONFIG_KEY]

            trained_model_file_path = os.path.join(model_training_artifact_dir,
            model_trainer_info[MODEL_TRAINER_TRAINED_MODEL_DIR_KEY],
            model_trainer_info[MODEL_TRAINER_MODEL_FILE_NAME]
            )

            model_config_file_path = os.path.join(model_trainer_info[MODEL_TRAINER_MODEL_CONFIG_DIR_KEY],
            model_trainer_info[MODEL_TRAINER_MODEL_CONFIG_FILE_NAME]
            )

            base_accuracy = model_trainer_info[MODEL_TRAINER_BASE_ACCURACY]
            
            
            model_trainer_config = modelTrainerconfig(
                trained_model_file_path=trained_model_file_path,
                base_accuracy=base_accuracy,
                model_config_file_path=model_config_file_path
            )


            lg.info(f"train model config {model_trainer_config}")
            return model_trainer_config
        
        except Exception as e :
            raise HousingException(e,sys) from e

    def get_model_evaluation_config(self) -> modelEvaluationconfig:
        try:
            model_evaluation_config = self.config_info[MODEL_EVALUATION_CONFIG_KEY]
            artifact_dir = os.path.join(self.training_pipeline_config.artifact_dir,
                                        MODEL_EVALUATION_ARTIFACT_DIR, )

            model_evaluation_file_path = os.path.join(artifact_dir,
                                                    model_evaluation_config[MODEL_EVALUATION_FILE_NAME])
            response = modelEvaluationconfig(model_evaluation_file_path=model_evaluation_file_path,
                                            time_stamp=self.time_stamp)
            
            lg.info(f"model evaluation config: {response}.")
            return response
        
        except Exception as e :
            raise HousingException(e,sys) from e

    def get_model_pusher_config(self) -> modelPusherconfig :
        try:
            time_stamp = f"{datetime.now().strftime('%Y%m%d%H%M%S')}"
            model_pusher_config_info = self.config_info[MODEL_PUSHER_CONFIG_KEY]
            export_dir_path = os.path.join(ROOT_DIR, model_pusher_config_info[MODEL_PUSHER_EXPORT_KEY],
                                           time_stamp)

            model_pusher_config = modelPusherconfig(export_dir_path=export_dir_path)
            lg.info(f"Model pusher config {model_pusher_config}")
            return model_pusher_config

        except Exception as e :
            raise HousingException(e,sys) from e

    def get_training_pipeline_config(self) ->trainingPipelineconfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )

            training_pipeline_config = trainingPipelineconfig(artifact_dir=artifact_dir)
            lg.info(f"Training pipleine config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise HousingException(e,sys) from e

    