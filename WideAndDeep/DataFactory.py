import pandas as pd
pd.set_option("display.max_columns",None)
class DataFactory:

    def __init__(self,params):
        self.params=params

    def loadData(self,datapath):
        data=pd.read_csv(datapath,names=self.params["colNames"]).dropna()
        return data

    def getDataMap(self):
        pathMap={
            "trainData":self.params["trainData"],
            "testData": self.params["testData"]
        }
        DataMap={}
        for k,v in pathMap.items():
            DataMap[k]=self.loadData(v)
        return DataMap

    def labelData(self,traindata,testdata):
        traindata[self.params["label"]]=(traindata[self.params["labelcol"]].apply(lambda x: 1 if ">50K" in x else 0)).astype(int)
        testdata[self.params["label"]] =(testdata[self.params["labelcol"]].apply(lambda x: 1 if ">50K" in x else 0)).astype(int)
        return traindata,testdata


    def getCorssCols(self,cols):
        corssMap={}
        for col in cols:
            featureName="-".join(col)
            corssMap[featureName]=col
        return corssMap

    def getCrossFeatures(self,data,crossCols):
        for k,v in crossCols.items():
            data[k]=data[v].apply(lambda x:"-".join(x),axis=1)
        return data


    def getColGroup(self,data):
        cutcols=self.params["group_cols"]
        for col in cutcols:
            colname=col+"_group"
            bins=self.params["cutThreshold"][col]
            labels=range(len(bins)-1)
            data[colname]=pd.cut(data[col].astype(int),bins=bins,labels=labels)
        return data



