#include <iostream>
#include <unordered_map>
using namespace std;

const int MAXN = 3000;

int N, Q;
int A[MAXN];

int findMode(int l, int r) {
    unordered_map<int, int> vals;
    for (int i = l; i <= r; i++) vals[A[i]]++;
    int bestV = -1, bestA = -1;
    for (auto p : vals) {
        if (p.second > bestA) {
            bestV = p.first;
            bestA = p.second;
        } else if (p.second == bestA) {
            bestV = -1;
        }
    }
    return bestV;
}

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) cin >> A[i];
    cin >> Q;
    for (int i = 0; i < Q; i++) {
        int l, r;
        cin >> l >> r;
        l--, r--;
        int m = findMode(l, r);
        if (m == -1) cout << "many" << endl;
        else cout << m << endl;
    }
    return 0;
}