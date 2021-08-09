1. Here's an easier question to think about: How long can Mary hold out before she *has* to wash her clothes? (What conditions would force Mary to wash her clothes?)

2. Does it ever make sense for Mary to wash her clothes earlier than she absolutely has to?

3. [Bonus hint] Instead of keeping track of the # of clothes Mary has left, it may help more to track the # of $0$, $1$, and $2$ days that she has come across without washing her clothes. See if you can use this info to find out when Mary has to wash them.

<hr>

#### SOLUTION

First of all, let's try to answer an easier question: How long can Mary hold out before she *has* to wash her clothes?

Since Mary is forced to wear the right type of clothing for each day, she will be forced to wash her clothes once she runs out of the type of clothing required for a day. In terms of code, Mary is forced to wash her clothes when she has $0$ clothes of the type required on a day.

Intuitively, it never makes sense for Mary to wash her clothes earlier than she absolutely has to. There is no benefit to washing her clothes early; since she washes all of them at once, the # of clean clothes she has will be the same after each wash, regardless of how early she washes them. The later Mary washes her clothes, the less days she will have to deal with.

This suggests a **greedy solution**: Iterate through each day in Mary's schedule, tracking the number of each type of clothing that she has. Once Mary reaches a point where she needs to wear a type of clothing that she has $0$ of, she is forced to wash her clothes (and the # of clean clothes she has is reset to $B$ business and $C$ casual). Keep doing this for all $N$ days in her schedule to get the answer.