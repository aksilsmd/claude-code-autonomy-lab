# Contribuer

1. Ouvre une issue qui décrit le manque (contrôle oublié, faille de robustesse, erreur de référence) avec un exemple
   reproductible.
2. Un contrôle s'ajoute par une ligne dans le fichier `checklist-*.md` du pôle, au format des autres, puis
   `python3 skills/lancer-projet/scripts/cortex.py plugin verifier`.
3. Les essais restent locaux par défaut ; tout essai qui appelle un modèle doit être facultatif et documenté.
4. N'ajoute ni vrai secret, ni invite privée, ni donnée personnelle, ni charge utile visant un système tiers.
5. Préfère les contrôles déterministes et indique clairement ce qui relève d'une notation heuristique.
6. Avant une pull request : `python3 -m unittest discover -s tests -v` et le vérificateur de checklists ci-dessus.
