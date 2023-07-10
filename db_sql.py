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
    except Exception as e:
        logger.error(f'''table={table_name} | Error: {str(e)}''')
    finally:
        if conn:
            conn.close()

def save_into_db(db_path, symbol, start_date, end_date, name, comment):
    """
    create a new record into database
    :param db_path: Database path
    :type db_path: str
    :param symbol: ticker name
    :type symbol: str
    :param start_date: start date
    :type start_date: date
    :param end_date: end date
    :type end_date: date
    :param name: record name
    :type name: str
    :param comment: Comment
    :type comment: str
    :return: None
    """
    conn = sq.connect(db_path)
    
    try:
        c = conn.cursor()
        c.execute("INSERT INTO myTable (symbol, start_date, end_date, name, comment) VALUES (?, ?, ?, ?, ?)",
                  (symbol, start_date, end_date, name, comment))
        conn.commit()
        logger.info(f'name={name} | Success')
    except sq.Error as e:
        logger.info(f'name={name} | Error={str(e)}')
    finally:
        if conn:
            conn.close()

