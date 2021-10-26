# Datatable -- Airlines -- Contains Data on Each Airline
# Samuel Adamson

# Outputting Tabular Data
from tabulate import tabulate

import config
import operations
import filterValues as filter

# Table Schema
TAB_NAME = 'airline'
# Columns
COL_ID = 'ID'
COL_NAME = 'name'


# Create Airline Table
def create_airline_table(db=config.DB_NAME):
    # Output for testing
    # print('Airline table created...')

    # Create Table Command
    sql = f''' 
        create table if not exists { TAB_NAME } (
            { COL_ID } integer primary key,
            { COL_NAME } string not null
        )
    '''
    # Sqlite operations
    operations.create_table(sql, db)


# Drop Airline Table
def drop_airline_table(db=config.DB_NAME):    
    # Sqlite operations
    operations.drop_table(TAB_NAME, db)


# Insert into Airline Table
# Returns last row id of insert
def insert_airline(values, db=config.DB_NAME):
    # Output for testing
    # print('Inserting into Airline table...')

    # Insert Into Table Command
    sql = f'''
        insert into { TAB_NAME } (
            { COL_NAME }
        )
        values (
            :{ COL_NAME }
        )
    '''

    # Parameters -- Filter to avoid SQL Injection
    params = {
        COL_NAME: filter.dbString(values[COL_NAME])
    }

    # Sqlite operations and last row id
    last_row_id = operations.insert_table(sql, params, db)
    # Return last row id
    return last_row_id


# Select by ID
def select_airline_by_id(id, db=config.DB_NAME):
    # Select Command sql
    sql = f'''
        select { COL_NAME } from { TAB_NAME }
        where { COL_ID } = :{ COL_ID }
    '''
    # Parameters
    params = {
        COL_ID: filter.dbInteger(id)
    }

    # Store response from sql operation
    response = operations.select_from_table(sql, params, db)

    if response is not None:
        return {
            COL_ID: filter.dbInteger(id),
            COL_NAME: response[0]
        }
    else:
        return None

# Testing Create, Update, Read, Delete
def test_airline(db=config.DB_NAME):
    # Drop Old Table (Delete)
    drop_airline_table(db)
    # Create New Table (Create)
    create_airline_table(db)

    # Add Airline Rows (Update)
    american_id = insert_airline({ # American Airlines
        COL_NAME: 'American Airlines'
    })
    united_id = insert_airline({ # United Airlines
        COL_NAME: 'United Airlines'
    })

    # Select by ID (Read)
    row1 = select_airline_by_id(american_id, db)
    row2 = select_airline_by_id(united_id, db)

    # Row ID out of range
    badRow = select_airline_by_id(54321, db)

    # Test for failures
    # Null Row
    if badRow is not None:
        raise ValueError('Bad Row Not None')

    # Row 1 Values Test
    if row1['ID'] != american_id:
        raise ValueError(f'american_id incorrect: { row1["ID"] }!')
    if row1['name'] != 'American Airlines':
        raise ValueError(f'american_id name incorect!') 

    # Row 2 Values Test
    if row2['ID'] != united_id:
        raise ValueError(f'united_id incorrect: { row1["ID"] }!')
    if row2['name'] != 'United Airlines':
        raise ValueError(f'united_id name incorect!')

    # Output tests complete
    print('\nAirline tests passed! Resultant table: \n')

    # Print selection outputs
    # Combine Data from Row 1 and Row 2
    data = {}
    for key in row1.keys():
        data[key] = [row1[key], row2[key]]


    # Output using tabulate
    print(tabulate(data, 'keys') + '\n')