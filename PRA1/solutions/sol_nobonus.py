N = int(input())
# Get your cards
cards = list(map(int, input().split()))

has2N = False
for card in cards:
    if card == 2 * N:
        has2N = True

if has2N:
    print("You win")
else:
    print("Friend wins")
