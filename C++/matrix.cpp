#include <iostream>    // for input and output of matrices
#include "matrix.h"    // includes class declaration

using namespace std;    // eliminate use of std:: prefix

/*
    Creates and fills a matrix of the specified size with all elements as the
    specified initialization value.

    Arguments:
        num_rows (unsigned int):
            the number of rows in the matrix (m for an mxn matrix)
        num_columns (unsigned int):
            the number of columns in the matrix (n for an mxn matrix)
        init (float):
            the numeric value to fill all elements of the matrix as

    Returns:
        None, but creates a matrix object
*/
Matrix::Matrix(unsigned int num_rows, unsigned int num_columns, float init) {
    numbers = new float*[num_rows];    // array of arrays contains each row
    rows = num_rows;
    columns = num_columns;
    // iterate over every element, assigning its value to the specified number
    for (int i = 0; i < rows; i++) {
        float* row = new float[num_columns];    // array for each row
        for (int j = 0; j < columns; j++) {
            *(row + j) = init;    // every value is just the specified number
        }
        *(numbers + i) = row;    // set the row into the matrix
    }
}

/*
    Creates and fills a matrix of the specified size with the values of the
    elements correspoding to the specified array.

    Arguments:
        num_rows (unsigned int):
            the number of rows in the matrix (m for an mxn matrix)
        num_columns (unsigned int):
            the number of columns inthe matrix (n for an mxn matrix)
        arr_ptr (float*):
            a pointer to an array of numbers to fill the matrix with

    Returns:
        None, but creates a matrix object
*/
Matrix::Matrix(unsigned int num_rows, unsigned int num_columns,
        float * arr_ptr) {
    numbers = new float*[num_rows];    // array of arrays contains each row
    rows = num_rows;
    columns = num_columns;
    int counter = 0;    // represents how many numbers we have written so far
    // iterate over every element, assigning its value to corresponding number
    for (int i = 0; i < rows; i++) {
        float* row = new float[num_columns];    // array for each row
        for (int j = 0; j < columns; j++) {
            // current value is next value in the input array
            *(row + j) = *(arr_ptr + counter);
            counter++;    // move along the input array for next assignment
        }
        *(numbers + i) = row;    // set the row into the matrix
    }
}

/*
    Creates and fills a matrix to be identical but distinct from another
    specified matrix.

    Arguments:
        other (Matrix&):
            a reference to the matrix to create based off of

    Returns:
        None, but creates a matrix object identical to another
*/
Matrix::Matrix(const Matrix& other) {
    // create basic info based off of other matrix's attributes
    numbers = new float*[other.get_rows()];
    rows = other.get_rows();
    columns = other.get_columns();
    // iterate over every element, assigning its value to corresponding number
    for (int i = 0; i < rows; i++) {
        float* row = new float[other.get_columns()];    // array for each row
        for (int j = 0; j < columns; j++) {
            // each element at every position is identical to element at same
            // position in the other matrix
            *(row + j) = other[i][j];
        }
        *(numbers + i) = row;    // set the row into the matrix
    }
}

/*
    Destroys the matrix object, freeing all memory associated with it.

    Arguments:
        None

    Returns:
        None, but destroys the matrix object
*/
Matrix::~Matrix() {
    // could not figure out how to properly free the memory, all of these
    // result in errors

    // delete numbers;

    // for (int i = 0; i < rows; i++) {
    //     delete numbers[i];
    // }

    // delete[] numbers;

    // for (int i = 0; i < rows; i++) {
    //     delete[] numbers[i];
    // }

    numbers = NULL;    // remove dangling pointer
}

/*
    Performs matrix addition, producing an output matrix that is the sum of
    the input matrices (each element is sum of corresponding input elements).

    Arguments:
        other (Matrix):
            the other matrix to be added with the present one

    Returns:
        result (Matrix&):
            a reference to the matrix created by addition of the present
            matrix and the other provided matrix
*/
Matrix Matrix::operator+(const Matrix& other) const {
    // create empty (all zeroes) resultant matrix of identical size
    Matrix result(rows, columns, 0.0);
    // iterate over every element, assigning its value to corresponding sum
    for (int i = 0; i < rows; i++) {
        float* row = numbers[i];    // get the current row of present matrix
        for (int j = 0; j < columns; j++) {
            // each element is sum of corresponding element in each matrix
            result[i][j] = row[j] + other[i][j];
        }
    }
    return result;
}

/*
    Performs matrix subtraction, producing an output matrix that is the
    difference of the input matrices (each element is result of subtracting
    each element in the present matrix with the element of the other matrix).

    Arguments:
        other (Matrix):
            the other matrix to be subtracted from the present one

    Returns:
        result (Matrix&):
            a reference to the matrix created by subtraction of the other
            provided matrix from the present one
*/
Matrix Matrix::operator-(const Matrix& other) const {
    // create empty (all zeroes) resultant matrix of identical size
    Matrix result(rows, columns, 0.0);
    // subtraction is the same as addition of a negative
    result = *this + (-other);
    return result;
}

