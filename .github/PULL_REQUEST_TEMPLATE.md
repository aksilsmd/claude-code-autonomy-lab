## Ce que fait cette pull request

<!-- Une à trois phrases. Ce qui change, et pour quel manque. -->

## Pourquoi

<!-- Le ticket lié (« Corrige #12 »), ou le besoin si aucun ticket n'existe. -->

## Nature du changement

- [ ] Contrôle de couverture ajouté ou corrigé
- [ ] Skill ou agent modifié
- [ ] Correction de droit, de norme ou de version d'outil (source citée ci-dessous)
- [ ] Script ou outillage du dépôt
- [ ] Documentation
- [ ] Nouvelle version du plugin

## Sources

<!-- Pour toute affirmation de droit, de norme ou de sécurité : le texte, l'article, la page, sa date.
     « À vérifier » est une réponse acceptable, à condition d'être écrite dans le fichier. -->

## Vérifications

- [ ] `make verify` passe en entier, et je cite ci-dessous son résultat réel
- [ ] `make build` relancé si `dan-cortex/` a changé, et `dist/dan-cortex.plugin` est dans le commit
- [ ] version concordante aux quatre endroits si elle change (`plugin.json`, `marketplace.json`, `CHANGELOG.md`, badge du `README.md`)
- [ ] compteurs et catalogues des deux README à jour si un skill ou un agent est ajouté
- [ ] aucun secret, aucune donnée personnelle, aucune charge utile offensive ajoutés
- [ ] les mentions de licence de `NOTICE.md` et `THIRD_PARTY_NOTICES.md` sont intactes

```
<!-- Colle ici la fin de la sortie de make verify. -->
```

## Ce que la revue doit regarder en premier

<!-- Le fichier ou la décision sur laquelle tu veux un avis. -->
