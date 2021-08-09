#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int N, K;
    cin >> N;
    // Store point values in an array
    int* points = new int[N];
    for (int i = 0; i < N; i++) {
        cin >> points[i];
    }
    cin >> K;
    sort(points, points + N);

    long long sum = 0;
    for (int i = N-1; i >= K; i--) sum += points[i];
    cout << sum << endl;
    return 0;
}