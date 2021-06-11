# Name: projeqtor_requirements_converter
# Authors: Jonathan CASSAING
# Tool for importing requirements in ProjeQtOr software


# Cette classe représente une exigence, définie par :
# une référence, un titre, un contenu et une méthode de test
class Requirement:
    # constructeurs
    def __init__(self: object):
        pass

    def __init__(self: object, ref="", title="", body="", test=""):
        self.__ref = ref
        self.__title = title
        self.__body = body
        self.__test = test

    @property
    def ref(self: object) -> str:
        return self.__ref

    @property
    def title(self: object) -> str:
        return self.__title

    @property
    def body(self: object) -> str:
        return self.__body

    @property
    def test(self: object) -> str:
        return self.__test

    @ref.setter
    def ref(self: object, ref: str):
        self.__ref = ref

    @title.setter
    def title(self: object, title: str):
        self.__title = title

    @body.setter
    def body(self: object, body: str):
        self.__body = body

    @test.setter
    def test(self: object, test: str):
        self.__test = test