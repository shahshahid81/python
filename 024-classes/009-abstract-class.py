from abc import ABC, abstractmethod


# needs to inherit ABC since python will use metadata to enforce abstract class method implementation
# @abstractmethod only marks a method as "must be implemented" by setting a flag on it. Inheriting from ABC gives the class the ABCMeta metaclass, which reads those flags, tracks unimplemented abstract methods, and blocks instantiation until they're implemented. This is needed because the default Python metaclass (type) ignores the @abstractmethod flag, so without ABC, no enforcement occurs.
class FileMover(ABC):
    @abstractmethod
    def check_file_exists(self):
        pass

    @abstractmethod
    def file_move(self):
        pass

    def say_hi(self):
        print("Hi")


class CSVFileMover(FileMover):
    def check_file_exists(self):
        print("CSV Exists")

    def file_move(self):
        print("Moving a CSV File")


class XLSXFileMover(FileMover):
    # Below error if method is not implemented from abstract class
    # TypeError: Can't instantiate abstract class XLSXFileMover with abstract method check_file_exists
    def check_file_exists(self):
        print("XLSX Exists")

    def file_move(self):
        print("Moving a XlSX File")


csv_mover = CSVFileMover()
csv_mover.check_file_exists()
csv_mover.file_move()
csv_mover.say_hi()

xlsx_mover = XLSXFileMover()
xlsx_mover.check_file_exists()
xlsx_mover.file_move()
xlsx_mover.say_hi()


class DataProcessor(ABC):
    @abstractmethod
    def read_data(self, source):
        pass

    @abstractmethod
    def process_data(self, data):
        pass

    @abstractmethod
    def write_data(self, destination, data):
        pass
