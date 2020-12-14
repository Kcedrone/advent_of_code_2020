import numpy as np
input_file = 'day6_test_input.txt'
input_file = 'day6_input.txt'

with open(input_file, 'r') as f:
	lines = f.readlines()

# Make it into one long string
joined = ''.join([line for line in lines])

# Entries are separated by blank lines
groups = joined.split("\n\n")

number_of_people_in_group = [1 + x.count('\n') for x in groups]

print("headcount of group", number_of_people_in_group)

print(groups)

# Delete newlines
groups_collapsed = [entry.replace('\n', '') for entry in groups]
# Convert to unique
number_of_unique_questions = [len(list(set(x))) for x in groups_collapsed]
print("number of unique answers in group", number_of_unique_questions)

print("part 1:", np.sum(np.array(number_of_unique_questions)))



# part 2

# for idx = range(len(groups) - 1)

running_total = 0
group_of_groups = [group.split('\n') for group in groups]
for form in group_of_groups:
	# intsersection = 
	if len(form) == 1:
		common = list(set(form[0]))
		N = len(common)


	else:
		word_1 = form[0]
		common = word_1
		for idx in range(1, len(form)):
			word_2 = form[idx]
			common = ''.join(set(common).intersection(word_2))
		N = len(common)
	
	print(form, common, N)
	running_total += N
print("part 2: ", running_total)


