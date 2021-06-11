# Name: projeqtor_requirements_converter
# Authors: Jonathan CASSAING
# Tool for importing requirements in ProjeQtOr software


# Cette classe représente une exigence, définie par :
# une référence, un titre, un contenu et une méthode de test
class Requirement:
    # constructeurs
    def __init__(self: object):
        pass

    def __init__(self: object, requirement_ref="", requirement_title="", requirement_body="", requirement_test=""):
        self.__requirement_ref = requirement_ref
        self.__requirement_title = requirement_title
        self.__requirement_body = requirement_body
        self.__requirement_test = requirement_test

    @property
    def requirement_ref(self: object) -> str:
        return self.__requirement_ref

    @property
    def requirement_title(self: object) -> str:
        return self.__requirement_title

    @property
    def requirement_body(self: object) -> str:
        return self.__requirement_body

    @property
    def requirement_test(self: object) -> str:
        return self.__requirement_test

    @requirement_ref.setter
    def requirement_ref(self: object, requirement_ref: str):
        self.__requirement_ref = requirement_ref

    @requirement_title.setter
    def requirement_title(self: object, requirement_title: str):
        self.__requirement_title = requirement_title

    @requirement_body.setter
    def requirement_body(self: object, requirement_body: str):
        self.__requirement_body = requirement_body

    @requirement_test.setter
    def requirement_test(self: object, requirement_test: str):
        self.__requirement_test = requirement_test