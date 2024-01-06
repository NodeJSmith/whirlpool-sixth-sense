import logging

logging.basicConfig(format="%(asctime)s [%(name)s %(levelname)s]: %(message)s")
logger = logging.getLogger("whirlpool")
logger.setLevel(logging.DEBUG)

logger = logging.getLogger("whirlpool.eventsocket")
logger.setLevel(logging.INFO)
