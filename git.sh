#!/usr/bin/env bash

echo "git starting ......"

# Vérifier qu'un paramètre est passé
if [ -z "$1" ]; then
  echo "Usage: ./git.sh <parametre>"
  exit 1
fi

PARAM="$1"

echo "Add file"

# Exemple 1 : ajouter tous les fichiers modifiés
git add .

echo "Commit..."
# Commit avec message personnalisé
git commit -m "add modifications $PARAM"
echo "Commit OK!"

echo "Push..."
# Push
git push


echo "git ok!"