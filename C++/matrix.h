#include <iostream>
using namespace std;

/*
    A class to define a matrix object. Stores the dimensions and elements of a
    matrix along with some of its common behvaiours, including addition,
    subtraction, multiplication, negation, and transposition.
*/
class Matrix {
    public:
        // parametrized constructors for class
        Matrix(unsigned int num_rows, unsigned int num_columns, float init);
        Matrix(unsigned int num_rows, unsigned int num_columns, float * arr_ptr);

        // copy constructor for class
        Matrix(const Matrix& other);

        // destructor for class
        ~Matrix();

        // addition of matrices operator
        Matrix operator+(const Matrix& other) const;

        // subtraction of matrices operator
        Matrix operator-(const Matrix& other) const;

        // multiplication of matrices operator
        Matrix operator*(const Matrix& other) const;

        // negation of a matrix operator
        Matrix operator-() const;

        // transpose of a matrix operator
        Matrix transpose() const;

        // access operator, const and nonconst
        float* operator[](int number) const;
        float* operator[](int number);

        // ostream operator for printing
        friend ostream& operator<<(ostream& output, Matrix var);

        // istream operator for reading in data
        friend istream& operator>>(istream& input, Matrix& var);

        // for getting number of rowss in the matrix
        int get_rows() const;

        // for getting number of columns in the matrix
        int get_columns() const;

    private:
        // store array of arrays of numbers in the matrix
        float** numbers;

        // store size of matrix
        int rows, columns;
};
