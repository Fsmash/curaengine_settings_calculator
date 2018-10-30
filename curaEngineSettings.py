#! python3
# curaEngineSettings.py - Loads all default values for settings and overrides ones that are affected by setting inputs from UI.

import json, sys, os, math

def extruderValue(first, second):
	return globals()[second]

def extruderValues(param):
	return globals()[param]

def resolveOrValue(param):
	return globals()[param]

def load_file(filename):
	filepath = os.getcwd() + "/settings/" + filename
	with open(filepath) as f:
		return json.load(f)

def load_settings(settings):
	for key in settings.keys():
		setting = settings[key]
		if type(setting) is dict:
			# globals()[key] = dict.fromkeys(["default_value", "value"])
			if "default_value" in setting:
				default_value = setting["default_value"]
				# print(key + " has default_value=")
				# print(default_value)
				globals()[key] = default_value
				# globals()[key]["default_value"] = default_value
			if "value" in setting:
				value = setting["value"]
				# print(key + " has value=")
				# print(value)
				global values_dict
				values_dict[key] = value
				# globals()[key]["value"] = value
			if "children" in setting:
				# print(key + " has children")
				load_settings(setting["children"])

def eval_values(values_dict):
	for key, value in values_dict.items():
		print("This is the key " + key)
		# value = values_dict[key]
		print("This is the value " + value)
		globals()[key] = eval(value)


# def override_settings(defintions, settings):
# 	if 'inherits' in defintions and defintions['inherits'] != 'fdmprinter':
# 		file = '/defintions/' + defintions['inherits'] + '.def.json'
# 		with open(os.getcwd() + file) as f:
# 			return load_default_values(json.load(f))
# 	else:
		#TODO override default value and value setting/attribute.


# removed dual.json, not dealing with that right now.
files = ["blackmagic.json", "command_line_settings.json", "cooling.json", "speed.json", "experimental.json", "infill.json", "machine_settings.json", "material.json", "meshfix.json", "platform_adhesion.json", "resolution.json", "shell.json", "speed.json", "support.json", "travel.json"]
values_dict = dict()

for file in files:
	settings = load_file(file)
	load_settings(settings)	

eval_values(values_dict)
del settings
del values_dict
print(globals())

# if len(sys.argv) < 2:
# 	print('Usage: curaEngineSettings.py defintion')
# 	sys.exit()

# file = ''.join(sys.argv[1:])

# with open(os.getcwd() + file) as f:
# 	defintions = json.load(f)

# settings = defintions['settings']

# for key in settings.keys():
# 	print(key)


