import unittest
from Problem_1 import Problem_1


class Problem_test(unittest.TestCase):
  def test_solution(self):
    p = Problem_1()
    self.assertEqual(233168, p.solve(1000))


if __name__ == '__main__':
  unittest.main()

