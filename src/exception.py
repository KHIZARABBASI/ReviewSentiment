import sys

def error_message_detail(error, error_detail: sys):
    _,_, exc_tb = error_detail.exc_info()

    file_name= exc_tb.tb_frame.f_code.co_filename
    error_message = f'Error occure in python script [{file_name}], line no [{ exc_tb.tb_lineno}] error message [{str(error)}]'
    #. format(file_name,  exc_tb.tb_lineno, str(error))
    return error_message

        
    
class CustomeException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_mesage = error_message_detail(error_message, error_detail)        

    def __str__(self):
        return self.error_mesage