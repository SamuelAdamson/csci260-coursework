#!/usr/bin/env python

# Reads CSV Into Table
# Samuel Adamson

from csv import DictReader
from datetime import datetime
import sys
from config import DB_NAME
import filterValues as filter
import airline
import airport
import flight

# Creates a row in the flight datatable
def createRecord(row, db=DB_NAME):
    # Associate airline name with airline id
    airlineName = filter.dbString(row['airline']) if 'airline' in row else 'No airline'
    airlineRow = airline.select_airline_by_name(airlineName, db)
    
    if airlineRow: # Check not null and store ID
        airlineID = airlineRow['ID']
    else: # Row is null
        airlineID = airline.insert_airline({
            airline.COL_NAME: filter.dbString(airlineName)
        }, db)

    # Associate departure airport name with airport id
    deptAirpName = filter.dbString(row['departureAirport']) if 'departureAirport' in row else 'Missing Departure Airport'
    deptAirpRow = airport.select_airport_by_name(deptAirpName)
    
    if deptAirpRow: # Check not null and store ID
        deptAirpID = deptAirpRow['ID']
    else: # Row is null
        raise ValueError(f'Departure Airport: { deptAirpName } does not exist in database!')

    # Associate arrival airport name with airport id
    arrAirpName = filter.dbString(row['arrivalAirport']) if 'arrivalAirport' in row else 'Missing Arrival Airport'
    arrAirpRow = airport.select_airport_by_name(arrAirpName)
    
    if arrAirpRow: # Check not null and store ID
        arrAirpID = arrAirpRow['ID']
    else: # Row is null
        raise ValueError(f'Arrival Airport: { arrAirpName } does not exist in database!')

    # Store departure and arrival times
    deptTime = filter.dbDateTimeForm(row['departureTime'])
    arrTime = filter.dbDateTimeForm(row['arrivalTime'])

    # Check that departure time is past current time
    if deptTime > datetime.now():
        raise ValueError (f'Departure Time: { deptTime } is past current date!')
    # Check that arrival time is past current time
    if arrTime > datetime.now():
        raise ValueError (f'Arrival Time: { arrTime } is past current date!')

    # Convert back to string
    deptTime = filter.dbDateToString(deptTime)
    arrTime = filter.dbDateToString(arrTime)

    # Store on time status
    onTime = filter.dbBoolean(row['onTime'])
    
    # Insert into flight table
    flight.insert_flight({
        flight.COL_DEP_AIRPT_ID: deptAirpID,
        flight.COL_ARR_AIRPT_ID: arrAirpID,
        flight.COL_AIRLINE_ID: airlineID,
        flight.COL_DEP_UTC: deptTime,
        flight.COL_ARR_UTC: arrTime,
        flight.COL_ON_TIME: onTime
    })



# Import CSV File to Database
def importFile(file, db=DB_NAME):
    # Open file using CSV
    with open(file) as dataFile:
        # Store as dictionary using csv lib
        data = DictReader(dataFile)
        # For each row -- create a record
        for row in data:
            createRecord(row, db)



# Runs on function call
if __name__ == '__main__':
    # Iterate through files passed to function
    for file in sys.argv[1:]:
        # Import CSV File
        importFile(file)