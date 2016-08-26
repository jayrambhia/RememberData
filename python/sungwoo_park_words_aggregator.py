import re
import sys
import os
import json

def writeToFile(classjson, output_filename):
	w = open(output_filename + "/" + classjson['code'] + ".json", 'w')
	w.write(json.dumps(classjson))
	w.close()

def writeClassesToFile(classes, output_filename):
	w = open(output_filename + "/_classes.json", "w")
	for classjson in classes:
		classjson.pop('data')

	w.write(json.dumps(classes))	
	w.close()


def writeToJson2(filename, output_filename):
	f = open(filename, 'r')
	

	i=0

	classes = []
	cards = []
	classjson = {}

	for line in f:
		words = line.split()
		word = words[0].strip()

		if len(word) == 1:
			if len(cards) != 0:
				classjson['data'] = cards
				classes.append(classjson)
				writeToFile(classjson, output_filename)
				cards = []
				classjson = {}

			name = word + " " + words[1].strip()

			classjson['name'] = name
			classjson['descriptopn'] = 	name
			classjson['code'] = "GRE_B " + name
			continue


		meaning = (" ".join(words[1:])).replace("; ", "\n")
		# print word.strip(), "->", meaning.strip()

		card = {}
		
		card['key'] = unicode(word.strip())
		try :
			card['value'] = unicode(meaning.strip())
		except UnicodeDecodeError:
			print "UnicodeDecodeError", meaning.strip()
			continue

		cards.append(card)
		
		# i = i+1
		# if i > 250:
		# 	break

	classjson['data'] = cards
	writeToFile(classjson, output_filename)
	classes.append(classjson)		
	writeClassesToFile(classes, output_filename)
	# w.write(json.dumps(classes))
	print "wrote", len(classes), "classes"


def writeToJson(filename, output_filename):

	f = open(filename, 'r')
	w = open(output_filename, 'w')

	i=0

	classes = []
	cards = []
	classjson = {}

	for line in f:
		# print line
		# print line.replace("\t", "\\t")
		
		words = line.split("\t \t")
		if (len(words) == 1):
			if len(cards) != 0:
				classjson['data'] = cards
				classes.append(classjson)
				cards = []
				classjson = {}

			classjson['name'] = words[0].strip()
			classjson['descriptopn'] = 	words[0].strip()
			classjson['code'] = words[0].strip()
			print 'name: ', words[0].strip()
			continue

		word, meaning = words[:2]
		card = {}
		card['key'] = word
		card['value'] = "\n".join(meaning.strip().split("; "))
		cards.append(card)

		i = i+1
		# if i > 150:
		# 	break

	classjson['data'] = cards
	classes.append(classjson)		

	w.write(json.dumps(classes))
	print "wrote", len(classes), "classes"

filename = os.path.abspath(sys.argv[1])
output_filename = sys.argv[2]

writeToJson2(filename, output_filename)	
