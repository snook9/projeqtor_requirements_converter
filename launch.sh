#!/bin/bash

cd "$(dirname "$0")"

# Activation de l'environnement virtuel
source venv/bin/activate
# Lancement du scrypt python
python3 main.py $*
