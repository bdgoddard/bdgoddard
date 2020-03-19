# -*- coding: utf-8 -*-
import yaml
import os
import csv
import codecs
from urllib.request import urlopen
import getopt
import sys

import pandas as pd
import requests

csv_file = 'Beers.csv'
csv_s_file = 'BeerSorted.csv'
output  = 'beers.yml'

# Download csv file
response = requests.get('https://docs.google.com/spreadsheet/ccc?key=1a7qfn6Dq664N_0ynsL48eLv09zIcjJ3Mb7uTX_bgUJg&output=csv')
assert response.status_code == 200, 'Wrong status code'
data = response.content

with open(csv_file, 'wb') as f:
    f.write(data)
    print('Downloaded csv')

# Sort csv file
df = pd.read_csv(csv_file)
df_s = df.sort_values(['Brewery', 'Beer'])
df_s.to_csv(csv_s_file, index = False, header=True)
print('Sorted csv')

# Write yml file
with open(csv_s_file, 'r') as f_csv:

    csv_reader = csv.reader(f_csv)
    keys = next(csv_reader)
    
    f_yml = open(output, 'w',encoding="utf-8")
    for row in csv_reader:
        yaml.dump([dict(zip(keys, row))], f_yml, default_flow_style=False)

print('Converted to yml')

