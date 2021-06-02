# Name: projeqtor_requirements_converter
# Authors: Jonathan CASSAING
# Tool for importing requirements in ProjeQtOr software


import sys
import os


def set_syspath(absolute_dependencies: list):
    # absolute_dependencies : une liste de noms absolus de dossiers

    # on ajoute au syspath les dépendances absolues du projet
    for directory in absolute_dependencies:
        # on vérifie l'existence du dossier
        existe = os.path.exists(directory) and os.path.isdir(directory)
        if not existe:
            # on lève une exception
            raise BaseException(f"[set_syspath] le dossier du Python Path [{directory}] n'existe pas")
        else:
            # on joute le dossier au début du syspath
            sys.path.insert(0, directory)

def configure():
    import os

    # chemin absolu du dossier de ce script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # dépendances absolues
    absolute_dependencies=[
        # les dossiers locaux contenant des classes et interfaces
        f"{script_dir}/interfaces",
        f"{script_dir}/services",
        f"{script_dir}/utils",
    ]

    # mise à jour du syspath
    set_syspath(absolute_dependencies)

    # on rend la config
    return {}