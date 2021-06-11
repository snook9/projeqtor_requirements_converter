# Name: projeqtor_requirements_converter
# Authors: Jonathan CASSAING
# Tool for importing requirements in ProjeQtOr software


# autres dépendances
from MyException import MyException
from odf.opendocument import load
from odf import text
from Requirement import Requirement

# Classe pour lire des documents ODT de spécification (SRS - Software Requirements Specification) ou (STBL)
# Une exigence doit commencer par un style REF-EXIGENCE
# Elle doit finir par un style VERIF-EXIGENCE
# Elle doit contenir un seul style TITRE-EXIGENCE
# Elle doit contenir un seul style CORPS-EXIGENCE
class SrsDocument:
    # constructeur
    def __init__(self: object):
        self.requirement_ref_style = "REF-EXIGENCE"
        self.requirement_title_style = "TITRE-EXIGENCE"
        self.requirement_body_style = "CORPS-EXIGENCE"
        self.requirement_test_style = "VERIF-EXIGENCE"

    def displayRequirements(self, requirements):
        for requirement in requirements:
            print("Ref :", requirement.requirement_ref)
            print("Titre :", requirement.requirement_title)
            print("Corps :", requirement.requirement_body)
            print("Vérif :", requirement.requirement_test)

    def read(self, file: str):
        try:
            print("Lecture du fichier :", file)
            doc = load(file)

            requirements = []
            is_requirement_ref_found = False
            # Lecture du document
            for paragraph in doc.getElementsByType(text.P):
                # Recherche d'une référence d'exigence
                if self.requirement_ref_style == paragraph.getAttribute('stylename'):
                    # Si nous en trouvons une, on instancie une exigence
                    is_requirement_ref_found = True
                    requirement = Requirement()
                    requirement.requirement_ref = paragraph
                    print("Ref :", requirement.requirement_ref)

                # Recherche d'un titre d'exigence
                if self.requirement_title_style == paragraph.getAttribute('stylename'):
                    # Seulement si nous avions trouvé une référence d'exigence
                    if True == is_requirement_ref_found:
                        requirement.requirement_title = paragraph
                        print("Titre :", requirement.requirement_title)
                    else:
                        print("Erreur de format : pas de référence d'exigence pour le titre suivant", paragraph)

                # Recherche d'un corps d'exigence
                if self.requirement_body_style == paragraph.getAttribute('stylename'):
                    # Seulement si nous avions trouvé une référence d'exigence
                    if True == is_requirement_ref_found:
                        requirement.requirement_body = paragraph
                        print("Corps :", requirement.requirement_body)
                    else:
                        print("Erreur de format : pas de référence d'exigence pour le contenu suivant", paragraph)

                # Recherche d'une méthode de test d'exigence
                if self.requirement_test_style == paragraph.getAttribute('stylename'):
                    # Seulement si nous avions trouvé une référence d'exigence
                    if True == is_requirement_ref_found:
                        requirement.requirement_test = paragraph
                        print("Vérif :", requirement.requirement_test)
                        # Fin de la création de l'exigence
                        requirements.append(requirement)
                        is_requirement_ref_found = False
                    else:
                        print("Erreur de format : pas de référence d'exigence pour la méthode de test suivante", paragraph)

            print("FIN DE L'IMPORT DES EXIGENCES")
            self.displayRequirements(requirements)

        except MyException as error:
            print(f"L'erreur suivante s'est produite : {error}")
