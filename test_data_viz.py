import unittest
import sys
import os
import data_viz as dv


class TestDataViz(unittest.TestCase):

    def test_data_viz_boxplot_name_already_exists(self):
        r = dv.boxplot([1, 2, 3, 4], 'empty.txt', 'SMTS')
        self.assertEqual(r, 'this file name is taken, choose another.')

    def test_data_viz_boxplot_empty_list(self):
        with self.assertRaises(ValueError):
            dv.boxplot([], 'test1.png', 'SMTS')

    def test_data_viz_no_list(self):
        with self.assertRaises(ValueError):
            dv.boxplot(None, 'test1.png', 'SMTS')


if __name__ == '__main__':
    unittest.main()
