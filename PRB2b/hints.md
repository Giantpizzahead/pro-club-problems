1. Here is some sample source code for all 3 languages. This code uses a **for loop** to store the point values of the questions into an **array**. Then, it prints out the sum of that array. It doesn't solve the problem though; that's up to you to figure out!

Java
```java
import java.util.Scanner;

public class PRB2b {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        // Store point values in an array
        int[] points = new int[N];
        for (int i = 0; i < N; i++) {
            points[i] = sc.nextInt();
        }

        // Print out the sum of the array
        int pointSum = 0;
        for (int i = 0; i < N; i++) {
            pointSum += points[i];
        }
        System.out.println(pointSum);
    }
}
```

Python 3
```python
N = int(input())
# Store point values in an array
points = list(map(int, input().split()))

# Print out the sum of the array
point_sum = 0
for i in range(N):
    point_sum += points[i]
print(point_sum)
```

C++
```cpp
#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;
    // Store point values in an array
    int* points = new int[N];
    for (int i = 0; i < N; i++) {
        cin >> points[i];
    }

    // Print out the sum of the array
    int pointSum = 0;
    for (int i = 0; i < N; i++) {
        pointSum += points[i];
    }
    cout << pointSum << endl;
    return 0;
}
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2\. The score Eve will get on the CS exam is equal to the sum of the point values for all the questions on the exam, minus the # of points that the question Eve decides to skip is worth. So, given this formula, what question should Eve skip to maximize the score that she gets on this exam?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3\. It might help to know how to find the minimum of two numbers, or the maximum of two numbers, as this may help with solving the problem.

In Java, **Math.min(a, b)** returns the minimum of two numbers a and b, while **Math.max(a, b)** returns the maximum of two numbers a and b.

In Python 3, the **min(a, b)** and **max(a, b)** functions do a similar thing.

C++ also has min(a, b) and max(a, b) functions, although you will need to do **#include &lt;algorithm&gt;** to use it.

<hr>

#### SOLUTION

Intuitively, Eve should skip the question worth the least number of points in order to maximize the score she gets on the CS test. So, take the sum of the point values of all the questions. Then, subtract the point value of the question worth the least number of points to get the answer.

Here is some Java code that demonstrates the above idea. This code uses a **for loop** to store the point values of the questions into an **array**, and to find the question with the least point value.

```java
import java.util.Scanner;

public class PRB2b {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        // Store point values in an array
        int[] points = new int[N];
        for (int i = 0; i < N; i++) {
            points[i] = sc.nextInt();
        }
        // Find the question with the least point value
        int least = points[0];
        for (int i = 1; i < N; i++) {
            least = Math.min(points[i], least);
        }
        // Calculate the answer (sum of points - least point value)
        int answer = 0;
        for (int i = 0; i < N; i++) {
            answer += points[i];
        }
        answer -= least;
        System.out.println(answer);
    }
}
```