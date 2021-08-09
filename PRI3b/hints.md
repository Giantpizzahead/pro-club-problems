1. This problem can be divided into two parts: Checking if a number is prime, and finding the prime number that is the closest to $N$. It may help to tackle these parts one at a time.

2. Checking if a number is prime basically means making sure the number is not divisible by anything except $1$ and itself. Is there a math operator that could tell us whether a number is divisible by another number (has a remainder of zero)?

3. To check the numbers that are closest to $N$ first, your code could follow a pattern like $N$, $N-1$, $N+1$, $N-2$, $N+2$, etc. This also works in the case of a tie.

4. For test cases 7-10, $N$ is really big... if you aren't careful with the way you check if a number is prime, your code could TLE (exceed the time limit). To check if a number is prime, do ALL the numbers from $2$ to $N-1$ need to be checked for divisibility? Maybe some of those checks are unnecessary...