import random
import subprocess

'''
Distribution:
{881: 10, 403: 6, 1093: 5, 1337: 4, 968: 3, 998: 3, 140: 2, 363: 2, 200: 2, 192: 2, 385: 2, 1025: 2, 1110: 2, 131: 1, 59: 1, 235: 1, 81: 1, 24: 1, 138: 1, 12: 1, 222: 1, 261: 1, 63: 1, 274: 1, 117: 1, 68: 1, 35: 1, 204: 1, 106: 1, 199: 1, 210: 1, 314: 1, 420: 1, 263: 1, 191: 1, 313: 1, 243: 1, 294: 1, 357: 1, 391: 1, 395: 1, 378: 1, 632: 1, 495: 1, 496: 1, 542: 1, 730: 1, 483: 1, 524: 1, 607: 1, 508: 1, 556: 1, 686: 1, 615: 1, 638: 1, 654: 1, 655: 1, 659: 1, 807: 1, 763: 1, 742: 1, 789: 1, 1028: 1, 1012: 1, 1100: 1, 949: 1, 1239: 1, 1078: 1}
'''

random.seed(23427238)

colors = ['charcoal', 'shamrock', 'marmalade', 'coffee', 'sand', 'azure', 'gold', 'navy', 'gray', 'wood', 'wine', 'red', 'obsidian', 'crepe', 'lime', 'arctic', 'chiffon', 'frost', 'iris', 'pear', 'latte', 'brick', 'watermelon', 'violet', 'cloud', 'rouge', 'yellow', 'carrot', 'oyster', 'sky', 'emerald', 'lemon', 'blood', 'corn', 'purple', 'blue', 'pickle', 'ruby', 'iron', 'chocolate', 'jade', 'hazelnut', 'penny', 'peach', 'flint', 'tiger', 'white', 'fire', 'marigold', 'scarlet', 'basil', 'plum', 'seaweed', 'berry', 'pink', 'squash', 'lapis', 'tan', 'cherry', 'rosewood', 'black', 'rose', 'lead', 'pearl', 'orchid', 'cotton', 'tortilla', 'crimson', 'shortbread', 'bone', 'silver', 'porcelain', 'coral', 'fern', 'ivory', 'green', 'fawn', 'candy', 'orange', 'teal', 'coconut', 'macaroon', 'rust', 'sage', 'banana', 'stone', 'cobalt', 'granola', 'amethyst', 'dijon', 'bubblegum', 'hickory', 'bronze', 'honey', 'pineapple', 'sandstone', 'daisy', 'blush', 'ash', 'apricot', 'brown', 'magenta', 'butter', 'caramel', 'buttermilk', 'grape', 'eggplant']
weights = []

def gen_bomb(fin, bomb_num):
    C = len(colors)

    # Generate biased_colors
    weights = [0 for _ in range(C)]
    W = random.randint(1, 20)
    # Account for less than restrictions
    if bomb_num > 90:
        W *= 4
        weights[11] = 5
        weights[6] = 5
        weights[14] = 9
    elif bomb_num > 75:
        W *= 3
        weights[11] = 3
        weights[6] = 3
    elif bomb_num > 40:
        W *= 2
        weights[11] = 1

    for i in range(W):
        weights[random.randrange(0, C)] += 1
    biased_colors = []
    for i in range(C):
        for j in range(weights[i]):
            biased_colors.append(colors[i])
    
    wires = [random.choice(biased_colors) for _ in range(20)]
    for w in wires:
        fin.write(w + '\n')

i = 1
triggered = {}
while i <= 100:
    fin = open('subtasks/main/{:03}.in'.format(i), 'w')
    gen_bomb(fin, i)
    fin.close()

    fin = open('subtasks/main/{:03}.in'.format(i), 'r')
    # See which rule is triggered
    rule_num = int(subprocess.run(['python3', './solutions/sol.py'], stdin=fin, capture_output=True).stdout)
    print(i, rule_num)
    if rule_num not in triggered:
        triggered[rule_num] = 0
    if abs(i*13 - rule_num) >= 200:
        # Must get a better rule
        i -= 1
    else:
        triggered[rule_num] += 1
    fin.close()

    i += 1

print('Test cases:')
print({k: v for k, v in sorted(triggered.items(), key=lambda item: -item[1])})
