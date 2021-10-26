# Test Deleting
# Set up for Inner Join Testing
# Samuel Adamson

import flight
import airport
import city
import airline

# Drop all tables
def clean():
    flight.drop_flight_table()
    airport.drop_airport_table()
    city.drop_city_table()
    airline.drop_airline_table()

# Create all tables
def create():
    flight.create_flight_table()
    airport.create_airport_table()
    city.create_city_table()
    airline.create_airline_table()


# Run Setup
def setup():
    # Clean and Create Tables
    clean()
    create()

    # Add Cities ==
    houston_id = city.insert_city({ # Houston
        city.COL_NAME: 'Houston',
        city.COL_LAT: 29.750,
        city.COL_LON: -95.358,
        city.COL_POP: 2310000
    })
    denver_id = city.insert_city({ # Denver
        city.COL_NAME: 'Denver',
        city.COL_LAT: 39.742,
        city.COL_LON: -104.992,
        city.COL_POP: 705000
    })
    losangeles_id = city.insert_city({
        city.COL_NAME: 'Los Angeles',
        city.COL_LAT: 34.052,
        city.COL_LON: -118.244,
        city.COL_POP: 3967000
    })
    newyork_id = city.insert_city({ # New York
        city.COL_NAME: 'New York',
        city.COL_LAT: 40.731,
        city.COL_LON: -73.935,
        city.COL_POP: 8419000
    })
    tokyo_id = city.insert_city({ # Tokyo
        city.COL_NAME: 'Tokyo',
        city.COL_LAT: 35.653,
        city.COL_LON: 139.839,
        city.COL_POP: 13960000
    })
    seoul_id = city.insert_city({ # Seoul
        city.COL_NAME: 'Seoul',
        city.COL_LAT: 37.533,
        city.COL_LON: 127.025,
        city.COL_POP: 9776000
    })


    # Add Airlines ==
    american_id = airline.insert_airline({ # American Airlines
        airline.COL_NAME: 'American Airlines'
    })
    southwest_id = airline.insert_airline({ # South West Airlines
        airline.COL_NAME: 'South West Airlines'
    })
    united_id = airline.insert_airline({ # United Airlines
        airline.COL_NAME: 'United Airlines'
    })
    korean_id = airline.insert_airline({ # Korean Airlines
        airline.COL_NAME: 'Korean Airlines'
    })
    japan_id = airline.insert_airline({ # Japan Airlines
        airline.COL_NAME: 'Japan Airlines'
    })


    # Add Airports ==
    gbia_id = airport.insert_airport({ # George Bush Intercontinental Airport
        airport.COL_NAME: 'George Bush Intercontinental Airport',
        airport.COL_CITY_ID: 0,
        airport.COL_TYPE: 'Intercontinental'
    })
    dia_id = airport.insert_airport({ # Denver International Airport
        airport.COL_NAME: 'Denver International Airport',
        airport.COL_CITY_ID: 1,
        airport.COL_TYPE: 'International'
    })
    laia_id = airport.insert_airport({ # Los Angeles International Airport
        airport.COL_NAME: 'Los Angeles International Airport',
        airport.COL_CITY_ID: 2,
        airport.COL_TYPE: 'International'
    })
    jfkia_id = airport.insert_airport({ # John F Kennedy International Airport
        airport.COL_NAME: 'John F Kennedy International Airport',
        airport.COL_CITY_ID: 3,
        airport.COL_TYPE: 'International'
    })
    lga_id = airport.insert_airport({ # LaGuardia Airport
        airport.COL_NAME: 'LaGuardia Airport',
        airport.COL_CITY_ID: 2,
        airport.COL_TYPE: 'International'
    })
    ha_id = airport.insert_airport({ # Hanenda Airport
        airport.COL_NAME: 'Hanenda Airport',
        airport.COL_CITY_ID: 4,
        airport.COL_TYPE: 'International'
    })
    nia_id = airport.insert_airport({ # Narita International Airport
        airport.COL_NAME: 'Narita International Airport',
        airport.COL_CITY_ID: 4,
        airport.COL_TYPE: 'International'
    })
    iia_id = airport.insert_airport({ # Incheon International Airport
        airport.COL_NAME: 'Incheon International Airport',
        airport.COL_CITY_ID: 5,
        airport.COL_TYPE: 'International'
    })
    

    # Add Flights ==
    flight0_id = flight.insert_flight({ # Flight Number 0
        flight.COL_DEP_AIRPT_ID: 0,
        flight.COL_ARR_AIRPT_ID: 1,
        flight.COL_AIRLINE_ID: 1,
        flight.COL_DEP_UTC: '2021-09-07 06:32:21',
        flight.COL_ARR_UTC: '2021-09-07 08:56:32',
        flight.COL_ON_TIME: 1
    })
    flight1_id = flight.insert_flight({ # Flight Number 1
        flight.COL_DEP_AIRPT_ID: 0,
        flight.COL_ARR_AIRPT_ID: 3,
        flight.COL_AIRLINE_ID: 2,
        flight.COL_DEP_UTC: '2021-09-07 07:54:15',
        flight.COL_ARR_UTC: '2021-09-07 11:43:54',
        flight.COL_ON_TIME: 0
    })
    flight2_id = flight.insert_flight({ # Flight Number 2
        flight.COL_DEP_AIRPT_ID: 1,
        flight.COL_ARR_AIRPT_ID: 4,
        flight.COL_AIRLINE_ID: 2,
        flight.COL_DEP_UTC: '2021-09-07 08:13:10',
        flight.COL_ARR_UTC: '2021-09-07 11:58:06',
        flight.COL_ON_TIME: 1
    })
    flight3_id = flight.insert_flight({ # Flight Number 3
        flight.COL_DEP_AIRPT_ID: 4,
        flight.COL_ARR_AIRPT_ID: 2,
        flight.COL_AIRLINE_ID: 0,
        flight.COL_DEP_UTC: '2021-09-07 08:32:46',
        flight.COL_ARR_UTC: '2021-09-07 14:43:43',
        flight.COL_ON_TIME: 1
    })
    flight4_id = flight.insert_flight({ # Flight Number 4
        flight.COL_DEP_AIRPT_ID: 2,
        flight.COL_ARR_AIRPT_ID: 1,
        flight.COL_AIRLINE_ID: 0,
        flight.COL_DEP_UTC: '2021-09-07 09:01:28',
        flight.COL_ARR_UTC: '2021-09-07 11:56:23',
        flight.COL_ON_TIME: 1
    })
    flight5_id = flight.insert_flight({ # Flight Number 5
        flight.COL_DEP_AIRPT_ID: 4,
        flight.COL_ARR_AIRPT_ID: 0,
        flight.COL_AIRLINE_ID: 2,
        flight.COL_DEP_UTC: '2021-09-07 09:27:54',
        flight.COL_ARR_UTC: '2021-09-07 12:21:03',
        flight.COL_ON_TIME: 0
    })
    flight6_id = flight.insert_flight({ # Flight Number 6
        flight.COL_DEP_AIRPT_ID: 6,
        flight.COL_ARR_AIRPT_ID: 7,
        flight.COL_AIRLINE_ID: 4,
        flight.COL_DEP_UTC: '2021-09-07 09:50:12',
        flight.COL_ARR_UTC: '2021-09-07 12:39:32',
        flight.COL_ON_TIME: 1
    })
    flight7_id = flight.insert_flight({ # Flight Number 7
        flight.COL_DEP_AIRPT_ID: 6,
        flight.COL_ARR_AIRPT_ID: 2,
        flight.COL_AIRLINE_ID: 4,
        flight.COL_DEP_UTC: '2021-09-07 10:41:17',
        flight.COL_ARR_UTC: '2021-09-07 20:04:28',
        flight.COL_ON_TIME: 1
    })
    flight8_id = flight.insert_flight({ # Flight Number 8
        flight.COL_DEP_AIRPT_ID: 7,
        flight.COL_ARR_AIRPT_ID: 6,
        flight.COL_AIRLINE_ID: 3,
        flight.COL_DEP_UTC: '2021-09-07 11:21:49',
        flight.COL_ARR_UTC: '2021-09-07 13:36:38',
        flight.COL_ON_TIME: 0
    })
    flight9_id = flight.insert_flight({ # Flight Number 9
        flight.COL_DEP_AIRPT_ID: 7,
        flight.COL_ARR_AIRPT_ID: 2,
        flight.COL_AIRLINE_ID: 0,
        flight.COL_DEP_UTC: '2021-09-07 11:48:56',
        flight.COL_ARR_UTC: '2021-09-07 20:15:13',
        flight.COL_ON_TIME: 0
    })


setup()