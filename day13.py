import numpy as np
# timestamp = 1007268
buses = [17,'x','x','x','x','x','x',41,'x','x','x','x','x','x','x','x','x',937,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',13,'x','x','x','x',23,'x','x','x','x','x',29,'x',397,'x','x','x','x','x',37,'x','x','x','x','x','x','x','x','x','x','x','x',19]

# # timestamp = 939
# # buses = [7,13,'x','x',59,'x',31,19]

# # Part 1
# v_buses = []
# v_waits = []

# for idx, bus in enumerate(buses):
# 	if bus == 'x':
# 		continue
# 	else:
# 		bus = int(bus)

# 		next_catch = bus*(1 + timestamp//bus)
# 		wait = next_catch - timestamp

# 		v_buses.append(bus)
# 		v_waits.append(wait)

# 	print(bus, next_catch, wait, wait*bus)

# idx_min_wait = np.argmin(v_waits)
# bus, wait = v_buses[idx_min_wait], v_waits[idx_min_wait]
# print("Part 1: ", bus, wait, bus*wait)

x='x'
buses = [17,x,13,19]
# buses = [7,13,x,x,59,x,31,19]
# buses = [67,7,59,61]
# buses = [67,x,7,59,61]
# buses = [1789,37,47,1889]
buses = [17,'x','x','x','x','x','x',41,'x','x','x','x','x','x','x','x','x',937,'x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x',13,'x','x','x','x',23,'x','x','x','x','x',29,'x',397,'x','x','x','x','x',37,'x','x','x','x','x','x','x','x','x','x','x','x',19]

v_buses = [a for a in buses if a!=x]

bus_offsets = {}
offset_buses = {}
for idx, bus in enumerate(buses):
	if bus == 'x':
		continue
	else:
		bus_offsets[bus] = idx
		offset_buses[idx] = bus
# print(bus_offsets)
print(offset_buses)
print(v_buses)

iter_limit = 1000000

def bus_wait(time, bus):
	next_catch = bus * (1 + time//bus)
	wait = next_catch - time
	return wait


header = ["time",]
header += [f"bus {a:d}" for a in v_buses]
header = [f"{entry:^8}" for entry in header]
# print(header)
success = False
# for iteration in range(iter_limit):
# t = 100000000000000
t = v_buses[0]
delta_t = v_buses[0]
iter_count = 0

while not success:
	# results = ['D' if not (t % bus) else '.' for bus in v_buses ]
	# line_out = [f"{t:^8}", ] + [f"{a:^8}" for a in results]
	# print(line_out)
	# t += v_buses[0]
	iter_count += 1
	for idx in range(1, len(v_buses)): # first bus is guaranteed
		next_bus = v_buses[idx]
		offset = bus_offsets[next_bus]
		iter_count += 1
		if (t + offset) % next_bus == 0:
			# skip to next iteration
			if next_bus == v_buses[-1]:
				print(f"starting time={t} works at iteration {iter_count}")
				success = True
		else:
			t += np.lcm.reduce(v_buses[0:idx])
			break



# t = 0
# iter_count = 0
# success = False
# while not success:
# # 	# results = ['D' if not (t % bus) else '.' for bus in v_buses ]
# # 	# line_out = [f"{t:^8}", ] + [f"{a:^8}" for a in results]
# # 	# print(line_out)
# 	t += v_buses[0]
# 	iter_count += 1
# 	print(iter_count, t)
# 	for next_bus in v_buses[1:]: # first bus is guaranteed
# 		offset = bus_offsets[next_bus]
# 		iter_count += 1
# 		if (t + offset) % next_bus == 0:
# 			# first two align properly
# 			starting_offset = t
# 			success = True
# 			print('hooray')
# 			break

# # 			if next_bus == v_buses[-1]:
# # 				print(f"starting time={t} works at iteration {iter_count}")
# # 				success = True
# # 		else:
# # 			# t += offset
# # 			break

# print(starting_offset)
# print(np.lcm.reduce(np.array(v_buses[1:])))



