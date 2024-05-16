import logging
import os

def setup_logger(execution_id):
    """
    Set up the logger with a specific execution ID.
    
    Parameters:
    execution_id (str): The unique execution ID for the logging session.
    
    Returns:
    Logger: Configured logger object.
    """
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    
    # Set up the logger
    logger = logging.getLogger('RelationalDataFlowLogger')
    logger.setLevel(logging.DEBUG)
    
    # Create file handler
    log_file = 'logs/logs_relational_data_pipeline.txt'
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    
    # Create formatter
    formatter = logging.Formatter(f'%(asctime)s - {execution_id} - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    # Add the file handler to the logger
    logger.addHandler(file_handler)
    
    return logger
