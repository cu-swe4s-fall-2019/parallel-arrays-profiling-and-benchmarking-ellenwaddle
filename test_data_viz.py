import unittest
import sys
import os
import data_viz as dv
import random

#def boxplot(L, out_file_name, x_axis, y_axis, title, groups = None):

class TestDataViz(unittest.TestCase):

    def test_data_viz_boxplot_name_already_exists(self):
        L = [1, 2, 3, 4]
        r = dv.boxplot(L, 'empty.txt','x','y','title')
        self.assertEqual(r, 'this file name is taken, choose another.')

    def test_data_viz_boxplot_empty_list(self):
        with self.assertRaises(ValueError):
            dv.boxplot([], 'test1.png','x','y','title' )

    def test_data_viz_no_list(self):
        with self.assertRaises(ValueError):
            L = []
            dv.boxplot(L, 'test1.png', 'x','y','title')
        self.assertFalse(os.path.exists('test1.png'))

    def test_boxplot_one_boxplot(self):
        file_name = 'out.png'
        data = [1, 2, 3]
        for i in range(100):
            data.append(random.randint(0,1000))
        dv.boxplot(data,file_name, 'x', 'y', 'title')
        self.assertTrue(os.path.exists(file_name))

    def test_boxplot_many_boxplot(self):
        file_name = 'many.png'
        data = []
        for j in range(10):
            d = []
            for i in range(100):
                d.append(random.randint(0,1000))
            data.append(d)
        dv.boxplot(data,file_name, 'x', 'y', 'title')
        self.assertTrue(os.path.exists(file_name))

    def test_boxplot_name_boxes(self):
        file_name = 'nameboxes.png'
        data = []
        groups = []
        for j in range(10):
            d = []
            groups.append('Sample ' + str(j))
            for i in range(100):
                d.append(random.randint(0,1000))
            data.append(d)
        dv.boxplot(data, file_name, 'x', 'y', 'title', groups)
        self.assertTrue(os.path.exists(file_name))


if __name__ == '__main__':
    unittest.main()
