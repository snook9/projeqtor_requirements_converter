# Name: projeqtor_requirements_converter
# Authors: Jonathan CASSAING
# Tool for importing requirements in ProjeQtOr software


# imports des couches
from InterfaceUi import InterfaceUi
from SrsDocument import SrsDocument
from CsvDocument import CsvDocument

# autres dépendances
from MyException import MyException


class Ui(InterfaceUi):
    # constructeur
    def __init__(self: object):
        self.srs_document = SrsDocument();
        self.csv_document = CsvDocument();

    def displayRequirements(self, requirements):
        for requirement in requirements:
            print("Ref :", requirement.ref)
            print("Titre :", requirement.title)
            print("Corps :", requirement.body)
            print("Vérif :", requirement.test)

    def run(self, input_file: str, output_file: str):
        try:
            print("Fichier ODT d'entrée :", input_file)
            print("Fichier CSV de sortie :", output_file)

            requirements = self.srs_document.read(input_file)

            print("FIN DE L'IMPORT DES EXIGENCES")
            self.displayRequirements(requirements)

            if requirements is not None:
                self.csv_document.write(output_file, requirements)
                print("Fichier", output_file, "créé")

        except MyException as erreur:
            print(f"L'erreur suivante s'est produite : {erreur}")
