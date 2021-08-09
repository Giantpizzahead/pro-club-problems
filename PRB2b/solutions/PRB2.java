import java.util.Scanner;
import java.util.Arrays;

public class PRB2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        // Store point values in an array
        int[] points = new int[N];
        for (int i = 0; i < N; i++) {
            points[i] = sc.nextInt();
        }
        Arrays.sort(points);
        int K = sc.nextInt();

        long sum = 0;
        for (int i = N-1; i >= K; i--) sum += points[i];
        System.out.println(sum);
    }
}