import pandas as pd
class DataFactory:
    def __init__(self,params):
        self.params=params

    def loadData(self,datapath):
        data=pd.read_csv(datapath,names=self.params["colNames"])
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