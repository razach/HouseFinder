# %%

import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy as db

# %%

# Use sqlalchemy to read in the SQLite database stored at 'sqlite:///data_work/rentals.db'

engine = db.create_engine('sqlite:///rentals.db')

conn = engine.connect()


# %%

# Read in rentals.db SQLLite into a pandas dataframe
rentals_base_table = pd.read_sql_table('rentals', conn)
rentals_base_table.set_index('listing_id', inplace=True)

# %%
rentals_base_table.head()

# %%
            
# plot average list_price with basements = 1 and basements = 0

# Extract data for plotting
basement_data = rentals_base_table[['basement', 'list_price']]

# Plot scatter plot  

plt.scatter(basement_data['basement'], basement_data['list_price'])


plt.xlabel('Basement')
plt.ylabel('List Price')
plt.title('List Price vs Basement')

plt.show()

# %%

# create a scatter plot of list_price vs. sqft

# Extract data for plotting
sqft_data = rentals_base_table[['sqft', 'list_price']]

# Plot scatter plot

plt.scatter(sqft_data['sqft'], sqft_data['list_price'])
plt.xlabel('sqft')
plt.ylabel('List Price')
plt.title('Sqft vs. List Price')

plt.show()
