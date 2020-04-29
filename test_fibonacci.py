from unittest import TestCase
from fibonacci import Fibonacci

class FibonacciShouldReturn(TestCase):
    def setUp(self):
        self.fibonacci = Fibonacci()

    def test_zeroForFirstNumber(self):
        self.assertEqual(0, self.getNumberAtIndex(0))

    def test_oneForSecondNumber(self):
        self.assertEqual(1, self.getNumberAtIndex(1))

    def test_oneForThirdNumber(self):
        self.assertEqual(1, self.getNumberAtIndex(2))

    def test_twoForFourthNumber(self):
        self.assertEqual(2, self.getNumberAtIndex(3))

    def test_threeForFifthNumber(self):
        self.assertEqual(3, self.getNumberAtIndex(4))

    def test_fiveForSixthNumber(self):
        self.assertEqual(5, self.getNumberAtIndex(5))

    def test_hugeValueForFiftiethNumber(self):
        self.assertTrue(self.getNumberAtIndex(49) > 1000000000)

    def getNumberAtIndex(self, index):
        return self.fibonacci.generate(index + 1)[index]