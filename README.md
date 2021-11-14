# Matrix in Python
This repository contains the code for a Matrix() class in Python.

## Introduction
My first introduction to computer programming was in my first year of the Engineering program at the University of Alberta. Everyone took ENCMP 100, a coding class based around the language MATLAB, short for matrix laboratory. As the name suggests, much of what one can do in this language, especially what we focused on for general engineering purposes in that class, revolves around the built-in matrix data type. 

When I went into Computeer Engineering, I took the introductory class CMPUT 274, which is based in Python. Until this point, my only programming experience was in MATLAB, so I had assumed matrices were a fairly universal data type. When I learned Python did not have such a data type, I knew I wanted to implement one myself.

The aim of the project was to create a user-defined class to represent a matrix. I wanted this class to have basic functionality, such as the ability to add, remove, and overwrite elements, but I also wanted to implement other more adcanced methods, such as the ability to multiply matrices or compute the determinant of a matrix, so it could be used to solve relevant problems.

## Technologies
All code contained is written in Python 3.6. I created all the code here using my personal virtual machine, running the Ubuntu distribution of the Linux operating system, using Sublime Text editor and the Linux terminal.

## Setup
Currently, the program can only be used through a Python interpreter. Upon entering the Python interpreter using <<python3>>, you can import the class using <<from Matrix import Matrix>> and begin to use the functionality of the class by instantiating objects (for example, <<A = Matrix()>> or <<B = Matrix([[1,2,3],[4,5,6],[7,8,9]])>>).
