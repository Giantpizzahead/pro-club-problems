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