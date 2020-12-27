from DataFactory import DataFactory
from OptionParser import OptionParser
from ModelFactory import ModelFactory
import Conf as conf



if __name__ == '__main__':
    optionparser=OptionParser(conf)
    params=optionparser.getParams()
    datafacory=DataFactory(params)
    datamap=datafacory.getDataMap()
    trainData,testData=datafacory.labelData(datamap["trainData"],datamap["testData"])
    modelfactroy=ModelFactory(params,datafacory)
    modelfactroy.wideModel(trainData,testData)










