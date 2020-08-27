#!/usr/bin/python
#-*-coding: utf-8 -*-
##from __future__ import absolute_import
######
# import botnoi as bn
# import pickle
# import pandas as pd
# from sklearn.svm import LinearSVC
# import numpy as np

# def trainmodel(modelFileName='condoprice.mod'):
#     ### extract feature
#     goodfeat = [bn.nlp.text(sen).getw2v_light() for sen in goodlist]
#     badfeat = [bn.nlp.text(sen).getw2v_light() for sen in badlist]
#     ### create training set
#     nlpdataset = pd.DataFrame()
#     nlpdataset['feature'] = goodfeat + badfeat
#     nlpdataset['label'] = ['good']*5 + ['bad']*5
#     ### train model
#     clf = LinearSVC()
#     mod = clf.fit(np.vstack(nlpdataset['feature'].values),nlpdataset['label'].values)
#     ### save model
#     pickle.dump(mod,open(modelFileName,'wb'))
#     return 'model created'

### load model
#mod = pickle.load(open('condoprice.mod','rb'))
def get_predict(arg1,arg2,arg3):
  print(arg1, arg2, arg3)
  # feat = bn.nlp.text(sen).getw2v_light()
  res = {
    'arg1': arg1,
    'arg2': arg2,
    'arg3': arg3,
    'price predict': 234567
  }
  return {'result':res}