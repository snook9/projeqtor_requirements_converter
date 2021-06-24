#!/bin/bash

cd "$(dirname "$0")"

# Création de l'environnement virtuel
python3 -m venv venv/
# Activation de l'environnement virtuel
source venv/bin/activate
# Installation des dépendances
pip install -r requirements.txt
