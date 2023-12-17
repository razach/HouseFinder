
# Scraper(for_sale)
# Store_db(for_sale)
# Scraper(for_rent)
# Store_db(for_rent)



# --
# Scraper(Query)
    # Main Query
    # Get school



from scraper import *
# Calls the scraper function imported from the scraper module, passing 
# 'for_rent' as the listing_type argument. This will scrape rental listing 
# data and return it as a Pandas dataframe. The dataframe is assigned to 
# df and then printed.

# df = scraper('for_rent')
# print(df)

df = scraper('get_schools', listing_id_param = '5121897759')
print(df)