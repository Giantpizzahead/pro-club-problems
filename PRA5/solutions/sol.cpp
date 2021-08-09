#include <iostream>
#include <fstream>
using namespace std;
const int MAXN = 1e2+5;

int N;
int P[MAXN];

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) cin >> P[i];
    P[N] = 987654321;
    int K = N;
    for (int i = N-1; i >= 0; i--) {
        if (P[i] < P[i+1]) {
            // Cow is fine
            K--;
        } else break;
    }

    cout << K << endl;
    return 0;
}