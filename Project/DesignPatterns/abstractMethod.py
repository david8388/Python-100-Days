# Python support multiple inheritance, so it doesn't need interface.
# http://net-informations.com/python/iq/interfaces.htm
import abc
from abc import ABC


class TaxCalculator(abc.ABC):
    @abc.abstractmethod
    def calculateTax(self):
        return NotImplemented

# or
#class TaxCalculator(metaclass=abc.ABCMeta):
#    @abc.abstractmethod
#    def calculateTax(self):
#        return NotImplemented


class TaxCalculate2019(TaxCalculator):
    # if not implement abstract method, it will show class XXX must implement all abstract methods
    def calculateTax(self):
        return 0

    def calculateInsurance(self):
        return 1


class TaxCalculate2020(TaxCalculator):
    # if not implement abstract method, it will show class XXX must implement all abstract methods
    def calculateTax(self):
        return 2


def getCalculator():
    return TaxCalculate2019()


if __name__ == '__main__':
    a = getCalculator()
    print('2019 tax was {0}, insurnace was {1}'.format(a.calculateTax(), a.calculateInsurance()))




