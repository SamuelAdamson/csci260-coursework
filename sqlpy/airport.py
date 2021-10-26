# Datatable -- Airports -- Contains Data on Each Airport
# Samuel Adamson

# Outputting Tabular Data
from tabulate import tabulate

import config
import operations
import filterValues as filter

# Table Schema
TAB_NAME = 'airport'
# Columns
COL_ID = 'ID'
COL_NAME = 'name'
COL_CITY_ID = 'cityID'
COL_TYPE = 'type'


# Create Airport Table
def create_airport_table(db=config.DB_NAME):
    # Output for testing
    # print('Airport table created...')

    # Create Table Command
    sql = f''' 
        create table if not exists { TAB_NAME } (
            { COL_ID } integer primary key,
            { COL_NAME } string not null,
            { COL_CITY_ID } integer not null,
            { COL_TYPE } string not null
        )
    '''
    # Sqlite operations
    operations.create_table(sql, db)


# Drop Airport Table
def drop_airport_table(db=config.DB_NAME):
    # Sqlite operations
    operations.drop_table(TAB_NAME, db)


# Insert into Airport Table
# Returns last row id of insert
def insert_airport(values, db=config.DB_NAME):
    # Output for testing
    # print('Inserting into Airport table...')

    # Insert Into Table Command
    sql = f'''
        insert into { TAB_NAME } (
            { COL_NAME }, { COL_CITY_ID }, { COL_TYPE }
        )
        values (
            :{ COL_NAME }, :{ COL_CITY_ID }, :{ COL_TYPE }
        )
    '''

    # Parameters -- Filter to avoid SQL Injection
    params = {
        COL_NAME: filter.dbString(values[COL_NAME]),
        COL_CITY_ID: filter.dbInteger(values[COL_CITY_ID]),
        COL_TYPE: filter.dbString(values[COL_TYPE])
    }

    # Sqlite operations and last row id
    last_row_id = operations.insert_table(sql, params, db)
    # Return last row id
    return last_row_id


# Select by ID
def select_airport_by_id(id, db=config.DB_NAME):
    # Select Command sql
    sql = f'''
        select { COL_NAME }, { COL_CITY_ID }, { COL_TYPE } from { TAB_NAME }
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
            COL_NAME: response[0],
            COL_CITY_ID: response[1],
            COL_TYPE: response[2]
        }
    else:
        return None


# Testing Create, Update, Read, Delete
def test_airport(db=config.DB_NAME):
    # Drop Old Table (Delete)
    drop_airport_table(db)
    # Create New Table (Create)
    create_airport_table(db)

    # Add Airport Rows (Update)
    gbia_id = insert_airport({ # George Bush Intercontinental Airport
        COL_NAME: 'George Bush Intercontinental Airport',
        COL_CITY_ID: 0,
        COL_TYPE: 'Intercontinental'
    })
    dia_id = insert_airport({ # Denver International Airport
        COL_NAME: 'Denver International Airport',
        COL_CITY_ID: 1,
        COL_TYPE: 'International'
    })

    # Select by ID (Read)
    row1 = select_airport_by_id(gbia_id, db)
    row2 = select_airport_by_id(dia_id, db)

    # Row ID out of range
    badRow = select_airport_by_id(54321, db)

    # Test for errors
    if badRow is not None:
        raise ValueError('Bad Row Not None')

    # Row 1 Values Test
    if row1['ID'] != gbia_id:
        raise ValueError(f'gbia_id incorrect: { row1["ID"] }!')
    if row1['name'] != 'George Bush Intercontinental Airport':
        raise ValueError(f'gbia_id name incorect!')
    if row1['cityID'] != 0:
        raise ValueError(f'gbia_id city ID is incorrect!')
    if row1['type'] != 'Intercontinental':
        raise ValueError(f'gbia_id type is incorrect!')

    # Row 2 Values Test
    if row2['ID'] != dia_id:
        raise ValueError(f'dia_id incorrect: { row1["ID"] }!')
    if row2['name'] != 'Denver International Airport':
        raise ValueError(f'dia_id name incorect!')
    if row2['cityID'] != 1:
        raise ValueError(f'dia_id city ID is incorrect!')
    if row2['type'] != 'International':
        raise ValueError(f'dia_id type is incorrect!')

    # Output tests complete
    print('\nAirport tests passed! Resultant table: \n')

    # Print selection outputs
    # Combine Data from Row 1 and Row 2
    data = {}
    for key in row1.keys():
        data[key] = [row1[key], row2[key]]


    # Output using tabulate
    print(tabulate(data, 'keys') + '\n')