import json
import png
import sys
from glob import glob

if len(sys.argv) < 2:
    print('Generating pngs for all images')
    maps = glob('maps/*.txt')
else:
    maps = [sys.argv[1]]

for map in maps:
    print('Processing map {}'.format(map))
    name = map.split('/')[1].split('.')[0]
    with open(map, 'r') as mapfile:
        content = json.load(mapfile)
        print(content)
        output = []
        for line in content['data']:
            outline = []
            for column in line:
                outline.extend(content['palette'][column])
            print(tuple(outline))
            output.append(tuple(outline))
        print(output)

        with open('./pngs/' + name + '.png', 'wb') as pngfile:
            w = png.Writer(8, 6)
            w.write(pngfile, output)
