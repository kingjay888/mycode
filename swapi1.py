#!/usr/bin/env python3
"""Alta3 Research
   Star Wars API HTTP response parsing"""

# pprint makes dictionaries a lot more human readable
from pprint import pprint

# requests is used to send HTTP requests (get it?)
import requests

# The following URL is constructed incorrectly. It should be api/people/4/
#URL= "https://swapi.dev/api/people/four"
URL= "https://swapi.dev/api/people/4"
def main():
    """sending GET request, checking response"""

    # SWAPI response is stored in "resp" object
    resp= requests.get(URL)

    # check to see if the status is anything other than what we want, a 200 OK
    if resp.status_code == 200:
        # convert the JSON content of the response into a python dictionary
        vader= resp.json()
        pprint(vader)

    else:
        pprint("That is not a valid URL.")

    # convert the JSON content of the response into a python dictionary
    #vader= resp.json()

    #pprint(vader)

if __name__ == "__main__":
    main()