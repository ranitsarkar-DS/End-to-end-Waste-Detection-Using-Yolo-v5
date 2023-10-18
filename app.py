from wasteDetection.exception import AppException
from wasteDetection.logger import logging
import sys

try:
    a = 3 / "s"
except Exception as e:
    raise AppException(e,sys)


