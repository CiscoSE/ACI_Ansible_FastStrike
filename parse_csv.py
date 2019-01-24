#!/usr/bin/env python

# ======================================================
# Parse CSV file and create yml input file
# Created on Jan 10, 2019
# Author: Tom Qian, Henry Carmouche, and Mark Ellwanger
# ======================================================
 
import csv
import sys
import yaml
 
csv_data = []
with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        csv_data.append(row)
 
with open(sys.argv[1] + '.yml', 'w') as outfile:
    outfile.write(yaml.dump({'raw_data': csv_data}))
