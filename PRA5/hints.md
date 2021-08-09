A good way to approach this problem is to come up with some strategy that Farmer John can use to sort his cows. For example, one simple strategy is to just keep the last few cows sorted by placing the cows in the right places; this would guarantee that he could finish sorting the cows in $N$ steps. An example of this is below:
```text
              Steps
FJ: 1 2 4 3  |  0
FJ: 2 4 3 1  |  1
FJ: 4 3 1 2  |  2
FJ: 3 1 2 4  |  3
FJ: 1 2 3 4  |  4
```
This method does not minimize the number of time steps needed to sort the cows, but it's a start. Try to find a way to improve on this strategy!