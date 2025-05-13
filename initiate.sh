#!/bin/bash
# This script is used to set up the virtual environment, install dependencies, and run the data ingestion script.

 
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
 
source venv/bin/activate
pip install --upgrade pip
 
pip install -r requirements.txt
 
export PYTHONPATH=.; python src/components/data_ingestion.py
 
echo "Data ingestion completed. Do you want to run the app.py script? (y/n)"
read choice
if [ "$choice" == "y" ]; then
    echo "App will running on  http://127.0.0.1:5000"
   
    export PYTHONPATH=.; python app.py
    
    

else
    echo "Run the app.py script manually using the command 'python app.py' in the terminal."
    echo "Cant run app.py script? Rerun the initiate.sh script and 'y' when prompted to run app.py script.This happens for the first time only."
    echo "This makes sure that the app.py script is run in the same environment as the data ingestion script."
    echo "Hereafter, you can run the app.py script manually using the command 'python app.py' in the terminal."
fi
echo "Thanks for installing this 'INSURENCE PREDICTION'"






