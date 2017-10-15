import csv
import json

vj = json.loads(open('gvp_volcanoes.json', 'r').read())
ej = json.loads(open('eruptions.json', 'r').read())

vl = []

#print('NAME,COUNTRY,LATITUDE,LONGITUDE,ELEVATION,TYPE,LARGEST YEAR,LARGEST VEI,LATEST YEAR,LATEST VEI')
for v in vj:
    my_e = []
    for e in ej:
        if e['name'] == v['name']:
            my_e += [e]
    my_e.sort(key=lambda e: int(e['start']))
    if len(my_e) > 0:
        latest = my_e[-1]
        #print v['name'], latest['start'], latest['vei']
        largest = my_e[0]
        for e in my_e:
            if e['vei'] >= largest['vei']:
                largest = e
            #print '  ', e['start'], e['vei']
        #print '  ', largest['start'], largest['vei']
        v['largestStart'] = largest['start']
        v['largestVei'] = largest['vei']
        v['latestStart'] = latest['start']
        v['latestVei'] = latest['vei']
        vl += [v]
        #print(v['name'])
        #print(','.join([str(item) for item in [ \
        #    v['name'], v['country'], \
        #    v['latitude'], v['longitude'], v['elevation'], \
        #    v['type'], \
        #    v['largestStart'], v['largestVei'], v['latestStart'], v['latestVei'] \
        #]]))
    
print(json.dumps(vl, indent=2))
