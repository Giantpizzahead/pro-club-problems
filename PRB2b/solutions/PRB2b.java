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