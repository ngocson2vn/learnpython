import time

try:
    map_base
except NameError:
    map_base = {}

def display():
    print map_base

def update1():
    map_base['update1'] = 'First'

def update2():
    map_base['update2'] = 'Second'
