# Datatable -- Cities -- Contains Data on Each City
# Samuel Adamson

# Outputting Tabular Data
from tabulate import tabulate

import config
import operations
import filterValues as filter

# Table Schema
TAB_NAME = 'city'
# Columns
COL_ID = 'ID'
COL_NAME = 'name'
COL_LAT = 'latitude'
COL_LON = 'longitude'
COL_POP = 'population'


# Create City Table
def create_city_table(db=config.DB_NAME):
    # Output for testing
    # print('City table created...')

    # Create Table Command
    sql = f''' 
        create table if not exists { TAB_NAME } (
            { COL_ID } integer primary key,
            { COL_NAME } string not null,
            { COL_LAT } real not null,
            { COL_LON } real not null,
            { COL_POP } real
        )
    '''
    # Sqlite operations
    operations.create_table(sql, db)


# Drop City Table
def drop_city_table(db=config.DB_NAME):
    # Sqlite operations
    operations.drop_table(TAB_NAME, db)


# Insert into City Table
# Returns last row id of insert
def insert_city(values, db=config.DB_NAME):
    # Output for testing
    # print('Inserting into City table...')

    # Insert Into Table Command
    sql = f'''
        insert into { TAB_NAME } (
            { COL_NAME }, { COL_LAT }, { COL_LON }, { COL_POP }
        )
        values (
            :{ COL_NAME }, :{ COL_LAT }, :{ COL_LON }, :{ COL_POP }
        )
    '''

    # Parameters -- Filter to avoid SQL Injection
    params = {
        COL_NAME: filter.dbString(values[COL_NAME]),
        COL_LAT: filter.dbReal(values[COL_LAT]),
        COL_LON: filter.dbReal(values[COL_LON]),
        COL_POP: filter.dbInteger(values[COL_POP])
    }

    # Sqlite operations and last row id
    last_row_id = operations.insert_table(sql, params, db)
    # Return last row id
    return last_row_id


# Select by ID
def select_city_by_id(id, db=config.DB_NAME):
    # Select Command sql
    sql = f'''
        select { COL_NAME }, { COL_LAT }, { COL_LON }, { COL_POP } from { TAB_NAME }
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
            COL_LAT: response[1],
            COL_LON: response[2],
            COL_POP: response[3]
        }
    else:
        return None


# Testing Create, Update, Read, Delete
def test_city(db=config.DB_NAME):
    # Drop Old Table (Delete)
    drop_city_table(db)
    # Create New Table (Create)
    create_city_table(db)

    # Add City Rows (Update)
    houston_id = insert_city({ # Houston
        COL_NAME: 'Houston',
        COL_LAT: 29.750,
        COL_LON: -95.358,
        COL_POP: 2310000
    })
    denver_id = insert_city({ # Denver
        COL_NAME: 'Denver',
        COL_LAT: 39.742,
        COL_LON: -104.992,
        COL_POP: 705000
    })

    # Select by ID (Read)
    row1 = select_city_by_id(houston_id, db)
    row2 = select_city_by_id(denver_id, db)

    # Row ID out of range
    badRow = select_city_by_id(54321, db)

    # Test for errors
    if badRow is not None:
        raise ValueError('Bad Row Not None')

    # Row 1 Values Test
    if row1['ID'] != houston_id:
        raise ValueError(f'houston_id incorrect: { row1["ID"] }!')
    if row1['name'] != 'Houston':
        raise ValueError(f'houston_id name incorect!') 
    if row1['latitude'] != 29.750 or row1['longitude'] != -95.358:
        raise ValueError(f'houston_id location incorrect!')
    if row1['population'] != 2310000:
        raise ValueError(f'houston_id population incorrect!')

    # Row 2 Values Test
    if row2['ID'] != denver_id:
        raise ValueError(f'denver_id incorrect: { row1["ID"] }!')
    if row2['name'] != 'Denver':
        raise ValueError(f'denver_id name incorect!')
    if row2['latitude'] != 39.742 or row2['longitude'] != -104.992:
        raise ValueError(f'denver_id location incorrect!')
    if row2['population'] != 705000:
        raise ValueError(f'denver_id population incorrect!')

    # Output tests complete
    print('\nCity tests passed! Resultant table: \n')

    # Print selection outputs
    # Combine Data from Row 1 and Row 2
    data = {}
    for key in row1.keys():
        data[key] = [row1[key], row2[key]]


    # Output using tabulate
    print(tabulate(data, 'keys') + '\n')