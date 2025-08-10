import logging
import os
from datetime import datetime

class CustomLogger:
    def __init__(self, log_dir="logs"):
        # Ensure logs directory exists
        self.logs_dir = os.path.join(os.getcwd(), log_dir)
        os.makedirs(self.logs_dir, exist_ok=True)

        # Create timestamped log file name
        log_file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
        self.log_file_path = os.path.join(self.logs_dir, log_file)

        # Create formatter
        self.formatter = logging.Formatter(
            "[ %(asctime)s ] %(levelname)s %(name)s (line:%(lineno)d) - %(message)s"
        )

    def get_logger(self, name=__file__):
        # Get logger instance
        logger = logging.getLogger(os.path.basename(name))
        
        # Avoid adding handlers if they already exist
        if not logger.handlers:
            # File handler
            file_handler = logging.FileHandler(self.log_file_path)
            file_handler.setFormatter(self.formatter)
            
            # Console handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(self.formatter)
            
            # Add handlers
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)
            
            # Set level
            logger.setLevel(logging.INFO)

        return logger

if __name__ == "__main__":
    custom_logger = CustomLogger()
    logger = custom_logger.get_logger(__file__)
    logger.info("Custom logger initialized.")
    
    # Verify file creation
    if os.path.exists(custom_logger.log_file_path):
        print(f"Log file created at: {custom_logger.log_file_path}")
    else:
        print("Failed to create log file!")