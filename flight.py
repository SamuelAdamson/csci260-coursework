# Datatable -- Flights -- Contains Data on Each Flight
# Samuel Adamson

# Outputting Tabular Data
from tabulate import tabulate

import config
import operations
import filterValues as filter

# Table Schema
TAB_NAME = 'flight'
# Columns
COL_ID = 'ID'
COL_DEP_AIRPT_ID = 'departureAirportID'
COL_ARR_AIRPT_ID = 'arrivalAirportID'
COL_AIRLINE_ID = 'airlineID'
COL_DEP_UTC = 'departureUTC' 
COL_ARR_UTC = 'arrivalUTC'
COL_ON_TIME = 'onTime' # Is Flight On Time

# Create Flight Table
def create_flight_table(db=config.DB_NAME):
    # Output for testing
    # print('Flight table created...')


    # Create Table Command
    sql = f''' 
        create table if not exists { TAB_NAME } (
            { COL_ID } integer primary key,
            { COL_DEP_AIRPT_ID } integer not null,
            { COL_ARR_AIRPT_ID } integer not null,
            { COL_AIRLINE_ID } integer not null,
            { COL_DEP_UTC } datetime not null,
            { COL_ARR_UTC } datetime not null,
            { COL_ON_TIME } integer not null
        )
    '''
    # Sqlite operations
    operations.create_table(sql, db)


# Drop Flight Table
def drop_flight_table(db=config.DB_NAME):
    # Sqlite operations
    operations.drop_table(TAB_NAME, db)


# Insert into Flight Table
# Returns last row id of insert
def insert_flight(values, db=config.DB_NAME):
    # Output for testing
    # print('Inserting into Flight table...')


    # Insert Into Table Command
    sql = f'''
        insert into { TAB_NAME } (
            { COL_DEP_AIRPT_ID }, { COL_ARR_AIRPT_ID }, { COL_AIRLINE_ID },
            { COL_DEP_UTC }, { COL_ARR_UTC }, { COL_ON_TIME } 
        )
        values (
            :{ COL_DEP_AIRPT_ID }, :{ COL_ARR_AIRPT_ID }, :{ COL_AIRLINE_ID },
            :{ COL_DEP_UTC }, :{ COL_ARR_UTC }, :{ COL_ON_TIME } 
        )
    '''

    # Parameters -- Filter to avoid SQL Injection
    params = {
        COL_DEP_AIRPT_ID: filter.dbInteger(values[COL_DEP_AIRPT_ID]),
        COL_ARR_AIRPT_ID: filter.dbInteger(values[COL_ARR_AIRPT_ID]),
        COL_AIRLINE_ID: filter.dbInteger(values[COL_AIRLINE_ID]),
        COL_DEP_UTC: filter.dbDateTime(values[COL_DEP_UTC]),
        COL_ARR_UTC: filter.dbDateTime(values[COL_ARR_UTC]),
        COL_ON_TIME: filter.dbInteger(values[COL_ON_TIME])
    }

    # Sqlite operations and last row id
    last_row_id = operations.insert_table(sql, params, db)
    # Return last row id
    return last_row_id


# Select by ID
def select_flight_by_id(id, db=config.DB_NAME):
    # Select Command sql
    sql = f'''
        select { COL_DEP_AIRPT_ID }, { COL_ARR_AIRPT_ID }, { COL_AIRLINE_ID },
               { COL_DEP_UTC }, { COL_ARR_UTC }, { COL_ON_TIME } from { TAB_NAME }
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
            COL_DEP_AIRPT_ID: response[0],
            COL_ARR_AIRPT_ID: response[1],
            COL_AIRLINE_ID: response[2],
            COL_DEP_UTC: response[3],
            COL_ARR_UTC: response[4],
            COL_ON_TIME: response[5]
        }
    else:
        return None


# Testing Create, Update, Read, Delete
def test_flight(db=config.DB_NAME):
    # Drop Old Table (Delete)
    drop_flight_table(db)
    # Create New Table (Create)
    create_flight_table(db)

    # Add Flight Rows (Update)
    flight0_id = insert_flight({ # Flight Number 0
        COL_DEP_AIRPT_ID: 0,
        COL_ARR_AIRPT_ID: 1,
        COL_AIRLINE_ID: 1,
        COL_DEP_UTC: '2021-09-07 06:32:21',
        COL_ARR_UTC: '2021-09-07 08:56:32',
        COL_ON_TIME: 1
    })
    flight1_id = insert_flight({ # Flight Number 1
        COL_DEP_AIRPT_ID: 0,
        COL_ARR_AIRPT_ID: 3,
        COL_AIRLINE_ID: 2,
        COL_DEP_UTC: '2021-09-07 07:54:15',
        COL_ARR_UTC: '2021-09-07 11:43:54',
        COL_ON_TIME: 0
    })

    # Select by ID (Read)
    row1 = select_flight_by_id(flight0_id, db)
    row2 = select_flight_by_id(flight1_id, db)

    # Row ID out of range
    badRow = select_flight_by_id(54321, db)

    # Test for errors
    if badRow is not None:
        raise ValueError('Bad Row Not None')

    # Row 1 Values Test
    if row1['ID'] != flight0_id:
        raise ValueError(f'flight0_id incorrect: { row1["ID"] }!')
    if row1['departureAirportID'] != 0:
        raise ValueError(f'flight0_id departure airport incorrect!')
    if row1['arrivalAirportID'] != 1:
        raise ValueError(f'flight0_id arrival airport incorrect!')
    if row1['airlineID'] != 1:
        raise ValueError(f'flight0_id airline incorrect!')
    if row1['departureUTC'] != '2021-09-07 06:32:21':
        raise ValueError(f'flight0_id departure datetime incorrect!')
    if row1['arrivalUTC'] != '2021-09-07 08:56:32':
        raise ValueError(f'flight0_id arrival datetime incorrect!')
    if row1['onTime'] != 1:
        raise ValueError(f'flight0_id on time status incorrect!')

    # Row 2 Values Test
    if row2['ID'] != flight1_id:
        raise ValueError(f'dia_id incorrect: { row1["ID"] }!')
    if row2['departureAirportID'] != 0:
        raise ValueError(f'flight1_id departure airport incorrect!')
    if row2['arrivalAirportID'] != 3:
        raise ValueError(f'flight1_id arrival airport incorrect!')
    if row2['airlineID'] != 2:
        raise ValueError(f'flight1_id airline incorrect!')
    if row2['departureUTC'] != '2021-09-07 07:54:15':
        raise ValueError(f'flight1_id departure datetime incorrect!')
    if row2['arrivalUTC'] != '2021-09-07 11:43:54':
        raise ValueError(f'flight1_id arrival datetime incorrect!')
    if row2['onTime'] != 0:
        raise ValueError(f'flight1_id on time status incorrect!')


    # Output tests complete
    print('\nFlight tests passed! Resultant table: \n')

    # Print selection outputs
    # Combine Data from Row 1 and Row 2
    data = {}
    for key in row1.keys():
        data[key] = [row1[key], row2[key]]


    # Output using tabulate
    print(tabulate(data, 'keys') + '\n')