#include <iostream>

using namespace std;

int main() {
    int N, S;
    cin >> N >> S;
    
    // Process all swaps
    int peaLoc = S;
    for (int i = 0; i < N; i++) {
        int a, b;
        cin >> a >> b;
        if (peaLoc == a) {
            peaLoc = b;
        } else if (peaLoc == b) {
            peaLoc = a;
        }
    }

    cout << peaLoc << endl;
    return 0;
}