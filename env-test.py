import os

print(os.getenv("resp"));

# Set environment variables
os.environ['API_USER'] = 'username'
os.environ['API_PASSWORD'] = 'secret'

# Get environment variables
USER = os.getenv('API_USER')
PASSWORD = os.environ.get('API_PASSWORD')

print(USER)

print(os.environ["API_USER"])

# Getting non-existent keys
FOO = os.getenv('FOO') # None
BAR = os.environ.get('BAR') # None
BAZ = os.environ['BAZ'] # KeyError: key does not exist.
