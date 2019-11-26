from urllib.request import urlopen
from  pprint import pprint
import csv
from io import StringIO
import pandas as pd

link = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/iris.csv"
with urlopen(link) as resp:
    file = resp.read().splitlines()

def parseCSV(bString):
    tempList = list(csv.reader(StringIO(bString.decode('utf-8')),delimiter=','))
    if len(tempList) > 0:
        tempList = tempList[0]
    return tempList

cols = ['sepal_length','sepal_width','petal_length','petal_width','class']
iris = pd.DataFrame([parseCSV(lines) for lines in file], columns = cols)

iris.to_csv('iris_with_labels.csv', index=None)
# def separate_by_class(dataset):
#     separated = dict()
# 	for i in range(len(dataset)):
#         vector = dataset[i]
#         class_value = vector[-1]
# 		if (class_value not in separated):
# 			separated[class_value] = list()
# 		separated[class_value].append(vector)
# 	return separated

