import java.util.Scanner;

public class sol {
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
