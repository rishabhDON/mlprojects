import logging
import os
from datetime import datetime 

# Define log directory
log_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(log_dir, exist_ok=True)  # Create only the directory if it doesn't exist

# Define log file path
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# Print the log file path for debugging
print(f"Log file will be created at: {LOG_FILE_PATH}")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


