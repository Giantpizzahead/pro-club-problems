#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("lostcow.in");
ofstream fout("lostcow.out");
int X, Y, L, D, T, answer;

int main() {
    fin >> X >> Y;
    D = 1;
    L = X;
    while (true) {
        T = X + D;
        while (L < T) {
            L++;
            answer++;
            if (L == Y) goto end;
        }
        while (L > T) {
            L--;
            answer++;
            if (L == Y) goto end;
        }
        D *= -2;
    }
    end:
    fout << answer << endl;
    fout.close();
    return 0;
}