import numpy as np

input_file = 'day8_test_input.txt'
input_file = 'day8_input.txt'

with open(input_file, 'r') as f:
	lines = f.readlines()

accumulator = 0
commands = []
values = []
for line in lines:
	cmd, val = line.strip().split(' ')
	commands.append(cmd)
	values.append(int(val))


command_idx = 0
print(commands, len(commands))
commands_execution_count = np.zeros(len(commands))

while True:
	if command_idx < len(commands):
		command = commands[command_idx]
		value = values[command_idx]
	else:
		print(f"Terminates with Accumulator = {accumulator}")
		break

	if commands_execution_count[command_idx]:
		print(f"Running idx={command_idx} a second time! Accumulator = {accumulator}")
		break

	commands_execution_count[command_idx] += 1	
	if command == 'nop':
		command_idx += 1
		continue
	elif command == 'acc':
		accumulator += value
		command_idx += 1
	elif command == 'jmp':
		command_idx += value

print("*" * 50)
# part 2
original_commands = commands.copy()

def run_program(commands, values):
	accumulator = 0
	command_idx = 0
	commands_execution_count = np.zeros(len(commands))

	while True:
		if command_idx < len(commands):
			command = commands[command_idx]
			value = values[command_idx]
		else:
			print(f"Terminates with Accumulator = {accumulator}")
			return 0

		if commands_execution_count[command_idx]:
			# print(f"Running idx={command_idx} a second time! Accumulator = {accumulator}")
			return -1

		commands_execution_count[command_idx] += 1	
		if command == 'nop':
			command_idx += 1
			continue
		elif command == 'acc':
			accumulator += value
			command_idx += 1
		elif command == 'jmp':
			command_idx += value

idx_nops = [idx for idx, x in enumerate(original_commands) if x == "nop"]
idx_jmps = [idx for idx, x in enumerate(original_commands) if x == "jmp"]


for idx_nop in idx_nops:
	commands = original_commands.copy()
	commands[idx_nop] = "jmp"
	ret_val = run_program(commands, values) 
	if ret_val == 0:
		print(f"Replace idx_nop = {idx_nop}, value = {values[idx_nop]}")

for idx_jmp in idx_jmps:
	commands = original_commands.copy()
	commands[idx_jmp] = "nop"
	ret_val = run_program(commands, values)
	if ret_val == 0:
		print(f"Replace idx_jmp = {idx_jmp}, value = {values[idx_jmp]}")


