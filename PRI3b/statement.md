After constructing a triangle with her metal rods, Alice realized that she really liked when the rods had a length equal to a prime number. A prime number is an integer greater than $1$ that has only two factors: $1$ and the number itself. For example, the first 10 prime numbers are $[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]$.

Alice now has a clay rod of length $N$. She would like to stretch or compress this rod so that it has a length equal to a prime number.

Please help Alice find the **prime number that is the closest to $N$** (smallest distance), so that she can shape her clay rod as quickly as possible. The distance between two integers $a$ and $b$ is equal to $|a-b|$ (the absolute value of their difference). For example, the distance between $5$ and $7$ is $2$. If there are multiple prime numbers with the same distance, output the smallest one.

#### INPUT FORMAT

The only line of input contains a single integer $N$.

#### OUTPUT FORMAT

Output a single integer: The prime number that is the closest to $N$ (or the smallest one in case of a tie).

#### CONSTRAINTS

$2 \leq N \leq 10^9$

#### SCORING

* Test cases 1-6 satisfy $N \leq 10^5$.
* Test cases 7-10 satisfy no additional constraints.

#### SAMPLE INPUT 1
```text
27
```

#### SAMPLE OUTPUT 1
```text
29
```

#### EXPLANATION 1

The prime number that is the closest to $27$ is $29$, with a distance of $2$.

#### SAMPLE INPUT 2
```text
12
```

#### SAMPLE OUTPUT 2
```text
11
```

#### EXPLANATION 2

Both $11$ and $13$ are prime numbers with a distance of $1$ from $12$. Since the smallest prime number should be outputted in case of a tie, $11$ is the answer.

#### SAMPLE INPUT 3
```text
8161
```

#### SAMPLE OUTPUT 3
```text
8161
```

#### EXPLANATION 3

$8161$ is already prime, so it is the closest prime number (with a distance of $0$).