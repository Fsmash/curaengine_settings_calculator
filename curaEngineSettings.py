#! python3
# curaEngineSettings.py - Loads all default values for settings and overrides ones that are affected by setting inputs from UI.

import json, sys, os, math

# MULTIPLE EXTRUDER FUNCTIONS, STUBS TO GET THINGS WORKING
def extruderValue(first, second):
	return globals()[second]

def extruderValues(param):
	return globals()[param]

def resolveOrValue(param):
	return globals()[param]

def print_mode():
	return 'regular'
# END MULTIPLE EXTRUDER FUNCTIONS

def load_file(filepath):
	full_filepath = os.getcwd() + filepath
	with open(full_filepath) as f:
		return json.load(f)

def override_settings(definitions):
	global values_dict
	if 'inherits' in definitions and definitions['inherits'] != 'fdmprinter':
		inherited_definitions = load_file('/cura/definitions/' + definitions['inherits'] + '.def.json')
		override_settings(inherited_definitions)
	for key, setting in definitions['overrides'].items():
		if 'default_value' in setting and key in globals():
			globals()[key] = setting['default_value']
		if 'value' in setting and key in values_dict:
			values_dict[key] = setting['value']

def load_settings(settings):
	for key in settings.keys():
		setting = settings[key]
		if type(setting) is dict:
			if 'default_value' in setting:
				global keys
				keys.append(key)
				# print(key + ' has default_value=')
				# print(setting['default_value'])
				globals()[key] = setting['default_value']
			if 'value' in setting:
				value = setting['value']
				# print(key + ' has value=')
				# print(value)
				global values_dict
				values_dict[key] = value
			if 'children' in setting:
				# print(key + ' has children')
				load_settings(setting['children'])

def eval_values(values_dict):
	for key, value in values_dict.items():
		value = str(value)
		# print('This is the key ' + key)
		# print('This is the calculation ' + value)
		calculation = eval(value)
		globals()[key] = calculation
		# print('Assigned the value ' + str(calculation) + ' to key')

# Main
if len(sys.argv) < 3:
	print('Usage: curaEngineSettings.py /defintions/example.def.json [json_string: ....]')
	sys.exit()

definition_file = ''.join(sys.argv[1])

definitions = load_file(definition_file)
inputs = json.loads(''.join(sys.argv[2]))
# print(inputs)

# removed dual.json, not dealing with that right now.
files = ['blackmagic.json', 'command_line_settings.json', 'cooling.json', 'speed.json', 'experimental.json', 'infill.json', 'machine_settings.json', 'material.json', 'meshfix.json', 'platform_adhesion.json', 'resolution.json', 'shell.json', 'speed.json', 'support.json', 'travel.json']

values_dict = dict()
keys = []

for file in files:
	settings = load_file('/cura/settings/' + file)
	load_settings(settings)	

override_settings(definitions)

for key, value in inputs.items():
	# print('This is the key ' + key)
	# print('This is the value ' + str(value))
	globals()[key] = value

eval_values(values_dict)

settings_string = ''
for key in keys:
	settings_string += ' -s ' + key + '=' + '"' + str(globals()[key]) + '"'

print(settings_string)