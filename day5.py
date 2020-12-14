import numpy as np

seat_code = 'FBFBBFFRLR'

tests = {	'FBFBBFFRLR': {'row' : 44, 'col': 5, 'seat_ID': 357},
			'BFFFBBFRRR': {'row' : 70, 'col': 7, 'seat_ID': 567},
			'FFFBBBFRRR': {'row' : 14, 'col': 7, 'seat_ID': 119},
			'BBFFBBFRLL': {'row' : 102, 'col': 4, 'seat_ID': 820},
		}

def find_seat_vals(seat_code):
	min_row = 0
	max_row = 127

	min_col = 0
	max_col = 7

	while len(seat_code):
		key = seat_code[0]

		# print(min_row, max_row, min_col, max_col)

		if key == 'F':
			max_row = (min_row + max_row + 1) // 2 - 1
		elif key == 'B':
			min_row = (min_row + max_row - 1) // 2 + 1

		if key == 'L':
			max_col = (min_col + max_col + 1) // 2 - 1
		elif key == 'R':
			min_col = (min_col + max_col - 1) // 2 + 1

		seat_code = seat_code[1:]

	if min_col == max_col:
		if min_row == max_row:
			seat_ID = min_row * 8 + min_col
			return min_row, min_col, seat_ID
		else:
			raise ValueError('Error: row mismatch!')
	else:
		raise ValueError('Error: col mismatch!')		

for test_code, test_vals in tests.items():
	try:
		row, col, seat_ID = find_seat_vals(test_code)
		if row == test_vals['row'] and col==test_vals['col'] and seat_ID == test_vals['seat_ID']:
			print(f"Test passed! row {row}, column {col}, seat ID {seat_ID}")
		else:
			print(f"Test failed!!")
	except ValueError as e:
		print(e)


# part 1:
input_file = 'day5_part1.txt'
with open(input_file, 'r') as f:
	lines = f.readlines()

lines = [line.strip() for line in lines]

max_seat_ID = 0

for seat_code in lines:
	try:
		row, col, seat_ID = find_seat_vals(seat_code)
		max_seat_ID = max(seat_ID, max_seat_ID)
	except ValueError as e:
		print(e)
		print(seat_code)

print("Part 1: ", max_seat_ID)


seat_ID_list = []
for seat_code in lines:
	try:
		row, col, seat_ID = find_seat_vals(seat_code)
		seat_ID_list.append(seat_ID)
	except ValueError as e:
		print(e)
		print(seat_code)

sorted_seats = np.array(sorted(seat_ID_list), dtype=np.int)
idx_my_seat = np.where(np.diff(sorted_seats) > 1)
print(sorted_seats[idx_my_seat] + 1) # 1 because of diff


res = [ele for ele in range(max(sorted_seats)+1) if ele not in sorted_seats] 
print(res)