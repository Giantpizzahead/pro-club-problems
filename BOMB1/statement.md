Listen up, Agent 47. Our officers just found $100$ bombs laying on a table. Apparantly someone clicked a mission on a book, and the bombs just spawned in. Anyways, we need you to help us defuse them.

It looks like there are $3$ wires on each bomb. We'll list the colors to you, one bomb at a time, and you need to tell us which wire to cut. There should be a list of instructions somewhere.

Be quick!

#### BOMB 1 (INPUT)
```text
red
blue
white
```

#### BOMB 1 (OUTPUT)
```text
Cut wire 3
```

#### BOMB 2 (INPUT)
```text
yellow
yellow
yellow
```

#### BOMB 2 (OUTPUT)
```text
Cut wire 2
```

The rest of the bombs will be hidden until you submit a solution.

#### BOMB DEFUSAL MANUAL

Only the **first** correct wire needs to be cut to defuse the bomb (the first instruction that matches). Wire ordering begins with the first on the top. Follow the instructions starting at the top, and working your way down.

* If there are exactly 0 red wires, cut the 2nd wire.
* If the 3rd wire is white, cut the 3rd wire.
* If there is more than 1 blue wire, cut the 1st wire.
* Cut the 3rd wire.

Credit to [KTANE](https://keeptalkinggame.com/) for this problem idea!