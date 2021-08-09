1. Here is some sample source code for all 3 languages. This code stores the point values of the questions into 3 variables, and then prints out the sum of these point values. It doesn't solve the problem though; that's up to you to figure out!

Java
```java
import java.util.Scanner;

public class PRB2a {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        // Print out the sum of the variables
        System.out.println(A + B + C);
    }
}
```

Python 3
```python
A, B, C = map(int, input().split())

# Print out the sum of the variables
print(A + B + C)
```

C++
```cpp
#include <iostream>

using namespace std;

int main() {
    int A, B, C;
    cin >> A >> B >> C;
    
    // Print out the sum of the variables
    cout << A + B + C << endl;
    return 0;
}
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2\. It might help to know how to find the minimum of two numbers, or the maximum of two numbers, as this may help with solving the problem.

In Java, **Math.min(a, b)** returns the minimum of two numbers a and b, while **Math.max(a, b)** returns the maximum of two numbers a and b.

In Python 3, the **min(a, b)** and **max(a, b)** functions do a similar thing.

C++ also has min(a, b) and max(a, b) functions, although you will need to do **#include &lt;algorithm&gt;** to use it.

<hr>

#### SOLUTION

Intuitively, Eve should skip the question worth the least number of points in order to maximize the score she gets on the CS test. So, take the sum of the point values of all the questions. Then, subtract the point value of the question worth the least number of points to get the answer.

Here is some Java code that demonstrates the above idea.

```java
import java.util.Scanner;

public class PRB2a {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();
        // Find question worth least number of points
        int minPoints = Math.min(A, B);
        minPoints = Math.min(C, minPoints);
        // Caluclate & output answer
        int answer = A + B + C - minPoints;
        System.out.println(answer);
    }
}
```