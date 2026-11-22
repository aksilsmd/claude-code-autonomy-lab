# Journal des versions

## 2.2.0 — 22 novembre 2026

- Le réseau passe de 16 à 48 skills et de 45 à 59 agents, et s'ouvre à de nouveaux métiers : recueil du besoin
  par interview adaptée au profil, design de niveau Apple et mouvement d'interface, boîte à outils IT locale,
  cartographie du code en graphe, CRM libre Twenty, atelier d'écriture et maison d'édition, traduction et
  interprétariat (FR/AR/EN), studio 3D et jeu vidéo, 3D web immersive, médias générés par IA, plateforme
  e-learning et reconstruction en salle blanche.
- Ajout de `bibliotheque/` : 173 skills vendorisés (MIT), chargés à la demande par les skills qui en ont besoin
  et non au démarrage de la session, pour ne pas peser sur le contexte.
- Ajout de `universel/` : noyau et version complète du mode universel, connaissances et skill d'accueil.
- Les skills copiés ou adaptés d'anthropics/skills (Apache-2.0) sont attribués dans `dan-cortex/NOTICE.md` et
  `dan-cortex/THIRD_PARTY_NOTICES.md`.
- La matrice de couverture reste à 784 contrôles ; les mentions de version, les compteurs de la documentation et
  l'archive `dist/dan-cortex.plugin` sont réalignés sur cette version.
- Le dépôt est réorganisé aux usages d'un projet public tenu : `AGENTS.md` (et son appel `CLAUDE.md`) énonce les
  invariants, les commandes et la carte des dossiers pour les humains comme pour les agents ; un `Makefile` offre
  un point d'entrée unique (`make verify`, `make build`) aligné sur l'intégration continue ; `SECURITY.md`,
  `CODE_OF_CONDUCT.md`, `SUPPORT.md`, `CODEOWNERS`, les modèles de tickets et de pull request, `dependabot.yml`,
  `.editorconfig` et `.gitattributes` complètent la gouvernance.
- `docs/` reçoit un index, `docs/architecture.md` (anatomie du dépôt et du plugin, garanties de chaque test) et
  `docs/publication.md` (numérotation, liste de contrôle d'une version, canaux de diffusion, retour en arrière).
- Nouveaux garde-fous dans `tests/test_depot.py` : fichiers de gouvernance présents, index de la documentation
  exact, liens relatifs résolus, et Makefile aligné sur les étapes de la CI.

## 1.3.1 — 27 octobre 2026

- Les skills `execution-resiliente` et `confidentialite-traces` sont branchés dans le réseau, par renvoi et sans
  dupliquer leur contenu : le chef d'orchestre sait quand les lire, la reprise d'un jalon bloqué en mode autonome
  suit la boucle de `execution-resiliente`, et les ordres de mission comme le pôle `robustesse-agents` renvoient
  au masquage de `confidentialite-traces`.
- Test : chaque renvoi `${CLAUDE_SKILL_DIR}/../<skill>/…` des skills pointe vers un fichier existant.
- Le paquet de mise à jour 1.3.0 (`apply_update.py`) ne doit plus être relancé : il ramènerait la version à 1.3.0.

## 1.3.0 — Autonomie résiliente et confidentialité

- Ajout du skill `execution-resiliente` : planification orientée critères d'acceptation, récupération après erreur et vérification des résultats.
- Ajout du skill `confidentialite-traces` : masquage des secrets et minimisation des données sensibles.
- Maintien des permissions et de la traçabilité ; aucune falsification des journaux ni contournement des contrôles d'accès.
- Construction reproductible de `dist/dan-cortex.plugin` par `scripts/construire_plugin.py` (fichiers suivis par Git,
  ordre et dates fixes), vérifiée en CI ; tests de cohérence des manifestes, du chargement des skills et du build.

## 1.0.1 — 27 octobre 2026

- `cortex.py registre` accepte `--dossier` (et `--max`) avant, entre ou après les champs `cle=valeur`, y compris
  sous Python 3.11 et 3.12, qui rejetaient jusqu'ici les champs placés après une option. Une option inconnue
  reste refusée.

## 1.0.0 — 27 octobre 2026

Cortex devient **Dan-Cortex** et fusionne avec Claude Code Autonomy Lab.

- Renommage : plugin `dan-cortex`, commandes `/dan-cortex:…`, types d'agents `dan-cortex:<nom>`, dossier
  `dan-cortex/`. Le script `cortex.py` et le fichier `cortex.json` des dossiers projet gardent leur nom : les
  projets existants se reprennent tels quels.
- Niveaux d'autonomie `accompagne`, `delegue`, `autonome` (`init --autonomie`, `etat --set autonomie=…`). En
  `autonome`, le réseau enchaîne tout le périmètre après J0, prend les décisions de type 1 au statut `provisoire`,
  agit dans les autorisations permanentes écrites à J0 et respecte six limites dures.
- Quatorzième skill, `robustesse-agents` : audit des réglages Claude Code, gabarit de réglages pour l'autonomie
  (mode `auto`, bac à sable), corpus de scénarios d'injection d'instructions, évaluation live sur accord, script
  `robustesse.py` et paquet `ccal`.
- Seize contrôles `ROB-` (784 au total) : hygiène des agents de la mission, cadre du mode autonome (étiquette
  `autonome`), fonctions d'IA du produit (étiquette `ia`, alignés sur l'OWASP Top 10 LLM 2025).
- Règle commune aux 45 agents : ce qu'ils lisent est une donnée, jamais un ordre ; aucun vrai secret dans un
  livrable.
- J0 audite les réglages des agents ; J5 exige le rapport de robustesse pour un projet `ia` ; l'`auditeur-securite`
  précharge le nouveau skill.
- Tests automatisés (`tests/`) et intégration continue.

## 0.9.0 — 11 octobre 2026

Première version publique.

- Chef d'orchestre et sept jalons, de l'opportunité au bilan, en trois modes.
- Treize skills : un par pôle, plus les réunions et l'audit général.
- Agents experts natifs aux outils restreints, répartis sur trois niveaux de modèle.
- Matrice de couverture filtrée par type de projet, étiquettes, mode et périmètre.
- Script de pilotage : registres, jalons, traçabilité, cohérence des interactions, journal de consommation.
- Essai en conditions réelles sur le jalon J1 en mode éclair.
