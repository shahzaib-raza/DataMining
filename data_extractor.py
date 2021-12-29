# Imports
import requests
import pandas as pd

# An empty array to store data
data: list = []
# Loop for iterating over first 15 pages of Pakwheels api calls
for i in range(1, 16):
    # Url of api
    url: str = "https://www.pakwheels.com/used-cars/search/-/ct_karachi/.json?client_id=37952d7752aae22726aff51be531cddd&client_secret=014a5bc91e1c0f3af4ea6dfaa7eee413&api_version=15&page=" + str(i) + "&extra_info=true"
    # Jason object of result
    res = requests.get(url).json()['result']
    # Total number of in-listed cars for sale
    n_entries = len(res)
    # Loop for iterating over each car entry
    for j in range(n_entries):
        # The amount of car
        amount = res[j]['price']
        try:
            # If amount is a number
            amount = int(amount)
            # We as a human decide the category by observing the price
            if amount in range(1, 1200000):
                category: str = "affordable"
            elif amount in range(1200000, 2200000):
                category: str = "mid_range"
            else:
                category: str = "luxury"
            # Now we add the car's features as an entry in our data array with its price
            data.append([str(res[j]['make']),
                         int(res[j]['model_year']),
                         int(''.join(filter(str.isdigit, res[j]['engine_capacity']))),
                         bool(res[j]['air_bags']),
                         bool(res[j]['air_conditioning']),
                         bool(res[j]['power_windows']),
                         bool(res[j]['power_steering']),
                         bool(res[j]['sun_roof']),
                         bool(res[j]['alloy_rims']),
                         category,
                         amount])
        except ValueError:
            # Else if the price is not a number we simply neglect the entry
            pass

# Column names of our data
cols = ['make',
        'model_year',
        'engine_capacity',
        'air_bags',
        'air_conditioning',
        'power_windows',
        'power_steering',
        'sun_roof',
        'alloy_rims',
        'category',
        'price']

# Converting the data into Pandas DataFrame object
df = pd.DataFrame(data, columns=cols)

# Saving the data in a csv file
df.to_csv("data.csv", index=False)
