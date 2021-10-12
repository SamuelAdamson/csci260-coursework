# General Operations for Tables
# Samuel Adamson

import sqlite3 as sqlite
import config

# Drop Table
def drop_table(tabName, db=config.DB_NAME):
    # Establish DB Connection
    connection = sqlite.connect(db)
    cursor = connection.cursor()

    # Sql Command
    sql = f'drop table if exists { tabName }'

    # Execute sql and close connection
    cursor.execute(sql)
    connection.commit()
    connection.close()

# Create Table
def create_table(sql, db=config.DB_NAME):
    # Establish DB Connection
    connection = sqlite.connect(db)
    cursor = connection.cursor()

    # Execute sql and close connection
    cursor.execute(sql)
    connection.commit()
    connection.close()

# Insert into Table
def insert_table(sql, params, db=config.DB_NAME):
    # Establish DB Connection
    connection = sqlite.connect(db)
    cursor = connection.cursor()

    # Execute sql and close connection
    cursor.execute(sql, params)
    connection.commit()
    connection.close()

    # Return last row id
    return cursor.lastrowid

# Select from table -- Fetch One
def select_from_table(sql, params, db=config.DB_NAME):
    # Establish DB Connection
    connection = sqlite.connect(db)
    cursor = connection.cursor()

    # Execute sql and store response
    cursor.execute(sql, params)
    connection.commit()
    response = cursor.fetchone() # Select Statement Response

    # Close connection
    connection.close()

    # Return response if not null
    return response if not None else None

# Select from table -- Fetch All -- Get more than one response
def select_from_table_all(sql, params, db=config.DB_NAME):
    # Establish DB Connection
    connection = sqlite.connect(db)
    cursor = connection.cursor()

    # Execute sql and store response
    cursor.execute(sql, params)
    connection.commit()
    response = cursor.fetchall() # Select Statement Response

    # Close connection
    connection.close()

    # Return response if not null
    return response if not None else None

