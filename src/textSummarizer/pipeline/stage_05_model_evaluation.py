from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_evaluation import ModelEvaluation
from textSummarizer.logging import logger

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.evaluate()