import re

with open('misc/instructions.txt', 'r') as fin:
    text = fin.read()

text = re.sub(r'''\* ''', r'''''', text)
text = re.sub(r'''If there (?:is|are) exactly ([0-9]*) (.*) wires?, cut the ([0-9]*)[a-z]* wire.''', r'''add_key('\2')\nif cnt['\2'] == \1: cut_wire(\3)''', text)
text = re.sub(r'''If there (?:is|are) more than ([0-9]*) (.*) wires?, cut the ([0-9]*)[a-z]* wire.''', r'''add_key('\2')\nif cnt['\2'] > \1: cut_wire(\3)''', text)
text = re.sub(r'''If there (?:is|are) less than ([0-9]*) (.*) wires?, cut the ([0-9]*)[a-z]* wire.''', r'''add_key('\2')\nif cnt['\2'] < \1: cut_wire(\3)''', text)
text = re.sub(r'''If the ([0-9]*)[a-z]* wire is (.*), cut the ([0-9]*)[a-z]* wire.''', r'''add_key('none')\nif wires[\1] == '\2': cut_wire(\3)''', text)
text = re.sub(r'''Cut the ([0-9]*)[a-z]* wire.''', r'''add_key('none')\ncut_wire(\1)''', text)

with open('misc/boilerplate.py', 'r') as fin:
    boilerplate = fin.read()

with open('solutions/sol.py', 'w') as fout:
    fout.write(boilerplate + '\n')
    fout.write(text)
