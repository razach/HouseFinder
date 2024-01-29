#%%

import pandas as pd

#%%
# Import in ../backend/big_list_of_schools.csv as a dataframe
big_list_of_schools = pd.read_csv("../../backend/big_list_of_schools.csv")
big_list_of_schools.set_index('slug_id', inplace=True)

#%%
# Check if all the id's in column id start with a leading 0. If not, append a 0 to be beginning of each id.
for index, row in big_list_of_schools.iterrows():
    id = str(row['id'])
    if id[0]!= '0':
        big_list_of_schools.at[index, 'id'] = '0' + id

# Print out the list of ids
print(big_list_of_schools.loc[:,'id'])       


# %%
# Check the big_list_of_schools dataframe for duplicates and print them out

print(big_list_of_schools[big_list_of_schools.duplicated(subset=['id'])])


#%%

# Remove the column 'distance_in_miles' from big_list_of_schools
big_list_of_schools = big_list_of_schools.drop(columns=['distance_in_miles'])

# Remove duplicate rows from big_list_of_schools
big_list_of_schools.drop_duplicates(inplace=True)

#check by printing out a list of duplicate rows
print(big_list_of_schools[big_list_of_schools.duplicated(subset=['id'])])

# %%
# Save back the big_list_of_schools dataframe to../backend/big_list_of_schools.csv
big_list_of_schools.to_csv("../../backend/big_list_of_schools.csv", index=True)