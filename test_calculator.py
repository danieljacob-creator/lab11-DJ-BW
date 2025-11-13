#https://github.com/danieljacob-creator/lab11-DJ-BW
#Partner 1: Daniel Jacobs
#Partner 2: Bryce Williams



import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        assert add(2,3) == 5
        assert add(-3, 6) == 3
        assert add(0,0) == 0

    def test_subtract(self): # 3 assertions
        assert subtract(5,3) == 2
        assert subtract(3,5) == -2
        assert subtract(0,0) == 0
    # ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertIsEqual(mul(3,4), 12)
        self.assertIsEqual(mul(3, -4), -12)
        self.assertIsEqual(mul(-3, -6), 18)
        self.assertIsEqual(mul(4, 0), 0)

    def test_divide(self): # 3 assertions
        self.assertIsEqual(div(6, 3), 0.5)
        self.assertIsEqual(div(0, 3), "Cannot divide by a = 0")
        self.assertIsEqual(div(3, -6), -2)
        self.assertIsEqual(div(-12,-24), 2)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        assert logarithm(10,100) == math.log(100,10)
        assert logarithm(2,8) == math.log(8,2)
        assert logarithm(5,25) == math.log(25,5)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1,10)
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
        with self.assertRaises(ValueError):
            logarithm(5, 0)
        with self.assertRaises(ValueError):
            logarithm("hi", 3)

    def test_hypotenuse(self): # 3 assertions
        self.assertIsEqual(hypotenuse(3, 4), 5)
        self.assertIsEqual(hypotenuse(-3, -4), 5)
        self.assertIsEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-4)
    #     # Test basic function
        self.assertIsEqual(square_root(4), 2)
        self.assertIsEqual(square_root(0), 0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()