import csv
import json

arv = []

#print('NAME,PRIMARY TYPE,LAST ERUPTION YEAR,COUNTRY,REGION2,SUBREGION,LATITUDE,LONGITUDE,ELEVATION,EVIDENCE CATEGORY,POPULATION WITHIN 5KM,POPULATION WITHIN 10KM,POPULATION WITHIN 30KM,POPULATION WITHIN 100KM')
with open('gvp_volcanoes-utf8.csv') as csvfile:
    volcs = csv.DictReader(csvfile)
    for volc in volcs:
        if volc['Country'] != '' and volc['Latitude'] != '' and volc['Volcano Name'] != 'Unnamed':
            names = volc['Volcano Name'].strip().split(',')
            #if len(names) == 2:
            #    name = ' '.join([names[1].strip(), names[0].strip()])
            #else:
            #    name = names[0]
            lat = float(volc['Latitude'])
            lon = float(volc['Longitude'])
            try:
                ele = int(volc['Elevation'])
            except:
                ele = 0
            try:
                pop005 = int(volc['Population within 5 km'])
            except:
                pop005 = 0
            try:
                pop010 = int(volc['Population within 10 km'])
            except:
                pop010 = 0
            try:
                pop030 = int(volc['Population within 30 km'])
            except:
                pop030 = 0
            try:
                pop100 = int(volc['Population within 100 km'])
            except:
                pop100 = 0
            volcj = {'name':names[0], 'type':volc['Primary Volcano Type'], 'lastErupYear':volc['Last Eruption Year'], 'country':volc['Country'], 'region2':volc['Region'], \
                    'subregion':volc['Subregion'], 'latitude':lat, 'longitude':lon, 'elevation':ele, 'evidence':volc['Evidence Category'], \
                    'pop005':pop005, 'pop010':pop010, 'pop030':pop030, 'pop100':pop100}
            arv += [volcj]
            region = '"' + volc['Region'] + '"'
            subregion = '"' + volc['Subregion'] + '"'
            #print(','.join([str(item) for item in [names[0], volc['Primary Volcano Type'], volc['Last Eruption Year'], volc['Country'], region, subregion, \
            #        lat, lon, ele, volc['Evidence Category'], pop005, pop010, pop030, pop100]]))
            
print(json.dumps(arv, indent=2))
