# Made by Isaac Joffe

class Matrix:
	"""
	A class to represent a matrix, a two-dimensional array of numbers.

	Attributes
	----------
		values : list of lists of integer/float numbers
			all the elements of the matrix, where each list inside the list
			contains all the elements of a row of the matrix
		m : integer
			numbers of rows in the matrix (for an m x n matrix)
		n : integer
			number of columns in the matrix (for an m x n matrix)

	Methods
	-------
		check_validity() :
			determines if the matrix's elements are numbers and if each row
			has the same number of elements (number of columns is constant)
		add_row(row) :
			adds a row of numbers to the matrix
		add_rows(rows) :
			adds a list of rows to the matrix
		get_size() :
			gives the size of the matrix (for an m x n matrix)
	"""

	def __init__(self, values=[]):
		"""
		Instantiates the matrix, assigning all the attributes of the matrix
		either as an empty matrix or based on the inputted values.

		Parameters
		----------
		values : list of lists of integer/float numbers
			elements to be placed in the matrix, default is empty to create
			an empty matrix

		Returns
		-------
			None, but creates the matrix
		"""

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

		matrixString = []
		for i in self.values:
			# Join elements of each row into a space-separated string
			matrixString.append(" ".join(list(map(str,i))))
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
		matrixString = "{} x {} Matrix object with id of {}.".format(m, n, str(id(self)))
		return(matrixString)

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

		# Only check matrix if it is not empty
		if self.values:
			lengths = []
			for i in self.values:
				lengths.append(len(i))    # Document length of each row
				for j in i:
					# Terminate if any element is not a number
					assert isinstance(j, float) or isinstance(j, int), "Element is of invalid type"
			# Terminate if the rows are of different length
			assert min(lengths) == max(lengths), "Rows are of different length"
		return

	def add_row(self, row):
		"""
		Appends a single row to the bottom of the existing matrix.

		Parameters
		----------
			row : list of integer/float numbers
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

		if self.values:
			# Only add if the new row is the same length as the existing ones
			assert len(row) == self.__n
		self.values.append(row)    # Add the new row
		self.__m += 1    # Update number of rows
		self.__n = len(row)    # Update number of columns
		self.check_validity()    # Ensure matrix is still valid
		return

	def add_rows(self, rows):
		"""
		Appends more rows to the bottom of the existing matrix.

		Parameters
		----------
			rows : list of lists of integer/float numbers
				elements of the rows to be added to the matrix

		Returns
		-------
			None, but updates the existing matrix

		See Also
		--------
			add_row(row) :
				adds each individual row from the rows variable
		"""

		for i in rows:
			self.add_row(i)    # Add row by row
		self.check_validity()    # Ensure matrix is still valid
		return

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
			n :
				number of columns in the matrix
		"""

		m, n = self.__m, self.__n
		return(m, n)
