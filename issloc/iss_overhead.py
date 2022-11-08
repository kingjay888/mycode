#!/usr/bin/python3
"""Alta3 Research | 
   Using an HTTP GET to determine when the ISS will pass over head"""

# python3 -m pip install requests
import requests
import urllib
import json
import datetime as datetime
import reverse_geocoder as rg

# Pass the ISS Location tracker URL
ISLT = 'http://api.open-notify.org/iss-now.json'


def main():
    ## Call the webserv
    resp = requests.get(ISLT).json()

    lon= resp["iss_position"]["longitude"]
    lat= resp["iss_position"]["latitude"]
    ts= resp["timestamp"]
    ts = datetime.datetime.fromtimestamp(ts)


    # return an ordered dictionary using our lat/lon vars
    locator_resp= rg.search((lat, lon))


    # slice that object to return the city name only
    city= locator_resp[0]["name"]

    # slice the object again to return the country
    country= locator_resp[0]["cc"]

    print(f"""
    CURRENT LOCATION OF THE ISS:
    Timestamp: {ts}
    Lon: {lon}
    Lat: {lat}
    City/Country: {city}, {country}
    """)
   # print("Lon : {}".format(iss_position['longitude']))


if __name__ == "__main__":
    main()

