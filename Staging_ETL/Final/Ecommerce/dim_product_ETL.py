#!/usr/bin/env python3
from cgitb import html
from woocommerce import API
import pandas as pd
import json

def connect():
    wcapi = API(
        url="https://ga.kpim.vn",
        consumer_key="ck_467bf0ebc8ff9715483dfbd736fe84eecb68bba2",
        consumer_secret="cs_bb5b93416d49e6eae02a014f36b8f9f3589ad11a",
        version="wc/v3"
    )
    return wcapi

def extract(wcapi):
    wc_products_json = wcapi.get("products").json()

    wc_products = pd.DataFrame(wc_products_json)

    wc_products.to_csv("files/Ecommerce/wc_products.csv")

def main():
    source = connect()
    extract(source)

main()