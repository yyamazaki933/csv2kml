#!/usr/bin/env python3

import pandas as pd

csv_filename = '/media/yudai/ssd/20230222_lv3_proto/map/corrected.csv'
lat_colmn = 'latitude'
lon_colmn = 'longitude'
interval = 50
kml_filename = csv_filename.replace('.csv', '.kml')

KML_HEADER = '<?xml version="1.0" encoding="UTF-8"?>\n\
<kml xmlns="http://earth.google.com/kml/2.0">\n\
<Document>\n'

KML_FOOTER = '</Document>\n</kml>'

LINE_HEADER = '\
<Placemark>\n\
<LineString>\n\
<coordinates>\n'

LINE_FOOTER = '\
</coordinates>\n\
</LineString>\n\
<Style>\n\
<LineStyle>\n\
<color>#ff0000ff</color>\n\
<width>5</width>\n\
</LineStyle>\n\
</Style>\n\
</Placemark>\n'

POINT_HEADER = '<Placemark>\n<Point>\n<coordinates>\n'

POINT_FOOTER = '</coordinates>\n</Point>\n</Placemark>\n'


def writeKML(data: pd.DataFrame, lon_axis: str, lat_axis: str, interval: int, kml_name: str):
    kml = KML_HEADER
    kml += LINE_HEADER
    i = 0
    for lon, lat in zip(data[lon_axis], data[lat_axis]):
        if i % interval == 0:
            kml += str(lon) + ',' + str(lat) + ',0.0\n'
        i += 1
    kml += LINE_FOOTER

    # for lon, lat in zip(data[long_axis], data[lat_axis]):
    #     kml += POINT_HEADER
    #     kml += str(lon) + ',' + str(lat) +',0.0\n'
    #     kml += POINT_FOOTER

    kml += KML_FOOTER

    with open(kml_name, mode='w') as f:
        f.write(kml)
        f.close()

    print("Save file:", kml_name)


if __name__ == '__main__':
    data = pd.read_csv(csv_filename)
    writeKML(data, lon_colmn, lat_colmn, interval, kml_filename)
