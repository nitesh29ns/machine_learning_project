from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import lg
from housing.config.configuration import configuration
def main():
    try:
       # pipeline = Pipeline()
       # pipeline.run_pipeline()
       data_validation_config = configuration.get_data_validation_config()
       print(data_validation_config)
    except Exception as e:
        lg.error(f"{e}")
        print(e)


if __name__ =="__main__":
    main()