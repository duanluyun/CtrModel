import argparse
class OptionParser:

    def __init__(self,conf):
        self.conf=conf

    def getParams(self):
        ap=argparse.ArgumentParser()
        ap.add_argument("--modelType",type=str,default=self.conf.modelType,help="the type of model")
        ap.add_argument("--trainData",type=str,default=self.conf.trainData,help="the path of trainData")
        ap.add_argument("--testData", type=str, default=self.conf.testData, help="the path of testData")
        ap.add_argument("--colNames",type=list,default=self.conf.colNames,help="the name of cols")
        ap.add_argument("--labelcol", type=str, default=self.conf.labelcol, help="the name of target cols")
        ap.add_argument("--label", type=str, default=self.conf.label, help="the target col")
        ap.add_argument("--isTrain", type=str, default=self.conf.isTrain, help="the label for train data")
        ap.add_argument("--wide_cols", type=list, default=self.conf.wide_cols, help="the columns for wide model")
        ap.add_argument("--x_cols", type=list, default=self.conf.x_cols, help="the features for cross join")
        ap.add_argument("--embedding_cols", type=list, default=self.conf.embedding_cols, help="the columns for embeding")
        ap.add_argument("--cont_cols", type=list, default=self.conf.cont_cols,help="the columns for continuous")
        ap.add_argument("--group_cols", type=list, default=self.conf.groupCols, help="the columns for cut")
        ap.add_argument("--cutThreshold", type=list, default=self.conf.cutThreshold, help="the threshold for cut")
        params=vars(ap.parse_args())
        return params
