#!/usr/bin/env python

# Run Inner Join Query on Flight Database
# Samuel Adamson

from tabulate import tabulate

import flight
import airport
import city

import config
import operations
import setup


# Query all US Departures
def US_departures(db=config.DB_NAME):
    
    # Find all flights departing US 
    # Note: two inner joins because airport table is referenced twice (Departure, Arrival)
    sql = f'''
        select f.{ flight.COL_ID },
               a1.{ airport.COL_NAME },
               a2.{ airport.COL_NAME },
               f.{ flight.COL_DEP_UTC },
               f.{ flight.COL_ARR_UTC },
               f.{ flight.COL_ON_TIME }
        from { flight.TAB_NAME } f
        inner join { airport.TAB_NAME } a1 on f.{ flight.COL_DEP_AIRPT_ID } = a1.{ airport.COL_ID }
        inner join { airport.TAB_NAME } a2 on f.{ flight.COL_ARR_AIRPT_ID } = a2.{ airport.COL_ID }
        where f.{ flight.COL_DEP_AIRPT_ID } < :{ airport.COL_ID }
    '''

    # Any columns with a value less than 6 are located in US
    params = {airport.COL_ID: 6}

    # Get response
    response = operations.select_from_table_all(sql, params, db)

    # Parse Response
    if response is not None:
        # Column Headers
        headers = [
            'Flight ID', 'Departure Airport', 'Arrival Airport',
            'Departure (UTC)', 'Arrival (UTC)', 'On Time Status'
        ]
        # Response Body
        data = response

        # Output response in tabular format
        print(tabulate(data, headers) + '\n')
    else:
        print('Empty Response!')



# Query Airport Locations
def airport_locations(db=config.DB_NAME):
    
    # Find location city of each airport
    sql = f'''
        select { airport.TAB_NAME }.{ airport.COL_ID },
               { airport.TAB_NAME }.{ airport.COL_NAME },
               { city.TAB_NAME }.{ city.COL_NAME }
        from { airport.TAB_NAME }
        inner join { city.TAB_NAME } on { airport.TAB_NAME }.{ airport.COL_CITY_ID } = { city.TAB_NAME }.{ city.COL_ID }
    '''

    # No parameters
    params = []

    # Get response
    response = operations.select_from_table_all(sql, params, db)

    # Parse Response
    if response is not None:
        # Column Headers
        headers = [
            'Airport ID', 'Airport Name', 'City Name'
        ]
        # Response Body
        data = response

        # Output response in tabular format
        print(tabulate(data, headers) + '\n')
    else:
        print('Empty Response!')


# Run inner join query
def inner_join_query():
    # Setup DB For Inner Join
    setup.setup()

    # US Departures Query
    US_departures()
    airport_locations()

inner_join_query()