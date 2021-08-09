This problem is asking us to take in two numbers as input, and output the number that is two greater than their sum.
In more formal terms, our program should take in two integers $A$ and $B$. Then, it should output the integer $A+B+2$.

The goal of PRB1 was to teach you how to get a numeric input from the user, and how to output something to the console. Sample programs showing how to do this can be found below.

Here are some model solutions for this problem in all 3 languages.

Java (You'll need to change the class name to match your file name)
```java
import java.util.Scanner;

public class PRB1 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();
		int fakeSum = A + B + 2;
		System.out.println(fakeSum);
	}
}
```

Python 3
```python
A, B = map(int, input().split())
fake_sum = A + B + 2
print(fake_sum)
```

C++
```cpp
#include <iostream>

int main() {
	int A, B;
	std::cin >> A >> B;
	int fakeSum = A + B + 2;
	std::cout << fakeSum << std::endl;
}
```