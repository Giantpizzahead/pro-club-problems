/*
Key idea: Take the closest pair of cows (without removing any). If neither of those 2 are removed, the shortest distance
will stay the same! So, you only need to simulate isolating those 2 cows, leading to a O(N^2) solution.
*/

#include <iostream>
#include <cmath>
#include <algorithm>
#include <iomanip>
using namespace std;
const int MAXN = 3005;

int N;
int X[MAXN], Y[MAXN];
float D[MAXN][MAXN];

float removeCow(int x) {
    float d = INFINITY;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i == j || i == x || j == x) continue;
            d = min(D[i][j], d);
        }
    }
    return d;
}

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> X[i] >> Y[i];
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            D[i][j] = sqrt(pow(X[i] - X[j], 2) + pow(Y[i] - Y[j], 2));
        }   
    }

    float baseD = removeCow(-1);

    int fi, fj;
    float minD = INFINITY;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i == j) continue;
            if (D[i][j] < minD) {
                minD = D[i][j];
                fi = i;
                fj = j;
            }
        }
    }

    float id = removeCow(fi);
    float jd = removeCow(fj);

    cerr << setprecision(18);
    cerr << "baseD " << baseD << endl;
    cerr << "fi " << fi << endl;
    cerr << "fj " << fj << endl;
    cerr << "id " << id << endl;
    cerr << "jd " << jd << endl;

    if (id == baseD && jd == baseD) cout << 1 << endl;
    else if (id > jd) cout << fi+1 << endl;
    else if (jd > id) cout << fj+1 << endl;
    else cout << min(fi, fj)+1 << endl;
    return 0;
}