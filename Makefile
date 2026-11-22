# Dan-Cortex — point d'entrée des commandes du dépôt.
# Aucune dépendance : Python 3.11 ou plus, bibliothèque standard uniquement.
# Les cibles reprennent, dans le même ordre, les étapes de .github/workflows/tests.yml.

PYTHON ?= python3
PLUGIN := dan-cortex
CORTEX := $(PLUGIN)/skills/lancer-projet/scripts/cortex.py
ROBUSTESSE := $(PLUGIN)/skills/robustesse-agents/scripts/robustesse.py
REGLAGES := $(PLUGIN)/skills/robustesse-agents/assets/reglages-autonomes.json

.DEFAULT_GOAL := help
.PHONY: help verify checklists test archive audit build clean

help: ## Affiche cette aide
	@printf 'Cibles disponibles :\n\n'
	@grep -E '^[a-z-]+:.*?## ' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "} {printf "  \033[36m%-12s\033[0m %s\n", $$1, $$2}'
	@printf '\nAvant toute pull request : make verify\n'

verify: checklists test archive audit ## Lance les quatre contrôles de la CI, dans l'ordre
	@printf '\nTout est vert.\n'

checklists: ## Vérifie le format et le compte des contrôles de couverture
	$(PYTHON) $(CORTEX) plugin verifier

test: ## Lance les tests unitaires
	$(PYTHON) -m unittest discover -s tests -v

archive: ## Vérifie que dist/dan-cortex.plugin est à jour
	$(PYTHON) scripts/construire_plugin.py --verifier

audit: ## Audite le gabarit de réglages du mode autonome
	$(PYTHON) -I $(ROBUSTESSE) audit-config --path $(REGLAGES)

build: ## Reconstruit dist/dan-cortex.plugin (après toute modification du plugin)
	$(PYTHON) scripts/construire_plugin.py

clean: ## Supprime les caches Python (jamais l'archive livrée)
	find . -name __pycache__ -type d -prune -exec rm -rf {} +
	find . -name '*.pyc' -delete
