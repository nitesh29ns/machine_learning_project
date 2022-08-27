from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import lg
from housing.config.configuration import configuration
from housing.component.data_transformation import DataTransformation
import os



def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(configuration(config_file_path=config_path))
        #pipeline.run_pipeline()
        pipeline.start()
        lg.info("main function execution completed.")
       #data_validation_config = configuration().get_data_transformation_config()
       #print(data_validation_config)
    except Exception as e:
        lg.error(f"{e}")
        print(e)


if __name__ =="__main__":
    main()