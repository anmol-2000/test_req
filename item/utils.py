import logging
import sys
import os
import sqlite3
from logging.handlers import TimedRotatingFileHandler

FORMATTER = logging.Formatter('%(asctime)s - %(levelname)s - %(lineno)d - %(message)s')

def get_db_connection():
    try:
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute('''Create Table If Not Exists item_book
                    (item_id Integer Primary Key AUTOINCREMENT, userid TEXT,item_name Text, item_price Float)''')
        
        cursor.execute('''CREATE TABLE IF NOT EXISTS user (
                            userid TEXT PRIMARY KEY,
                            password TEXT)''')

        # Insert a default user named admin if the user table is empty
        cursor.execute('''INSERT INTO user (userid, password)
                          SELECT 'admin', '$2b$12$gv0tukvgxt1sNYg5KLQG3O8ofWHY8jUh81oBA.nRwVTRjxEB8eItC'
                          WHERE NOT EXISTS (SELECT 1 FROM user where userid='admin')''')
        cursor.execute('''INSERT INTO user (userid, password)
                          SELECT 'normal', '$2b$12$gv0tukvgxt1sNYg5KLQG3O8ofWHY8jUh81oBA.nRwVTRjxEB8eItC'
                          WHERE NOT EXISTS (SELECT 1 FROM user where userid='normal')''')
        conn.commit()
        return conn
    except Exception as err:
        raise Exception("Not able to connect")

def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler

def get_file_handler(log_file):
    file_handler = TimedRotatingFileHandler(log_file, when='midnight', backupCount=3)
    file_handler.setFormatter(FORMATTER)
    return file_handler

def get_logger(logger_name):
    logs_dir = "logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir, exist_ok=True)

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_console_handler())
    logger.addHandler(get_file_handler(f"{logs_dir}/item.log"))

    return logger