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

    try:
        cursor = conn.cursor()
        cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT,
                start_date DATE,
                end_date DATE,
                name TEXT,
                comment TEXT
            )
        ''')
        conn.commit()
        logger.info(f'''table={table_name} | Success''')
        
