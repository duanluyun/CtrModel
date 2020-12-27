import argparse
class OptionParser:

    def __init__(self,conf):
        self.conf=conf

    def getParams(self):
        ap=argparse.ArgumentParser()
        ap.add_argument("--trainData",type=str,default=self.conf.trainData,help="the path of trainData")
        ap.add_argument("--testData", type=str, default=self.conf.testData, help="the path of testData")
        ap.add_argument("--colNames",type=list,default=self.conf.colNames,help="the name of columns")
        params=vars(ap.parse_args())
        return params
