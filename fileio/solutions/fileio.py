# Read from a file
fin = open('fileio.in', 'r')

# Parse the integer array & find the sum
N = int(fin.readline())
arr = fin.readline().strip().split()
# Convert each element in the array to an integer
for i in range(N):
    arr[i] = int(arr[i])
curr_sum = 0
for i in range(N):
    curr_sum += arr[i]

# Write to a file (don't forget to close it)
fout = open('fileio.out', 'w')
# Python can only write strings, so you must explictly cast to a string
# Make sure to add a newline too
fout.write(str(curr_sum) + '\n')
fout.close()
