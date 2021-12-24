import requests
import pandas as pd

data: list = []
for i in range(1, 16):
    url: str = "https://www.pakwheels.com/used-cars/search/-/ct_karachi/.json?client_id=37952d7752aae22726aff51be531cddd&client_secret=014a5bc91e1c0f3af4ea6dfaa7eee413&api_version=15&page=" + str(i) + "&extra_info=true"
    res = requests.get(url).json()['result']
    n_entries = len(res)
    for j in range(n_entries):
        amount = res[j]['price']
        try:
            amount = int(amount)
            if amount in range(1, 1200000):
                category: str = "affordable"
            elif amount in range(1200000, 2200000):
                category: str = "mid_range"
            else:
                category: str = "luxury"
            data.append([str(res[j]['make']),
                         int(res[j]['model_year']),
                         int(''.join(filter(str.isdigit, res[j]['engine_capacity']))),
                         bool(res[j]['air_bags']),
                         bool(res[j]['air_conditioning']),
                         bool(res[j]['power_windows']),
                         bool(res[j]['power_steering']),
                         bool(res[j]['sun_roof']),
                         bool(res[j]['alloy_rims']),
                         category])
        except ValueError:
            pass

cols = ['make',
        'model_year',
        'engine_capacity',
        'air_bags',
        'air_conditioning',
        'power_windows',
        'power_steering',
        'sun_roof',
        'alloy_rims',
        'category']
df = pd.DataFrame(data, columns=cols)
df.to_csv("data.csv", index=False)
