from Red_Wine_Quality_Prediction import logger
from Red_Wine_Quality_Prediction.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Red_Wine_Quality_Prediction.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from Red_Wine_Quality_Prediction.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from Red_Wine_Quality_Prediction.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline


STAGE_NAME = "Data Ingestion"

try:
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Transformation"
try:
   logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<") 
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Model Trainer"
try:
   logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<") 
   data_ingestion = ModelTrainerTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e
