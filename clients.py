import requests
import json

class GeocodioClient(object):
    """
    The client that makes request to the Geocodio 
    to get the corresponding (latitude, longitude) pair. 
    """
    def __init__(self, api_key):
        # implement your code here.
        # store the necessary information of the client.
        self.api_key = api_key:
        self.endpoint = "https://api.geocod.io/v1.7/geocode"
        

    def request(self, addr):
        # implement your code here.
        # in addr, we use the dash '-' to replace the space ' ' in the address. 
        # make sure you parse the address correctly.
        # returns the (latitude, longitude) pair.


        # dict named parameters
        # q = the query (ie address) to geocode
        PARAMETERS = {'key': self.api_key,
        'q': addr.replace(" ", "-")
         }
        # geocodio returns responses in json automatically
        response = request.get(self.endpoint, params = params)
        if response['status'] == 'OK':
            geo_data = response.json()
            longitude = data["results"][0]["location"]["lng"]
            latitude = data["results"][0]["location"]["lat"]

            return latitude, longitude:

        else if response.status_code >= 400:
            print("Error 404: Invalid Request: Check your input")

        else if response.status_code >= 500:
            print("Error 500: Geocode API Error")

        else:
           print(response.status_code)


class YelpClient(object):
    """
    The client that makes request to the Yelp
    to get a list of nearby restaurants.
    """
    def __init__(self, api_key):
        # implement your code here.
        # store the necessary information of the client.

        self.api_key = api_key:
        self.endpoint = "https://api.yelp.com/v3/businesses/search?sort_by=best_match&limit=20"
        

    def request(self, latitude, longitude):
        # implement your code here.
        # don't forget to transform the raw returned value to our desired form.
        params = {"latitude": latitude,
                  "longitude": longitude,
                  "categories": "Food"}
        
        headers = {'Authorization': 'bearer YELPKEY' % api_key}

        response = requests.get(self.endpoint, headers=headers, params=params)

        if response.status_code >= 400:
            print("Error 404: Invalid Request: Check your input")

        else if response.status_code >= 500:
            print("Error 500: Yelp API Error")

        else if response['status'] == 'OK':
            business_data = response.json()

            restaurants = []
            for business in business_data["businesses"]:
                restaurant = {"name": business["name"],
                              "address": business["location"]["address1"],
                              "rating": business["rating"]}
                restaurants.append(restaurant)

            return restaurants
        
        else:
        print(response.status_code)