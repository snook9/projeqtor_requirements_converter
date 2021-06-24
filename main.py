# Name: projeqtor_requirements_converter
# Authors: Jonathan CASSAING
# Tool for importing requirements in ProjeQtOr software


# on configure l'application
import config
import getopt
import sys

config = config.configure()

from Ui import Ui
from pathlib import Path

program_name = "ProjeQtOr Requirements Converter"
program_version = "0.0.3"


def print_help(script_name: str):
    print(script_name, '[options]\n'
                       'Ce programme convertit un fichier ODT contenant des exigences vers un fichier CSV, '
                       'prêt à être importé dans le logiciel ProjeQtOr.\n'
                       '\t-h | --help\t\t\t: affiche la présente aide\n'
                       '\t-v | --version\t\t\t: affiche la version du programme\n'
                       '\t-i | --inputfile=[filepath]\t: spécifie le chemin '
                       'vers le fichier ODT à convertir\n'
                       '\t-o | --outputfolder=[path]\t: spécifie le dossier '
                       'où sera enregistré le fichier CSV, à importer dans ProjeQtOr (par défaut : dossier courant)')


def parse_opt(script_name: str, argv):
    input_file = Path()
    output_folder = Path("./")
    try:
        opts, args = getopt.getopt(argv, "hvi:o:", ["help", "version", "inputfile=", "ouputfolder="])
    except getopt.GetoptError:
        print_help(script_name)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help(script_name)
            sys.exit()
        elif opt in ("-v", "--version"):
            print(program_name, program_version)
            sys.exit()
        elif opt in ("-i", "--inputfile"):
            input_file = Path(arg)
        elif opt in ("-o", "--ouputfolder"):
            output_folder = Path(arg)

    if not input_file.is_file():
        print('Vous devez indiquer un fichier ODT d\'entrée à convertir.')
        print_help(script_name)
        sys.exit(2)

    return input_file, output_folder


if __name__ == '__main__':
    input_file_selected, output_folder_selected = parse_opt(sys.argv[0], sys.argv[1:])

    # instanciation
    ui = Ui()
    # exécution
    ui.run(input_file_selected, output_folder_selected)
