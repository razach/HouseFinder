# %%

import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy as db
import seaborn as sns

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
# basement_data = rentals_base_table.loc[:, ['basement', 'list_price']]
basement_data = rentals_base_table[['basement', 'list_price']]


#Convert both columns to integers
basement_data.loc[:,'basement'] = basement_data.loc[:,'basement'].astype(bool)
basement_data.loc[:,'list_price'] = basement_data.loc[:,'list_price'].astype(int)

# Plot a graph of the average list price for each basement value
# Show the spread of each average list price

average_list_price = basement_data.groupby('basement').mean()
standard_deviation = basement_data.groupby('basement').std()

# plt.errorbar(average_list_price.index, average_list_price['list_price'], yerr=standard_deviation)
sns.set_theme(style="darkgrid")

sns.violinplot(x='basement', y='list_price', data=basement_data)

plt.ylabel('List Price')

plt.show()


# %%

# create a scatter plot of list_price vs. sqft

# Extract data for plotting
sqft_data = rentals_base_table[['sqft', 'list_price']]

#Replace 'None' with 0
sqft_data = sqft_data.replace('None', 0)

#Convert both columns to integers
sqft_data['sqft'] = sqft_data['sqft'].astype(int)
sqft_data['list_price'] = sqft_data['list_price'].astype(int)

# Plot scatter plot

plt.scatter(sqft_data['sqft'], sqft_data['list_price'])
plt.xlabel('sqft')
plt.ylabel('List Price')
plt.title('Sqft vs. List Price')

plt.show()

# %%
# Scatter plot of sold_price vs list price

sold_price_data = rentals_base_table[['sold_price', 'list_price']]

#Replace 'None' with 0
sold_price_data = sold_price_data.replace('None', 0)

#Convert both columns to integers
sold_price_data['sold_price'] = sold_price_data['sold_price'].astype(int)
sold_price_data['list_price'] = sold_price_data['list_price'].astype(int)


plt.scatter(sold_price_data['sold_price'], sold_price_data['list_price'])
plt.xlabel('Sold Price')
plt.ylabel('List Price')
plt.title('Sold Price vs. List Price')

# Fix x-axis labels by taking the max and min and dividing into equal intervals
max_sold_price = max(sold_price_data['sold_price'].dropna())
min_sold_price = min(sold_price_data['sold_price'].dropna())

plt.ticklabel_format(style='plain')    # to prevent scientific notation.

plt.show()

# %%

# Scatter plot of sold_price vs. sqft. Color the dots based on middle school rating

plotting_data = rentals_base_table[['list_price','sqft','elementary_school_rating', 'middle_school_rating', 'high_school_rating']]

# Replace 'None' with 0
plotting_data = plotting_data.replace('None', 0)

# Convert all values to ints
plotting_data.loc[:,'list_price'] = plotting_data.loc[:,'list_price'].astype(float)
plotting_data.loc[:,'sqft'] = plotting_data.loc[:,'sqft'].astype(float)
plotting_data.loc[:,'middle_school_rating'] = plotting_data.loc[:,'middle_school_rating'].astype(float)
plotting_data.loc[:,'elementary_school_rating'] = plotting_data.loc[:,'elementary_school_rating'].astype(float)
plotting_data.loc[:,'high_school_rating'] = plotting_data.loc[:,'high_school_rating'].astype(float)

# Replace NaN with 0
plotting_data = plotting_data.fillna(0)

# Add a column to plotting_data to bin the middle_school_ratings into 0-3, 4-7, 7-10
bins = [0, 5, 10]
plotting_data['middle_school_rating_bin'] = pd.cut(plotting_data['middle_school_rating'], bins)
plotting_data['elementary_school_rating_bin'] = pd.cut(plotting_data['elementary_school_rating'], bins)
plotting_data['high_school_rating_bin'] = pd.cut(plotting_data['high_school_rating'], bins)

sns.set_theme(style="darkgrid")

#Plot three scatter plots side by side
fig, ax = plt.subplots(1, 3, figsize=(15, 5))
# sea = sns.FacetGrid(plotting_data, col="middle_school_rating_bin", hue="middle_school_rating_bin",

sns.lmplot(x='sqft', y='list_price', hue='elementary_school_rating_bin', data=plotting_data)
sns.lmplot(x='sqft', y='list_price', hue='middle_school_rating_bin', data=plotting_data)
sns.lmplot(x='sqft', y='list_price', hue='high_school_rating_bin', data=plotting_data)

plt.xlabel('Sqft')
plt.ylabel('Rent Price')