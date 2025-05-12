import sys
import numpy as np
import pandas as pd

from src.logger import logging
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path = "artifacts/model.pkl"
            preprocessor_path = "artifacts/preprocessor.pkl"
            model = load_object(model_path)
            preprocessor = load_object(preprocessor_path)
            data_preocessed = preprocessor.transform(features)
            prediction = model.predict(data_preocessed)
            return prediction
        except Exception as e:
            raise CustomException(e,sys)

class CustomData:
    def __init__(self,sex:str, smoker:str, loc_y:str, loc_x:str,age:int, bmi:float, children:int):
        self.sex = sex
        self.smoker = smoker
        self.loc_y = loc_y
        self.loc_x  = loc_x 
        self.age = age
        self.bmi = bmi
        self.children = children

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "sex":[self.sex],
                "smoker":[self.smoker],
                "loc_y":[self.loc_y],
                "loc_x":[self.loc_x],
                "age":[self.age],
                "bmi":[self.bmi],
                "children":[self.children]
            }
            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e,sys)