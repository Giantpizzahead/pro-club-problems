/**
 * dp[i][j] = Min deletions to fix program in [i, j]
 * 
 * Base:
 * dp[i][i] = 1
 * d[i][i+1] = 0 if match, else 2
 * 
 * Trans:
 * dp[i][j] =
 * if match -> dp[i+1][j-1]
 * for k in i...j-1 -> dp[i][k] + dp[k+1][j]
 * 
 * Answer:
 * dp[0][N-1]
 * 
 * Runtime: O(N^2)
 */

import java.util.*;

public class sol {
    char[] S;
    int N;

    boolean parenMatches(int i, int j) {
        return (S[i] == '(' && S[j] == ')') || (S[i] == '[' && S[j] == ']') || (S[i] == '{' && S[j] == '}');
    }

    void solve() {
        Scanner sc = new Scanner(System.in);
        S = sc.next().toCharArray();
        N = S.length;
        int[][] dp = new int[N][N];
        // Base cases
        for (int i = 0; i < N; i++) dp[i][i] = 1;
        for (int i = 0; i < N - 1; i++) {
            if (parenMatches(i, i+1)) dp[i][i+1] = 0;
            else dp[i][i+1] = 2;
        }
        // Transitions
        for (int r = 2; r < N; r++) {
            for (int i = 0, j = r; j < N; i++, j++) {
                dp[i][j] = 987654321;
                if (parenMatches(i, j)) dp[i][j] = dp[i+1][j-1];
                // Merge locations
                for (int k = i; k < j; k++) dp[i][j] = Math.min(dp[i][k] + dp[k+1][j], dp[i][j]);
            }
        }
        /*
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                cout << dp[i][j] << ' ';
            }
            cout << endl;
        }
        */
        if (dp[0][N-1] == 0) System.out.println("YES");
        else {
            System.out.println("NO");
            System.out.println(dp[0][N-1]);
        }
    }

    public static void main(String[] args) {
        new sol().solve();
    }
}