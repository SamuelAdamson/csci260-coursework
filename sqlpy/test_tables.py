#!/usr/bin/env python

# Test Create, Update, Read for each table
# Samuel Adamson

import flight
import airport
import city
import airline

def test_airline(): # Airline Tests
    airline.test_airline()

def test_city(): # City Tests
    city.test_city()

def test_airport(): # Airport Tests
    airport.test_airport()

def test_flight(): # Flight Tests
    flight.test_flight()

def test_all(): # Test all 4 tables
    airline.test_airline()
    city.test_city()
    airport.test_airport()
    flight.test_flight()

# test_airline()
# test_city()
# test_airport()
# test_flight()
test_all()