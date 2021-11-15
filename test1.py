# This is a script to test the basic functionality (string representations,
# sizes, value setting/getting, row/column operations) of the Matrix() object
# defined in matrix.py as well as certain expected errors

# Made by Isaac Joffe

import unittest
from matrix import Matrix

class TestMatrix(unittest.TestCase):
    def test_str(self):
        A = Matrix([[1,2,3],[4,5,6],[7,8,9]])
        B = Matrix([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])
        C = Matrix([[1,2,3]])
        D = Matrix([[1],[2],[3]])
        self.assertEqual(str(A), "1 2 3\n4 5 6\n7 8 9")
        self.assertEqual(str(B), " 0  1  2  3\n 4  5  6  7\n 8  9 10 11" + \
            "\n12 13 14 15")
        self.assertEqual(str(C), "1 2 3")
        self.assertEqual(str(D), "1\n2\n3")
        return

    def test_size(self):
        A = Matrix([[1,2,3],[4,5,6],[7,8,9]])
        B = Matrix([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])
        C = Matrix([[1,2,3]])
        D = Matrix([[1],[2],[3]])
        self.assertEqual(A.get_size(), (3,3))
        self.assertEqual(B.get_size(), (4,4))
        self.assertEqual(C.get_size(), (1,3))
        self.assertEqual(D.get_size(), (3,1))
        return

    def test_value(self):
        A = Matrix([[1,2,3],[4,5,6],[7,8,9]])
        B = Matrix([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]])
        C = Matrix([[1,2,3]])
        D = Matrix([[1],[2],[3]])
        self.assertEqual(A.get_value(1,1), 1)
        self.assertEqual(A.get_value(2,2), 5)
        self.assertEqual(A.get_value(3,3), 9)
        self.assertEqual(B.get_value(1,4), 3)
        self.assertEqual(B.get_value(2,3), 6)
        self.assertEqual(B.get_value(3,2), 9)
        self.assertEqual(B.get_value(4,1), 12)
        self.assertEqual(C.get_value(1,2), 2)
        self.assertEqual(D.get_value(2,1), 2)
        A.set_value(3,3,100)
        self.assertEqual(A.get_value(3,3), 100)
        B.set_value(1,1,-10)
        self.assertEqual(B.get_value(1,1), -10)
        C.set_value(1,2,0)
        self.assertEqual(C.get_value(1,2), 0)
        D.set_value(1,1,4.5)
        self.assertEqual(D.get_value(1,1), 4.5)
        return

    def test_row(self):
        pass

    def test_column(self):
        pass

    def test_errors(self):
        pass


if __name__ == "__main__":
    unittest.main()
