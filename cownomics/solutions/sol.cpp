#include <iostream>
using namespace std;
const int MAXN = 100;

int N, M;
string cows[MAXN], cows2[MAXN];
bool isSpotty[256], isPlain[256];

int main() {
    freopen("cownomics.in", "r", stdin);
    freopen("cownomics.out", "w", stdout);
    cin >> N >> M;
    for (int i = 0; i < N; i++) cin >> cows[i];
    for (int i = 0; i < N; i++) cin >> cows2[i];
    int answer = 0;
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < 256; j++) {
            isSpotty[j] = false;
            isPlain[j] = false;
        }
        for (int j = 0; j < N; j++) isSpotty[cows[j][i]] = true;
        for (int j = 0; j < N; j++) isPlain[cows2[j][i]] = true;
        for (int j = 0; j < 256; j++) {
            if (isSpotty[j] && isPlain[j]) {
                // Invalid
                answer--;
                break;
            }
        }
        answer++;
    }
    cout << answer << endl;
    fclose(stdout);
}