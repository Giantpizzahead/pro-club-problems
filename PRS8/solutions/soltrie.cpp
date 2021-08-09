#include <iostream>
#include <string>
#include <cctype>
using namespace std;

const int MAXN = 100005;

struct Node {
    Node* children[27];
    int x, r;

    Node() {
        for (int i = 0; i < 27; i++) children[i] = nullptr;
        x = 0;
        r = 0;
    }

    void addString(string& str, int i, int x, int r) {
        if (i == str.length()) {
            // Done
            markEnd(x, r);
        } else {
            int e = (str[i] == ' ' ? 26 : str[i] - 'a');
            if (children[e] == nullptr) children[e] = new Node();
            children[e]->addString(str, i+1, x, r);
        }
    }

    void markEnd(int x, int r) {
        if (r > this->r) {
            this->r = r;
            this->x = x;
        }
    }

    void dfs() {
        for (int i = 0; i < 27; i++) {
            if (children[i] != nullptr) {
                children[i]->dfs();
                if (this->r < children[i]->r) {
                    this->r = children[i]->r;
                    this->x = children[i]->x;
                }
            }
        }
    }

    int query(string& str, int i) {
        if (i == str.length()) return this->x;
        else {
            int e = (str[i] == ' ' ? 26 : str[i] - 'a');
            if (children[e] == nullptr) return 0;  // Invalid
            else return children[e]->query(str, i+1);
        }
    }

    void print() {
        for (int i = 0; i < 27; i++) {
            if (children[i] != nullptr) {
                cout << (i == 26 ? ' ' : static_cast<char>('a' + i));
                children[i]->print();
                cout << '/';
            }
        }
        cout << " (" << x << ", " << r << ") ";
    }
};

void trim(string& str) {
    while (isspace(str.back())) str.pop_back();
    while (isspace(str.front())) str = str.substr(1);
}

int N, Q;
int R[MAXN];
string W[MAXN], S[MAXN];
Node trie;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    for (int i = 0; i < N; i++) cin >> R[i];
    string temp;
    getline(cin, temp);
    for (int i = 0; i < N; i++) getline(cin, W[i]);
    cin >> Q;
    getline(cin, temp);
    for (int i = 0; i < Q; i++) getline(cin, S[i]);

    for (int i = 0; i < N; i++) {
        trim(W[i]);
        // cout << W[i] << endl;
    }
    for (int i = 0; i < Q; i++) {
        trim(S[i]);
        // cout << S[i] << endl;
    }

    // Add strings to trie
    for (int i = 0; i < N; i++) trie.addString(W[i], 0, i, R[i]);

    // Print trie
    // trie.print();
    trie.dfs();

    // Queries
    for (int i = 0; i < Q; i++) {
        cout << trie.query(S[i], 0) + 1 << '\n';
    }
    return 0;
}