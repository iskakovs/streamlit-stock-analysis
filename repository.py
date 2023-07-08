import helpers_config #imports the 'helpers_logging.py' file to the 'repository.py' file
import os #package is useful for joining information from different files (os.path.join)

# Here we define two functions 'get_config' and 'get_get_database_path'
# 'get_config' used to load the configuration information from the 'config.toml' file

def get_config(toml_file='config.toml'):
    """
    get config information from a toml file
    :param toml_file: toml_file name with extension
    :type toml_file: str
    :return: config information
    :rtype: dict
    """
full_path = os.path.join(os.path.dirname(__file__), toml_file)
    paths = helpers_config.get_toml_data(full_path)
    return paths

# 'get_database_path' takes a database name as a parameter and returns the full path to that database

def get_database_path(db_name):
    """
    get database path
    :param db_name: database name
    :type db_name: str
    :return: database path
    :rtype: string
    """
  path = os.path.join(os.path.dirname(__file__), db_name)
    return path

