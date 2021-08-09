#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

int N;
int X[100];

vector<int> cows;
queue<pair<int, int>> q;

int tryCow(int ci) {
    cows.clear();
    for (int i = 0; i < N; i++) if (i != ci) cows.push_back(X[i]);
    int answer = 1;
    q.emplace(X[ci], 1);
    while (!q.empty()) {
        pair<int, int> p = q.front();
        q.pop();
        // cout << "pair " << p.first << " " << p.second << endl;
        for (int i = 0; i < cows.size(); i++) {
            if (abs(cows[i] - p.first) <= p.second) {
                q.emplace(cows[i], p.second + 1);
                cows.erase(cows.begin()+i);
                i--;
                answer++;
            }
        }
        // cout << "cows ";
        // for (int x : cows) cout << x << ' ';
        // cout << endl;
    }
    return answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    freopen("angry.in", "r", stdin);
    freopen("angry.out", "w", stdout);

    cin >> N;
    for (int i = 0; i < N; i++) cin >> X[i];
    sort(X, X+N);

    int answer = 0;
    for (int i = 0; i < N; i++) {
        answer = max(tryCow(i), answer);
        // cout << tryCow(i) << " " << i << endl;
    }
    cout << answer << endl;

    fclose(stdin);
    fclose(stdout);
    return 0;
}