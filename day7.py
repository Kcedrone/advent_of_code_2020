# possible_contents={}
# possible_contents['light red'] = ['1_bright white', '2_muted yellow']
# possible_contents['dark orange'] = ['3_bright white', '4_muted yellow']
# possible_contents['bright white'] = ['1_shiny gold']
# possible_contents['muted yellow'] = ['2_shiny gold', '9_faded blue']
# possible_contents['shiny gold'] = ['1_dark olive', '2_vibrant plum']
# possible_contents['dark olive'] = ['3_faded blue', '4_dotted black']
# possible_contents['vibrant plum'] = ['5_faded blue', '6_dotted black']
# possible_contents['faded blue'] = []
# possible_contents['dotted black'] = []

import re
input_file = 'day7_part1_test_input.txt'
# input_file = 'day7_part1_input.txt'

with open(input_file, 'r') as f:
	lines = f.readlines()

rules = []
possible_contents = {}
for line in lines:
	outer_bag_colour, rule = line.split(' bags contain ')
	if 'no other bags' in rule:
		possible_contents[outer_bag_colour] = ['0 other bag',]
	else:
		rule = rule.replace('bags', 'bag')
		rule = rule.replace('bag.', 'bag')
		rule = rule.replace(', ', ',')
		rule = rule.replace('\n', '')
		rule = rule.replace(' bag', '')
		rules = rule.split(',')
		possible_contents[outer_bag_colour] = rules
		# print(rules)


def find_containers(test_bag):
	usable_bags = []
	for outer_bag_colour, allowable_contents in possible_contents.items():
		if allowable_contents:
			for bag_spec in allowable_contents:
				if test_bag in bag_spec:
					# bag_count = bag_spec.split('_')[0]
					num_of_bags = int(re.match(r"[0-9]+", bag_spec)[0])
					usable_bags.append(outer_bag_colour)
	return usable_bags 

test_bag = 'shiny gold'
usable_bags = find_containers(test_bag)

print(usable_bags)

other_test_bags = ['shiny gold',]
all_usable_bags = []
colors_tested = []
while len(other_test_bags):
	for test_bag in other_test_bags:
		if test_bag not in colors_tested:
			colors_tested.append(test_bag)
			usable_bags = find_containers(test_bag)
			all_usable_bags += usable_bags
			other_test_bags += usable_bags
	break

all_usable_bags = list(set(all_usable_bags))
print("Part 1: ", input_file, all_usable_bags)
print("Part 1: ", len(all_usable_bags))

print("*" * 60)


# Part 2
test_bag = 'shiny gold'
def count_bags_inside(test_bag):
	bag_contents = possible_contents[test_bag]
	new_bags = []
	if bag_contents:
		for bag_spec in bag_contents:
			idx_start, idx_end = re.match(r"[0-9]+", bag_spec).span()
			num_of_bags = int(bag_spec[idx_start:idx_end])
			bag_colour = bag_spec[idx_end+ 1:]
			# print(bag_spec, ":", num_of_bags, bag_colour)
			new_bags.append([num_of_bags, bag_colour])
	return new_bags

# print(count_bags_inside(test_bag))



def count_bags(bag):
	other_test_bags = [bag,]
	colors_tested = []
	bag_count_dict = {}
	while sorted(other_test_bags) != sorted(colors_tested):
		for test_bag in other_test_bags:
			if test_bag not in colors_tested:
				if 'other' not in test_bag:
					new_bags = count_bags_inside(test_bag)
					bags = [b for a,b in new_bags]
					# counts = [a for a,b in new_bags]
					bag_count_dict.update({b:a for a,b in new_bags})
					# other_test_bags += bags
					# other_test_bags = list(set(other_test_bags))
				else:
					counts = [0,]
					bags = ['none']

				colors_tested += [test_bag,]
			
				# print(test_bag, ": ", bags, counts)
	return bag_count_dict

def sum_next_level_down(bag_count_dict):
	total = 0
	for color, count in bag_count_dict.items():
		total += count
	return count

def count_the_bags(starting_bag):
	bag_count_dict = count_bags(starting_bag)
	count = sum_next_level_down(bag_count_dict)
	return count + count * count_the_bags()

			
