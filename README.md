# projeqtor_requirements_converter
Ce programme convertit un fichier ODT contenant des exigences vers un fichier CSV, prêt à être importé dans le logiciel ProjeQtOr : https://www.projeqtor.org/

## Dépendances
### odfpy 1.4.1
Installation de la librairie Odfpy.
    
    pip install odfpy

## Utilisation
    python3 main.py [options]
    -h | --help                     : affiche la présente aide
    -v | --version                  : affiche la version du programme
    -i | --inputfile=[filepath]     : spécifie le chemin vers le fichier ODT à convertir
    -o | --outputfolder=[path]      : spécifie le dossier où sera enregistré le fichier CSV, à importer dans ProjeQtOr (par défaut : dossier courant)

### Exemple
La ligne de commande ci-dessous, produit à partir du fichier 'doc/exemple_exigences.odt' un fichier CSV dans le dossier 'doc'.
    
    python3 main.py -i doc/exemple_exigences.odt -o doc/

## Document d'entrée ODT
Le document donné en entrée de l'application doit être au format ODT.
Il peut s'agir d'un document de spécification, qui doit contenir des exigences codifiées.
Exemple de documents : STBL (Spécification Technique de Besoin Logiciel) ou SRS (Software Requirements Specification).

### Format des exigences
Le présent programme détecte les styles créés dans les documents ODT.
Ainsi, chaque exigence doit respecter les noms de style indiqués ci-dessous.

#### Référence d'une exigence
Une exigence doit commencer par un style nommé : **REF-EXIGENCE**.
Il s'agit d'une numéro/libellé servant de référence unique de l'exigence.

#### Titre d'une exigence
Une exigence doit contenir un seul style nommé : **TITRE-EXIGENCE**.
Il s'agit du titre de l'exigence.

#### Contenu d'une exigence
Une exigence doit contenir un seul style nommé : **CORPS-EXIGENCE**.
Il s'agit du contenu de l'exigence.

#### Méthode de vérification d'une exigence
Une exigence doit finir par un style nommé : **VERIF-EXIGENCE**.
Il s'agit de la méthode de vérification de l'exigence.

### Exemple de document de spécification
Vous trouverez un exemple de document de spécification d'exigence dans le document suivant :
    
    doc/exemple_exigences.odt

## Limitations
Une fois le fichier CSV généré, il est nécessaire d'y renseigner manuellement certains champs, comme l'identifiant de votre projet de destination, dans ProjeQtOr.
D'autres champs sont également concernés en fonction de votre besoin.
