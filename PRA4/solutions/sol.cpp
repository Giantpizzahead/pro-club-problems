#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

const int MAXN = 100005;
const int MAXM = 75005;

int N, M;
int A[MAXM], B[MAXM];
bool I[MAXM], scanned[MAXN];
string iToName[MAXN];
unordered_map<string, int> nameToI;

bool tryImp(int x) {
    for (int i = 0; i < M; i++) {
        if (A[i] == x) continue;  // Could be fake (from imp)
        if (B[i] != x && I[i]) return false;  // Crewmate lied about imp
        if (B[i] == x && !I[i]) return false;  // Crewmate lied about safe
    }
    return true;
}

vector<int> isImp;

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        string name;
        cin >> name;
        nameToI[name] = i;
        iToName[i] = name;
    }
    cin >> M;
    int ca = -1, cb = -1;
    for (int i = 0; i < M; i++) {
        string name, temp;
        cin >> name >> temp;
        A[i] = nameToI[name];
        cin >> name >> temp;
        B[i] = nameToI[name];
        cin >> name;
        if (name == "impostor") {
            I[i] = true;
            ca = min(A[i], B[i]);
            cb = max(A[i], B[i]);
        } else {
            scanned[B[i]] = true;
        }
        // cout << A[i] << ' ' << B[i] << ' ' << I[i] << endl;
    }

    if (ca == -1) {
        // No accusations; anyone who didn't scan could be imp
        for (int i = 0; i < N; i++) if (!scanned[i]) isImp.push_back(i);
    } else {
        // Accusation; only 2 could be imp
        if (tryImp(ca)) isImp.push_back(ca);
        if (tryImp(cb)) isImp.push_back(cb);
    }

    cout << isImp.size() << endl;
    for (int i = 0; i < isImp.size(); i++) cout << iToName[isImp[i]] << endl;
    return 0;
}