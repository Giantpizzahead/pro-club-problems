#### BONUS (20 points)

This bonus is meant to be a tiebreaker. You are NOT expected to get all the points for it. Just try your best!

<hr>

The time limit for this problem is 1.5 seconds. [x1.5 for Java, x2 for Python]

After trying out Brackets for a while, Jake has realized that it's pretty much impossible to write such a long program without making errors. So, he has resorted to correcting his code after writing it.

Jake wants to correct his program by deleting a couple of characters from it, so that the resulting program is balanced. Here is an example of how Jake might fix a Brackets program:

```text
Original program = (([))
After deleting the [ character...
Balanced program = (())
```

Note that an empty Brackets program is technically balanced, so it's always possible for Jake to fix his program this way.

Before fixing his program, Jake would like to know how much time he'll need to invest to make the code balanced. If the Brackets program is not already balanced, please determine the **minimum number of deletions** Jake will have to make in order to make the program balanced.

#### INPUT FORMAT

The input format remains the same.

#### OUTPUT FORMAT

If $S$ is balanced, print "YES" on a single line. Do not print anything else.

Otherwise, the first line of output should contain the string "NO".
The second line of output should contain a single integer: The minimum number of deletions Jake needs to make to fix his Brackets program.

#### CONSTRAINTS

$1 \leq |S| \leq 300$

#### SCORING

* In test cases 11-14, the Brackets program will consist of only two characters '(' and ')'.
* Test cases 15-17 satisfy $|S| \leq 20$.
* Test cases 18-20 satisfy no further constraints.

In the base test cases, the second line of output will be completely ignored; your program will get an Accepted verdict no matter what that line contains (as long as it prints "YES" or "NO" correctly).

#### SAMPLE INPUT
```text
{{[}]}((())}
```

#### SAMPLE OUTPUT
```text
NO
2
```

#### EXPLANATION

One way Jake could fix the Brackets program while only deleting $2$ characters is by deleting the brackets at indexes $4$ and $9$ (one-indexed).

#### NOTES

Note that the constraints on the length of $S$ have been lowered for the bonus!

To avoid losing points on the main problem because of TLEs, add an if statement to only calculate the minimum # of deletions if the length of the Brackets program is less than a certain amount (and to use the solution for the base problem otherwise).

Some small hints for this bonus have been added; click the "Show Hints" button to see them.