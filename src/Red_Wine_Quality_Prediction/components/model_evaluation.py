import os
import pandas as pd
from sklearn.metrics import classification_report, accuracy_score
import numpy as np
import joblib
from Red_Wine_Quality_Prediction.utils.common import logger, save_json
from Red_Wine_Quality_Prediction.entity.config_entity import ModelEvaluationConfig
from pathlib import Path


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def eval_metrics(self, actual, pred):
        accuracy = accuracy_score(actual, pred) * 100
        metrics = classification_report(actual, pred)
        return metrics, accuracy

    def save_results(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[self.config.target_column]

        pred = model.predict(test_x)

        metrics, accuracy = self.eval_metrics(test_y, pred)

        scores = {
            "accuracy": accuracy,
            "classification_report": metrics
        }

        save_json(path=Path(self.config.metric_file_name), data=scores)