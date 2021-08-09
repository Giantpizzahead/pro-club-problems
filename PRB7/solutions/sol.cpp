#include <iostream>
using namespace std;

int main() {
    int N, K;
    cin >> N >> K;
    int ans = 0;
    for (int i = 0; i < N; i++) {
        int x; cin >> x;
        if (x < K) ans += K-x;
    }
    cout << ans << endl;
    return 0;
}