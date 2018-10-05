
import unittest
from sklearn.datasets import load_iris
from iris_classifier.classifier import KNN
from sklearn.neighbors import KNeighborsClassifier

class Test_Classifier(unittest.TestCase):
    def setUp(self):
        self.iris = load_iris()
        self.classifier = KNN(self.iris)
        self.x = self.iris.data
        self.y = self.iris.target
        self.neighbors = 1
    
    def test_shape_data(self):
        self.assertEqual(self.x.shape,  self.classifier.x.shape)
    
    def test_shape_taget(self):
        self.assertEqual(self.y.shape, self.classifier.y.shape)

    def test_neighbors(self):
        self.assertEqual(self.neighbors, self.classifier.neighbors)
    
    def test_KNN(self):
        self.assertIsInstance(self.classifier.model, KNeighborsClassifier)

    def test_classifer_has_train_method(self):
        self.assertTrue(self.classifier.train)