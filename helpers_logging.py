import logging #package is responsible for collecting all the logs (see the file)
import os #package is useful for joining information from different files (os.path.join)

# define the log file and open logging session
FILE_LOG = 'file.log'
logger = logging.getLogger()
