#! python3
# curaEngineSettings.py - Loads all default values for settings and overrides ones that are affected by setting inputs from UI.

import json, sys, os

def load_settings(settings):
	for key in settings.keys():
		a_setting = settings[key]
		if type(a_setting) is dict:
			# globals()[key] = dict.fromkeys(['default_value', 'value'])
			if 'default_value' in a_setting:
				default_value = a_setting['default_value']
				print(key + " has default_value=")
				print(default_value)
				globals()[key] = default_value
				# globals()[key]['default_value'] = default_value
			if 'value' in a_setting:
				value = a_setting['value']
				print(key + " has value=")
				print(value)
				# globals()[key]['value'] = value
			if 'children' in a_setting:
				print(key + " has children")
				load_settings(a_setting['children'])

# def override_settings(defintions, settings):
# 	if 'inherits' in defintions and defintions['inherits'] != 'fdmprinter':
# 		file = '/defintions/' + defintions['inherits'] + '.def.json'
# 		with open(os.getcwd() + file) as f:
# 			return load_default_values(json.load(f))
# 	else:
		#TODO override default value and value setting/attribute.

filename = 'speed.json'
filepath = os.getcwd() + '/settings/' + filename
with open(filepath) as f:
	settings = json.load(f)

load_settings(settings)
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


