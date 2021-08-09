import java.util.Scanner;

public class sol {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int S = sc.nextInt();

        // Process all swaps
        int peaLoc = S;
        for (int i = 0; i < N; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            if (peaLoc == a) {
                peaLoc = b;
            } else if (peaLoc == b) {
                peaLoc = a;
            }
        }

        System.out.println(peaLoc);
    }
}