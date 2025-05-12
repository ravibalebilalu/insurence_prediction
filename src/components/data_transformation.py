import os
import sys
from dataclasses import dataclass
import pickle

import pandas as pd
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler,OneHotEncoder,FunctionTransformer
from sklearn.compose import ColumnTransformer

from sklearn.model_selection import train_test_split,GridSearchCV


from src.exception import CustomException
from src.logger import logging
from src.utils import chop_outliers,save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts","preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation_object(self):
        try:
           
            numerical_columns = ['age', 'bmi', 'children']
            categorical_columns = ['sex', 'smoker', 'loc_y', 'loc_x']

            outlier_transformer = FunctionTransformer(chop_outliers)

            cat_pipe = Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("encoder",OneHotEncoder(handle_unknown="ignore",sparse_output=False)),
                    ("scaler",StandardScaler())
                ]
            )

            nums_pipe =  Pipeline(
                steps=(
                    [
                        ("imputer",SimpleImputer(strategy="mean")),
                        ("outliers",outlier_transformer),
                        ("scaler",StandardScaler())
                    ]
                )
            )
            preprocessor = ColumnTransformer(
               [ ("num",nums_pipe,numerical_columns),
                ("cat",cat_pipe,categorical_columns)]
            )

            return preprocessor
            
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("Read train and test data")

            train_df["loc_y"] =  train_df["region"].apply(lambda x: x[:5])
            train_df["loc_x"] =  train_df["region"].apply(lambda x: x[5:])

            test_df["loc_y"] =  test_df["region"].apply(lambda x: x[:5])
            test_df["loc_x"] =  test_df["region"].apply(lambda x: x[5:])
            train_df.drop(columns="region",inplace=True)
            test_df.drop(columns="region",inplace=True)

            preprocessing_obj = self.get_data_transformation_object()

            target_column_name = "expenses"

            input_feature_train_df = train_df.drop(columns=target_column_name)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=target_column_name)
            target_feature_test_df = test_df[target_column_name]
            logging.info("Seperating independent and dependent deatires")
             

            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_df = preprocessing_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr,np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_df,np.array(target_feature_test_df)]

            save_object(file_path=self.data_transformation_config.preprocessor_obj_file_path,obj=preprocessing_obj)
            logging.info("preprocessing object saved")

            return (train_arr,test_arr,self.data_transformation_config.preprocessor_obj_file_path)
        except Exception as e:
            raise CustomException(e,sys)
