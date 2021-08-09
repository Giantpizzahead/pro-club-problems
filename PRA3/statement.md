While chasing links to find the answers to his math homework, Jake has come across an interesting programming language called Brackets. This language is quite unique: A program written in Brackets is only a single line of code, and it contains just the characters '(', ')', '{', '}', '[', and ']'.

In order for a Brackets program to run, it must be perfectly balanced (as all things should be).

A Brackets program is balanced if:

* Open brackets are closed by the same type of closing brackets.
* Open brackets are closed in the correct order.

Here are some examples of balanced and unbalanced Brackets programs:

```text
([]) = Balanced
[{{}}] = Balanced
{}[()()] = Balanced
()) = Not balanced
}{ = Not balanced
[(]) = Not balanced
```

Jake has just written a very long Brackets program, but he's not sure if it will actually run. Given a string $S$ representing this Brackets program, please help Jake determine **whether or not the program is balanced**.

#### INPUT FORMAT

The only line of input contains the string $S$ representing the Brackets program. This string will only contain the 6 valid Brackets characters.

#### OUTPUT FORMAT

If $S$ is balanced, print "YES" on a single line. Else, print "NO".

#### CONSTRAINTS

$1 \leq |S| \leq 10^6$
(The length of the Brackets program $S$ is in the range $1...10^6$.)

#### SCORING

* Test cases 1-5 satisfy $|S| \leq 10^3$.
* Test cases 6-10 satisfy no additional constraints.

#### SAMPLE INPUT 1
```text
((())[]){[]}
```

#### SAMPLE OUTPUT 1
```text
YES
```

#### SAMPLE INPUT 2
```text
{[}]()
```

#### SAMPLE OUTPUT 2
```text
NO
```