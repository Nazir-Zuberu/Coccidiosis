import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log") # Creating a path for running_logs.log
os.makedirs(log_dir, exist_ok=True) # Creating logs directory


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        # Saving logging info in log_filepath
        logging.FileHandler(log_filepath),
        # Displaying logging info on the console
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("Cocci_ClassifierLogger")