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
  condo_area = data.get('condo-area', 'Bang Kapi')
  address = data.get('address', 'ถนนเสรีไทย คลองจั่น บางกะปิ')
  year = data.get('year', '2011')
  sqm = data.get('sqm', 6470)
  tower = data.get('tower', 2)
  floor = data.get('floor', 30)
  price_sqm = data.get('price-sqm', 52065)
  rent_yeild = data.get('rent-yeild', 5.81)
  rent_yeild_inc = data.get('rent-yeild-inc-year', -23.79)
  lat = data.get('lat', 13.758903)
  long = data.get('long', 100.649395)
  min_dist = data.get('min-dist-station', 3757)
  print(condo_area, address, year, sqm, tower, floor, price_sqm, rent_yeild)
  # feat = bn.nlp.text(sen).getw2v_light()
  res = {
    'condo_area': condo_area,
    'address': address,
    'year': year,
    'sqm': sqm,
    'tower': tower,
    'floor': floor,
    'price_sqm': price_sqm,
    'rent_yeild': rent_yeild,
    'rent_yeild_inc': rent_yeild_inc,
    'lat': lat,
    'long': long,
    'min_dist': min_dist,
    'price predict': 234567
  }
  return {'result':res}