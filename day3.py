with open('day3_part1_input.txt', 'r') as f:
	lines = f.readlines()

lines = [line.strip() for line in lines]

def count_trees(right, down, verbose=False):
# delta_row = 1 # down positive
# delta_col = 3 # right positive
	delta_row = down
	delta_col = right
	start = (1, 1)

	n_rows = len(lines)
	n_cols = len(lines[0])

	row, col = start

	tree_count = 0
	while (row <= n_rows):
		line = lines[row-1]
		# Pattern extends far to the right
		if col > n_cols:
			col = col % n_cols
		character = line[col-1]
		if verbose: print(row, col, character)
		row += delta_row
		col += delta_col
		if character == '#':
			tree_count += 1

	return tree_count

part_1 = count_trees(3,1,True)
print('part 1:', part_1)

total = None
for (right, down) in [(1,1), (3,1), (5,1), (7,1),(1,2)]:
	tree_count = count_trees(right, down)
	print(tree_count)
	if total is None:
		total = tree_count
	else:
		total *= tree_count

print(total)
