# Call the scraper function for rental information. Pass in the 'for_rent' parameter.
# Then iterate through the results, call the scraper function with 'get schools'.
# Take the results of that call and append them to the results list.

# %%
from scraper import *
import pandas as pd

# %%

# Bunch of code to reload state - WIP; Ignore for now

# Load in rentals.csv as a dataframe; just load the top 10 values for testing
# rentals = pd.read_csv('rentals.csv', nrows=10)
rentals = pd.read_csv('rentals.csv')

property_id_dict = {}



# %%
# Get the rentals and store in a csv for further processing
rentals = scraper('for_rent')

# Add the current date and time column as 'pull date' column to rentals
rentals['pull_date'] = datetime.now()

#store the rentals in a csv
rentals.to_csv('rentals.csv', index=False)

# %%

# Eventually we need to replace this to read in the initial list of schools.
big_list_of_schools = pd.DataFrame()
# Create set to store unique school slug ids
unique_schools = set()
# Need to add this in once we start reading in the big list of schools.
# unique_schools.add(big_list_of_schools['slug_id'])


for i, property_id in enumerate(rentals['property_id']):
    print(f"handling {i} of {len(rentals)}", end='\r')
    print(f"Running id number {property_id}")
    
    # Call scraper function with listing_id parameter to pull back ASSIGNED schools
    schools_df = scraper('get_schools', listing_id_param = property_id)
    
    # create a dictionary with a key of property_id, values of each of the id from school
    schools_df = schools_df.set_index('slug_id')
    # schools_dict = schools_df.to_dict()
    property_id_dict[property_id] = schools_df.index.tolist()

    # Iterate through each school slug id
    for slug_id in schools_df.index:
    
        # If slug id is not already in unique_schools set, add it
        if slug_id not in unique_schools:
            unique_schools.add(slug_id)
            
            # Filter schools_df to only include current unique row
            new_df = schools_df[schools_df.index == slug_id]
            
            # Append unique row to big_list_of_schools
            big_list_of_schools = pd.concat([big_list_of_schools, new_df])

# %%
# Save the big list of schools to a csv file.
big_list_of_schools.to_csv('big_list_of_schools.csv', index=True)
# %%
# Append the property_id_dict back into the rentals dataframe
rentals = rentals.set_index('property_id')
rentals['school_ids'] = rentals.index.map(property_id_dict)

# %%
# Save rentals back to csv
rentals.to_csv('rentals_with_schools.csv', index=False)