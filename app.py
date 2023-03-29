from flask import Flask
from flask import request

import argparse
import requests
import json

from clients import GeocodioClient, YelpClient

app = Flask(__name__)

GEOCOD_IO_API_KEY = "Insert_Key"
YELP_API_KEY = "Insert_Key"

@app.route('/restaurant/<restaurant_addr>', methods=['GET'])
def restaurant(restaurant_addr):
    if request.method == 'GET':
        # Implement your function here.

          address = request.args.get('address')
          if (address == []):
            return "Error: Enter Valid Address"

          restaurant_addr = address

          geocodio_client = GeocodioClient(GEOCOD_IO_API_KEY)
          yelp_client = YelpClient(YELP_API_KEY)

          latitude, longitude = geocodio_client.request(restaurant_addr)

          nearby_restaurants = yelp_client.request(latitude, longitude)
          restaurants = response.json()
          return restaurants
          
        
    else:
        # Implement your function to deal with false requests.
            return "Error 400: Invalid Request"

    

##########################
# Do **NOT** remove this.
def parse_args():
    parser =argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=5000,
                        help='port number.')
    return parser.parse_args()

if __name__ == '__main__': 
    args = parse_args()
    app.run(port=args.port)