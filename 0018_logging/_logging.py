# ---------------------------------------------------------------------------- #
#                                    Logging                                   #
# ---------------------------------------------------------------------------- #

import logging, os
os.chdir('0018_logging')

logging.basicConfig(filename="my_log.log",
                    encoding="utf-8", 
                    filemode="w",
                    level=logging.DEBUG)

logging.debug("DEBUG")
logging.info("INFO") 
logging.warning("WARNING")
logging.error("ERROR")
logging.critical("CRITICAL") 