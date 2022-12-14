import re, copy

# data = """
#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2"""
# data = data.split("\n")[1::]

with open("input.txt") as f:
    data = f.read().split("\n")
data = data[:-1]


def move_boxes(stacks: list, instruction_lines: list, reverse: bool) -> list:
    for instruction_line in instruction_lines:
        amount_to_move = int(
            re.search("(?<=move )(\d+)(?= from)", instruction_line).group(0)
        )
        starting_point = (
            int(re.search("(?<=from )(\d+)(?= to)", instruction_line).group(0)) - 1
        )
        ending_point = int(re.search("(?<=to )(\d+)", instruction_line).group(0)) - 1

        if reverse:
            items_removing = list(reversed(stacks[starting_point][0:amount_to_move]))
        else:
            items_removing = stacks[starting_point][0:amount_to_move]

        stacks[ending_point] = items_removing + stacks[ending_point]
        stacks[starting_point] = stacks[starting_point][amount_to_move:]
    return stacks


def replace_multiple_chars(chars: list, input: str, replacement_char: str):
    for char in chars:
        input = input.replace(char, replacement_char)
    return input


stack_lines = []
instruction_lines = []
doing_stacks = True
for line in data:
    if line == "":
        # Separator between stacks and instructions
        doing_stacks = False
        continue
    if doing_stacks:
        stack_lines.append(line)
    else:
        instruction_lines.append(line)

amount_of_stacks = int(re.findall("\d+", stack_lines[-1])[-1])

stacks = [[] for i in range(amount_of_stacks)]

for stack_line in stack_lines[:-1]:
    stack_line = [
        replace_multiple_chars(["[", "]", " "], stack_line[i : i + 4], "")
        for i in range(0, len(stack_line), 4)
    ]
    for col in stack_line:
        if col.replace(" ", "") == "":
            continue
        pos = stack_line.index(col)
        stacks[pos].append(col)
        stack_line[pos] = ""

p1_stacks = move_boxes(copy.copy(stacks), instruction_lines, True)
p2_stacks = move_boxes(copy.copy(stacks), instruction_lines, False)

output = ""
for stack in p1_stacks:
    output += stack[0].replace(" ", "")
print(output)
output = ""
for stack in p2_stacks:
    output += stack[0].replace(" ", "")
print(output)
