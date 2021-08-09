import random

random.seed(621535)

W = 20
N = 1336
colors = ['charcoal', 'shamrock', 'marmalade', 'coffee', 'sand', 'azure', 'gold', 'navy', 'gray', 'wood', 'wine', 'red', 'obsidian', 'crepe', 'lime', 'arctic', 'chiffon', 'frost', 'iris', 'pear', 'latte', 'brick', 'watermelon', 'violet', 'cloud', 'rouge', 'yellow', 'carrot', 'oyster', 'sky', 'emerald', 'lemon', 'blood', 'corn', 'purple', 'blue', 'pickle', 'ruby', 'iron', 'chocolate', 'jade', 'hazelnut', 'penny', 'peach', 'flint', 'tiger', 'white', 'fire', 'marigold', 'scarlet', 'basil', 'plum', 'seaweed', 'berry', 'pink', 'squash', 'lapis', 'tan', 'cherry', 'rosewood', 'black', 'rose', 'lead', 'pearl', 'orchid', 'cotton', 'tortilla', 'crimson', 'shortbread', 'bone', 'silver', 'porcelain', 'coral', 'fern', 'ivory', 'green', 'fawn', 'candy', 'orange', 'teal', 'coconut', 'macaroon', 'rust', 'sage', 'banana', 'stone', 'cobalt', 'granola', 'amethyst', 'dijon', 'bubblegum', 'hickory', 'bronze', 'honey', 'pineapple', 'sandstone', 'daisy', 'blush', 'ash', 'apricot', 'brown', 'magenta', 'butter', 'caramel', 'buttermilk', 'grape', 'eggplant']
print('# of colors: ' + str(len(colors)))
formats = [
    ['If there is exactly {} {} wire, cut the {} wire.', 'If there are exactly {} {} wires, cut the {} wire.'],
    ['If there is more than {} {} wire, cut the {} wire.', 'If there are more than {} {} wires, cut the {} wire.'],
    ['If there is less than {} {} wire, cut the {} wire.', 'If there are less than {} {} wires, cut the {} wire.'],
    'If the {} wire is {}, cut the {} wire.'
]
format_req = [
    [['n', 1, 20], 's', 'o'],
    [['n', 7, 19], 's', 'o'],
    [['n', 1, 2], 's', 'o'],
    ['o', 's', 'o']
]
format_weights = [125, 25, 1, 100]

temp_F = len(formats)
for i in range(temp_F):
    for j in range(format_weights[i]-1):
        formats.append(formats[i])
        format_req.append(format_req[i])

def gen_bomb(fin):
    wires = [random.choice(colors) for _ in range(3)]
    for w in wires:
        fin.write(w + '\n')

fout = open('misc/new_instructions.txt', 'w')
for i in range(N):
    while True:
        f_num = random.randrange(0, len(formats))
        if f_num != 2: break
    f = formats[f_num]
    v = []
    for x in format_req[f_num]:
        if x[0] == 'n':
            n = random.randint(x[1], x[2])
            if type(f) == list:
                if n == 1: f = f[0]
                else: f = f[1]
            v.append(str(n))
        elif x[0] == 'o':
            o = random.randint(1, 20)
            if o == 11 or o == 12 or o == 13: suff = 'th'
            elif o % 10 == 1: suff = 'st'
            elif o % 10 == 2: suff = 'nd'
            elif o % 10 == 3: suff = 'rd'
            else: suff = 'th'
            v.append(str(o) + suff)
        elif x[0] == 's':
            s = random.choice(colors)
            v.append(s)
    fout.write('* ' + f.format(*v) + '\n')
fout.write('* Cut the 1st wire.\n')
    
fout.close()
