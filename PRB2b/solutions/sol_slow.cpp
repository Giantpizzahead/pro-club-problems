#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")

#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int N, K;
    cin >> N;
    // Store point values in an array
    int* points = new int[N];
    long long sum = 0;
    for (int i = 0; i < N; i++) {
        cin >> points[i];
        sum += points[i];
    }
    cin >> K;
    for (int i = 0; i < K; i++) {
        int minI = 0;
        for (int j = 1; j < N; j++) {
            if (points[j] < points[minI]) {
                minI = j;
            }
        }
        sum -= points[minI];
        // Swap min with last element
        points[minI] = points[--N];
    }
    cout << sum << endl;
    return 0;
}