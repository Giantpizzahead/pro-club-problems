import java.io.*;
import java.util.*;

public class fileio2 {
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
        out.println(weight);

        // Don't forget to close PrintWriter at the end!
        out.close();
    }
}