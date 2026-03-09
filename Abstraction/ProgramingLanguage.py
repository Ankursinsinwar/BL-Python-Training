from abc import ABC, abstractmethod

class ProgramingLanguage(ABC):

    @abstractmethod
    def run(self):
        pass


class Python(ProgramingLanguage):
    def run(self):
        print(self.__class__.__name__,"Use Interpriter")


class Cpp(ProgramingLanguage):
    def run(self):
        print(self.__class__.__name__,"Use Compiler")


python = Python()
python.run()

cpp = Cpp()
cpp.run()