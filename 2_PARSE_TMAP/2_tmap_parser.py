import codecs
import json

IN_DIR = "../1_GET_TMAP/RESULT/"
OUT_DIR = "./RESULT/"

for area_index in range(16):
	in_file = codecs.open(IN_DIR+'traffic_%02d.json' % (area_index) , 'r', 'utf-8')
	cont = in_file.read()
	j = json.loads(cont)
	parses = ""
	for feat in j['features']:
		coordinates = str(feat['geometry']['coordinates']).replace("[", "").replace("]", "").replace("]", "").replace(", 1", " 1").replace(", 3", ",3")
		congestion = str(feat['properties']['congestion'])
		parse = congestion + ';' + coordinates + "\n"
		parses += parse
	print(area_index)
	print(parses)
	print("parses")
	out_file = open(OUT_DIR+'congestion_coor_%02d.txt' % (area_index), 'w')
	out_file.write(parses)
	out_file.close()
