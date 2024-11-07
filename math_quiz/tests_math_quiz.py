import unittest
from math_quiz import get_random_integer, get_random_operator, generate_problem

class TestMathQuizFunctions(unittest.TestCase):

    def test_get_random_integer(self):
        
        result = get_random_integer(1, 10)
        self.assertGreaterEqual(result, 1)
        self.assertLessEqual(result, 10)

        result = get_random_integer(5, 15)
        self.assertGreaterEqual(result, 5)
        self.assertLessEqual(result, 15)

    def test_get_random_operator(self):
       
        result = get_random_operator()
        self.assertIn(result, ['+', '-', '*'])

    def test_generate_problem(self):
       
        problem, answer = generate_problem(5, 3, '+')
        self.assertEqual(problem, "5 + 3")
        self.assertEqual(answer, 8)

        problem, answer = generate_problem(5, 3, '-')
        self.assertEqual(problem, "5 - 3")
        self.assertEqual(answer, 2)

        problem, answer = generate_problem(5, 3, '*')
        self.assertEqual(problem, "5 * 3")
        self.assertEqual(answer, 15)

if __name__ == '__main__':
    unittest.main()
