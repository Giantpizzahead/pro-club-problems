N = int(input())

mine = list(map(int, input().split()))
friend = list(map(int, input().split()))

if len(mine) != N or len(friend) != N: exit(1)

while len(mine) > 0:
    maxMine = 0
    maxFriend = 0
    for x in mine:
        maxMine = max(x, maxMine)
    for x in friend:
        maxFriend = max(x, maxFriend)
    if maxMine == maxFriend:
        # Delete from both
        mine.remove(maxMine)
        friend.remove(maxFriend)
    elif maxMine > maxFriend:
        print("You win")
        exit(0)
    elif maxFriend > maxMine:
        print("Friend wins")
        exit(0)

print("Draw")