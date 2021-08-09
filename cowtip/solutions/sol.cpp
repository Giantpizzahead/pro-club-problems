#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("cowtip.in");
ofstream fout("cowtip.out");

int N;
bool A[10][10];

int main() {
    fin >> N;
    string str;
    for (int i = 0; i < N; i++) {
        fin >> str;
        for (int j = 0; j < N; j++) {
            A[i][j] = str[j] == '1';
        }
    }
    fin.close();
    int answer = 0;
    for (int i = N-1; i >= 0; i--) {
        for (int j = N-1; j >= 0; j--) {
            if (A[i][j]) {
                answer++;
                for (int k = i; k >= 0; k--) {
                    for (int l = j; l >= 0; l--) {
                        A[k][l] ^= 1;
                    }
                }
            }
        }
    }
    fout << answer << endl;
    fout.close();
    return 0;
}