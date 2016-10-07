#!/usr/bin/python3

import sys
import png
from glob import glob
import json

if len(sys.argv) < 2:
    print('Generating maps for all images')
    images = glob('flags/*.png')
else:
    images = [sys.argv[1]]

for image in images:
    print('Processing file {}'.format(image))
    with open(image, 'rb') as imagefile:
        r = png.Reader(file=imagefile)
        content = r.read()
        data = list(content[2])
        meta = content[3]
        palette = meta['palette']

        # print('Raw data output')
        # for line in data:
        #     print(''.join([str(x) for x in line]))

        # print('Sample data output')
        output = []
        for numline, line in enumerate(data):
            outputline = []
            if numline not in list(range(6, 40, 6)):
                continue
            for numcolumn, column in enumerate(line):
                if numcolumn not in list(range(8, 68, 8)):
                    continue
                outputline.append(column)
            output.append(outputline)

        mapname = image.split('.')[0].split('/')[1]

        with open('./maps/' + mapname + '.txt', 'w') as mapfile:
            json.dump({'palette': palette, 'data': output}, mapfile)
