The HHS Programming Club has just created a very impressive website containing a bunch of challenge problems. There are $N$ people who have completed a couple of these problems. Unfortunately, a crucial part of this system is missing: The leaderboard!

Given the names of the $N$ people and their current scores, please **output the current leaderboard**. This leaderboard should be sorted from highest to lowest score, and ties should be broken based on which name comes first in alphabetical order.

#### INPUT FORMAT

The first line of input contains a single integer $N$.

The next $N$ lines of input each contain the name and score of a person, separated by a single space. All names will consist of lowercase English letters, and they will be distinct.

#### OUTPUT FORMAT

Output $N$ lines, representing the current leaderboard. Each line should contain the name and score of a person, separated by a single space.

#### CONSTRAINTS

$1 \leq N \leq 100$

The name of each person will be at most $10$ characters long.
The score of each person will be in the range $[0, 10^9]$.

#### SAMPLE INPUT 1
```text
4
bob 200
diana 100
alice 199
carl 300
```

#### SAMPLE OUTPUT 1
```text
carl 300
bob 200
alice 199
diana 100
```

#### SAMPLE INPUT 2
```text
3
zebra 42
chicken 42
mouse 42
```

#### SAMPLE OUTPUT 2
```text
chicken 42
mouse 42
zebra 42
```

Tip: Don't be afraid to **search for help online** while doing the challenge problems! If you're not sure how to do something (...like sorting custom objects), chances are someone has already posted the answer to your question on StackOverflow.