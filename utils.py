import re
import lxml.html as parser
import cjson

from settings import *

def is_user_valid(id):
	"""
	Checks if the USERNAME is valid.
	"""
	r = re.compile(ID_REGEX_STRICT)
	return bool(r.match(id))

def parse_html(html):
	"""
	Takes the HTML and spits out the list of fields
	relevant to the status.
	"""
	tree = parser.fromstring(html)
	elements = tree.find_class(MAGIC_CLASS)
	if not elements:
		return None

	long_global=elements[0].getchildren()[1].getchildren()[1].getchildren()[0].getchildren()[0].text
	if(long_global!='NA'):
		long_country=elements[0].getchildren()[1].getchildren()[1].getchildren()[1].getchildren()[0].text
	else:
		long_country='NA'
	long_rating=elements[0].getchildren()[1].getchildren()[2].text
	short_global=elements[0].getchildren()[2].getchildren()[1].getchildren()[0].getchildren()[0].text
	if(short_global!='NA'):
		short_country=elements[0].getchildren()[2].getchildren()[1].getchildren()[1].getchildren()[0].text
	else:
		short_country='NA'
	short_rating=elements[0].getchildren()[1].getchildren()[2].text
	return (long_global,long_country,long_rating,short_global,short_country,short_rating)

def build_response_dict(data):
	"""
	Takes in the field parameters and builds JSON.
	"""
	response = {}

	for i in range(len(FIELDS)):
		response[FIELDS[i]] = data[i]

	return response