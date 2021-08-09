#include <bits/stdc++.h>
using namespace std;

const int MAXN = 100005;

void trim(string& str) {
    while (isspace(str.back())) str.pop_back();
    while (isspace(str.front())) str = str.substr(1);
}

int N, Q;
struct Website {
    int r, id;
    string w;
    bool operator<(const Website& o) const {
        return w < o.w;
    }
};
Website W[MAXN];
string rawW[MAXN];
string S[MAXN];

void solve() {
    sort(W, W+N);
    for (int i = 0; i < N; i++) {
        rawW[i] = W[i].w;
        // cout << rawW[i] << endl;
    }
    for (int i = 0; i < Q; i++) {
        string& query = S[i];
        int l = lower_bound(rawW, rawW+N, query) - rawW;
        query += '|';
        int r = lower_bound(rawW, rawW+N, query) - rawW - 1;
        // cout << query << ": " << l << " " << r << endl;
        if (l > r) {
            // Nothing works
            cout << 1 << '\n';
            continue;
        }

        // Everything from l to r works
        int select = l + rand() % (r-l+1);
        cout << W[select].id << '\n';
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> W[i].r;
        W[i].id = i+1;
    }
    string temp;
    getline(cin, temp);
    for (int i = 0; i < N; i++) getline(cin, W[i].w);
    cin >> Q;
    getline(cin, temp);
    for (int i = 0; i < Q; i++) getline(cin, S[i]);

    for (int i = 0; i < N; i++) trim(W[i].w);
    for (int i = 0; i < Q; i++) trim(S[i]);

    solve();
    return 0;
}