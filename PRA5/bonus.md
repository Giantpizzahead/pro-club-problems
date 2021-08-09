#### BONUS (20 points)

Now Farmer John knows how long it will take him to complete the sorting, but he realizes that this info doesn't help much on its own. After all, what good is a time estimate if you don't know the actual steps to take?

Please fix this terrible condundrum for Farmer John; help him find a sequence of instructions that sorts the cows in the minimum number of time steps.

#### INPUT FORMAT

The input format remains the same.

#### OUTPUT FORMAT

The first line should contain a single integer, $K$, giving the minimum number of time steps required to sort the cows.

The second line should contain $K$ space-separated integers, $c_1,c_2,...,c_K$, each in the range $1...N-1$. Furthermore, if in the $i$-th time step FJ instructs the cow facing him to move $c_i$ paces down the line, then after $K$ time steps the cows should be in sorted order.

If there are multiple optimal instruction sequences, your program may output any of them.

#### SAMPLE INPUT
```text
4
1 2 4 3
```

#### SAMPLE OUTPUT
```text
3
2 2 3
```