# data = """2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8"""
# data = data.split("\n")

with open("input.txt") as f:
    data = f.read().split("\n")
data = data[:-1]


part_1_total = 0
part_2_total = 0
for line in data:
    elves_data = line.split(",")
    elves = []
    for elf in elves_data:
        this_elf = []
        this_elf.append(int(elf.split("-")[0]))
        this_elf.append(int(elf.split("-")[1]))
        elves.append(this_elf)

    elf_1_range = set(list(range(elves[0][0], elves[0][1] + 1)))
    elf_2_range = set(list(range(elves[1][0], elves[1][1] + 1)))
    intersect = list(set.intersection(elf_1_range, elf_2_range))
    if intersect == list(elf_2_range) or intersect == list(elf_1_range):
        part_1_total += 1
    if len(intersect) > 0:
        part_2_total += 1


print(part_1_total)
print(part_2_total)
