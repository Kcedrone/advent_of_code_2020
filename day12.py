import numpy as np

input_file = 'day12_test.txt'
input_file = 'day12_input.txt'
with open(input_file, 'r') as f:
	lines = f.readlines()

lines = [line.rstrip() for line in lines]

east_sum = 0
north_sum = 0

wpt_n_offset = 1
wpt_e_offset = 10


def cosd(theta):
	return np.cos( theta * np.pi/180.0 )

def sind(theta):
	return np.sin( theta * np.pi/180.0 )

def tand(n, e):
	return np.arctan2(n, e) * 180.0 / np.pi

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.
    The angle should be given in degrees.
    """
    ox, oy = origin
    px, py = point

    qx = ox + cosd(angle) * (px - ox) - sind(angle) * (py - oy)
    qy = oy + sind(angle) * (px - ox) + cosd(angle) * (py - oy)
    return qx, qy

for line in lines:
	cmd = line[0]
	amnt = int(line[1:])

	wpt_n = north_sum + wpt_n_offset
	wpt_e = east_sum + wpt_e_offset
	hdg = tand(wpt_n_offset, wpt_e_offset)

	if cmd == 'F':
		delta_N = amnt * wpt_n_offset 
		delta_E = amnt * wpt_e_offset

		east_sum += delta_E
		north_sum += delta_N

	elif cmd == 'N':
		wpt_n_offset += amnt

	elif cmd == 'E':
		wpt_e_offset += amnt

	elif cmd == 'S':
		wpt_n_offset -= amnt

	elif cmd == 'W':
		wpt_e_offset -= amnt

	elif cmd == 'L':
		wpt_e_offset, wpt_n_offset = rotate((0,0), (wpt_e_offset, wpt_n_offset), amnt)

	elif cmd == 'R':
		wpt_e_offset, wpt_n_offset = rotate((0,0), (wpt_e_offset, wpt_n_offset), -amnt)

	else:
		raise ValueError(f"Invalid command {line}")

	# print(cmd, amnt, hdg, east_sum, north_sum, wpt_e_offset, wpt_n_offset)

print(east_sum, north_sum, abs(east_sum)+ abs(north_sum))

