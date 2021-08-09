This problem is asking us to output the gesture that beats Elsie's gesture in $N$ games of Hoof, Paper, Scissors (which is really just Rock Paper Scissors, but with a hoof instead).

The goal of PRI1 was to teach you how to get a string input from the user, and how to use a for loop. Model solutions for this problem in all 3 languages can be found below.

Java
```java
import java.util.Scanner;

public class PRI1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        for (int i = 0; i < N; i++) {
            // Get Elsie's gesture for this game
            String gesture = sc.next();
            // Print out the gesture Bessie should play
            if (gesture.equals("hoof")) {
                System.out.println("paper");
            } else if (gesture.equals("paper")) {
                System.out.println("scissors");
            } else {
                System.out.println("hoof");
            }
        }
    }
}
```

Python 3
```python
N = int(input())

for i in range(N):
    # Get Elsie's gesture for this game
    gesture = input().strip()
    # Print out the gesture Bessie should play
    if gesture == "hoof":
        print("paper")
    elif gesture == "paper":
        print("scissors")
    else:
        print("hoof")
```

C++
```cpp
#include <iostream>
#include <string>

using namespace std;

int main() {
    int N;
    cin >> N;

    string gesture;
    for (int i = 0; i < N; i++) {
        // Get Elsie's gesture for this game
        cin >> gesture;
        // Print out the gesture Bessie should play
        if (gesture == "hoof") {
            cout << "paper" << endl;
        } else if (gesture == "paper") {
            cout << "scissors" << endl;
        } else {
            cout << "hoof" << endl;
        }
    }
    return 0;
}
```