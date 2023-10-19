from InShorts.logging import logger
from InShorts.pipeline.stage1_data_ingestion import DataIngestionTrainingPipeline
from InShorts.pipeline.stage2_data_validation import DataValidationTrainingPipeline
from InShorts.pipeline.stage3_data_transformation import DataTransformationTrainingPipeline
from InShorts.pipeline.stage4_model_trainer import ModelTrainerTrainingPipeline
from InShorts.pipeline.stage5_model_evaluation import ModelEvaluationTrainingPipeline

# STAGE_NAME = "DATA INGESTION"

# try:
#     logger.info("Starting {} Stage".format(STAGE_NAME))
#     data_ingestion = DataIngestionTrainingPipeline()
#     data_ingestion.main()
#     logger.info("Completed {} Stage".format(STAGE_NAME))
# except Exception as e:
#     logger.exception(e)
#     raise e

# STAGE_NAME = "DATA VALIDATION"

# try:
#     logger.info("Starting {} Stage".format(STAGE_NAME))
#     data_validation = DataValidationTrainingPipeline()
#     data_validation.main()
#     logger.info("Completed {} Stage".format(STAGE_NAME))
# except Exception as e:
#     logger.exception(e)
#     raise e

# STAGE_NAME = "DATA TRANSFORMATION"

# try:
#     logger.info("Starting {} Stage".format(STAGE_NAME))
#     data_validation = DataTransformationTrainingPipeline()
#     data_validation.main()
#     logger.info("Completed {} Stage".format(STAGE_NAME))
# except Exception as e:
#     logger.exception(e)
#     raise e


# STAGE_NAME = "MODEL TRAINER"

# try:
#     logger.info("Starting {} Stage".format(STAGE_NAME))
#     data_validation = ModelTrainerTrainingPipeline()
#     data_validation.main()
#     logger.info("Completed {} Stage".format(STAGE_NAME))
# except Exception as e:
#     logger.exception(e)
#     raise e


STAGE_NAME = "MODEL EVALUATION"

try:
    logger.info("Starting {} Stage".format(STAGE_NAME))
    data_validation = ModelEvaluationTrainingPipeline()
    data_validation.main()
    logger.info("Completed {} Stage".format(STAGE_NAME))
except Exception as e:
    logger.exception(e)
    raise e

