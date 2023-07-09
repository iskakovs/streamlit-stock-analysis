import logging #package is responsible for collecting all the logs (see the file)
import os #package is useful for joining information from different files (os.path.join)

# define the log file and open logging session
FILE_LOG = 'file.log'
logger = logging.getLogger()

# define init_logging function that uses 'dir_path' variable from 'run_streamlit' file. Everything to collect the logs
def init_logging(dir_path, file_log='file.log', console_log_level='CRITICAL', file_log_level='CRITICAL',
                 discard_old_info=False):
 """
    create a console log and a file log

    :param dir_path:
    :type dir_path: str
    :param file_log: log file name with extension log
    :type file_log: str
    :param console_log_level: DEBUG, INFO, WARNING, ERROR, CRITICAL
    :type console_log_level: str
    :param file_log_level: DEBUG, INFO, WARNING, ERROR, CRITICAL
    :type file_log_level: str
    :param discard_old_info:
    :type discard_old_info: Boolean
    :return: None
    """
    path = os.path.join(dir_path, file_log)

    if discard_old_info:
        with open(path, "w") as f:
            f.write('')
    console_format = '%(name)s | %(funcName)s | %(levelname)s | %(message)s'
    logging.basicConfig(level=console_log_level, format=console_format)

