import string

priorities = list(string.ascii_lowercase)
priorities.insert(0, 0)

# data = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw"""
# data = data.split("\n")

with open("input.txt") as f:
    data = f.read().split("\n")
data = data[:-1]

total = 0

# Part 1
for line in data:
    # Split line in half
    mid = int(len(line)/2)
    first_half, second_half = set(line[:mid]), set(line[mid:])

    # Find items in both compartments
    in_both = first_half.intersection(second_half)
    for item in in_both:
        # Add up the priorities
        total += priorities.index(item.lower())
        if item.isupper():
            total += 26

print(total)

# Part 2
total = 0
chunk_size = 3
for i in range(0, len(data), chunk_size):
    chunk = data[i : i + chunk_size]
    first = set(chunk[0])
    second = set(chunk[1])
    third = set(chunk[2])

    in_all = set.intersection(first, second, third)
    for item in in_all:
        # Add up the priorities
        total += priorities.index(item.lower())
        if item.isupper():
            total += 26

print(total)
