# This file compiles all the files in one
import logging #package is responsible for collecting all the logs (see the file)
import os #package is useful for joining information from different files (os.path.join)

import repository #imports the 'repository.py' file to the Python project 'main.py' file
import view #imports the 'view.py' file to the Python project 'main.py' file
import helpers_logging #imports the 'helpers_logging.py' file to the Python project 'main.py' file
import db_sql #imports the 'db_sql.py' file to the Python project 'main.py' file

logger = logging.getLogger()

# Defining 'main' function
def main():
    """
    main function
    :return: None
    """
    config = repository.get_config()

    helpers_logging.init_logging(dir_path=os.path.dirname(__file__),
                                 file_log=config['initialisation']['log_file'],
                                 console_log_level=config['initialisation']['log_level_console'],
                                 file_log_level=config['initialisation']['log_level_file'],
                                 discard_old_info=config['initialisation']['discard_old_info'])
    db_path = repository.get_database_path(config['sqlite_parameters']['database'])
    db_sql.create_myTable(db_path=db_path,
                          table_name=config['sqlite_parameters']['table'])
    view.config_streamlit(config=config, db_path=db_path)

    logger.info('End Main')


if __name__ == "__main__":
    main()
