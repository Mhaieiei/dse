#!/usr/bin/python
#-*-coding: utf-8 -*-
##from __future__ import absolute_import
######

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
# import pickle
# mod = pickle.load(open('sentiment.mod','rb'))
def get_predict(data):
  # ans = mod.predict(["ดีมาก"])[0]
  # print(ans)
  obj = {
    'Condo_area': data.get('condo-area', 'Bang Kapi'),
    'Adress_TH': data.get('address', 'ถนนเสรีไทย'),
    'Year_built': data.get('year', '2009'),
    'Area_m2': data.get('sqm', 4695.5),
    '#_Tower': data.get('tower', 1),
    '#_Floor': data.get('floor', 8),
    'Sale_Price_Sqm': data.get('price-sqm', 52065),
    'Rental_Yield': data.get('rent-yeild', 5.16),
    'Latitude': data.get('lat', 13.738209),
    'Longtitude': data.get('long', 100.566949),
    'MinDist_Station': data.get('min-dist-station', 1833.883835)
  }
  print(obj)

  # calculate price from model 
  price = 1234567
  return {'result': price}