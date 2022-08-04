from collections import namedtuple
### entity is used to give the structure to the configuration. 

dataingestionconfig = namedtuple("dataingestionconfig",
["dataset_download_url","tgz_download_dir","raw_data_dir","ingested_train_dir","ingested_test_dir"])


datavalidationconfig = namedtuple("datavalidationconfig",["schema_file_path","report_file_path","report_page_file_path"])

dataTransformationconfig = namedtuple("dataTraformationconfig",["add_bedroom_per_room",
                                                                "transformed_train_dir",
                                                                "transformed_test_dir",
                                                                "preprocessed_object_file_path"])


modelTrainerconfig = namedtuple("modelTrainerconfig",["trained_model_file_path","base_accuracy"])

modelEvaluationconfig = namedtuple("modelEvaluationconfig",["model_evaluation_file_path","time_stamp"])


modelPusherconfig = namedtuple("modelPusherconfig",["export_dir_path"])


trainingPipelineconfig = namedtuple("trainingPiplineconfig",["artifact_dir"])

