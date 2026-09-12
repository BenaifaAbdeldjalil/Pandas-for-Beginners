#!/usr/bin/env bash

echo "git starting ......"
echo "\n"

# Vérifier qu'un paramètre est passé
if [ -z "$1" ]; then
  echo "Usage: ./git.sh <parametre>"
  exit 1
fi

PARAM="$1"

echo "Adding file : $PARAM ..."
echo "\n"
echo "\n"

# Exemple 1 : ajouter tous les fichiers modifiés
git add .

echo "Commiting  file : $PARAM ...."
echo "\n"
# Commit avec message personnalisé
git commit -m "add modifications $PARAM"
echo "Commit OK!"
echo "\n"
echo "\n"

echo "Pushing file : $PARAM ..."
echo "\n"
# Push
git push

echo "\n"
echo "git ok!"