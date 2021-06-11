# Name: projeqtor_requirements_converter
# Authors: Jonathan CASSAING
# Tool for importing requirements in ProjeQtOr software


# imports des couches
from InterfaceUi import InterfaceUi
from SrsDocument import SrsDocument
from CsvDocument import CsvDocument
from Error import Error
from datetime import datetime
from pathlib import Path


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

    def run(self, input_file: Path, output_folder: Path):
        if False == input_file.exists():
            print("Erreur: le fichier ODT '" + str(input_file) + "' n'existe pas")
            return

        if False == input_file.is_file():
            print("Erreur: le fichier ODT '" + str(input_file) + "' n'est pas un fichier")
            return

        if False == output_folder.exists():
            print("Erreur: le dossier '" + str(output_folder) + "' spécifié n'existe pas")
            return

        if False == output_folder.is_dir():
            print("Erreur: le chemin '" + str(output_folder) + "' n'est pas un dossier")
            return

        today = datetime.today()
        output_file = output_folder.joinpath('output_generated_' + today.strftime("%Y-%m-%d-%H-%M-%S.%f") + '.csv')

        print("Fichier ODT d'entrée :", input_file)
        print("Fichier CSV de sortie :", output_file)

        try:
            requirements = self.srs_document.read(input_file)
        except Error as error:
            print(f"Erreur : {error}")
            return

        print("FIN DE L'IMPORT DES EXIGENCES")
        self.displayRequirements(requirements)

        try:
            if requirements is not None:
                self.csv_document.write(output_file, requirements)
        except Error as error:
            print(f"Erreur : {error}")
            return

        print("Fichier '" + str(output_file) + "' créé")


