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
    wc_orders_json = wcapi.get("orders").json()

    wc_orders = pd.DataFrame(wc_orders_json)

    wc_orders.to_csv("files/Ecommerce/wc_orders.csv")

def main():
    source = connect()
    extract(source)

main()