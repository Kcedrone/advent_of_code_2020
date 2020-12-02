import parse
import re

with open('problem02_input.txt', 'r') as f:
	lines = f.readlines()

# Part one
valid_count = 0
entry_format = "{}-{} {}: {}"

for line in lines:
	# Ugh, I wish I was better at regex...
	parsed = parse.parse(entry_format, line.strip())
	min_count = int(parsed[0])
	max_count = int(parsed[1])
	letter = parsed[2]
	password = parsed[3]

	letter_count = password.count(letter)

	if (letter_count >= min_count) and (letter_count <= max_count):
		valid_count += 1

print(f"{valid_count} valid passwords") # 517 is correct

# Part one, too stubborn not to try regex...
valid_count = 0
regex_format = r"(\d+)\-(\d+) ([a-zA-Z])\: ([a-zA-Z]+(?:\s+#[a-zA-Z]+)*)"

for line in lines:
	regex_parsed = re.search(regex_format, line.strip())
	min_count = int(regex_parsed.group(1))
	max_count = int(regex_parsed.group(2))
	letter = regex_parsed.group(3)
	password = regex_parsed.group(4)

	letter_count = password.count(letter)

	if (letter_count >= min_count) and (letter_count <= max_count):
		valid_count += 1

print(f"{valid_count} valid passwords with regex") # 517 is correct

# Part two
valid_count = 0
for line in lines:
	parsed = parse.parse(entry_format, line.strip())
	position_1 = int(parsed[0]) - 1 # Convert to zero index
	position_2 = int(parsed[1]) - 1 # Convert to zero index
	letter = parsed[2]
	password = parsed[3]

	# Apply XOR
	if  ((password[position_1] == letter) and not (password[position_2] == letter)) or \
		(not (password[position_1] == letter) and (password[position_2] == letter)):
		valid_count += 1



print(f"{valid_count} valid passwords") # 284 is correct
