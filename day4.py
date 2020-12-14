import re

input_file = 'day4_part1_testinput.txt'
input_file = 'day4_part1_input.txt'
# input_file = 'day4_some_invalid_passports.txt'
input_file = 'day4_some_valid_passports.txt'
input_file = 'day4_input.txt'

with open(input_file, 'r') as f:
	lines = f.readlines()

# Make it into one long string
joined = ''.join([line for line in lines])

# Entries are separated by blank lines
entries = joined.split("\n\n")

# Convert newline into space
entries = [entry.replace('\n', ' ') for entry in entries]

# Parse entries into dictionary credential sets
credentials = []
for entry in entries:
	kv_pairs = entry.split(' ')
	document_vals = {}
	for kv_pair in kv_pairs:
		try:
			key, val = kv_pair.split(':')
		except ValueError:
			print('Error with: ', kv_pair)
		document_vals[key] = val
	
	credentials.append(document_vals)

# print(sorted(list(credentials[0].keys())))


### PART 1
ALL_KEYS = ['byr', 'cid', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
ALLOWABLE_KEYS = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']

def validate_fields_present(entry):
	has_all_fields = sorted(list(entry.keys())) == ALL_KEYS
	has_all_north_pole_fields = (sorted(list(entry.keys())) == ALLOWABLE_KEYS)
	return has_all_fields or has_all_north_pole_fields

total_valid = 0
for person in credentials:
	doc_status = validate_fields_present(person)
	if doc_status:
		total_valid += 1
print('Part 1:', total_valid)


### PART 2
def validate_year(year, min_val, max_val):
	if len(year) != 4:
		return False
	try:	
		year = int(year)
		valid_year = (year >= min_val) and (year <= max_val)
		return valid_year
	except ValueError:
		return False

def validate_byr(year):
	return validate_year(year, 1920, 2002)

def validate_iyr(year):
	return validate_year(year, 2010, 2020)

def validate_eyr(year):
	return validate_year(year, 2020, 2030)

def validate_height(height):
#	units_limits = {'cm': (150, 193), 'in': (59, 76)}
	if height.endswith('cm'):
		height_num = height.split('cm')[0]
		try:
			height_num = int(height_num)
			if (height_num >= 150) and (height_num <= 193):
				return True
			else:
				return False
		except ValueError:
			return False
		
	elif height.endswith('in'):
		height_num = height.split('in')[0]
		try:
			height_num = int(height_num)
			if (height_num >= 59) and (height_num <= 76):
				return True
			else:
				return False
		except ValueError:
			return False
	else:
		return False

def validate_hcl(hcl):
	# if re.match(r"[#]{1}[abcdefABCDEF0-9]{6}", hcl) is None:
		# return False
	# else:
		# return True
	rematch = re.match(r"[#]{1}[abcdefABCDEF0-9]{6}", hcl)
	if rematch is None:
		return False
	else:
		return rematch[0] == hcl

def validate_ecl(ecl):
	VALID_ECL = ['amb','blu','brn','gry','grn','hzl','oth']
	return ecl in VALID_ECL

def validate_pid(pid):
	rematch = re.match(r"[0-9]{9}", pid)
	if rematch is None:
		return False
	else:
		return rematch[0] == pid


total_valid = 0
for person in credentials:
	all_fields = validate_fields_present(person)
	valid_credentials = all_fields

	if all_fields:
		valid_credentials &= validate_byr(person['byr'])
		valid_credentials &= validate_iyr(person['iyr'])
		valid_credentials &= validate_eyr(person['eyr'])
		valid_credentials &= validate_height(person['hgt'])
		valid_credentials &= validate_hcl(person['hcl'])
		valid_credentials &= validate_ecl(person['ecl'])
		valid_credentials &= validate_pid(person['pid'])

	if valid_credentials and all_fields:
		total_valid += 1

print('Part 2: ', total_valid)
