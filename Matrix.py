# Made by Isaac Joffe


class Matrix:
    """
    A class to represent a matrix, a two-dimensional array of numbers.

    Attributes
    ----------
        values : list of lists of integer/floating point numbers
            all the elements of the matrix, where each list inside the list
            contains all the elements of a row of the matrix
        m : integer
            numbers of rows in the matrix (for an m x n matrix)
        n : integer
            number of columns in the matrix (for an m x n matrix)

    Methods
    -------
        get_size() :
            gives the size of the matrix (for an m x n matrix)
        get_value() :
            gives the value of a specified element of the matrix
        set_value() :
            changes the avlue fo a specified element of the matrix
        check_validity() :
            determines if the matrix's elements are numbers and if each row
            has the same number of elements (number of columns is constant)
        add_row(row) :
            adds a row of numbers to the matrix
        add_rows(rows) :
            adds a list of rows to the matrix
        delete_row(row) :
            deletes a specified row of the matrix
        add_column(column) :
        add_columns(columns) :
        delete_column(column) :

    Example Usage
    -------------
        A = Matrix()    # Empty matrix
        B = Matrix([[1,2,3],[4,5,6],[7,8,9]])    # 3 x 3 matrix
        C = Matrix([[1,2,3]])    # Row vector
        D = Matrix([[1],[2],[3]])    # Column vector
    """

    def __init__(self, values=[]):
        """
        Instantiates the matrix, assigning all the attributes of the matrix
        either as an empty matrix or based on the inputted values.

        Parameters
        ----------
        values : list of lists of integer/floating point numbers
            elements to be placed in the matrix, default is empty to create
            an empty matrix

        Returns
        -------
            None, but creates the matrix
        """

        # Ensure argument passed in is valid
        assert isinstance(values, list), "Argument must be a list."
        # Instantiate an empty matrix
        self.values = []
        self.__m = 0
        self.__n = 0
        if values:
            self.add_rows(values)    # Add rows if provided
            self.check_validity()    # Ensure matrix is valid
        return

    def __str__(self):
        """
        Gives a string representation of the matrix as a grid of numbers.

        Parameters
        ----------
            None

        Returns
        -------
            matrixString : string
                elements of the matrix represented in an easily printable and
                human-readable form
        """

        # Ensure the matrix is not empty
        assert self.values, "Matrix must not be empty."
        # Determine the largest number of characters among all the elements
        maxLength = 0
        for i in self.values:
            for j in i:
                if len(str(j)) > maxLength:    # Check if longest number
                    maxLength = len(str(j))    # Mark a new maximum length
        # Pad each element with necessary whitespace for readablity
        stringValues = []
        for i in self.values:
            rowValues = []
            for j in i:
                # Create a right-justified string representation of element
                # according to the largest length seen
                rowValues.append(str(j).rjust(maxLength))
            stringValues.append(rowValues)
        # Join strings representing each eleemnt into one single string
        matrixString = []
        for i in stringValues:
            # Join elements of each row into a space-separated string
            matrixString.append(" ".join(i))
        # Join each row into a newline-separated string
        matrixString = "\n".join(matrixString)
        return(matrixString)

    def __repr__(self):
        """
        Gives an official string representation of the matrix.

        Parameters
        ----------
            None

        Returns
        -------
            matrixString : string
                official string representation of the matrix, contaning the
                size of the matrix and the object's id
        """

        m, n = self.get_size()
        matrixString = "{} x {} Matrix object with id of {}.".format(
            m, n, str(id(self)))
        return(matrixString)

    def get_size(self):
        """
        Gives the size of the matrix.

        Parameters
        ----------
            None

        Returns
        -------
            m : integer
                number of rows in the matrix
            n : integer
                number of columns in the matrix
        """

        m, n = self.__m, self.__n    # Get info from private attributes
        return(m, n)

    def get_value(self, row, column):
        """
        Gives the value of a specified element of the matrix.

        Parameters
        ----------
            row : integer
                row number of desired element
            column : integer
                column number of desired element

        Returns
        -------
            value : integer/floating point number
                value of the element at the given location
        """

        # Ensure arguments passed in are valid
        assert isinstance(row, int) and isinstance(column, int), \
            "Location must be an integer value."
        m, n = self.get_size()
        # Ensure matrix is big enough to have the specified index
        assert row <= m and column <= n, \
            "Matrix must be defined at the given location."
        value = self.values[row-1][column-1]    # Index into matrix
        return(value)

    def set_value(self, row, column, value):
        """
        Changes the value of a specified element of the matrix.

        Parameters
        ----------
            row : integer
                row number of element to be changed
            column : integer
                column number of element to be changed
            value : integer/floating point number
                new value for the specified element to take

        Returns
        -------
            None, but updates the matrix elements
        """

        # Ensure arguments passed in are valid
        assert isinstance(row, int) and isinstance(column, int), \
            "Location must be an integer value."
        assert isinstance(value, int) or isinstance(value, float), \
            "Value must be a number."
        m, n = self.get_size()
        # Ensure matrix is big enough to have the specified index
        assert row <= m and column <= n, \
            "Matrix must be defined at the given location."
        self.values[row-1][column-1] = value    # Update value in matrix
        self.check_validity()    # Double check that matrix is still valid
        return

    def check_validity(self):
        """
        Checks if the existing matrix is valid, meaning the matrix has
        elements which are exclusively integer/floating point numbers and has
        all its rows of the same length.

        Paramters
        ---------
            None

        Returns
        -------
            None, but terminates if the matrix is invalid
        """

        m, n = self.get_size()
        # Only check matrix if it is not empty
        if self.values:
            for i in self.values:
                # Terminate if the rows are of different length
                assert len(i) == n, "Rows must be of same length."
                for j in i:
                    # Terminate if any element is not a number
                    assert isinstance(j, float) or isinstance(j, int), \
                        "Elements must be numbers."
        return

    def add_row(self, row):
        """
        Appends a single row to the bottom of the existing matrix.

        Parameters
        ----------
            row : list of integer/floating point numbers
                elements of the row to be added to the matrix

        Returns
        -------
            None, but updates the existing matrix

        See Also
        --------
            add_rows(rows) :
                wrapper function that appends multiple rows at once by calling
                this function repeatedly
        """

        # Ensure argument passed in is valid
        assert isinstance(row, list), "Argument must be a list."
        m, n = self.get_size()
        if self.values:
            # Only add if the new row is the same length as the existing ones
            assert len(row) == n, "Rows must be of same length."
        self.values.append(row)    # Add the new row
        self.__m += 1    # Update number of rows
        self.__n = len(row)    # Update number of columns
        self.check_validity()    # Double check that matrix is still valid
        return

    def add_rows(self, rows):
        """
        Appends more rows to the bottom of the existing matrix.

        Parameters
        ----------
            rows : list of lists of integer/floating point numbers
                elements of the rows to be added to the matrix

        Returns
        -------
            None, but updates the existing matrix

        See Also
        --------
            add_row(row) :
                adds each individual row from the rows variable
        """

        # Ensure argument is valid
        assert isinstance(rows, list), "Argument must be a list."
        for i in rows:
            self.add_row(i)    # Add row by row
        self.check_validity()    # Double check that matrix is still valid
        return

    def delete_row(self, row):
        """
        Removes a specified row of the matrix, moving all rows below up one.

        Parameters
        ----------
            row : integer
                the number of the row to be removed

        Returns
        -------
            None, but updates the matrix elements
        """

        # Ensure argument is valid
        assert isinstance(row, int), "Row index must be an integer."
        m, n = self.get_size()
        # Ensure matrix is big enough to have the specified row
        assert row <= m, "Matrix must be defined at the given location."
        del self.values[row-1]    # Remove the list for that row
        return

    def add_column(self, column):
        pass

    def add_columns(self, columns):
        pass

    def delete_column(self, column):
        pass
