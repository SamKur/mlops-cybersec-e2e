import os
import logging
from datetime import datetime

# Create logs directory if not exists
LOGS_DIR = os.path.join(os.getcwd(), "logs")
os.makedirs(LOGS_DIR, exist_ok=True)

# Generate a timestamped log filename
timestamp = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
log_filename = f"{timestamp}.log"
log_filepath = os.path.join(LOGS_DIR, log_filename)

# Configure logging
logging.basicConfig(
    filename=log_filepath,
    level=logging.INFO,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    filemode='a'  # optional: ensures logs append if file exists
)

# Console logger - Uncomment to display log to console as well

# console = logging.StreamHandler()
# console.setLevel(logging.INFO)
# formatter = logging.Formatter("[ %(asctime)s ] %(levelname)s - %(message)s")
# console.setFormatter(formatter)
# logging.getLogger().addHandler(console) # Attach to root logger 
