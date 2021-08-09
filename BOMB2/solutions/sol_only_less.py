wires = ['XXX']
cnt = {}
rules = 0

for i in range(20):
    w = input().strip()
    wires.append(w)
    if w not in cnt:
        cnt[w] = 0
    cnt[w] += 1

def add_key(k):
    global rules
    rules += 1
    if k not in cnt:
        cnt[k] = 0

def cut_wire(w):
    print('Cut wire ' + str(w))
    exit(0)

add_key('red')
if cnt['red'] < 1: cut_wire(4)
add_key('gold')
if cnt['gold'] < 1: cut_wire(9)
add_key('lime')
if cnt['lime'] < 2: cut_wire(12)
cut_wire(1)