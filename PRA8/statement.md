You are given the layout of a maze, and your task is to determine the length of the shortest path from start to end. You can walk left, right, up and down.

#### INPUT FORMAT

The first line of input contains two integers $N$ and $M$: The height and width of the layout.

The next $N$ lines of input each contain $M$ characters describing the maze. Each character is either '.' (floor), '#' (wall), 'A' (start), or 'B' (end). There is exactly one A and one B in the input.

#### OUTPUT FORMAT

Output one integer: The length of the shortest path from start to end. If there is no path, output $-1$.

#### CONSTRAINTS

$1 \leq N, M \leq 1{,}000$

#### SAMPLE INPUT 1
```text
5 8
########
#.A#...#
#.##.#B#
#......#
########
```

#### SAMPLE OUTPUT 1
```text
9
```

#### EXPLANATION 1

The shortest path is marked with '*' characters in the diagram below.

```text
########
#*A#...#
#*##.#B#
#******#
########
```

#### SAMPLE INPUT 2
```text
4 4
....
B.##
.#.A
#...
```

#### SAMPLE OUTPUT 2
```text
-1
```

#### EXPLANATION 2

The path cannot go outside of the grid, so there is no path from A to B.