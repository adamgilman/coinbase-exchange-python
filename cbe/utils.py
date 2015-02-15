from dateutil import parser

def ConvertTime(json_time):
	return parser.parse(json_time)

def insertPythonTime(return_json):
	for row in return_json:
		if type(row) is dict:
			if row.has_key("time"):
				row['python_time'] = ConvertTime(row['time'])
	return return_json