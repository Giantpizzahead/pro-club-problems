a = input().strip()
b = input().strip()
c = input().strip()

# Rule 1
red = 0
if a == 'red': red += 1
if b == 'red': red += 1
if c == 'red': red += 1
if red == 0:
    print('Cut wire 2')
    exit(0)

# Rule 2
if c == 'white':
    print('Cut wire 3')
    exit(0)

# Rule 3
blue = 0
if a == 'blue': blue += 1
if b == 'blue': blue += 1
if c == 'blue': blue += 1
if blue > 1:
    print('Cut wire 1')
    exit(0)

# Rule 4
print('Cut wire 3')
exit(0)
