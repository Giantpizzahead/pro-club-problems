The harder version of this problem is very similar to the easier version. The only difference is that there are now a variable amount of questions on the exam, instead of just 3.

(In the future, easier / harder versions of a problem will not be divided into two separate problems. Instead, there will be one problem with multiple *subtasks*, where each subtask is worth some number of points.)

<hr>

Eve has a computer science exam coming up. **This exam will have $N$ questions**, and each question will have a point value. $N$ is a variable that will be given to your program in the input. Eve is a very responsible student, so she is prepared enough to get full points on every question in the exam.

However, her CS teacher is very strict with time limits... After taking a mock exam, Eve has determined that she will need to skip exactly one question on this test in order to finish in time. She will get no points for the question that she skips.

Of course, Eve wants to get as high a score on this test as possible. Please help Eve determine the maximum possible score she can get on the CS exam if she is forced to skip one question.

#### INPUT FORMAT

The first line of input contains a single integer $N$: The number of questions on the CS test.

The second line of input contains $N$ space-separated integers. These integers represent the number of points that each question is worth.

#### OUTPUT FORMAT

Output a single integer: The maximum possible score Eve can get on the CS test if she is forced to skip one question.

#### CONSTRAINTS

$2 \leq N \leq 100$
(The number of questions on the CS test will be in the range $2...100$.)

The number of points each question is worth will be in the range $1...100$.

#### SAMPLE INPUT
```text
4
20 25 10 25
```

#### SAMPLE OUTPUT
```text
70
```

#### EXPLANATION

There are $4$ questions on the CS exam. The questions are worth $20$, $25$, $10$, and $25$ points.

To get the best possible score, Eve should skip question $3$. This results in a final score of $20$ + $25$ + $25$ = $70$ points.

#### NOTES

The concept of a **for loop** may help with solving this problem. Lots of useful tutorials explaining for loops are available online.
Here is a sample for loop in each language that prints out the numbers from 0 to 9, inclusive:

Java
```java
for (int i = 0; i < 10; i++) {
    System.out.println(i);
}
```

Python 3
```python
for i in range(10):
    print(i)
```

C++
```cpp
for (int i = 0; i < 10; i++) {
    cout << i << endl;
}
```