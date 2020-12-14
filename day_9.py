import numpy as np



def get_data(input_file):
	with open(input_file, 'r') as f:
		lines = f.readlines()

	number_list = np.array([np.float64(line.strip()) for line in lines])
	return number_list


def find_invalid(number_list, preamble_length):
	for idx in range(preamble_length, len(number_list)): 
		pair_list = number_list[idx - preamble_length : idx]

		valid_numbers = []
		for ii in range(len(pair_list)):
			for jj in range(ii, len(pair_list)):
				num_sum = pair_list[ii] + pair_list[jj]
				valid_numbers.append(num_sum)
		valid_numbers = sorted(list(sorted(valid_numbers)))

		# Next number after pair_list
		test_number = number_list[idx]

		# print(test_number, valid_numbers)
		if test_number not in valid_numbers:
			print(f"Found invalid number {test_number} on line {idx + 1}")  # line number is 1-indexed
			# print(valid_numbers)
			return test_number

# Test data
number_list = get_data('day_9_test_input.txt')
invalid_num = find_invalid(number_list, 5)

# Part 1
number_list = get_data('day9_input.txt') 
invalid_num = find_invalid(number_list, 25)


def find_sum(target):
	for idx_start in range(len(number_list)):
		for idx_end in range(idx_start+1, len(number_list)):
			list_slice = number_list[idx_start:idx_end]
			num_sum = np.sum(list_slice)
			if num_sum == target:			
				print(f"Found sum: ", list_slice)  
				# print(valid_numbers)
				return min(list_slice) + max(list_slice)

minmax_sum = find_sum(invalid_num)
print(minmax_sum)