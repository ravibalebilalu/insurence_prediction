import os
import sys
import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score
from src.exception import CustomException
from sklearn.model_selection import GridSearchCV


def save_object(file_path,obj):
    try:
        # definingg the file path for saving  object
        dir_path = os.path.dirname(file_path)
        # create directory  if it does not exist
        os.makedirs(dir_path,exist_ok=True)
         # Open the file in write-binary mode and dump the object using dill
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_models(x_train,y_train,x_test,y_test,models,params):

    try:
        train_report ,test_report= {},{}
        for name,algo in models.items():
            model = algo
            param = params[name]

            grid_search = GridSearchCV(model,param,cv=3)
            grid_search.fit(x_train,y_train)
            model.set_params(**grid_search.best_params_)
            
            model.fit(x_train,y_train)
            y_train_pred = model.predict(x_train)
            y_test_pred = model.predict(x_test)

            train_model_score = r2_score(y_train,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)
            
            train_report[name] = train_model_score
            test_report[name] = test_model_score
        return [train_report,test_report]

    except Exception as e:
        raise CustomException(e,sys)
    
def load_object(file_path):
    try:
        with open(file_path,"rb")as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)
        