/*
    Performs matrix multiplication, producing an output matrix that is the
    product of the input matrices (each element corresponds to the value
    obtained by multiplying the matrices together).

    Arguments:
        other (Matrix):
            the other matrix to be multiplied with the present one

    Returns:
        result (Matrix&):
            a reference to the matrix created by multiplication of the present
            matrix and the other provided matrix
*/
Matrix Matrix::operator*(const Matrix& other) const {
    // create empty (all zeroes) resultant matrix of proper size (mxn*nxp=mxp)
    Matrix result(rows, other.get_columns(), 0.0);
    // iterate over every element, assigning its value to corresponding number
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < other.get_columns(); j++) {
            for (int k = 0; k < columns; k++) {
                // increment each elements value, starting from the baseline
                // of zero, so that it is the sum of products of the
                // corresponding row and column vectors elements
                result[i][j] += numbers[i][k] * other[k][j];
            }
        }
    }
    return result;
}

/*
    Produces the negation of the matrix, where each element is the negative of
    previous value.

    Arguments:
        None

    Returns:
        result (Matrix):
            the matrix created by flipping the sign of each element of the
            present matrix
*/
Matrix Matrix::operator-() const {
    // create empty (all zeroes) resultant matrix of identical size
    Matrix result(rows, columns, 0.0);
    // iterate over every element, assigning its value to its negative
    for (int i = 0; i < rows; i++) {
        float* row = numbers[i];    // get the current row of present matrix
        for (int j = 0; j < columns; j++) {
            result[i][j] = -row[j];    // flip sign of corresponding element
        }
    }
    return result;
}

/*
    Produces the transpose of the matrix, where the dimensions and values of
    the matrix are flipped in terms of rows and columns.

    Arguments:
        None

    Returns:
        result (Matrix):
            the matrix created by performing the transpose operation on the
            present operation
*/
Matrix Matrix::transpose() const {
    // create empty (all zeroes) resultant matrix of flipped size (mxn->nxm)
    Matrix result(columns, rows, 0.0);
    // iterate over every element, assigning its value to corresponding number
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < columns; j++) {
            // each element has row and column indices swapped
            result[j][i] = numbers[i][j];
        }
    }
    return result;
}

/*
    Indexes into the matrix, allowing for the retrival of a certain element of
    the matrix, as a const method.

    Arguments:
        number (int):
            the row number to retrieve, starting indexing from 0

    Returns:
        row (float*):
            a pointer to an array representing the specified row of the matrix
*/
float* Matrix::operator[](int number) const {
    // return specified row vector
    float* row = numbers[number];
    return row;
}

/*
    Indexes into the matrix, allowing for the retrival of a certain element of
    the matrix, as a nonconst method.

    Arguments:
        number (int):
            the row number to retrieve, starting indexing from 0

    Returns:
        row (float*):
            a pointer to an array representing the specified row of the matrix
*/
float* Matrix::operator[](int number) {
    float* row = numbers[number];
    return row;
}

/*
    Prints the matrix elements to standard output.

    Arguments:
        output (ostream&):
            output stream to write to
        var (Matrix):
            matrix object to be printed out

    Returns:
        output (ostream&):
            output stream to print
*/
ostream& operator<<(ostream& output, Matrix var) {
    // iterate over every element of the matrix to print one by one
    for (int i = 0; i < var.rows; i++) {
        for (int j = 0; j < var.columns; j++) {
            output << var[i][j];    // add each element to output stream
            // add spaces iff element is not the final element of its row
            if (j + 1 != var.columns) {
                output << " ";
            }
        }
        // add newlines iff row is not the final row of the matrix
        if (i + 1 != var.rows) {
            output << endl;
        }
    }
    return output;
}

/*
    Reads matrix data in from standard input and assigns these values to all
    elements in the matrix.

    Arguments:
        input (istream&):
            input stream to fill in
        var (Matrix):
            matrix object to be filled in with input

    Returns:
        input (istream&):
            input stream to associate to values
*/
istream& operator>>(istream& input, Matrix& var) {
    // iterate over every element of the matrix to assign one by one
    for (int i = 0; i < var.get_rows(); i++) {
        for (int j = 0; j < var.get_columns(); j++) {
            // next input number is the next element
            input >> var[i][j];
        }
    }
    return input;
}

/*
    Gives the number of rows in the matrix.

    Arguments:
        None

    Returns:
        rows (int):
            the number of rows in the matrix
*/
int Matrix::get_rows() const {
    // return the private variable containing the number of rows
    return rows;
}

/*
    Gives the number of columns in the matrix.

    Arguments:
        None

    Returns:
        columns (int):
            the number of columns in the matrix
*/
int Matrix::get_columns() const {
    // return the private variable containing the number of columns
    return columns;
}
