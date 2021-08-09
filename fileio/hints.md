Model solutions in all 3 languages are below.

Java
```java
import java.io.*;
import java.util.*;

public class fileio {
    // Don't forget to add the "throws IOException" \/ \/ \/
    public static void main(String[] args) throws IOException {
        // Read from a file with a Scanner
        File fin = new File("fileio.in");
        Scanner sc = new Scanner(fin);

        // Parse the integer array & find the sum
        int N = sc.nextInt();
        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        int sum = 0;
        for (int i = 0; i < N; i++) {
            sum += arr[i];
        }

        // Write to a file with a PrintWriter (don't forget to close it!)
        File fout = new File("fileio.out");
        PrintWriter out = new PrintWriter(fout);
        out.println(sum);
        out.close();
    }
}
```

C++
```cpp
#include <fstream>
using namespace std;

int main() {
    // Read from a file with ifstream (input file stream)
    ifstream fin("fileio.in");

    // Parse the integer array & find the sum
    int N;
    fin >> N;
    int arr[N];
    for (int i = 0; i < N; i++) {
        fin >> arr[i];
    }
    int sum = 0;
    for (int i = 0; i < N; i++) {
        sum += arr[i];
    }

    // Write to a file with ofstream (output file stream, don't forget to close it)
    ofstream fout("fileio.out");
    fout << sum << endl;
    fout.close();
    return 0;
}
```

Python 3
```python
# Read from a file
fin = open('fileio.in', 'r')

# Parse the integer array & find the sum
N = int(fin.readline())
arr = fin.readline().strip().split()
# Convert each element in the array to an integer
for i in range(N):
    arr[i] = int(arr[i])
curr_sum = 0
for i in range(N):
    curr_sum += arr[i]

# Write to a file (don't forget to close it)
fout = open('fileio.out', 'w')
# Python can only write strings, so make sure to cast to a string
# Make sure to add a newline too
fout.write(str(curr_sum) + '\n')
fout.close()
```