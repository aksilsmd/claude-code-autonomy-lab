# Politique de sécurité

## Versions suivies

| Version | Suivie |
|---|---|
| 2.2.x | oui |
| 2.1.x et antérieures | non — mets à jour le plugin |

Une seule ligne de version est maintenue à la fois. Les correctifs sortent dans une nouvelle version de
`dan-cortex`, jamais sous forme de rustine appliquée à une version passée.

## Signaler une faille

**N'ouvre pas de ticket public** pour une faille.

1. Va dans l'onglet **Security** du dépôt, puis **Report a vulnerability** (signalement privé de GitHub).
2. Si cet onglet n'est pas disponible, ouvre un ticket qui demande un canal privé, **sans aucun détail
   technique**, et attends la réponse pour transmettre le reste.

Dans ton signalement, indique : la version du plugin, la skill ou le script concerné, les étapes de
reproduction, l'effet obtenu, et ce que tu estimes être l'impact. Un exemple minimal reproductible vaut mieux
qu'une longue description.

Ce dépôt est maintenu par une seule personne : la réponse se fait au mieux, sans engagement de délai. Tu seras
tenu informé de la correction et cité dans le journal des versions si tu le souhaites.

## Périmètre

**Dans le périmètre**

- les scripts Python du plugin (`dan-cortex/skills/*/scripts/`) et `scripts/construire_plugin.py` : exécution de
  code non voulue, traversée de chemin, injection de commande, lecture ou écriture hors du dossier projet ;
- les gabarits de réglages Claude Code fournis par le pôle `robustesse-agents` : tout réglage qui élargirait les
  permissions au-delà de ce qu'il annonce ;
- les instructions des skills et des agents : toute formulation qui conduirait un agent à exfiltrer un secret, à
  agir hors de l'espace de travail sans autorisation, ou à traiter un contenu lu comme un ordre ;
- l'archive `dist/dan-cortex.plugin` : contenu qui ne correspondrait pas aux fichiers suivis par Git.

**Hors périmètre**

- Claude, Claude Code et la plateforme Anthropic : signale-les à Anthropic ;
- les dépendances vendorisées de `dan-cortex/bibliotheque/` et `dan-cortex/universel/` : la correction va chez
  leur auteur amont, préviens-nous pour que nous mettions la copie à jour ;
- les outils tiers que la documentation cite (Blender, Godot, Twenty, Canvas LMS, IT-Tools…) ;
- l'exactitude juridique ou normative d'un contenu : c'est une anomalie de documentation, pas une faille. Ouvre
  un ticket « correction normative » ;
- un rapport produit par un scanner automatique, sans preuve d'exploitabilité.

## Ce que ce dépôt ne contient pas, et n'acceptera pas

Le plugin encadre des tests de sécurité **autorisés** ; il ne contient aucune technique d'attaque, aucun
exploit, aucune charge utile visant un système tiers. Une contribution qui en apporterait serait refusée. Les
scénarios d'injection d'instructions du pôle `robustesse-agents` servent à éprouver un produit **dont tu es
responsable**, et restent locaux par défaut.

Les tests de sécurité menés avec Dan-Cortex ne visent que les environnements du projet, avec l'autorisation
écrite de leur propriétaire.
