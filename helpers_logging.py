import logging #package is responsible for collecting all the logs (see the file)
import os #package is useful for joining information from different files (os.path.join)

# define the log file and open logging session
FILE_LOG = 'file.log'
logger = logging.getLogger()

# define init_logging function that uses 'dir_path' variable from 'run_streamlit' file. Everything to collect the logs
def init_logging(dir_path, file_log='file.log', console_log_level='CRITICAL', file_log_level='CRITICAL',
                 discard_old_info=False):
