#include <iostream>
using namespace std;
const int MAXN = 100;

int N, M, K;
char grid[MAXN][MAXN], result[MAXN][MAXN];

int main() {
    cin >> M >> N >> K;
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            cin >> grid[i][j];
        }
    }
    for (int i = 0; i < M*K; i++) {
        for (int j = 0; j < N*K; j++) {
            result[i][j] = grid[i/K][j/K];
            cout << result[i][j];
        }
        cout << endl;
    }
    return 0;
}