# Name: projeqtor_requirements_converter
# Authors: Jonathan CASSAING
# Tool for importing requirements in ProjeQtOr software


# on configure l'application
import config
import getopt
import sys

config = config.configure()

from Ui import Ui

program_name = "ProjeQtOr Requirements Converter"
program_version = "0.0.1"


def print_help(script_name: str):
    print(script_name, '[options]\n'
                       'Ce programme convertit un fichier ODT contenant des exigences vers un fichier CSV, '
                       'prêt à être importé dans le logiciel ProjeQtOr.\n'
                       '\t-h | --help\t\t\t: affiche la présente aide\n'
                       '\t-v | --version\t\t\t: affiche la version du programme\n'
                       '\t-i | --inputfile=[filepath]\t: spécifie le chemin '
                       'vers le fichier ODT à convertir\n'
                       '\t-o | --outputfile=[filepath]\t: spécifie le chemin '
                       'vers le fichier CSV de sortie pour ProjeQtOr')


def parse_opt(script_name: str, argv):
    input_file = ""
    output_file = ""
    try:
        opts, args = getopt.getopt(argv, "hvi:o:", ["help", "version", "inputfile=", "ouputfile="])
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
            input_file = arg
        elif opt in ("-o", "--ouputfile"):
            output_file = arg

    return input_file, output_file


if __name__ == '__main__':
    input_file_selected, output_file_selected = parse_opt(sys.argv[0], sys.argv[1:])

    # instanciation
    ui = Ui()
    # exécution
    ui.run(input_file_selected, output_file_selected)

