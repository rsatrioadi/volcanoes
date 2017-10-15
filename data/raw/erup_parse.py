import csv
import json

are = []

print('ERUP ID,NAME,VEI,START,END')
with open('gvp_erup.csv') as csvfile:
    erups = csv.DictReader(csvfile)
    for erup in erups:
        if erup['VEI'] != '' and erup['Volcano Name'] != 'Unnamed' and erup['Eruption Category'] == 'Confirmed Eruption':
            names = erup['Volcano Name'].strip().split(',')
            erupj = {'erupId':erup['Eruption Number'], 'name':names[0], 'vei':erup['VEI'], 'start':erup['Start Year'], 'end':erup['End Year']}
            are += [erupj]
            print(','.join([str(item) for item in [erup['Eruption Number'], names[0], erup['VEI'], erup['Start Year'], erup['End Year']]]))
            
#print(json.dumps(are, indent=2))
