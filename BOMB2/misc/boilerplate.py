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
    print(rules)
    # print('Cut wire ' + str(w))
    # print('(On rule ' + str(rules) + ')')
    exit(0)
