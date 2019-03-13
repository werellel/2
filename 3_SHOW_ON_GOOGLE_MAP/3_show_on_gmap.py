import webbrowser

GOOGLE_APP_KEY = 'AIzaSyCeHlDLsYcA9Ji0uonqW88h_oYYJYsPqNw'
CENTER = '37.60,126.90'

IN_DIR = '../2_PARSE_TMAP/RESULT/'
OUT_DIR = './RESULT/'

for area_index in range(16):
    in_file = open(IN_DIR + "congestion_coor_%02d.txt" % (area_index), 'r')
    out_file = open(OUT_DIR + "gmap_urlstr_%02d.txt" % (area_index), 'w')
    print(in_file)
    paths = ""
    for line in in_file:
        color = ""
        congestion, linestring = line.split(';')
        linelist = linestring.split()
        first = linelist[0]
        last = linelist[-1]
        F = first[:20]
        L = last[:20]
        FP = first[:20].find(",")
        LP = last[:20].find(",")
        First = F[FP+1:]+","+F[:FP]
        Last = L[LP+1:]+","+L[:LP]
        print(congestion)
        if congestion == '1':
            color = 'blue'
            print(color)
        elif congestion == '2':
            color = 'green'
            print(color)
        elif congestion == '3':
            color = 'yellow'
            print(color)
        elif congestion == '4':
            color = 'orange'
            print(color)
        elif congestion == '5':
            color = 'red'
            print(color)
        else:
            print("why?")

        paths += '&path=color:%s|weight:5|%s|%s'% (color, First, Last)
    # print(paths)
    # print(area_index)
    urlstr = ("https://maps.googleapis.com/maps/api/staticmap?key="+ GOOGLE_APP_KEY + "&center=" + CENTER + "&zoom=12&size=600x600&maptype=roadmap" + paths)

    webbrowser.open(urlstr)
    # print(urlstr)
    out_file.write(urlstr)
    out_file.close()