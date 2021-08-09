1. An interesting property about a valid Brackets expression (or program) is that at least one sub-expression of a valid expression should also be a valid expression. For example:
```text
{ { } [ ] [ [ [ ] ] ] } is valid expression
          [ [ [ ] ] ]   is valid sub-expression
  { } [ ]               is valid sub-expression
```
Can we exploit this recursive structure somehow?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2\. What if whenever we encounter a matching pair of brackets in the expression, we simply remove it from the expression? This would keep on shortening the expression, making the problem easier to solve. For example:
```text
{ { ( { } ) } }
      |_|

{ { ( ) } }
    |_|

{ { } }
  |_|

{ }
|_|

(Empty program)
```
In this case, all the brackets in the program were removed. Will this always happen if a Brackets program is valid?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3\. The **stack** data structure may help with removing matching pairs of brackets in the expression efficiently.

<hr>

#### BONUS HINTS

1. For test cases 11-14, there is a <a href="https://brilliant.org/wiki/greedy-algorithm/" target="_blank">greedy</a> way to remove brackets from the program. In other words, there is a smart way to determine the smallest # of deletions that Jake needs to make (without trying all possibilities).

2. For test cases 15-20, there is no greedy way to remove brackets from the program (as far as we know). So, there are two approaches to get as many points for these tests as possible. One method is to create a partially correct greedy solution that can get the optimal answer *most* of the time. Another method is to find an efficient way to try all the possibilities.

3. <a href="https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/m2G1pAq0OO0" target="_blank">What is dynamic programming?</a>