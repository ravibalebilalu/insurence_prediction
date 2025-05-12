import os
import sys
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object

from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import r2_score

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initial_model_trainer(self,train_arr,test_arr):

        try:
            x_train,y_train,x_test,y_test = train_arr[:,:-1],train_arr[:,-1],test_arr[:,:-1],test_arr[:,-1]
            model = GradientBoostingRegressor()

            params = {
                'n_estimators': [100,200,300],
                'learning_rate':[0.001,0.01, 0.1],
                 
                'loss': ['squared_error', 'absolute_error', 'huber', 'quantile']
            }
            grid_search = GridSearchCV(model,params,cv=3,n_jobs=-1,verbose=2)
            grid_search.fit(x_train,y_train)
            boosted_model = GradientBoostingRegressor()
            boosted_model.set_params(**grid_search.best_params_)

            boosted_model.fit(x_train,y_train)
            save_object(file_path=self.model_trainer_config.trained_model_file_path,obj=boosted_model)
            print(f"train : {boosted_model.score(x_train,y_train)}")
            print(f"test : {boosted_model.score(x_test,y_test)}")
            
        except Exception as e:
            raise CustomException(e,sys)
