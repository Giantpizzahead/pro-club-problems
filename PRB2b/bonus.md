#### BONUS (15 points)

After looking over her mock test, Eve realizes she actually went over the time limit by a lot more than she originally thought! Now, in order to finish in time, she will need to skip $K$ questions instead of just one.

Please help Eve determine the maximum possible score she can get on the CS exam if she is now forced to skip $K$ questions.

#### CONSTRAINTS

$2 \leq N \leq 100$

$0 \leq K \leq N$
(The number of questions Eve needs to skip will be in the range $0...N$.)

The number of points each question is worth will be in the range $1...100$.

#### INPUT FORMAT

To be consistent with the base problem's input format, the first 2 lines of input remain the same.

The third line of input contains a single integer $K$, the number of questions that Eve needs to skip.
($K=1$ for all test cases in the base problem.)

#### OUTPUT FORMAT

The output format is the same as in the base problem.

#### SAMPLE INPUT
```text
4
20 25 10 25
2
```

#### SAMPLE OUTPUT
```text
50
```

#### NOTES

As a preview of what's to come, the final test case of this bonus will have special constraints. In the final test case, $N=200{,}000$, and the point value of each question will be in the range $1...10^9$.

To get your code accepted for the final test case, you will need not just a *correct* solution, but an *efficient* one as well. Also note that the answer may not fit into a 32-bit integer!

Don't worry too much if you can't get the final test case; just skip it for now. In general, writing correct code is more important than writing efficient code. Future challenge problems will help guide you towards writing both correct and efficient programs.

(With that being said... here's a very subtle hint: The concept of *sorting* may help you with solving the final test case.)