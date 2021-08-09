Petra is preparing for her school's annual Archery Shootoff! Today, her practice session will consist of $N$ rounds.

In each round, Petra will shoot an arrow at the target, and depending on how close her shot is to the center, she will receive a score in the range $0...100$ for that round. Petra's final score for the practice session will simply be the sum of her scores for each round.

For example, if $N = 3$, and Petra's scores for each round are $50$, $80$, and $60$, her final score for that practice session would be $190$.

After completing her practice session, Petra realizes that she forgot to record her score for some of the rounds! Her score for these forgotten rounds could have been anything from $0$ (missing the target) to $100$ (hitting the bullseye).

Petra knows that she will be biased if she tries to recall these missing scores herself. So, she decides to use a fair method to judge how well she did. Given the scores that Petra recorded (or $-1$ if she forgot her score for a round), please help Petra determine the **minimum and maximum possible scores** that she could have gotten during her practice session.

#### INPUT FORMAT

The first line of input contains a single integer $N$, the number of rounds in Petra's  practice session.

The second line of input contains $N$ space separated integers, where the $i$th integer represents the score that Petra got in the $i$th round (or $-1$ if she forgot to record her score for that round).

#### OUTPUT FORMAT

The first line of output should contain a single integer: The minimum possible score.

The second line of output should contain a single integer: The maximum possible score.

#### CONSTRAINTS

$1 \leq N \leq 100$
(The number of rounds in Petra's practice session will be in the range $1...100$.)

#### SAMPLE INPUT
```text
5
100 -1 0 -1 85
```

#### SAMPLE OUTPUT
```text
185
385
```

#### EXPLANATION

Petra's practice session consisted of 5 rounds. Her 1st shot got a score of 100, her 3rd got a score of 0, and her 5th got a score of 85. She did not record the score of her 2nd and 4th shots.