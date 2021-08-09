Bo is planning to surprise his friends with $N$ bags ($1 \leq N \leq 100$) of sweet candies! Each bag already has some number of candies in it.

Bo's friends are easily angered, especially when they don't get enough candy. So, Bo would like to add additional candies to the bags so that every bag has at least $K$ candies in it ($1 \leq K \leq 100$). Due to sanitary reasons, Bo cannot take any candies out of the bags; he can only put more candies in.

Luckily, Bo has an infinite supply of candies, but he wants to save as many for himself as possible. What is the minimum # of candies he needs to add, so that every bag has at least $K$ candies?

#### INPUT FORMAT

The first line of input contains two space-separated integers $N$ and $K$.

The next line of input contains $N$ space-separated integers, giving the number of candies in the bags. These integers will be in the range $1 \ldots 100$.

#### OUTPUT FORMAT

Output one line containing a single integer: The smallest # of candies Bo needs.

#### SAMPLE INPUT
```text
5 7
2 8 7 6 15
```

#### SAMPLE OUTPUT
```text
6
```

#### EXPLANATION

There are $5$ bags, and Bo would like to place at least $7$ candies in each bag. The best solution is to place 5 candies into bag 1 and 1 candy into bag 4. This way, the # of candies in each bag becomes $[7, 8, 7, 7, 15]$. So, the answer is $5+1=6$.