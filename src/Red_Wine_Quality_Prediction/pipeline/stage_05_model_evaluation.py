from Red_Wine_Quality_Prediction.config.configuration import ConfigurationManager
from Red_Wine_Quality_Prediction.components.model_evaluation import ModelEvaluation
from Red_Wine_Quality_Prediction import logger


STAGE_NAME = "Model Evaluation"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_results()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e