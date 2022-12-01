elves = []

with open("input.txt") as f:
    this_elf = 0
    for line in f.readlines():
        if line == "\n":
            elves.append(this_elf)
            this_elf = 0
            continue
        this_elf += int(line)

# Prints elf with most calories (Part 1)
print(max(elves))

# Find total of top 3 elves (Part 2)
sorted_elves = list(reversed(sorted(elves)))

print(sorted_elves[0] + sorted_elves[1] + sorted_elves[2])
