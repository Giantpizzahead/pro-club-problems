#include <iostream>
#include <unordered_map>
using namespace std;

const int MAXN = 3000;

int N, Q;
int A[MAXN], cnt[MAXN];
int mode[MAXN][MAXN];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> A[i];
        A[i]--;
    }
    for (int i = 0; i < N; i++) {
        int bestV = -2, bestA = -1;
        for (int j = 0; j < MAXN; j++) cnt[j] = 0;
        for (int j = i; j < N; j++) {
            cnt[A[j]]++;
            if (cnt[A[j]] > bestA) {
                bestV = A[j];
                bestA = cnt[A[j]];
            } else if (cnt[A[j]] == bestA) {
                bestV = -2;
            }
            mode[i][j] = bestV+1;
        }
    }
    cin >> Q;
    for (int i = 0; i < Q; i++) {
        int l, r;
        cin >> l >> r;
        l--, r--;
        int m = mode[l][r];
        if (m == -1) cout << "many\n";
        else cout << m << '\n';
    }
    return 0;
}