import java.util.Scanner;

public class sol_nobonus {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        // Get your cards
        boolean has2N = false;
        for (int i = 0; i < N; i++) {
            int card = sc.nextInt();
            if (card == 2 * N) has2N = true;
        }

        if (has2N) System.out.println("You win");
        else System.out.println("Friend wins");
    }
}