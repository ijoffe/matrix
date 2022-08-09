// Small program to test if output is correct

#include <iostream>
#include "matrix.h"

using namespace std;

int main() {
    float values[] = {1.0, 2.1, 3.5, 4.5};
    Matrix A = Matrix(2, 2, values);
    cout << A << endl << endl;
    Matrix B = A;
    cout << B << endl << endl;
    Matrix C = Matrix(2, 2, 2);
    cout << C << endl << endl;
    C[0][0] = 1.5;
    cout << C << endl << endl;
    cout << C[0][0] << endl << endl;
    cin >> C;
    cout << C << endl << endl;
	Matrix D = Matrix(2, 3, 4.0);
    cin >> D;
    Matrix E = Matrix(2, 2, 2.5);
    cout << E << endl;
    cin >> E;
    cout << E << endl;
    cin >> E;
    cout << D << endl << endl;
    cout << -D << endl << endl;
    cout << D+E << endl << endl;
    cout << D-E << endl << endl;
    cout << D.transpose() << endl << endl;
    cout << E*D << endl << endl;
    Matrix F = D;
    cout << D << endl << endl << F << endl << endl;
	return 0;
}