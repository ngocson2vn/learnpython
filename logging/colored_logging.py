"""
pip3 install coloredlogs
"""
import logging
import coloredlogs

# install a handler on the root logger
coloredlogs.install(
    fmt='%(levelname)s %(message)s'
)

logging.info("This is a info message")
logging.warning("This is a warning message")
logging.error("This is a error message")