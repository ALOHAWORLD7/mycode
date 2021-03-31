#!/usr/bin/env python3

import requests

def main():
    r = requests.get("https://cat-fact.herokuapp.com/facts").json()

    print(r)

main()

