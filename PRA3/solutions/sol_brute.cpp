#include <iostream>
#include <string>
#include <stack>
using namespace std;

const int MAXN = 50;
const int INF = 987654321;

string S;
int N, answer;
bool skip[MAXN];

inline bool parenMatches(int i, int j) {
    return (S[i] == '(' && S[j] == ')') || (S[i] == '[' && S[j] == ']') || (S[i] == '{' && S[j] == '}');
}

stack<int> locs;

void simulate(int n) {
    for (int i = 0; i < N; i++) {
        if (!skip[i]) {
            if (S[i] == '(' || S[i] == '[' || S[i] == '{') {
                locs.push(i);
            } else if (!locs.empty() && parenMatches(locs.top(), i)) {
                locs.pop();
            } else {
                // Not valid
                while (!locs.empty()) locs.pop();
                return;
            }
        }
    }
    if (locs.empty()) {
        // Valid
        /*
        cout << "works ";
        for (int i = 0; i < N; i++) cout << skip[i] << ' ';
        cout << endl;
        */
        answer = min(n, answer);
    }
    while (!locs.empty()) locs.pop();
}

void bruteForce(int i, int n) {
    if (i == N) simulate(n);
    else {
        bruteForce(i+1, n);
        skip[i] = true;
        bruteForce(i+1, n+1);
        skip[i] = false;
    }
}

int main() {
    cin >> S;
    N = S.length();
    answer = INF;
    bruteForce(0, 0);
    if (answer == 0) cout << "YES" << endl;
    else {
        cout << "NO" << endl;
        cout << answer << endl;
    }
    return 0;
}