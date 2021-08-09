#include <iostream>
#include <string>
#include <stack>
using namespace std;

const int MAXN = 1e6;

string S;
int N, bestSoFar, answerOffset;
bool skip[MAXN];

inline bool parenMatches(int i, int j) {
    return (S[i] == '(' && S[j] == ')') || (S[i] == '[' && S[j] == ']') || (S[i] == '{' && S[j] == '}');
}

inline bool isOpenBracket(int i) {
    return S[i] == '(' || S[i] == '[' || S[i] == '{';
}

inline bool isCloseBracket(int i) {
    return S[i] == ')' || S[i] == ']' || S[i] == '}';
}

stack<int> locs;

int simulate() {
    int removed = 0;
    for (int i = 0; i < N; i++) {
        if (!skip[i]) {
            if (S[i] == '(' || S[i] == '[' || S[i] == '{') {
                locs.push(i);
            } else if (!locs.empty() && parenMatches(locs.top(), i)) {
                locs.pop();
            } else {
                // Not valid; use random chance to decide what to do
                if (rand() % 2 == 0 && !locs.empty()) {
                    // Ignore preceding bracket instead
                    locs.pop();
                    removed++;
                    i--;
                } else {
                    // Ignore this bracket
                    removed++;
                }
            }
        }
    }
    // Remove all extraneous brackets
    while (!locs.empty()) {
        locs.pop();
        removed++;
    }
    return removed;
}

bool bruteForce(int i, int n) {
    if (i == N) {
        int result = simulate();
        if (result == 0) return true;
    } else {
        // Must change exact # of brackets
        if (N-i-1 >= n) {
             if (bruteForce(i+1, n)) return true;
        }
        if (n > 0) {
            skip[i] = true;
            if (bruteForce(i+1, n-1)) return true;
            skip[i] = false;
        }
    }
    return false;
}

void shortenProgram() {
    // Remove edge brackets that cannot be used
    // Also remove adjacent pairs of matched brackets
    bool changed = true;
    while (changed) {
        changed = false;
        // Remove starting edge brackets
        bool open1 = false, open2 = false, open3 = false;
        for (int i = 0; i < S.length(); i++) {
            if (isOpenBracket(i)) {
                if (S[i] == '(') open1 = true;
                else if (S[i] == '[') open2 = true;
                else open3 = true;
            } else {
                // Remove bracket if no open pair exists
                if (S[i] == ')' && !open1 || S[i] == ']' && !open2 || S[i] == '}' && !open3) {
                    S = S.substr(0, i) + S.substr(i+1);
                    i--;
                    answerOffset++;
                    changed = true;
                }
            }
        }
        // Remove ending edge brackets
        open1 = false, open2 = false, open3 = false;
        for (int i = S.length() - 1; i >= 0; i--) {
            if (isCloseBracket(i)) {
                if (S[i] == ')') open1 = true;
                else if (S[i] == ']') open2 = true;
                else open3 = true;
            } else {
                // Remove bracket if no close pair exists
                if (S[i] == '(' && !open1 || S[i] == '[' && !open2 || S[i] == '{' && !open3) {
                    S = S.substr(0, i) + S.substr(i+1);
                    answerOffset++;
                    changed = true;
                }
            }
        }
        // Remove adjacent brackets of the same type
        for (int i = 1; i < S.length(); i++) {
            if (parenMatches(i-1, i)) {
                S = S.substr(0, i-1) + S.substr(i+1);
                i--;
                changed = true;
            }
        }
    }
}

int main() {
    cin >> S;
    if (S.length() <= 300) shortenProgram();
    cout << "Shortened: " << S << endl;
    cout << "# removed: " << answerOffset << endl;
    N = S.length();
    if (answerOffset == 0 && simulate() == 0) cout << "YES" << endl;
    else {
        cout << "NO" << endl;
        if (N <= 300) {
            if (N == 0) {
                // Edge case (entire sequence removed)
                cout << answerOffset << endl;
                return 0;
            }
            // RNG for the win...?
            srand(1337);
            bestSoFar = 987654321;
            for (int i = 0; i < 500000; i++) {
                bestSoFar = min(simulate(), bestSoFar);
            }
            cout << bestSoFar + answerOffset << endl;
            /*
            for (int i = 1; i <= N; i++) {
                if (bruteForce(0, i)) {
                    cout << i + answerOffset << endl;
                    break;
                }
            }
            */
        }
    }
    return 0;
}