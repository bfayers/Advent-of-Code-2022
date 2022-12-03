# read the input file
lines = open("input.txt").readlines()

# initialize variables
chunk = []
chunks = []
max_sum = 0

# iterate through the lines of the input file
for line in lines:
  # if the line is empty, it marks the end of a chunk
  # so we sum the chunk and append it to the list of chunks
  if line.strip() == "":
    chunks.append(sum(chunk))
    chunk = []
  # otherwise, it's a number, so we add it to the current chunk
  else:
    chunk.append(int(line))

# sum the last chunk (if any)
if chunk:
  chunks.append(sum(chunk))

# find the maximum sum
max_sum = max(chunks)

# sort the chunks in descending order by sum
chunks.sort(reverse=True)

# sum the top three chunk sums
top_three_sum = sum(chunks[:3])

# print the maximum sum and the top three sum
print("Max sum:", max_sum)
print("Top three sum:", top_three_sum)

