In this problem, your goal is to create a simplified version of a search engine - the Goggle search engine.

The Goggle search engine has $N$ websites, conveniently numbered $1 \ldots N$, stored in its database ($1 \leq N \leq 50\,000$). Each website has a name consisting of only lowercase letters / spaces. In addition, each website has a relevance rating $R_i$ ($1 \leq R_i \leq 10^9$) that measures how useful the website is to users.

$Q$ search queries have been sent to the Goggle search engine ($1 \leq Q \leq 50\,000$). Each query consists of only lowercase letters / spaces. In order to provide users with the most accurate search results possible, the search engine should return a website whose name has a **prefix that is equal to the query string**. If there are multiple websites with a matching prefix, Goggle should strive to return the most relevant result possible (the one with the highest relevance rating).

For example, if the query is "hello", the search engine could return websites like "hello world", "hellooooooo", and "hello". However, websites like "he", "what is hello", and "halloween" do not match the query.

Search engines aren't perfect though... For this problem, your program does not need to always output the best result. Instead, your program will receive **partial credit** based on how high of a score it gets.

For each query, if your program outputs a website that does not have a matching prefix, it will get $0$ points for that query. Otherwise, it will get $R_i$ points (the relevance rating for the outputted website). The final score of your code will be the sum of its scores for all the queries.

#### INPUT FORMAT

The first line of input contains a single integer $N$, the number of websites.
The second line of input contains $N$ space separated integers. The $i$th integer is $R_i$.
The next $N$ lines of input each contain the name of a website. The $i$th line gives the name of website $i$.

The next line of input contains a single integer $Q$, the number of queries.
The next $Q$ lines of input each contain a query string. The $i$th line gives the $i$th query.

The lengths of the website names and queries will not exceed $20$ characters.

#### OUTPUT FORMAT

Output $Q$ lines, where the $i$th line gives the number of the website Goggle should return for the $i$th query. Each of these numbers must be in the range $1...N$.

#### SCORING

If your program outputs an invalid website number for any queries (or does not answer all $Q$ queries), then it will get a wrong answer verdict.

Otherwise, let $P$ be the # of points your program earns for a test case, and let $O$ be the optimal # of points (if all queries are answered correctly). The score of your program for that test case will be equal to $P/O$, rounded to the nearest hundredth.

The time limit is 2 seconds (x1.5 for Java, x2 for Python). The memory limit is 192 MB.

#### SAMPLE INPUT
```text
5
10 1 8 6 10
sorting introduction
how to get robux
usaco guide
usaco contests
how to binary search
4
how
usaco co
who did this
sort
```

#### SAMPLE OUTPUT
```text
5
4
5
1
```

#### EXPLANATION

There are $5$ websites indexed by the Goggle search engine. The relevance of each website is listed below.

10 = sorting introduction
1 = how to get free robux
8 = usaco guide
6 = usaco contests
10 = how to binary search

The responses for the $4$ queries given in the sample are shown below.

Query "how" -> Response "how to binary search", prefix matches, relevance 10
Query "usaco co" -> Response "usaco contests", prefix matches, relevance 6
Query "who did this" -> Response "how to binary search", prefix does not match, scores 0
Query "sort" -> Response "sorting introduction", prefix matches, relevance 10

So, this output would receive $10+6+0+10=26$ points, which is the optimal score for the sample input.

Remember: There are a variety of solutions to this problem that can receive lots of partial credit. Even something as simple as outputting the number 1 for every query will get some credit. **Try to get as many points as possible!**