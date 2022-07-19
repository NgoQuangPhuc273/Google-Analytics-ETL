# from woocommerce import API
import json
import pandas as pd

# wcapi = API(
#     url="https://ga.kpim.vn",
#     consumer_key="ck_467bf0ebc8ff9715483dfbd736fe84eecb68bba2",
#     consumer_secret="cs_bb5b93416d49e6eae02a014f36b8f9f3589ad11a",
#     version="wc/v3"
# )

# r = wcapi.get("products").json()

# products_list_json = pd.read_json(r)
# products_list_csv = products_list_json.to_csv()

# print(products_list_csv)


pdObj = pd.read_json('sample.json')
pdObj.to_csv('streaming.csv', index=False)
