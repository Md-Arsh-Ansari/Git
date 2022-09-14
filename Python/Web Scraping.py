    from Public API

import requests

base_url = "https://api.exchangeratesapi.io/latest"

response = requests.get(base_url)

response.ok
>> True

response.status_code
>> 200

response.text

response.content

# Requests has in-build method to directly convert the response to JSON format
response.json()

# In Python, this JSON is stored as a dictionary
type(response.json())
>>dict


# A useful library for JSON manipulation and pretty print
import json

# It has two main methods:
# .loads(), which creates a Python dictionary from a JSON format string (just as response.json() does)
# .dumps(), which creates a JSON format string out of a Python dictionary 


# .dumps() has options to make the string 'prettier', more readable
# We can choose the number of spaces to be used as indentation
json.dumps(response.json(), indent=4)


response.json().keys()




















