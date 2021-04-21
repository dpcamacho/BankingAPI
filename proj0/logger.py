import logging


def log():
    logging.basicConfig(level=logging.INFO, filename='app.log', filemode='a',
                        format='%(name)s - %(levelname)s - %(message)s')

    logging.info("Program Started")
    logging.warning("Import statement not used")
    logging.error("NameError raised")

    logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler('file.log')
    console_handler = logging.StreamHandler()

    formatter = logging.Formatter("%(asctime)s = %(name)s - %(levelname)s - %(message)s")
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)


