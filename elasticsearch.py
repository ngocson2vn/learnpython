import sys
import requests
from datetime import date, timedelta
import requests
import time
import re
import json

ES_ENDPOINT = "http://localhost:9200/"

def dump(obj):
    for attr in dir(obj):
        print("obj.%s = %s" % (attr, getattr(obj, attr)))

def get_indices(pattern):
    r = requests.get(ES_ENDPOINT + pattern, timeout=600)
    return r.json().keys()

def get_index_settings(index):
    r = requests.get(ES_ENDPOINT + "%s/_settings" % index, timeout=600)
    #return json.dumps(r.json(), indent=4, sort_keys=True)
    return r.json()

def update_number_of_replicas(indices, n):
    d = {"index": {"number_of_replicas": n}}
    for index in indices:
        r = requests.put(ES_ENDPOINT + "%s/_settings" % index, data=json.dumps(d), timeout=600)
        print index, r.json()

def update_indices(pattern):
    indices = get_indices(pattern)
    print indices
    update_number_of_replicas(indices, 0)

    for index in indices:
        print "%s: number_of_replicas: %s" % (index, get_index_settings(index)[index]["settings"]["index"]["number_of_replicas"])

def main():
    #pattern = "*nginx-*/_aliases";
    #update_indices(pattern)

    pattern = "*-rails-*/_aliases";
    update_indices(pattern)

if __name__ == "__main__":
    main()
