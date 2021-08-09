#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
const int MAXN = 3005;

int N;
int X[MAXN], Y[MAXN];
double cowD[MAXN];

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> X[i] >> Y[i];
    }

    for (int i = 0; i < N; i++) {
        // Remove this cow
        double D = INFINITY;
        for (int j = 0; j < N; j++) {
            if (j == i) continue;
            for (int k = j+1; k < N; k++) {
                if (k == i) continue;
                D = min(sqrt(pow(X[j] - X[k], 2) + pow(Y[j] - Y[k], 2)), D);
            }
        }
        cowD[i] = D;
    }

    int best = 0;
    for (int i = 0; i < N; i++) {
        if (cowD[i] > cowD[best]) best = i;
        cerr << "Cow " << (i+1) << ": " << cowD[i] << endl;
    }
    cout << best+1 << endl;
    return 0;
}