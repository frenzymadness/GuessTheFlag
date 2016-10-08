import json
import sys
from glob import glob

if len(sys.argv) < 2:
    print('Generating data for all maps')
    maps = glob('maps/*.txt')
else:
    maps = [sys.argv[1]]

data = []

for map in maps:
    # print('Processing map {}'.format(map))
    name = map.split('/')[1].split('.')[0].lstrip('flag-of-')
    with open(map, 'r') as mapfile:
        content = json.load(mapfile)
        flagdata = []
        for line in content['data']:
            for point in line:
                flagdata.append(tuple(content['palette'][point]))
        print(str(tuple(flagdata)))
