from features import *
from functools import partial
from sklearn import naive_bayes
from sklearn import tree
from sklearn import linear_model
from sklearn import svm
from sklearn import ensemble
from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn import decomposition

class ScikitWrapper(object):
    def __init__(self, engine, features_to_use, dataset):
        self.feature_handler = FeatureHandler(
                use_features(features_to_use),
                dataset)
        self.engine = engine
        vector, labels = self.feature_handler.sklearn_format_train()
        self.engine.fit(vector, labels)

    def predict(self, items):
        return self.engine.predict(self.feature_handler.sklearn_format_test(items))

def NaiveBayes(dataset):
    return ScikitWrapper(naive_bayes.MultinomialNB(), [reversed_horizontal_silhouette, horizontal_silhouette], dataset)

def DecisionTree(dataset):
    return ScikitWrapper(tree.DecisionTreeRegressor(), [positions, reversed_horizontal_silhouette, horizontal_silhouette], dataset)

def SGD(dataset):
    return ScikitWrapper(linear_model.SGDClassifier(loss="hinge", penalty="l2"), [positions, reversed_horizontal_silhouette, horizontal_silhouette], dataset)

def SVM(dataset):
    return ScikitWrapper(svm.SVC(kernel='poly', degree=2), [vertical_symmetry, horizontal_symmetry, positions], dataset)

def NN(dataset):
    return ScikitWrapper(NearestCentroid(), [positions, reversed_horizontal_silhouette, horizontal_silhouette], dataset)

def RandomForest(dataset):
    return ScikitWrapper(ensemble.RandomForestClassifier(n_estimators=300, n_jobs=8), [x_histogram, y_histogram, positions, number_of_whites, number_of_pixels, horizontal_silhouette, reversed_horizontal_silhouette, vertical_silhouette, reversed_vertical_silhouette, middle_silhouette, vertical_symmetry, horizontal_symmetry], dataset)
