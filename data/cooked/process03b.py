import csv
import json

vl = []

with open('03c.csv') as vfile:
    vf = list(csv.DictReader(vfile))
    for v in vf:
        vl += [v]
    
print(json.dumps(vl, indent=2))
