import json

vfile = open('volcanoes.txt', 'r')
lines = vfile.readlines()

arv = []

#print('NAME,REGION,LATITUDE,LONGITUDE,ELEVATION,TYPE,STATUS,LAST ERUPTION CODE')
for line in lines:
    names = line[10:40].strip().split(',')
    #if len(names) == 2:
    #    name = ' '.join([names[1].strip(), names[0].strip()])
    #else:
    #    name = names[0]
    if names[0] != 'UNNAMED':
        region = line[41:62].strip()
        latitude = float(line[62:69].strip())
        longitude = float(line[70:78].strip())
        try:
            elevation = int(line[80:85].strip())
        except:
            elevation = 0
        vtype = line[86:107].strip()
        status = line[107:131].strip()
        last_erup = line[131:133].strip()
        volc = {'name':names[0], 'region':region, 'latitude':latitude, 'longitude':longitude, 'elevation':elevation, 'type':vtype, 'status':status, 'lastErupCode':last_erup}
        arv += [volc]
        #print(','.join([str(item) for item in [names[0], region, latitude, longitude, elevation, vtype, status, last_erup]]))
    
print(json.dumps(arv, indent=2))
