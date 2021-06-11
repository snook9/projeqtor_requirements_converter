# Name: projeqtor_requirements_converter
# Authors: Jonathan CASSAING
# Tool for importing requirements in ProjeQtOr software


# imports
from abc import ABC, abstractmethod


# interface UI
class InterfaceUi(ABC):
    # exécution de la couche UI
    @abstractmethod
    def run(self: object, input_file: str, output_file: str):
        pass
