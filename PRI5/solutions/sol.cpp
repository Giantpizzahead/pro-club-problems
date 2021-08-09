#include <iostream>
using namespace std;
const int MAXN = 100;
const int MAXT = 1000;

int N;
bool used[MAXT];
int A[MAXN], B[MAXN];

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> A[i] >> B[i];
    }

    int answer = 0;
    for (int i = 0; i < N; i++) {
        // Fire this lifeguard
        for (int j = 0; j < MAXT; j++) used[j] = false;
        for (int j = 0; j < N; j++) {
            if (j == i) continue;
            for (int k = A[j]; k < B[j]; k++) used[k] = true;
        }
        int numUsed = 0;
        for (int j = 0; j < MAXT; j++) if (used[j]) numUsed++;
        answer = max(numUsed, answer);
    }
    cout << answer << endl;
    return 0;
}