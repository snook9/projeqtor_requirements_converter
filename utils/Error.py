# Name: projeqtor_requirements_converter
# Authors: Jonathan CASSAING
# Tool for importing requirements in ProjeQtOr software


# une classe d'exception propriétaire dérivant de [BaseException]
class Error(Exception):
    # constructeur
    def __init__(self: Exception, code: int, message: str):
        # parent
        Exception.__init__(self, message)
        # code erreur
        self.code = code

    # toString
    def __str__(self):
        return f"Exception[{self.code}, {super().__str__()}]"

    # getter
    @property
    def code(self) -> int:
        return self.__code

    # setter
    @code.setter
    def code(self, code: int):
        self.__code = code
