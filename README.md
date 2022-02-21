# Matrix in Python

## Table of Contents
* [General Information](#general-information)
* [Description](#description)
* [Background](#background)
* [Technologies](#technologies)
* [Instructions](#instructions)
* [Example Usage](#example-usage)

## General Information
This repository contains the code for a `Matrix` class in Python, allowing for the creation of, manipulation of, and operation on matrices. All code was created by me, Isaac Joffe, from November of 2021 to January of 2022.

## Description
The aim of the project is to create a user-defined class to represent a matrix. This class has basic functionality, such as the ability to add, remove, delete, and overwrite matrix rows, columns, and elements, but it also has a growing number of more advanced methods. Currently, the transpose operation, determinant computation, scalar addition and multiplication as well as matrix addition and multiplication are supported, and I plan to add more functionality, such as the ability to compute the inverse of a matrix.

## Background
Matrices are essentially a two-dimensional array of numbers. They are widely used in mathematics, with countless applications in science and engineering. The code contained is designed to support mostly applications in the field of linear algebra, such as the ability to compute a matrix's determinant and the product of two matrices. More information about matrices and their uses and history can be found at the following link: https://en.wikipedia.org/wiki/Matrix_(mathematics).

My first introduction to computer programming was in my first year of the Engineering program at the University of Alberta. All engineering students had to take ENCMP 100, a coding class based around the language MATLAB, short for matrix laboratory. As the name suggests, much of what one can do in this language revolves around the built-in matrix data type. This was especially true for what we focused on for our general engineering purposes in that class. 

When I specialized in Computer Engineering, I took the class CMPUT 274, which is based in Python. Up until this point, my only programming experience was in MATLAB, so I had assumed matrices were a fairly universal data type. When I learned Python did not have such a data type, I decided to implement one myself.

## Technologies
All code contained is written in Python 3.8.10, except for the makefile used to run unit tests. I created all the code and files in this repository using my personal virtual machine, which runs the Ubuntu distribution of the Linux operating system, through the Sublime Text text editor and the Linux terminal window.

## Instructions
Currently, the program can only be used directly through a Python interpreter. Upon entering the Python interpreter using `python3` in the Linux terminal window, you can import the class using `from matrix import Matrix` and begin to use the functionality of the class by instantiating objects and operating on them.

Additionally, unit tests are available to test the functionality of the program. The provided makefile allows for the execution of all the available tests at once. To run all the tests, in the Linux terminal type `make` while in the proper directory.

## Example Usage
```python
from matrix import Matrix

my_matrix = Matrix([[1,2,3],[4,5,6]])    # Instantiates a 2 x 3 matrix
print(my_matrix)    # Prints a readable representation of the matrix

my_matrix.add_row([7,8,9])    # Appends another row to the bottom
print(my_matrix)    # Prints a readable representation of the matrix

my_matrix = my_matrix.transpose()    # Transposes matrix
print(my_matrix)    # Prints a readable representation of the matrix
print(my_matrix.determinant())    # Prints the scalar determinant of a matrix
```
