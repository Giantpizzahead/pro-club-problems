You have probably heard of the game "Rock, Paper, Scissors". The cows on Farmer John's field like to play a similar game they call "Hoof, Paper, Scissors".

The rules of "Hoof, Paper, Scissors" are simple. Two cows play against each other. They both count to three and then each simultaneously makes a gesture that represents either a hoof, a piece of paper, or a pair of scissors. **Hoof beats scissors** (since a hoof can smash a pair of scissors), **scissors beats paper** (since scissors can cut paper), and **paper beats hoof** (since the hoof can get a papercut). For example, if the first cow makes a "hoof" gesture and the second a "paper" gesture, then the second cow wins. Of course, it is also possible to tie, if both cows make the same gesture.

Farmer John watches in fascination as two of his cows - Bessie and Elsie - play a series of $N$ games of "Hoof, Paper, Scissors". ($N$ is a variable that will be given to your program in the input.) Unfortunately, Farmer John knows that poor Bessie doesn't understand the rules of this game (she thinks the gestures are some sort of secret language).

Farmer John would like to help Bessie win "Hoof, Paper, Scissors", in order to boost her self-confidence. Luckily, he knows Elsie really well, so he can predict exactly which gestures Elsie will play for each of the $N$ games.

Given the gestures that Farmer John predicts Elsie will make, please help Bessie by telling her the gestures that she has to make to win at "Hoof, Paper, Scissors".

#### INPUT FORMAT

The 1st line of input contains a single integer $N$, the number of "Hoof, Paper, Scissors" games that Bessie will play.

The next $N$ lines of input each contain one of the three possible gestures ("hoof", "paper", and "scissors"). The $i$th line represents the gesture that Elsie is going to play in the $i$th game.

#### OUTPUT FORMAT

Output $N$ lines, where the $i$th line contains the gesture that Bessie should play in order to beat Elsie in the $i$th game.

#### CONSTRAINTS

$1 \leq N \leq 100$
(The number of "Hoof, Paper, Scissors" games that Bessie will play is in the range $1...100$.)

#### SAMPLE INPUT
```text
4
hoof
paper
hoof
scissors
```

#### SAMPLE OUTPUT
```text
paper
scissors
paper
hoof
```

#### EXPLANATION

Paper beats hoof for the 1st game, scissors beats paper for the 2nd game, paper beats hoof for the 3rd game, and hoof beats scissors in the 4th game.