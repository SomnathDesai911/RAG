import logging

def set_logging(log_file:str,mode:str):
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)s:%(name)s:%(message)s:%(asctime)s',
        datefmt='%d/%m/%Y %I:%M:%S',
        handlers=[
            logging.FileHandler(log_file, mode=mode),
            logging.StreamHandler()
        ]
    )

def get_logger(name: str):
    return logging.getLogger(name)


