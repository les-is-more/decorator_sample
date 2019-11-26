import pandas as pd
from sklearn.preprocessing import LabelEncoder, Imputer, add_dummy_feature, LabelBinarizer, OneHotEncoder, PolynomialFeatures
from sklearn.feature_extraction import DictVectorizer, FeatureHasher

# print(PolynomialFeatures.__doc__)

Feature_Extraction_FCNS = ['DictVectorizer', 'image', 'img_to_graph', 'grid_to_graph', 'text', 'FeatureHasher']
PreProcessing_FNCS = ['Binarizer', 'FunctionTransformer', 'Imputer', 'KBinsDiscretizer', \
    'KernelCenterer', 'LabelBinarizer', 'LabelEncoder', 'MultiLabelBinarizer', 
    'MinMaxScaler', 'MaxAbsScaler', 'QuantileTransformer', 'Normalizer', 'OneHotEncoder', 
    'OrdinalEncoder', 'PowerTransformer', 'RobustScaler', 'StandardScaler', 'add_dummy_feature', 
    'PolynomialFeatures', 'binarize', 'normalize', 'scale', 'robust_scale', 'maxabs_scale', 
    'minmax_scale', 'label_binarize', 'quantile_transform', 'power_transform']

iris = pd.read_csv('iris_with_labels.csv')

# PRE-PROCESSING 1 - Label Encoder: If we want to encode
le_class = LabelEncoder()
le_class.fit(iris['class'])
iris['class_bin'] = le_class.transform(iris['class'])

# LABEL ENCODER: Inverse Transform to retrieve the original label
le_class.inverse_transform(iris['class_bin'])

# To create dummy variables/columns

iris = pd.get_dummies(iris, columns = ['class'], drop_first = True)
print(iris)

import inspect

print(inspect.getsource(pd.get_dummies))
# PRE-PROCESSING 2 - ONE HOT ENCODER : Creates a sparse/dense matrix containing binary columns from a single category
# ohe = OneHotEncoder(handle_unknown='ignore')

# ohe.fit(iris)
# print(ohe.transform(iris))
# print(ohe.categories_)
# print(OneHotEncoder.__doc__)


# Polynomial Features : 

poly_feat = PolynomialFeatures(3)
# print(poly_feat.fit_transform(iris[['petal_width','petal_length']]))
