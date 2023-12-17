# Basic Import

import pandas as pd
import requests
import concurrent.futures
import json
from datetime import datetime


from boiler_plate import *
# Contains the basic query for the API call

from Search_param import *
# Contains the user parameters for the API call

def scraper(listing_type, *args, **kwargs):
# Calls the get_listing function imported from the call_api module, passing in the listing_type argument. This will call the API and return a dataframe.
    if listing_type == 'for_rent':
        return get_listing(headers=headers, url=url, apistring=apistring, base_query=for_rent_query, userparams=user_param_for_rent)
    elif listing_type == 'for_sale':
        return get_listing(headers=headers, url=url, apistring=apistring, base_query=for_sale_query, userparams=user_param_for_sale)
    elif listing_type == 'get_schools':
        listing_id_param = kwargs.get('listing_id_param')
        return get_schools(headers=school_header, url=school_url, apistring=apistring, school_query=school_query, userparams = listing_id_param)
    else:
        return None
    
def get_listing(headers, url, apistring, base_query, userparams):
# This is the heart of the program. It takes the headers, url, apistring, base_query, and userparams as arguments. It then uses the requests module to make the API call.
    
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


def get_schools(headers, url, apistring, school_query, userparams):
    
    VARIABLES = {
            "propertyId": userparams
        }
    
    payload = {
        "query": school_query,
    "variables": VARIABLES
    }

    try:
        response = requests.request(
            "POST", url, json=payload, headers=headers, params=apistring)
        data = response.json()
    except:
        return 'ERROR'

    if data is None:
        return ''
    else:
        schools = data['data']['home']['schools']['schools']

        df = pd.DataFrame([school for school in schools if school['assigned']])
        # df = pd.DataFrame([school for school in schools if school['assigned']],columns=['name', 'education_level','rating'])

        return df

