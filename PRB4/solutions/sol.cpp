#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int N;
struct Person {
    string n;
    int s;

    const bool operator<(const Person& o) const {
        if (s == o.s) return n < o.n;
        else return s > o.s;
    }
};
Person people[105];

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> people[i].n >> people[i].s;
    }
    sort(people, people + N);
    for (int i = 0; i < N; i++) {
        cout << people[i].n << ' ' << people[i].s << endl;
    }
    return 0;
}