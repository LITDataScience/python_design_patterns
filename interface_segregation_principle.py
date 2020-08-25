# ISP
from abc import abstractmethod


class Machine:
    def print(self, document):
        raise NotImplementedError

    def scan(self, document):
        raise NotImplementedError

    def fax(self, document):
        raise NotImplementedError


class MultiFunctionPrinter(Machine):
    def print(self, document):
        pass

    def scan(self, document):
        pass

    def fax(self, document):
        pass


class OldFashionedPrinter(Machine):
    def print(self, document):
        # OK
        raise NotImplementedError('Unable to print')

    def scan(self, document):
        raise NotImplementedError('Unable to scan') # No operation here

    def fax(self, document):
        raise NotImplementedError('Unable to fax')


class Printer:

    @abstractmethod
    def print(self, document):
        pass


class Scanner:

    @abstractmethod
    def scan(self, document):
        pass