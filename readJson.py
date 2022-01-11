import json

# Below code reads the inputJson.json file

with open('inputJson.json') as fi:
    data = json.load(fi)
    for mycolor in data['colors']:
        print (mycolor['color'])
