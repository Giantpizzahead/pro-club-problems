1. Here is some base source code for all 3 languages. It handles all the input parsing required, but it does not do anything to actually solve the problem; that's up to you to figure out!

Java
```java
import java.util.Scanner;

public class PRI2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int S = sc.nextInt();

        // Process all swaps
        for (int i = 0; i < N; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            // Do something here
        }
        
        System.out.println(1);
    }
}
```

Python 3
```python3
N, S = map(int, input().split())

# Process all swaps
for i in range(N):
    a, b = map(int, input().split())
    # Do something here

print(1)
```

C++
```cpp
#include <iostream>

using namespace std;

int main() {
    int N, S;
    cin >> N >> S;
    
    // Process all swaps
    for (int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        // Do something here
    }

    cout << 1 << endl;
    return 0;
}
```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2\. Try using a variable to keep track of the pea's current location. For each swap, check if it affects the pea's location. If it does, move the pea accordingly.

<hr>

#### SOLUTION

This is a simulation problem; the goal is to keep track of the pea by simulating the swaps that Henry makes.

One way to approach this problem is to track the pea's current location in a variable; let's call this variable $L$. Initially, $L=S$ (since the pea starts at that location).

Whenever there is a swap that involves the location $L$, the pea should be swapped to the other location. That is, if $a=L$, the pea is moved to location $b$, and vice versa. If neither $a$ nor $b$ are equal to $L$, then the swap can safely be ignored.

A model Java solution for this problem can be found below.

```java
import java.util.Scanner;

public class PRI2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int S = sc.nextInt();
        // Process all swaps
        int L = S;
        for (int i = 0; i < N; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            if (L == a) {
                L = b;
            } else if (L == b) {
                L = a;
            }
        }
        System.out.println(L);
    }
}
```