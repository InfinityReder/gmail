#coding=utf-8
from sklearn.externals import joblib
import os

# os.chdir("ignore") # ？？？ 这是啥
# from sklearn import svm 
# X = [[0, 0], [1, 1]]
# y = [0, 1] 
# clf = svm.SVC()
# clf.fit(X, y) 
# # clf.fit(train_X,train_y)
# joblib.dump(clf, "train_model.m")



# 本地调取
# clf = joblib.load("train_model.m")

def export_model(clf,model_name = 'trade_txt_analyse_model.m'):
    os.chdir("ignore")
    joblib.dump(clf, model_name)
    return None

def import_model(model_name = 'trade_txt_analyse_model.m'):
    return joblib.load( model_name )

