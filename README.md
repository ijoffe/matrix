# Matrix in Python

## Table of Contents
* [General Info](#general-info)
* [Description](#description)
* [Background](#background)
* [Technologies](#technologies)
* [Instructions](#instructions)
* [Example Usage](#example-usage)

## General Info
This repository contains the code for a Matrix() class in Python, allowing for the creation of and operation on matrices.

## Description
The aim of the project is to create a user-defined class to represent a matrix. I wanted this class to have basic functionality, such as the ability to add, remove, and overwrite elements, but I also want to implement other more adcanced methods, such as the ability to multiply matrices or compute the determinant of a matrix, so it could be used to solve relevant problems.

## Background
My first introduction to computer programming was in my first year of the Engineering program at the University of Alberta. All engineering students had to take ENCMP 100, a coding class based around the language MATLAB, short for matrix laboratory. As the name suggests, much of what one can do in this language, especially what we focused on for general engineering purposes, revolves around the built-in matrix data type. 

When I specialized in Computeer Engineering, I took the class CMPUT 274, which is based in Python. Until this point, my only programming experience was in MATLAB, so I had assumed matrices were a fairly universal data type. When I learned Python did not have such a data type, I wanted to implement one myself.

## Technologies
All code contained is written in Python 3.8.10. I created all the code in this repository using my personal virtual machine, running the Ubuntu distribution of the Linux operating system, through Sublime Text editor and the Linux terminal window.

## Instructions
Currently, the program can only be used directly through a Python interpreter. Upon entering the Python interpreter using `python3` in the Linux terminal window, you can import the class using `from matrix import Matrix` and begin to use the functionality of the class by instantiating objects and operating on them.

Additionally, some unit tests are available to test the functionality of the program. The provided makefile allows for the execution of all the available tests at once. To run all the tests, in the Linux terminal type `make` while in the proper directory.

## Example Usage
```python
from matrix import Matrix

my_matrix = Matrix([[1,2,3],[4,5,6],[7,8,9]])
# Prints a readable representation of the matrix
print(my_matrix)
# Shrinks the matrix down to a 2 x 2 matrix
my_matrix.delete_row(3)
my_matrix.delete_column(3)
print(my_matrix)
```
