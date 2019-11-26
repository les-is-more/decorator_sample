import pandas as pd
from sklearn.model_selection import train_test_split
from  sklearn.tree import DecisionTreeClassifier
from sklearn import metrics


col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
diab = pd.read_csv('./data/diabetes.csv')
diab.columns = col_names

feat_var = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age']
X = diab[feat_var]
Y = diab['label']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 1)

DT_clf = DecisionTreeClassifier()
DT_clf.fit(X_train, Y_train)
Y_pred = DT_clf.predict(X_test)

print("Accuracy: ", metrics.accuracy_score(Y_test, Y_pred))

# we just need to visualize this thing using other option

# from io import StringIO  
# from sklearn.tree import export_graphviz
# import pydotplus

# dot_data = StringIO()
# export_graphviz(DT_clf, out_file = dot_data,  
#                 filled =True, rounded = True,
#                 special_characters = True, feature_names = feat_var, class_names = ['0','1'])

# graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
# graph.write_png('diabetes.png')

# decisionGraph = Source(tree.export_graphviz(DT_clf, 
#                 out_file = None, 
#                 feature_names = features, class_names = ['0', '1'], 
#                 filled = True, rounded = True))

# display(SVG(decisionGraph.pipe(format = "svg")))

dir(breast_cancer)
