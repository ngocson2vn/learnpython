import time

try:
    map_base
except NameError:
    map_base = {}

def loop():
    while True:
        print map_base
        time.sleep(1)

class Ca:
    def __init__(self):
        map_base["key1"] = "value1"
        self._map = map_base

class Cb:
    def __init__(self):
        map_base["key2"] = "value2"
        self._map = map_base
