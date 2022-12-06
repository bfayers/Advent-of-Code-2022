with open("input.txt") as f:
    data = f.read()


def find_message_start_marker(data: str, size: int) -> int:
    for i in range(0, len(data)):
        this_slice = data[i : i + size]
        this_set = set(this_slice)
        if len(this_set) == size:
            # This is the first occurence of 4 characters in the string that are unique
            return i + size
            break


# Part 1
print(find_message_start_marker(data, 4))

# Part 2
print(find_message_start_marker(data, 14))
