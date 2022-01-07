# >-------------------------------------------------- LOGGER ---------------------------------------------------------<
import logging

# create a directory if it does not exist
import os

from data.constants import APP_DATA, APP_ID, APP_NAME

if not os.path.exists(APP_DATA):
    os.makedirs(APP_DATA)

# log file address
log_file = os.path.join(APP_DATA, f'{APP_ID}.log')

if not os.path.isfile(log_file):
    with open(log_file, "w") as log_f:
        log_f.write("")

# define logging object
log_obj = logging.getLogger(APP_NAME)
log_obj.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler(log_file)
handler.setLevel(logging.DEBUG)

# create a logging format
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
log_obj.addHandler(handler)


def SENT_TO_LOG(text="", type="INFO"):
    if type == "INFO":
        log_obj.info(text)
    elif type == "ERROR":
        log_obj.error(text)
    elif type == "CRITICAL":
        log_obj.critical(text)
    else:
        log_obj.warning(text)