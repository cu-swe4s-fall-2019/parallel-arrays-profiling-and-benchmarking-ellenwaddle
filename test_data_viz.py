import unittest
import sys
import data_viz as dv

class TestDataViz(unittest.TestCase):

    def test_data_viz_boxplot_name_already_exists(self):
        r=dv.boxplot([1,2,3,4],'empty.txt')
        self.assertEqual(r,'this file name is taken, choose another.')

if __name__=='__main__':
    unittest.main()
