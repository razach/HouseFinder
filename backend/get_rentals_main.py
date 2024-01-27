def get_rentals():

    # Call the scraper function for rental information. Pass in the 'for_rent' parameter.
    # Then iterate through the results, call the scraper function with 'get schools'.
    # Take the results of that call and append them to the results list.

    # %%
    from .scraper import scraper
    import pandas as pd
    from datetime import datetime

    # %%

    # Bunch of code to reload state - WIP; Ignore for now

    # Load in rentals.csv as a dataframe; just load the top 10 values for testing
    # rentals = pd.read_csv('rentals.csv', nrows=10)
    rentals = pd.read_csv('backend/rentals.csv')

    property_id_dict = {}



    # %%
    # Get the rentals and store in a csv for further processing
    rentals_new_pull = scraper('for_rent')

    # Add the current date and time column as 'pull date' column to rentals
    rentals_new_pull['pull_date'] = datetime.now()

    # Append the rentals_new_pull dataframe to the rentals dataframe
    rentals = pd.concat([rentals, rentals_new_pull], ignore_index=True)

    #store the rentals in a csv.
    rentals.to_csv('backend/rentals.csv', index=False)

    # %%

    # Read in the initial list of schools from big_list_of_schools.csv
    # big_list_of_schools = pd.DataFrame()
    big_list_of_schools = pd.read_csv('./backend/big_list_of_schools.csv')
    # Set the index to the slug_id column
    big_list_of_schools = big_list_of_schools.set_index('slug_id')
    
    # Create set to store unique school slug ids
    unique_schools = set()
    # Need to add this in once we start reading in the big list of schools.
    for slug_id in big_list_of_schools.index:
        unique_schools.add(slug_id)
    # unique_schools.add(list(big_list_of_schools['slug_id']))

    # Create dictionary to store property_id as key and list of school slug ids as value
    property_id_dict = {}


    for i, property_id in enumerate(rentals_new_pull['property_id']):
        print(f"handling {i} of {len(rentals_new_pull)}", end='\r')
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
    big_list_of_schools.to_csv('./backend/big_list_of_schools.csv', index=True)

    # %%
    # Append the property_id_dict back into the rentals_new_pull dataframe
    rentals_new_pull = rentals_new_pull.set_index('property_id')
    rentals_new_pull['school_ids'] = rentals_new_pull.index.map(property_id_dict)

    # %%
    # Append results to the end of backend/rentals_with_schools.csv
    rentals_with_schools = pd.read_csv('./backend/rentals_with_schools.csv')
    rentals_with_schools = pd.concat([rentals_with_schools, rentals_new_pull], ignore_index=True)
    rentals_with_schools.to_csv('./backend/rentals_with_schools.csv', index=False)