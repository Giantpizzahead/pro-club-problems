Bob is playing an intense game of <a href="https://www.youtube.com/watch?v=Na8vHaCLwKc" target="_blank">Among Us</a>, the ultimate test of teamwork and betrayal. In this game, $1$ person is selected as the impostor, while the rest are given the role of a crewmate. The impostor's goal is to blend in with the crew, and to eliminate the other crewmates without being caught.

As luck would have it, someone decides to call an emergency meeting right before Bob finishes his Simon Says task. Now it's up to the $N$ people still alive (each person has a name) to figure out who the impostor is once and for all!

In the emergency meeting, a bunch of people contribute $M$ pieces of info to think about. Each piece of info is of the form "$a$ says $b$ is safe" or "$a$ says $b$ is impostor". For example, a possible piece of info could be "Bob says Caleb is impostor". If a crewmate says a piece of info, it is guaranteed that their info is accurate.

Unfortunately, the impostor isn't giving away their identity that easily. The impostor can say fake pieces of info, in order to throw off the other crewmates.

The voting timer is counting down... it's now or never! Help Bob figure out all the people who could be the impostor based on the pieces of info, so that he can find the impostor Among Us.

#### INPUT FORMAT

The first line of input contains a single integer $N$, the number of people currently alive in the game.

The next $N$ lines of input each contain the name of a person currently alive in the game. These names will be sorted in lexicographical order, and they will all be distinct.

The next line of input contains a single integer $M$, the number of pieces of info.

The next $M$ lines of input each contain a single piece of info.
Each piece of info is of the form "$a$ says $b$ is safe" or "$a$ says $b$ is impostor", where $a$ and $b$ are both names of people alive in the game, and $a \neq b$. Note that there could be duplicate pieces of info.

#### OUTPUT FORMAT

The first line of output should contain a single integer $P$, the number of people who could be the impostor.

The next $P$ lines should each contain the name of a person who could be the impostor. These names should be sorted in lexicographical order.

#### CONSTRAINTS

$3 \leq N \leq 500$
$0 \leq M \leq 500$

#### SCORING

* Test cases 1-5 will simulate actual Among Us games (that is, $N \leq 10$).
* Test cases 6-10 satisfy no additional constraints.

The names will consist of alphanumeric characters, and they will be no longer than $10$ characters long.

It is guaranteed that there is at least 1 person who could be the impostor, based on the given pieces of info.

#### SAMPLE INPUT 1
```text
4
Alice
Bob
Caleb
Diana
3
Alice says Bob is safe
Bob says Caleb is impostor
Caleb says Diana is safe
```

#### SAMPLE OUTPUT 1
```text
1
Caleb
```

#### EXPLANATION 1

Alice cannot be the impostor; if she was, Bob would be wrong about Caleb being the impostor.
Bob cannot be the impostor; if he was, Alice would be wrong about Bob being safe.
Caleb could be the impostor; if he was, both Alice and Bob would have correct pieces of info. Caleb's info happens to be correct as well (although it wouldn't matter if it was wrong).
Diana cannot be the impostor; if she was, Caleb would be wrong about Diana being safe.

Therefore, Caleb is the only person who could be the impostor.

#### SAMPLE INPUT 2
```text
3
Dave
lizzie
pewds
2
lizzie says pewds is impostor
pewds says lizzie is impostor
```

#### SAMPLE OUTPUT 2
```text
2
lizzie
pewds
```

#### EXPLANATION 2

Dave cannot be the impostor; if he was, both lizzie and pewds would be wrong about their pieces of info.
lizzie could be the impostor; if she was, pewds would be correct about his piece of info. It does not matter that lizzie's info is wrong, as she is the impostor (and could have lied about her info).
pewds could be the impostor; if he was, lizzie would be correct about her piece of info. It does not matter that pewds's info is wrong, as he is the impostor.

Therefore, both lizzie and pewds could be the impostor.

(The only change in the bonus is increased constraints.)