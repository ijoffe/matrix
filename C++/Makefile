# The makefile must be in the same directory as all other required files

test: test.o
	g++ test.o -o test -g -std=c++11 -Wall matrix.cpp

test.o: test.cpp matrix.cpp matrix.h
	g++ test.cpp -c

clean:
	rm -f test test.o
