import sys

def score(x):
    print(x)
    exit(0)

output_balanced = input().strip()

answer_path = sys.argv[2]
with open(answer_path, 'r') as fans:
    answer_balanced = fans.readline().strip()
    if output_balanced != answer_balanced:
        score(0)
    # If got this far, balanced answer is correct
    if answer_balanced == "YES":
        score(1)
    # Check if min number deletions is right (if bonus)
    answer_count = int(fans.readline())
    if answer_count == -1:
        score(1)
    output_count = int(input())
    if output_count == answer_count:
        score(1)
    else:
        score(0)
