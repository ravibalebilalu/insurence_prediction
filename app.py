from flask import Flask,request,render_template
from src.exception import CustomException
from src.logger import logging
import numpy as np
import pandas as pd
from src.pipelines.predict_pipeline import CustomData,PredictPipeline

app = Flask(__name__)

@app.route("/")
def home():
    logging.info("Home page opened or refreshd")
    return render_template("home.html")

@app.route("/predict",methods=["POST","GET"])
def predict_data():
    if request.method == "GET":
        return render_template("home.html")
    else:
        data = CustomData(
                sex = request.form.get("sex"),
                smoker = request.form.get("smoker"),
                loc_y = request.form.get("loc_y"),
                loc_x = request.form.get("loc_x"),
                age = request.form.get("age"),
                bmi = request.form.get("bmi"),
                children = request.form.get("children")
        )
        
         
        pred_df = data.get_data_as_dataframe()
        predict_pipeline = PredictPipeline()
        result  = predict_pipeline.predict(pred_df)[0]
        if result > 0:
            logging.info("data predicted")
        return render_template("home.html",result = round(result))
if __name__ == "__main__":
    app.run(host = "0.0.0.0",debug=True)