Farmer John's field has a fence with $N$ sections, numbered from $1$ to $N$. The section $i$ is initially painted in color $c_i$. Currently the fence has a bunch of different colors, which FJ doesn't like - he wants all sections of the fence to be painted in the same color.

Farmer John has an integer painting capacity $K$. On one day, FJ can do the following repainting process, consisting of two steps:

1. He chooses two integers $l$ and $r$ such that $1 \leq l \leq r \leq n$ and $r-l+1=K$.
2. For each fence section $i$ such that $l \leq i \leq r$, FJ can either repaint it with any color he wants, or ignore it and let it keep its current color.

Note that in the same day FJ can use different colors to repaint different sections of the fence.

Farmer John is lazy, so he wants to know the minimum number of days needed to repaint the fence so that all sections become the same color.

#### INPUT FORMAT

The first line of input contains two space-separated integers $N$ and $K$ ($1 \leq K \leq N \leq 10^5$).

The second line of input contains $N$ space-separated integers. The $i$-th of these integers denotes $c_i$ ($1 \leq c_i \leq 100$), the color which fence section $i$ is initially painted in.

#### OUTPUT FORMAT

Output one line with a single integer: The minimum # of days FJ needs to make all fence sections have the same color.

#### SAMPLE INPUT
```text
10 3
1 3 3 1 2 1 3 3 3 3
```

#### SAMPLE OUTPUT
```text
2
```

#### EXPLANATION

FJ can paint the first fence section with color 3 on the first day. Then, he can paint sections 4, 5, and 6 with color 3 on the second day.

#### SCORING

* Test cases 2-5 satisfy $K=1$.

* Test cases 6-10 satisfy no additional constraints.