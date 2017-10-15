import csv
import json

vl = []

print('NAME,COUNTRY,LATITUDE,LONGITUDE,ELEVATION,TYPE,POPULATION WITHIN 10KM,LARGEST YEAR,LARGEST VEI,LATEST YEAR,LATEST VEI,ERUPTION COUNT')
with open('gvp_volcanoes.csv') as vfile:
    with open('eruptions.csv') as efile:
        vf = list(csv.DictReader(vfile))
        ef = list(csv.DictReader(efile))
        for v in vf:
            my_e = []
            for e in ef:
                if e['NAME'] == v['NAME']:
                    my_e += [e]
            my_e.sort(key=lambda e: int(e['START']))
            if len(my_e) > 0:
                ec = 0
                latest = my_e[-1]
                largest = my_e[-1]
                for e in my_e:
                    if int(e['START']) > 1800:
                        ec += 1
                        if e['VEI'] >= largest['VEI']:
                            largest = e
                if int(largest['START']) > 1800:
                    vo = { \
                            'name':v['NAME'], 'country':v['COUNTRY'], \
                            'latitude':v['LATITUDE'], 'longitude':v['LONGITUDE'], 'elevation':v['ELEVATION'], \
                            'type':v['PRIMARY TYPE'], 'pop010':v['POPULATION WITHIN 10KM'], \
                            'largestStart':largest['START'], 'largestVei':largest['VEI'], 'latestStart':latest['START'], 'latestVei':latest['VEI'], \
                            'eruptionCount':ec \
                        }
                    vl += [vo]
                    print(','.join([str(item) for item in [ \
                        v['NAME'], v['COUNTRY'], \
                        v['LATITUDE'], v['LONGITUDE'], v['ELEVATION'], \
                        v['PRIMARY TYPE'], v['POPULATION WITHIN 10KM'], \
                        largest['START'], largest['VEI'], latest['START'], latest['VEI'], ec \
                    ]]))
    
#print(json.dumps(vl, indent=2))
