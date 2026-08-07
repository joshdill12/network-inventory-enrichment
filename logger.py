import logging
import uuid
from datetime import datetime

#Create a unique run ID for this execution that includes runtime and unique identifier
run_id= datetime.now().strftime("%Y%m%d_%H%M%S") + "_" + str(uuid.uuid4())

#creating the logger
def setup_logger():
     
     logging.basicConfig(
        level=logging.INFO,
        format=f"%(asctime)s | {run_id} |  %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )