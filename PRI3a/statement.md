The interweb is a very complicated place. Lots of webpages are being updated every day, and interweb links are everywhere. There are exactly $N$ webpages on the interweb. To make things easier, every webpage will be labeled with an integer in the range $1...N$. In addition, every webpage has exactly one link on it; this link goes to another one of the webpages on the interweb.

Jake is currently searching for answers to his math homework. His friend told him that he can find these answers on website $N$. Unfortunately, the structure of the interweb makes it quite hard to get to this website; all Jake can do is start at website $1$, and follow the one link that's on each website until he reaches website $N$.

Although Jake really wants these homework answers, he realizes that it may actually be faster to do the homework himself (if it takes too many links to get to the last website). Please help Jake decide what to do by telling him **how many links he will have to follow** to get from website $1$ to website $N$.

It is possible that Jake may never reach website $N$ by following the links - he could get stuck in an infinite loop. If this happens, output $-1$ as your answer.

#### INPUT FORMAT

The 1st line of input contains a single integer $N$, the number of webpages on the interweb.

The 2nd line of input contains $N$ space-separated integers, where the $i$th integer represents the location that the $i$th webpage links to.

#### OUTPUT FORMAT

Output a single integer: The number of links Jake will have to follow in order to get from the $1$st to the $N$th webpage (or $-1$ if Jake will get stuck in an infinite loop).

#### CONSTRAINTS

$2 \leq N \leq 5{,}000$

All website links are valid (the linked website number will be in the range $1...N$).

#### SCORING

For test cases 1-8 (worth 80% of the points), it is guaranteed that if Jake follows the chain of links, he will eventually get from website $1$ to website $N$.

For test cases 9-10 (worth 20% of the points), there are no additional constraints.

#### SAMPLE INPUT
```text
5
4 5 4 2 3
```

#### SAMPLE OUTPUT
```text
3
```

#### EXPLANATION

The following picture gives a visual representation of the websites in the sample input. The arrows show which location each website links to.

<img src="https://i.ibb.co/C0TSD22/sample.png" alt="Sample Input Visual" style="display: block; margin: auto; width: min(100%, 500px);">

Jake starts on website 1. He gets linked to website 4, and then again to website 2. Finally, he gets linked to website 5, and he stops his searching. In order to get to website 5, he had to click 3 links in total: 1 to 4, 4 to 2, and 2 to 5.

Hint: A **while loop** may help with solving this problem.