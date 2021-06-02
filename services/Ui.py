# Name: projeqtor_requirements_converter
# Authors: Jonathan CASSAING
# Tool for importing requirements in ProjeQtOr software


# imports des couches
from InterfaceUi import InterfaceUi

# autres dépendances
from MyException import MyException


class Ui(InterfaceUi):
    # constructeur
    def __init__(self: object):
        pass

    def run(self, input_file: str, output_file: str):
        try:
            print("Fichier ODT d'entrée :", input_file)
            print("Fichier CSV de sortie :", output_file)
        except MyException as erreur:
            print(f"L'erreur suivante s'est produite : {erreur}")
