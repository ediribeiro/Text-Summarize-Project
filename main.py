from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validate import DataValidateTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX=============X")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Validation Stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataValidateTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX=============X")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = 'Data Transformation Stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataTransformationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX=============X")
except Exception as e:
    logger.exception(e)
    raise e

"""STAGE_NAME = 'Model Trainer Stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = ModelTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX=============X")
except Exception as e:
    logger.exception(e)
    raise e"""

STAGE_NAME = 'Model Evaluation Stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = ModelTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nX=============X")
except Exception as e:
    logger.exception(e)
    raise e