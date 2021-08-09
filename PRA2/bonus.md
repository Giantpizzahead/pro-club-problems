#### BONUS (15 points)

After thinking about her schedule a bit, Mary realized that there are some days where she's fine with wearing either type of clothing (business or casual). These days will be represented by the integer $2$ (in addition to the $0$ for business and $1$ for casual).

The question remains the same: Help Mary determine the minimum # of times she has to wash her clothes in order to wear the correct type of clothing for all of the $N$ days in her schedule (if she acts optimally - this includes her choice of business or casual clothing for the days of type $2$).

For about 40% of the points, $N < 60$, and the number of days of type $2$ will be less than $20$.

#### SAMPLE INPUT
```text
9 2 1
2 0 1 2 0 0 2 2 2
```

#### SAMPLE OUTPUT
```text
2
```

#### EXPLANATION

Here is a sequence that allows Mary to wash her clothes only $2$ times:

Day 1 end: $1$ business, $1$ casual (Wore business clothes)
Day 2 end: $0$ business, $1$ casual
Day 3 end: $0$ business, $0$ casual
--- Wash clothes before next day ---
Day 4 end: $2$ business, $0$ casual (Wore casual clothes)
Day 5 end: $1$ business, $0$ casual
Day 6 end: $0$ business, $0$ casual
--- Wash clothes before next day ---
Day 7 end: $1$ business, $1$ casual (Wore business clothes)
Day 8 end: $0$ business, $1$ casual (Wore business clothes)
Day 9 end: $0$ business, $0$ casual (Wore casual clothes)

A hint has been added for this bonus. It can be found in the hints for the main problem.