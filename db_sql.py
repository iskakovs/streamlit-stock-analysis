import sqlite3 as sq
import pandas as pd
import logging

logger = logging.getLogger()

def create_myTable(db_path, table_name='myTable'):
