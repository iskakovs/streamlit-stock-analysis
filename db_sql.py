import sqlite3 as sq
import pandas as pd
import logging

logger = logging.getLogger()

def create_myTable(db_path, table_name='myTable'):
    """
    create a table if not exist
    :param db_path:
    :type db_path: string
    :param table_name:
    :type table_name: string
    :return: None
    """

conn = sq.connect(db_path)

