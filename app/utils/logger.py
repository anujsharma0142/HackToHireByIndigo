import logging


formatter = logging.Formatter('%(asctime)s - %(filename) - %(name)s - %(levelname)s - %(message)s')

handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger('indigo-6e')
# logger.setLevel(logger.info)
logger.addHandler(handler)

logger
