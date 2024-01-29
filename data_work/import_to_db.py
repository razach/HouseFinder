    
# def import_to_db(rentals_filepath, schools_filepath):
def import_to_db():
# Function to import data from a csv file into a database.
    # %%
    # Set filepath to the csv files to be imported
    # Used for testing
    rentals_filepath = '../backend/rentals_with_schools.csv'
    schools_filepath = '../backend/big_list_of_schools.csv'

    # %%
    #import pandas
    import pandas as pd
    import ast
    import json

    # Import SQLAlchemy 
    import sqlalchemy


    # %%
    # Load in rentals_with_schools.csv as a dataframe

    rentals_with_schools = pd.read_csv(rentals_filepath)

    # %%
    #Take a peek at the results
    # Testing
    # rentals_with_schools.head()
    # rentals_with_schools.columns

    # %%

    #Remove all duplicates from the rentals_with_schools dataframe

    rentals_with_schools.drop_duplicates(subset=['listing_id'], inplace=True)

    rentals_with_schools.shape


    # %%

    #Create a new dataframe that will be used to store the results

    rentals_base_table = pd.DataFrame()

    # Add in listing_id, list_price, and pull_date from the rentals_with_schools dataframe.

    rentals_base_table['listing_id'] = rentals_with_schools['listing_id']
    rentals_base_table['list_price'] = rentals_with_schools['list_price']
    rentals_base_table['pull_date'] = rentals_with_schools['pull_date']

    # Pull in the 'permalink' column and concatenate in 'https://www.realtor.com/realestateandhomes-detail/'
    rentals_base_table['permalink'] = 'https://www.realtor.com/realestateandhomes-detail/' + rentals_with_schools['permalink']
    #Set the index to listing_id.
    rentals_base_table.set_index('listing_id', inplace=True)

    # %%
    #Import addresses and add them to rental_base_table. Match values based on listing_ids

    for i, row in rentals_with_schools.iterrows():
        try:
            data = json.loads(row['location'].replace("'", '"'))
            rentals_base_table.loc[row['listing_id'], 'Address'] = f"{data['address']['line']} {data['address']['city']}, {data['address']['state_code']} {data['address']['postal_code']}"
            rentals_base_table.loc[row['listing_id'], 'Address_lat'] = data['address']['coordinate']['lat'] 
            rentals_base_table.loc[row['listing_id'], 'Address_long'] = data['address']['coordinate']['lon']
        except:
            pass


    # %%

    #Create a new variable to store all the unique tags
    unique_tags = []
    #Create a master list of unique tags by iterating through all the rows in rentals_with_schools and pulling unique tags from the column tag

    tags = []

    for i, row in rentals_with_schools.iterrows():

        #get a list of tag strings and store in a list.
        try:
            tags = ast.literal_eval(row['tags'])
        except:
            tags = []

        #iterate through the list of tag strings and add each unique tag to the unique_tags list.

        for tag in tags:
            if tag is not None and tag not in unique_tags:
                unique_tags.append(tag)

    # print (unique_tags)

    # %%

    # add in all the tags as columns to the rentals_base_table dataframe.

    for tag in unique_tags:
        rentals_base_table[tag] = 0

    # %%

    # Iterate through the rows in rentals_with_schools and add 1 to the column corresponding to the tag.
        
    for i, row in rentals_with_schools.iterrows():

        #get a list of tag strings and store in a list.
        try:
            tags = ast.literal_eval(row['tags'])
        except:
            tags = []

        #iterate through the list of tag strings and add 1 to the column corresponding row by listing_id to the tag.

        for tag in tags:
            if tag is not None:
                # rentals_base_table[tag][row['listing_id']] = 1
                rentals_base_table.loc[row['listing_id'], tag] = 1


    # %%

    # Add in all the values from the description column in rentals_with_schools as columns to the rentals_base_table dataframe.

    # First lets build a big list of all the keys in the description column

    unique_description_value = []

    for i, row in rentals_with_schools.iterrows():
        try:
            description_values = ast.literal_eval(row['description'])
        except:
            description_values = []

        for value in description_values:
            if value is not None and value not in unique_description_value:
                unique_description_value.append(value)

    # %%
                
    # Next lets add in all the columns into the rentals_base_table dataframe.
                
    for value in unique_description_value:
        rentals_base_table[value] = None

    # %%
        
    # Iterate through the rows in rentals_with_schools and pull in the right value to the column corresponding to the description value.

    for i, row in rentals_with_schools.iterrows():
        try:
            description_values = ast.literal_eval(row['description'])
        except:
            description_values = []

        for value in description_values:
            if value is not None:
                # rentals_base_table[value][row['listing_id']] = description_values[value]
                rentals_base_table.loc[row['listing_id'], value] = description_values[value]
    # %%

    # Read in big_list_of_schools.csv into a dataframe

    big_list_of_schools = pd.read_csv(schools_filepath)

    # Set the index to slug_id
    big_list_of_schools.set_index('slug_id', inplace=True)

    # Get rid of duplicate entries
    big_list_of_schools.drop_duplicates(inplace=True)

    # %%

    # Split up the 'education_level' into separate columns for each level
    big_list_of_schools['elementary'] = big_list_of_schools['education_levels'].str.contains('elementary', case=False)
    big_list_of_schools['middle'] = big_list_of_schools['education_levels'].str.contains('middle', case=False)
    big_list_of_schools['high'] = big_list_of_schools['education_levels'].str.contains('high', case=False)

    # Add in three columns that copy of the the rating into elementary_school_rating, middle_school_rating, and high_school_rating, if the elementary, middle, high columns are true.
    big_list_of_schools['elementary_school_rating'] = big_list_of_schools['elementary'] * big_list_of_schools['rating']
    big_list_of_schools['middle_school_rating'] = big_list_of_schools['middle'] * big_list_of_schools['rating']
    big_list_of_schools['high_school_rating'] = big_list_of_schools['high'] * big_list_of_schools['rating']


    # %%

    # Match on the listing_id and copy the school_ids over from rentals_with_schools
    rentals_base_table['school_ids'] = None
    
    for i, row in rentals_with_schools.iterrows():
        try:
            school_ids = ast.literal_eval(row['school_ids'])
        except:
            school_ids = []

        rentals_base_table.loc[row['listing_id'],'school_ids'] = str(school_ids)


    # %%
    # Add in three columns called 'elementary school rating', 'middle school rating', and 'high school rating' to the rentals_base_table dataframe.
    rentals_base_table['elementary_school_rating'] = 0
    rentals_base_table['middle_school_rating'] = 0
    rentals_base_table['high_school_rating'] = 0

    # %%


    # Add in three columns called 'elementary school rating', 'middle school rating', and 'high school rating' to the rentals_base_table dataframe.
    # Match on the school slig_id stored in the rentals_with_schools dataframe.

    elementary_school_rating = []
    middle_school_rating = []
    high_school_rating = []

    for i, row in rentals_with_schools.iterrows():
        try:
            school_slugs = ast.literal_eval(row['school_ids'])
        except:
            school_slugs = []
        
        #print(school_slugs)
        for school_slug in school_slugs:
            if school_slug is not None:
                #Append the rating for each school to the list
                elementary_school_rating.append(big_list_of_schools.loc[str(school_slug)]['elementary_school_rating'])
                middle_school_rating.append(big_list_of_schools.loc[str(school_slug)]['middle_school_rating'])
                high_school_rating.append(big_list_of_schools.loc[str(school_slug)]['high_school_rating'])

        # Take the max value from each list and append to new columns in the rentals_base_table dataframe.
        rentals_base_table.loc[row['listing_id'], 'elementary_school_rating'] = max(elementary_school_rating)
        rentals_base_table.loc[row['listing_id'],'middle_school_rating'] = max(middle_school_rating)
        rentals_base_table.loc[row['listing_id'], 'high_school_rating'] = max(high_school_rating)
        
    # %%
                
    # Loop through the columns
    for column in rentals_base_table.columns:

        # Print column name and data type
        #print(f"{column} - {rentals_base_table[column].dtype}")

        # Check if data type is object
        if rentals_base_table[column].dtype == 'object':
            
            # Convert column to string
            rentals_base_table[column] = rentals_base_table[column].astype(str)




    # %%
    # Export the rentals_base_table dataframe to a csv file
    rentals_base_table.to_csv('../data_work/rentals_base_table.csv')

    # %%
    # Save to a database.

    # Create SQLAlchemy engine to connect to SQLite database
    engine = sqlalchemy.create_engine('sqlite:///rentals.db')

    # Save rentals_base_table to SQLite database 
    rentals_base_table.to_sql('rentals', engine, if_exists='replace', index=True)


            
