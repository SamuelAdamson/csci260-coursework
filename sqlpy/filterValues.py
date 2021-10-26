# Filter values before insertion into DB
# Samuel Adamson

from datetime import datetime

# Ensure Integer
def dbInteger(value, nullable = False):
    return int(value) if not nullable or value != None else None

# Ensure Real (Float)
def dbReal(value, nullable = False):
    return float(value) if not nullable or value != None else None

# Ensure String
def dbString(value, nullable = False):
    return str(value) if not nullable or value != None else None

# Ensure Datetime
def dbDateTime(value, nullable = False):
    return datetime.strptime(value, '%Y-%m-%d %H:%M:%S') if not nullable or value != None else None