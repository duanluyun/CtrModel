import tensorflow as tf
from tensorflow.python.keras.layers import Dense,Dropout
import pandas as pd

class ModelFactory:
    def __init__(self,params,datafactory):
        self.params=params
        self.datafactory=datafactory


    def wideModel(self,trainData,testData):
        trainData[self.params["isTrain"]]=1
        testData[self.params["isTrain"]] =0
        wideData=pd.concat([trainData,testData])
        crossCols=self.datafactory.getCorssCols(self.params["x_cols"])
        wideData=self.datafactory.getCrossFeatures(wideData,crossCols)
        wideData=self.datafactory.getColGroup(wideData)
        wideCols=self.params["wide_cols"]+list(crossCols.keys())
        wideData=wideData[wideCols+[self.params["label"]]+[self.params["isTrain"]]]












