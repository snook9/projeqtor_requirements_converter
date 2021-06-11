# Name: projeqtor_requirements_converter
# Authors: Jonathan CASSAING
# Tool for importing requirements in ProjeQtOr software


from odf.opendocument import load
from odf import text, teletype
from Requirement import Requirement
from pathlib import Path


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

    def read(self, file: Path):
        doc = load(file)

        requirements = []
        is_requirement_ref_found = False
        # Lecture du document
        for paragraph in doc.getElementsByType(text.P):
            # Recherche d'une référence d'exigence
            if self.requirement_ref_style == paragraph.getAttribute('stylename'):
                # Si nous en trouvons une, on instancie une exigence

                # Si nous avions déjà trouvé une référence, alors il est probable que l'exigence soit mal terminée
                # c'est-à-dire qu'elle ne se termine pas par une méthode de test
                if is_requirement_ref_found:
                    # Alors, on sauvegarde l'exigence que nous avions
                    requirements.append(requirement)

                is_requirement_ref_found = True
                requirement = Requirement()
                requirement.ref = teletype.extractText(paragraph)

            # Recherche d'un titre d'exigence
            if self.requirement_title_style == paragraph.getAttribute('stylename'):
                # Seulement si nous avions trouvé une référence d'exigence
                if is_requirement_ref_found:
                    requirement.title = teletype.extractText(paragraph)
                else:
                    print("Erreur de format : pas de référence d'exigence pour le titre suivant ;", paragraph)

            # Recherche d'un corps d'exigence
            if self.requirement_body_style == paragraph.getAttribute('stylename'):
                # Seulement si nous avions trouvé une référence d'exigence
                if is_requirement_ref_found:
                    requirement.body = teletype.extractText(paragraph)
                else:
                    print("Erreur de format : pas de référence d'exigence pour le contenu suivant ;", paragraph)

            # Recherche d'une méthode de test d'exigence
            if self.requirement_test_style == paragraph.getAttribute('stylename'):
                # Seulement si nous avions trouvé une référence d'exigence
                if is_requirement_ref_found:
                    requirement.test = teletype.extractText(paragraph)
                    # Fin de la création de l'exigence
                    requirements.append(requirement)
                    is_requirement_ref_found = False
                else:
                    print("Erreur de format : pas de référence d'exigence pour la méthode de test suivante ;", paragraph)

        return requirements
