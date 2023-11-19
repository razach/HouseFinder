# Basic Import

import pandas as pd
import requests
import concurrent.futures
import json
from datetime import datetime


from boiler_plate import *
from Search_param import *

def scraper(listing_type):
    if listing_type == 'for_rent':
        return get_listing(headers=headers, url=url, apistring=apistring, base_query=for_rent_query, userparams=user_param_for_rent)
    elif listing_type == 'for_sale':
        return get_listing(headers=headers, url=url, apistring=apistring, base_query=for_sale_query, userparams=user_param_for_sale)
    elif listing_type == 'schools':
        return get_schools()
    else:
        return None
    
def get_listing(headers, url, apistring, base_query, userparams):

    # Initialize the results list
    results = []

    offset = 0
    # total gets updated, just need a value greater than offset for first iteration
    total = offset + 1

    # for the purpose of this example, creating a max
    max_results = 200

    VARIABLES = {
                "query": userparams,
                "limit": 42,
                "offset": offset,
                "sort_type": "relevant",
                "by_prop_type": ["home"]
            }

    while offset < total:

        print(f"handling offset {offset} in a total of {total}      ", end='\r')

        payload = {
            "query": base_query,
        "variables": VARIABLES,
            "operationName": "ConsumerSearchMainQuery",
            "callfrom": "SRP",
            "nrQueryType": "MAIN_SRP",
            "isClient": True,
        }

        response = requests.request(
            "POST", url, json=payload, headers=headers, params=apistring)

        if response.status_code != 200:
            raise ValueError(f"Bad status code on response: {response.status_code}")

        try:
            data = response.json()['data']['home_search']
        except:
            print("Failed to read data, something went wrong with the request")
            raise

        total = data['total']

        response_results = data['results']
        offset += len(response_results)

        results += response_results

        if max_results and offset >= max_results:
            print("\n")
            print(f"Hit max: {max_results}")
            break

    print("Done!")
    return results


def get_schools():
    pass