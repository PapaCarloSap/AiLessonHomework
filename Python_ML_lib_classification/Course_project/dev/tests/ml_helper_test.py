import unittest
import numpy as np
import pandas as pd
import Python_ML_lib_classification.Course_project.dev.ml_helper as mlhp

# import sys
# # sys.path.append('/Python_ML_lib_classification/Course_project/dev/')
# sys.path.insert(0, '../Python_ML_lib_classification/Course_project/dev/')
# import ml_helper as mlhp


class TestCalculator(unittest.TestCase):
    #setUp method is overridden from the parent class TestCase
    def setUp(self):
        df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

    #Each test method starts with the keyword test_
    def test_add(self):
        mlhp.add_id(df)


if __name__ == "__main__":
  unittest.main()