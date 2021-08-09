#include <iostream>
#include <string>

using namespace std;

int main() {
    int N;
    cin >> N;

    string gesture;
    for (int i = 0; i < N; i++) {
        // Get Elsie's gesture for this game
        cin >> gesture;
        // Print out the gesture Bessie should play
        if (gesture == "hoof") {
            cout << "paper" << endl;
        } else if (gesture == "paper") {
            cout << "scissors" << endl;
        } else {
            cout << "hoof" << endl;
        }
    }
    return 0;
}
