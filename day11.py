from scipy.signal import convolve2d
import numpy as np

input_file = 'day11_input.txt'
input_file = 'day11_test_1.txt'
with open(input_file, 'r') as f:
	lines = f.readlines()

lines = [line.rstrip() for line in lines]



# Convert L to 1 and . to 0
chairs = np.array([[1 if x=='L' else 0 for x in line] for line in lines])
floor = np.array([[1 if x=='.' else 0 for x in line] for line in lines])

# Pad to give it a border?
chair = np.pad(chairs, ((1, 1), (1, 1)), 'constant', constant_values=((0,0),(0,0)))
floor = np.pad(floor, ((1, 1), (1, 1)), 'constant', constant_values=((0,0),(0,0)))

# Initially no occupied spaces
prev_layout = np.zeros_like(floor)

# def floor_mtx_to_symbol(floor_mtx):
	# return [['.' if x==1 else 0 for x in line] for line in floor_mtx]
# print(floor_mtx_to_symbol(floor))


# Part 1
for iteration in range(1000):
	neighbour_sum = convolve2d(prev_layout,np.ones((3,3),dtype=int),'same') - prev_layout
	
	becomes_filled = (neighbour_sum == 0) & (floor == 0) & (prev_layout == 0) & (chair == 1)
	becomes_empty  = (neighbour_sum >= 4) & (floor == 0) & (prev_layout == 1) & (chair == 1)

	new_layout = prev_layout.copy()
	new_layout[becomes_filled] = 1
	new_layout[becomes_empty] = 0
	if new_layout.sum() == prev_layout.sum():
		if iteration:
			print(f"Iter {iteration}, sum = {new_layout.sum()}")
			break
	prev_layout = new_layout


# Part 2

def get_location_sum(chair_mtx, floor_mtx, occupant_mtx, r, c):
	vis_neighbour_sum = 0
	# North
	r_offset = -1
	c_offset = 0

	# starting from N, going CW
	# row_offset, col_offset
	offset_directions = [(-1,0), (-1, 1), (0, 1), (1,1), (1, 0), (1, -1), (0, -1), (-1, -1)]

	row_min, col_min = 0,0
	row_max, col_max = np.shape(occupant_mtx)
	row_max -= 1
	col_max -= 1

	for offset_direction in offset_directions:
		r_offset, c_offset = offset_direction
		# Starting from (r,c) initial space
		row = r
		col = c
		while True:
			row = row + r_offset
			col = col + c_offset
			if (row < row_min) or (row > row_max) or (col < col_min) or (col > col_max):
				break

			if floor_mtx[row, col]:
				if occupant_mtx[row, col]:
					print(f"ERROR! Shouldn't have a floor spot occupied! {floor_mtx[row, col]},{occupant_mtx[row, col]}")
				else:
					# floor spot, skip and move on
					continue
			elif chair_mtx[row, col] and not occupant_mtx[row, col]:
				# See a chair and it's empty, done with this direction
				break
			elif chair_mtx[row, col] and occupant_mtx[row, col]:
				# I can see a neighbour in this direction
				vis_neighbour_sum += 1
				break
			else:
				print(f"Error! Shouldn't be able to be in this state! {floor_mtx[row, col]},{occupant_mtx[row, col]},{chair_mtx[row, col]}")



	return vis_neighbour_sum

def get_neighbour_sum(occupant_mtx, floor_mtx, chair_mtx):
	rows, cols = np.shape(occupant_mtx)
	neighbour_sum = np.zeros_like(occupant_mtx)
	for r in range(rows):
		for c in range(cols):
			if floor_mtx[r,c]:
				pass
			else:
				neighbour_sum[r,c] = get_location_sum(chair_mtx, floor_mtx, occupant_mtx, r, c)

	return neighbour_sum



input_file = 'day11_input.txt'
# input_file = 'day11_test_1.txt'
with open(input_file, 'r') as f:
	lines = f.readlines()

lines = [line.rstrip() for line in lines]

# Initially no occupied spaces
# Convert L to 1 and . to 0
chair = np.array([[1 if x=='L' else 0 for x in line] for line in lines])
floor = np.array([[1 if x=='.' else 0 for x in line] for line in lines])
# Don't need padding
prev_layout = np.zeros_like(floor)

# def floor_mtx_to_symbol(floor_mtx):
	# return [['.' if x==1 else 0 for x in line] for line in floor_mtx]
# print(floor_mtx_to_symbol(floor))

# Part 2
for iteration in range(10000):
	neighbour_sum = get_neighbour_sum(prev_layout, floor, chair)
	
	becomes_filled = (neighbour_sum == 0) & (floor == 0) & (prev_layout == 0) & (chair == 1)
	becomes_empty  = (neighbour_sum >= 5) & (floor == 0) & (prev_layout == 1) & (chair == 1)

	new_layout = prev_layout.copy()
	new_layout[becomes_filled] = 1
	new_layout[becomes_empty] = 0
	if new_layout.sum() == prev_layout.sum():
		if iteration:
			print(f"Iter {iteration}, sum = {new_layout.sum()}")
			break
	prev_layout = new_layout



