import unittest
import numpy as np
from ml.model_training import train_model

class TestModelTraining(unittest.TestCase):
    def test_model_training(self):
        X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        y = np.array([0, 1, 0, 1])
        model = train_model(X, y)
        self.assertIsNotNone(model)

if __name__ == '__main__':
    unittest.main()
