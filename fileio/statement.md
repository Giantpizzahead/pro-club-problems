Working with files is a fundamental part of programming. So, let's learn how to work with files! (Spoiler: It's easier than you think.)

**File Input**

In Java, a Scanner can actually be used to read from files as well! The only difference is that instead of passing System.in to Scanner's constructor, you should pass a File object instead. See the below code sample for how this works:
```java
File fin = new File("<filename>");
Scanner sc = new Scanner(file);
```

After doing this, the rest becomes exactly the same as when you're working with the console / standard input! Scanner methods like nextInt(), nextFloat(), and next() can be used to parse input from a file. For example, to read an array of $N$ integers from numbers.txt, you could use the following code:
```java
// Scanner sc = new Scanner(System.in);
Scanner sc = new Scanner(new File("numbers.txt"));
int N = sc.nextInt();
int[] arr = new int[N];
for (int i = 0; i < N; i++) {
    arr[i] = sc.nextInt();
}
```

To show just how similar file IO is to standard IO, all you'd have to do in order to read from standard input is to uncomment the 1st line, and comment out the 2nd line. It's that simple!

**File Output**

A PrintWriter can be used to write to files, and it can be used in pretty much the same way as System.out! An example of how to do this is below:
```java
File fout = new File("<filename>");
PrintWriter out = new PrintWriter(fout);
out.println("This works!");
out.print("Oh yeah, this works ");
out.printf("%d\n", 2);
out.close();
```

All the methods you normally use with System.out, like print(), println(), and printf(), are available with PrintWriter as well. Don't forget to close the PrintWriter at the end of the program. For example, to print out a space-separated array of integers to array.txt, you could use the following code:
```java
int[] arr = {1, 3, 3, 1, 4};
PrintWriter out = new PrintWriter(new File("array.txt"));
for (int i = 0; i < arr.length; i++) {
    if (i != 0) out.print(' ');
    out.print(arr[i]);
}
out.println();
out.close();
```

**Summary**

(Note: For the above code samples to work, you need to either catch or throw an IOException when creating the Scanner, in case the file is not found on the computer. The easiest way to do this is to add **throws IOException** to the main method header. See the summary code below.)

Here is a summary of how to do file IO in Java:

```java
import java.io.*;
import java.util.*;

public class fileio {
    // Don't forget to add the "throws IOException" \/ \/ \/
    public static void main(String[] args) throws IOException {
        // Read from a file with a Scanner
        File fin = new File("fileio.in");
        Scanner sc = new Scanner(fin);

        // Example usages of Scanner
        int age = sc.nextInt();
        float weight = sc.nextFloat();
        String firstName = sc.next();

        // Write to a file with a PrintWriter
        File fout = new File("fileio.out");
        PrintWriter out = new PrintWriter(fout);

        // Example usages of PrintWriter
        out.println("I work just like System.out.println()!");
        out.print(firstName + " is " + age + " years old. Weight = ");
        out.printf("%f\n", weight);

        // Don't forget to close PrintWriter at the end!
        out.close();
    }
}
```

(If you are using either C++ or Python 3 to solve these problems, check the hints section for example code on how to do file IO.)

Now, try writing a program that will solve the below problem. Feel free to use the above code for reference.

<hr>

Bessie has written down $N$ numbers ($1 \leq N \leq 100$) in a file named "fileio.in". Each number is in the range $1...100$.

Help her determine the sum of these numbers, and output the answer to a file named "fileio.out".

#### INPUT FORMAT (fileio.in):

The first line of input contains $N$.

The next line contains $N$ space separated integers. These are the numbers that Bessie wants to sum.

#### OUTPUT FORMAT (fileio.out):

Output the sum of the $N$ numbers.

#### SAMPLE INPUT
```text
5
1 3 3 1 4
```

#### SAMPLE OUTPUT
```text
12
```

If your program receives a runtime error (exclamation mark) verdict for the sample test case, chances are your program didn't do file IO correctly. **Test your code locally** to check if it can read from the input file, and write to the output file.

Model solutions in all 3 languages can be found in the hints for this problem.