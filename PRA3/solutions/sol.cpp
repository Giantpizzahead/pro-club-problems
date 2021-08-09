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

#include <iostream>
#include <string>
#include <stack>
using namespace std;

const int MAXN = 5001;
const int INF = 987654321;

int dp[MAXN][MAXN];
int N;
string S;

inline bool parenMatches(int i, int j) {
    return (S[i] == '(' && S[j] == ')') || (S[i] == '[' && S[j] == ']') || (S[i] == '{' && S[j] == '}');
}

void solDP() {
    // Base cases
    for (int i = 0; i < N; i++) dp[i][i] = 1;
    for (int i = 0; i < N - 1; i++) {
        if (parenMatches(i, i+1)) dp[i][i+1] = 0;
        else dp[i][i+1] = 2;
    }
    // Transitions
    for (int r = 2; r < N; r++) {
        for (int i = 0, j = r; j < N; i++, j++) {
            dp[i][j] = INF;
            if (parenMatches(i, j)) dp[i][j] = dp[i+1][j-1];
            // Merge locations
            for (int k = i; k < j; k++) dp[i][j] = min(dp[i][k] + dp[k+1][j], dp[i][j]);
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
    if (dp[0][N-1] == 0) cout << "YES" << endl;
    else {
        cout << "NO" << endl;
        cout << dp[0][N-1] << endl;
    }
}

stack<int> locs;

void solStack() {
    for (int i = 0; i < N; i++) {
        if (S[i] == '(' || S[i] == '{' || S[i] == '[') {
            // Opening
            locs.push(i);
        } else {
            // Closing
            if (!locs.empty() && parenMatches(locs.top(), i)) {
                locs.pop();
            } else {
                cout << "NO" << endl;
                return;
            }
        }
    }
    if (locs.empty()) cout << "YES" << endl;
    else cout << "NO" << endl;
}

int main() {
    cin >> S;
    N = S.length();
    if (N <= 1000) solDP();
    else solStack();
    return 0;
}