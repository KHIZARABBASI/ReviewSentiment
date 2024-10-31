from src.exception import CustomeException
import sys

try:
    a = 4/0
except Exception as e:
    raise CustomeException(e, sys)



