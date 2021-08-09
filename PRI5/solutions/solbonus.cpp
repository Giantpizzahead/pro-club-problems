#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
const int MAXN = 100;

int N;
int A[MAXN], B[MAXN];

int simulate(int x) {
    vector<pair<int, bool>> points;
    for (int i = 0; i < N; i++) {
        if (i == x) continue;
        points.emplace_back(A[i], true);
        points.emplace_back(B[i], false);
    }
    sort(points.begin(), points.end());

    int numActive = 0, activeStart = -1, result = 0;
    for (auto p : points) {
        if (p.second) {
            if (numActive++ == 0) activeStart = p.first;
        } else {
            if (--numActive == 0) result += p.first - activeStart;
        }
    }
    return result;
}

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> A[i] >> B[i];
    }

    int answer = 0;
    for (int i = 0; i < N; i++) {
        // Fire this lifeguard
        answer = max(simulate(i), answer);
    }
    cout << answer << endl;
    return 0;
}