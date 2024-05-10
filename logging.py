import logging
import os

def setup_logging(execution_id):
    """Set up logging configuration."""
    log_formatter = logging.Formatter(f'%(asctime)s - {execution_id} - %(levelname)s - %(message)s')

    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)

    file_handler = logging.FileHandler(os.path.join(log_dir, 'logs_relational_data_pipeline.txt'))
    file_handler.setFormatter(log_formatter)

    logger = logging.getLogger('RelationalDataFlowLogger')
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)

    return logger
