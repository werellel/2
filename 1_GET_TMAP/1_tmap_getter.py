from urllib.request import Request, urlopen
TMAP_APP_KEY = "53431fa6-5c6f-35a2-b905-610febb1a2ef"
MIN_LAT = 37.56
MIN_LON = 126.88
MAX_LAT = 37.57
MAX_LON = 126.89
ZOOM_LEVEL = 19

OUT_DIR = "./RESULT/"

# TODO: use for loops to get the traffic info for 4 * 4 areas
# TODO: fill in the request string
NUM = 4
for i in range(NUM):
	for j in range(NUM):
		print(i/100)
		print(j/100)
		requestStr = "https://apis.skplanetx.com/tmap/traffic?sort=&centerLon=&centerLat=&minLat=%s&maxLon=%s&version=1&trafficType=&maxLat=%s&minLon=%s&reqCoordType=WGS84GEO&callback=xml&zoomLevel=%s&radius=&resCoordType=WGS84GEO&appKey=%s&callback=xml" % (MIN_LAT+i/100, MAX_LON+j/100, MAX_LAT+i/100, MIN_LON+j/100, ZOOM_LEVEL, TMAP_APP_KEY)
		AREA_INDEX = NUM*i + j
		in_file = urlopen(requestStr)
		out_file = open(OUT_DIR+'traffic_%02d.json' % (AREA_INDEX), 'wb')
		out_file.write(in_file.read())
		out_file.close()
