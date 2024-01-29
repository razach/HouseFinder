# Main script to run backend_main.py and import_to_db.py

# %%
from backend import get_rentals_main

from data_work import import_to_db


get_rentals_main.get_rentals()

import_to_db.import_to_db('./backend/rentals_with_schools.csv', './backend/big_list_of_schools.csv')


# %%

