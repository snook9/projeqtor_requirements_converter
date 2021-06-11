# Name: projeqtor_requirements_converter
# Authors: Jonathan CASSAING
# Tool for importing requirements in ProjeQtOr software


import csv
from MyException import MyException


# Classe permettant de créer des documents CSV d'exigences, prêts à importer dans le logiciel ProjeQtOr
class CsvDocument:
    # constructeur
    def __init__(self: object):
        pass

    def write(self, file: str, requirements):
        try:
            print("Creation du CSV :", file)
            with open(file, 'w') as csvfile:
                fieldnames = ['id', 'reference', 'name', 'idRequirementType', 'idProject', 'idProduct', 'idComponent', 'externalReference',
                              'creationDateTime', 'idContact', 'originType', 'originId', 'idBusinessFeature', 'idUrgency', 'initialDueDate',
                              'actualDueDate', 'description', 'idRequirement', 'idStatus', 'idResource', 'idCriticality', 'idFeasibility',
                              'idRiskLevel', 'idPriority', 'plannedWork', 'idTargetProductVersion', 'idTargetComponentVersion', 'idMilestone',
                              'handled', 'handledDate', 'done', 'doneDate', 'idle', 'idleDate', 'cancelled', 'result', 'locked', 'idLocker',
                              'lockedDate', 'countTotal', 'countPlanned', 'countPassed', 'countBlocked', 'countFailed', 'countIssues']
                writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)

                writer.writeheader()
                for requirement in requirements:
                    writer.writerow({'externalReference': requirement.ref,
                                     'name': requirement.title,
                                     'description': requirement.body + '\n\n' + requirement.test})
        except MyException as error:
            print(f"L'erreur suivante s'est produite : {error}")
