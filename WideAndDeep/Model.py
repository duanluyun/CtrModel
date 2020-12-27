from DataFactory import DataFactory
from OptionParser import OptionParser
import Conf as conf


if __name__ == '__main__':
    optionparser=OptionParser(conf)
    params=optionparser.getParams()
    datafacory=DataFactory(params)
    datamap=datafacory.getDataMap()
    print(datamap["trainData"].columns)



