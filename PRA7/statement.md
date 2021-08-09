(Time limit: 2 seconds, Memory limit: 128 MB)

Lily has come across an array $A$ of $N$ integers in her computer science class. The teacher wants her to do some sort of statistics lab with the array, but Lily comes up with something better. She decides to ask $Q$ queries of the following form: **What is the mode of the subarray from $l_i$ to $r_i$?**

A subarray is a contiguous section of the whole array consisting of the elements at indices $l_i \ldots r_i$, inclusive. For example, if $A=[5, 5, 7, 8, 9]$, then the subarray from 2 to 4 would be $[5, 7, 8]$. The subarray from 4 to 5 would be $[8, 9]$.

The mode of an array is the most frequent element in the array. For example, the mode of the above array would be $5$, because it appears twice, while all other elements appear once. For this problem, if the most frequent element is not unique, output "many" as the answer to the query (without quotes).

Please help Lily write a program that will answer her queries efficiently.

#### INPUT FORMAT

The first line of input contains $N$ ($1 \leq N \leq 3\,000$). The next line of input contains $N$ space-separated integers, giving the elements of $A$. All elements are in the range $1 \ldots 3\,000$.

The next line of input contains $Q$ ($1 \leq Q \leq 3\,000$). The next $Q$ lines of input each describe a single query, in the form of two integers $l_i$ and $r_i$. The queries will all be valid ($1 \leq l_i \leq r_i \leq N$).

#### OUTPUT FORMAT

For each of the $Q$ queries, output a single line with an integer: The mode of the queried subarray. If the mode is not unique, output "many" instead, without quotes.

#### SAMPLE INPUT
```text
6
3 8 5 3 8 3
3
1 6
2 5
4 5
```

#### SAMPLE OUTPUT
```text
3
8
many
```

#### EXPLANATION

The given array is $[3, 8, 5, 3, 8, 3]$. There are $3$ queries:

* Mode in the range $1...6$ = Mode of $[3, 8, 5, 3, 8, 3]$ = 3
* Mode in the range $2...5$ = Mode of $[8, 5, 3, 8]$ = 8
* Mode in the range $4...5$ = Mode of $[3, 8]$ = many

#### SCORING

* Test cases 2-5 satisfy $Q=1$, and the one query is for the entire array. This means that you can ignore the queries, and just output the mode of the entire array.

* Test cases 6-8 satisfy $Q \leq 50$.

* Test cases 9-12 satisfy no additional constraints.