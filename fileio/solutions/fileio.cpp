#include <fstream>
using namespace std;

int main() {
    // Read from a file with ifstream (input file stream)
    ifstream fin("fileio.in");

    // Parse the integer array & find the sum
    int N;
    fin >> N;
    int arr[N];
    for (int i = 0; i < N; i++) {
        fin >> arr[i];
    }
    int sum = 0;
    for (int i = 0; i < N; i++) {
        sum += arr[i];
    }

    // Write to a file with ofstream (output file stream, don't forget to close it)
    ofstream fout("fileio.out");
    fout << sum << endl;
    fout.close();
    return 0;
}