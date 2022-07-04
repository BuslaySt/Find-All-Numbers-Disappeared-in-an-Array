from solution import Solution
import unittest


class Test_findDisappearedNumbers(unittest.TestCase):
    def test1(self):    
        result = Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])
        expected = [5,6]
        self.assertEqual(result, expected)

    def test2(self):    
        result = Solution().findDisappearedNumbers([1,1])
        expected = [2]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()