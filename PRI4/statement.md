The time limit for all challenge problems is 1 second, unless otherwise stated. Java gets x1.5 the time limit, and Python gets x2.

The memory limit for all challenge problems is 64 MB, unless otherwise stated.

Update: For this problem, the time limit for Python has been extended to 5 seconds.

<hr>

A terrible new disease, COWVID-19, has begun to spread among cows worldwide. Farmer John is trying to take as many precautions as possible to protect his herd from infection.

Farmer John's $N$ cows, conveniently numbered $1...N$, are located at distinct points on the two-dimensional field. Having read about the importance of "social distancing", Farmer John wants to maximize $D$, where $D$ is the Euclidean distance between the two closest cows. For example, if the two closest cows on Farmer John's field are at $(2, 3)$ and $(5, 7)$, then $D=5$.

The Euclidean distance between two points $(x_1, y_1)$ and $(x_2, y_2)$ is just the straight line distance between the points. Formally, the distance is equal to $\sqrt{(x_1-x_2)^2 + (y_1-y_2)^2}$.

Farmer John has recently acquired a special "isolation stall", which can be used to isolate exactly one cow from the rest of the herd. Whichever cow FJ chooses to put into this stall is effectively removed from the field.

Please determine **which cow Farmer John should remove** so that the resulting value of $D$ is as large as possible. If there are multiple cows that achieve this largest value, output the one with the smallest number. Farmer John cannot move any of the existing cows (except that one that he places in the isolation stall).

#### INPUT FORMAT

The first line of input contains a single integer $N$.

The next $N$ lines each contain two integers $x_i$ and $y_i$, indicating that cow number $i$ is located at $(x_i, y_i)$. The info for cow 1 is given first, followed by cow 2, then 3, and so on.

#### OUTPUT FORMAT

Output a single integer: The number of the cow that Farmer John should remove so that the resulting value of $D$ is as large as possible. If there are multiple cows that achieve this largest value, output the one with the smallest number.

#### CONSTRAINTS

$3 \leq N \leq 200$

$-10{,}000 \leq x_i, y_i \leq 10{,}000$

The locations of all cows will be distinct.

#### SAMPLE INPUT
```text
5
1 4
4 1
1 2
4 4
2 1
```

#### SAMPLE OUTPUT
```text
3
```

#### EXPLANATION

There are $5$ cows on Farmer John's field. The visual below shows the positions of the cows.

<img src="https://i.ibb.co/ZxNWsdc/sample.png" alt="Sample Input Visual" style="display: block; margin: auto; width: min(100%, 400px);">

Removing either cow $3$ or cow $5$ would result in $D=2$, which is the maximum possible value of $D$. Since the cow with the smallest number should be outputted in case of a tie, $3$ is the answer.

Tip: Since $N \leq 200$, a solution with a cubic time complexity - sometimes written as $O(N^3)$ - should run within the time limit. In general, a computer can perform roughly 100 million operations per second. Since $200^3$ is less than 100 million, solutions with triple-nested loops should run in time.

(The only change in the bonus is increased constraints.)