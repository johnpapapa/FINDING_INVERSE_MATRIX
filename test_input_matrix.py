import sys, io
import unittest
from unittest.mock import patch
from matrix import input_matrix

# filepath: /Users/johnpatricklagrimas/Dropbox/sources/finding_inverse_matrix/test_matrix.py

class TestInputMatrix(unittest.TestCase):
    @patch('builtins.input')
    def test_input_matrix_cases(self, mock_input):
        test_cases = [
            {
                "name": "square_matrix",
                "side_effect": ["1 2 3", "4 5 6", "7 8 9", ""],
                "expected": [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]
                ]
            },
            {
                "name": "non_square_matrix",
                "side_effect": ["1 2", "3 4 5", ""],
                "expected": []
            },
            {
                "name": "non_square_matrix",
                "side_effect": ["1 1 1", "3 4 5", "1, 1, 1", "1, 1, 1", ""],
                "expected": []
            },
            {
                "name": "empty_input",
                "side_effect": ["", ""],
                "expected": []
            },
            {
                "name": "invalid_matrix_non_numeric",
                "side_effect": ["1 2 a", "4 5 6", ""],
                "expected": []
            }
        ]

        for case in test_cases:
            with self.subTest(case=case["name"]):
                mock_input.side_effect = case["side_effect"]
                result = input_matrix()
                self.assertEqual(result, case["expected"])

                

if __name__ == '__main__':
    unittest.main()
