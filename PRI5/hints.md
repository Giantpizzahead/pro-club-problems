1. Farmer John only has to fire one lifeguard, and the bounds for the problem are pretty low. So, a possible approach may be to try firing each lifeguard, and taking the best result from all these simulations.

2. Here's an example for how one might simulate firing a lifeguard. This example uses the sample input, firing the 1st lifeguard.
```text
0 1 2 3 4 5 6 7 8 9    Time steps

F F F F F F F F F F    Nothing covered initially

F T T T F F F F F F    Lifeguard 2
  ^ ^ ^
F T T T T T T F F F    Lifeguard 3
      ^ ^ ^ ^
```
At the end, the total time covered by the lifeguards is 6.