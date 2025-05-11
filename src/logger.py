import logging
import os
from datetime import datetime

# Creating a unique log file name with current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Defining the full path where the log file will be stored (inside a 'logs' directory)
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)

# Creating the 'logs' directory if it doesn't exist
os.makedirs(logs_path,exist_ok=True)

# Full path to the log file
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

# Configuring the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format = "[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
 )

 