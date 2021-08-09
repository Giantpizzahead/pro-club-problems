#include <iostream>
#include <fstream>
using namespace std;
const int MAXN = 1e5+5;

// ifstream fin("sleepy.in");
// ofstream fout("sleepy.out");

int N;
int P[MAXN];

struct BIT {
    int V[MAXN], total;

    void update(int i) {
        while (i < MAXN) {
            V[i]++;
            i += i & -i;
        }
        total++;
    }

    int query(int i) {
        int r = 0;
        while (i > 0) {
            r += V[i];
            i -= i & -i;
        }
        return total - r;
    }
};

BIT bit;

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) cin >> P[i];
    P[N] = 987654321;
    int K = N;
    for (int i = N-1; i >= 0; i--) {
        if (P[i] < P[i+1]) {
            // Cow is fine
            K--;
            bit.update(P[i]);
        } else break;
    }

    cout << K << endl;
    for (int i = 0; i < K; i++) {
        if (i != 0) cout << ' ';
        cout << N - 1 - bit.query(P[i]);
        bit.update(P[i]);
    }
    cout << endl;
    return 0;
}