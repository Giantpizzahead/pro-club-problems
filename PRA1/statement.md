You and your friend just got into a heated argument, so of course, you've decided to settle the debate once and for all by playing a quick game of High Card Wins!

At the start of High Card Wins, both players receive exactly $N$ cards. Each card has an integer number in the range $1...2N$ written on it, and no two cards have the exact same number on them (in other words, the cards have **distinct numbers**). Note that this means every number from $1$ to $2N$ will be used exactly once.

High Card Wins is a turn-based card game. On each turn, both you and your friend secretly choose one of your cards to play. Then, you'll both play your chosen card at the same time. The person with a **higher card wins** (larger number), and gets to take both of the played cards. This repeats until someone runs out of cards, in which case the person who still has cards remaining is the winner!

When your friend was dealing the cards out, they seemed to be a bit... picky. You're suspicious that your friend might've dealt the cards in an unfair way, and that you would be wasting your time to even try and beat them. Luckily, you managed to catch a glimpse of the cards that your opponent got (but you're sure they peeked at your cards too). Assuming you and your friend are absolute pros at High Card Wins, meaning that you two always make the right moves (you both play optimally), can you figure out who will ultimately win this game?

#### INPUT FORMAT

The 1st line of input contains a single integer $N$, the number of cards each person starts with.

The 2nd line of input contains $N$ integers, representing the cards that you start out with.

The 3rd line of input contains $N$ integers, representing the cards that your friend starts out with.

#### OUTPUT FORMAT

Depending on who will win if you both play optimally, print either "You win" or "Friend wins" (make sure to match capitalization).

#### CONSTRAINTS

$1 \leq N \leq 2{,}000$
(The number of cards each person starts with will be in the range $1...2{,}000$.)

#### SAMPLE INPUT
```text
3
5 1 6
2 4 3
```

#### SAMPLE OUTPUT
```text
You win
```

#### EXPLANATION

You start with the cards 5, 1, and 6. Your friend starts with the cards 2, 4, and 3.

Here is an example of how the game could play out (this is not optimal play, it's just to demo the game):

Turn 1: You play 5, your friend plays 3. You take both cards. (5 1 6 3 vs 2 4)
Turn 2: You play 1, your friend plays 4. Your friend takes both cards. (5 6 3 vs 2 4 1)
Turn 3: You play 6, your friend plays 4. You take both cards. (5 6 3 4 vs 2 1)
Turn 4: You play 3, your friend plays 1. You take both cards. (5 6 3 4 1 vs 2)
Turn 5: You play 4, your friend plays 2. You take both cards, and since your opponent no longer has any cards, you win!

It can be proven that if both you and your friend play optimally, you are guaranteed to win the card game (for the sample input).