import numpy as np

def find_2_match():
	with open('problem01_input.txt', 'r') as f:
		lines = f.readlines()
		entries = np.array(lines, dtype=int)
		N_entries = len(entries)
		for idx_outer in range(N_entries):
			for idx_inner in range(idx_outer, N_entries):
				# print(idx_outer, idx_inner)
				a = entries[idx_outer]
				b = entries[idx_inner]
				if a + b == 2020:
					print(a*b)
					return a*b

# find_2_match()

def find_3_match():
	with open('problem01_input.txt', 'r') as f:
		lines = f.readlines()
		entries = np.array(lines, dtype=int)
		N_entries = len(entries)
		for idx0 in range(N_entries):
			for idx1 in range(idx0, N_entries):
				for idx2 in range(idx1, N_entries):

					a = entries[idx0]
					b = entries[idx1]
					c = entries[idx2]
					if a + b + c == 2020:
						print(a*b*c)
						return a*b*c

find_3_match()
