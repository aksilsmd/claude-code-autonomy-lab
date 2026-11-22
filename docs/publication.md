# Publier une version

## 1. Numérotation

Le plugin suit le versionnage sémantique, lu du point de vue de celui qui l'utilise.

| Rang | Quand l'incrémenter | Exemple |
|---|---|---|
| majeur | une commande disparaît ou change de nom, le déroulé des jalons change, un livrable n'est plus produit | `1.3.1` → `2.0.0` |
| mineur | des skills, des agents, des contrôles ou des profils s'ajoutent sans rien retirer | `2.1.0` → `2.2.0` |
| correctif | correction de droit, de norme, de script ou de rédaction, à périmètre constant | `2.2.0` → `2.2.1` |

Le renommage d'une commande est une rupture, même si la fonction reste : les utilisateurs l'ont écrite dans
leurs habitudes et leurs scripts.

## 2. Liste de contrôle

À dérouler dans l'ordre. Chaque étape est vérifiée par un test ou par la CI.

- [ ] **1. La version, aux quatre endroits.** Ils doivent concorder exactement :
  - `dan-cortex/.claude-plugin/plugin.json` → `version`
  - `.claude-plugin/marketplace.json` → `metadata.version` **et** l'entrée du plugin → `version`
  - `CHANGELOG.md` → la **première** entrée, au format `## <x.y.z> — <jour> <mois> <année>`
  - `README.md` → le badge `badge/version-<x.y.z>-`
- [ ] **2. La description et les mots-clés** de `plugin.json` et de l'entrée de la place de marché disent ce que
  la version apporte. Aucun mot-clé en double.
- [ ] **3. Les compteurs**, si le nombre de skills ou d'agents a changé : la ligne `**<n> skills**, **<n> agents**`
  en tête du `README.md` racine, et les lignes `| Skills | <n> |` et `| Agents | <n> |` de `dan-cortex/README.md`.
- [ ] **4. Le catalogue** : chaque nouvelle commande `/dan-cortex:<nom>` est citée dans `docs/commandes.md`
  (ou dans le tableau des pôles du `README.md`) et dans `dan-cortex/README.md`.
- [ ] **5. Le journal** : l'entrée du `CHANGELOG` dit ce qui change pour l'utilisateur, pas ce qui change dans
  les fichiers. Une version n'y figure qu'une fois.
- [ ] **6. L'archive** : `make build`, et `dist/dan-cortex.plugin` entre dans le même commit que les sources.
- [ ] **7. Les contrôles** : `make verify` passe en entier, sur la version finale des fichiers.
- [ ] **8. L'hygiène** : aucun secret, aucune donnée personnelle, aucun chemin de machine, aucune charge utile
  offensive. Les mentions de `NOTICE.md` et `THIRD_PARTY_NOTICES.md` sont intactes.
- [ ] **9. Le commit et l'étiquette** : un commit dédié, puis
  `git tag -a v<x.y.z> -m "Dan-Cortex <x.y.z>"` et `git push --follow-tags`.

## 3. Diffuser

Le plugin atteint les utilisateurs par trois chemins, qui ne se mettent pas à jour ensemble.

| Chemin | Ce qui est servi | Ce qu'il faut faire |
|---|---|---|
| Place de marché dans Claude Code | le dépôt Git que l'utilisateur a ajouté | pousser la version sur la branche par défaut de **ce dépôt-là** ; l'utilisateur fait `/plugin marketplace update cortex-projets` puis `/plugin install dan-cortex@cortex-projets` |
| Place de marché dans l'application Claude | le même dépôt, par **Customize → Plugins → Add → Add marketplace → Add from a repository** | rien de plus, une fois la branche par défaut à jour |
| Plugin personnalisé | le fichier `dist/dan-cortex.plugin` | le téléverser dans l'application ; c'est la copie qui alimente la place de marché « My Uploads » d'un compte |

**Point de vigilance.** Les instructions d'installation du `README.md` nomment le dépôt que les utilisateurs
ajoutent. Si plusieurs dépôts portent la même place de marché `cortex-projets`, la version publiée doit être
poussée dans celui que le `README` indique, sinon `/plugin marketplace update` ne verra rien de neuf. Vérifie ce
point avant d'annoncer une version.

**Les sessions déjà ouvertes ne changent pas de version.** Un plugin est chargé au démarrage d'une session :
après une mise à jour, il faut en ouvrir une nouvelle. Pour une session infonuagique, la copie est synchronisée
côté serveur : rien ne bouge avant que le compte ait reçu la nouvelle archive.

## 4. Après la publication

1. Dans une **session neuve**, vérifie la version affichée dans le menu **Plugins**.
2. Lance `/dan-cortex:lancer-projet` sur un besoin d'essai et vérifie que le chef d'orchestre pose bien sa série
   de questions, puis qu'un jalon se vérifie.
3. Appelle une des commandes **nouvelles** de la version : c'est le défaut qui échappe le plus souvent aux tests,
   car un `SKILL.md` valide peut rester non branché.

## 5. Revenir en arrière

Aucune version n'est corrigée après coup : on en publie une nouvelle.

1. Remets les quatre emplacements de version sur un numéro **supérieur** (`2.2.1`), jamais sur un numéro déjà
   publié.
2. Rétablis le contenu fautif (`git revert` du commit de publication, ou correction ciblée).
3. `make build`, `make verify`, commit, étiquette, pousse.
4. Dis-le dans le `CHANGELOG` : ce qui était cassé, et depuis quelle version.

Ne réutilise jamais un numéro de version déjà diffusé : les copies installées chez les utilisateurs ne se
distingueraient plus. N'exécute aucun ancien paquet de mise à jour (`dan-cortex-update-1.3.0`) : son script
réécrit la version en arrière.
