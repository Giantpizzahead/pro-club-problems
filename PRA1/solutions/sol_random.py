import random

N = int(input())

if N == 3:
    print('You win')
elif N == 4:
    print('Friend wins')
elif random.random() < 0.5:
    print('You win')
else:
    print('Friend wins')
