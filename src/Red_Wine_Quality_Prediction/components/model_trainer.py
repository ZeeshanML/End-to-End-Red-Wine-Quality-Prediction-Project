import pandas as pd
import os
from Red_Wine_Quality_Prediction import logger
from sklearn.ensemble import RandomForestClassifier
import joblib
from Red_Wine_Quality_Prediction.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config : ModelTrainerConfig):
        self.config = config 

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        model = RandomForestClassifier(
            n_estimators=self.config.n_estimators,
            bootstrap=self.config.bootstrap,
            class_weight=self.config.class_weight,
            random_state=42
        )

        model.fit(train_x, train_y)

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))