import sys
from src.logger import logging 

def error_message_detail(error,error_detail):
    # extract exception info from the sys model
    _,_,exc_tb = error_detail.exc_info()
    # get the file name where the exception occured
    file_name = exc_tb.tb_frame.f_code.co_filename
    # Format a detailed error message with script name, line number, and error message
    error_message = f'Error occured in Python script name : {file_name} ,line nnumber : {exc_tb.tb_lineno}, error message : {str(error)}'

    return error_message



class CustomException(Exception):
    # Constructor takes the original error message and the system error detail (sys)
    def __init__(self, error_message,error_detail):
         # Initialize the base Exception with the original error message
        super().__init__(error_message)
        # Store the detailed error message using the helper function
        self.error_message = error_message_detail(error_message,error_detail=error_detail)
        
    # String representation of the CustomException
    def __str__(self):
        return self.error_message

 