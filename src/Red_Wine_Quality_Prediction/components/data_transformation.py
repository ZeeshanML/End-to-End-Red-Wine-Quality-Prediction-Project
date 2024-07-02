import os
from Red_Wine_Quality_Prediction import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from numpy import log
from Red_Wine_Quality_Prediction.entity.config_entity import DataTransformationConfig
from sklearn import preprocessing
from imblearn.over_sampling import SMOTE



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config


    def preprocess_data(self):

        oversample = SMOTE()
        data = pd.read_csv(self.config.data_path)
        data = data.drop('Id', axis=1)

        features, labels = oversample.fit_resample(data.drop('quality', axis=1), data.quality)

        scaler = preprocessing.MinMaxScaler()
        scaled_data = pd.DataFrame(scaler.fit_transform(features), columns=features.columns)

        normalized_arr = preprocessing.normalize(scaled_data)
        normalized_data = pd.DataFrame(normalized_arr, columns=features.columns)

        unskew_data = normalized_data.copy(deep=True)
        unskew_data['residual sugar'] = unskew_data['residual sugar'].replace(0.0, 0.01).apply(log)
        unskew_data['chlorides'] = unskew_data['chlorides'].replace(0.0, 0.01).apply(log)
        unskew_data['total sulfur dioxide'] = unskew_data['total sulfur dioxide'].replace(0.0, 0.01).apply(log)
        unskew_data['free sulfur dioxide'] = unskew_data['free sulfur dioxide'].replace(0.0, 0.01).apply(log)

        unskew_data['quality'] = labels

        unskew_data.to_csv(os.path.join(self.config.root_dir, "preprocessed_data.csv"), index=False)        


    def train_test_spliting(self):
        data = pd.read_csv(self.config.preprocessed_data_path)

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)