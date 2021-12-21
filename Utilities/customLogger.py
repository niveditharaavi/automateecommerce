import logging


class LogGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename='test.log',format='%(asctime)s: %(levelname)s: %(message)s',level=logging.INFO)
        logger = logging.getLogger()
        return logger