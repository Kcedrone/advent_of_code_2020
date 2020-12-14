
import numpy as np
mask = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'
# mem[8] = 11
# mem[7] = 101
# mem[8] = 0

# test = 'abcd'
# print(test[::-1])


def apply_mask(mask_string, num):
	or_mask  = 0
	and_mask = 0
	for offset, elem in enumerate(mask_string[::-1]):
		if elem == '1':
			or_mask += 2<<offset
		if elem == '0':
			and_mask += 2<<offset


	or_mask = or_mask >> 1
	and_mask = and_mask >> 1
	and_mask = ~and_mask

	# print(and_mask)
	# print(or_mask)
	return (num | or_mask) & and_mask


for n in [11, 101, 0]:
	print(apply_mask(mask, n))

# import sys
# sys.exit(0)

input_file = 'day14_part1_.txt'
with open(input_file, 'r') as f:
	lines = f.readlines()

mem = {}

for line in lines:
	if 'mask' in line:
		mask = line.split("= ")[-1].rstrip()
		# print(mask)
	else:
		mem_addr = line.split("[")[-1].split("]")[0].strip()
		num = int(line.split("= ")[-1])

		masked_num = apply_mask(mask, num)
		mem.update({mem_addr : masked_num})

cumsum = 0
for k,v in mem.items():
	cumsum += v

print(cumsum)
