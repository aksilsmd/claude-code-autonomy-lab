"""Le dépôt lui-même : gouvernance présente, index de la documentation exact, liens valides, CI et Makefile alignés."""
import re
import unittest
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
WORKFLOW = RACINE / ".github" / "workflows" / "tests.yml"
MAKEFILE = RACINE / "Makefile"

# Fichiers attendus d'un dépôt public tenu. Ceux qui portent un texte doivent dire quelque chose ;
# les pointeurs et les fichiers de réglage sont courts par nature et seulement vérifiés non vides.
POINTEURS = (
    "CLAUDE.md",
    "Makefile",
    ".editorconfig",
    ".gitattributes",
    ".gitignore",
    ".github/CODEOWNERS",
    ".github/dependabot.yml",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/workflows/tests.yml",
)

DOCUMENTS = (
    "README.md",
    "LICENSE",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "AGENTS.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
    "docs/README.md",
    "docs/architecture.md",
    "docs/publication.md",
)

GOUVERNANCE = DOCUMENTS + POINTEURS

# Les liens relatifs de ces fichiers doivent résoudre. expertise.md en est exclu : c'est un rapport sourcé,
# dont les liens sont externes et nombreux.
DOCUMENTS_LIES = tuple(
    n for n in DOCUMENTS if n.endswith(".md")
) + ("CLAUDE.md", "docs/essai-a-blanc.md")

LIEN = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
TITRE = re.compile(r"(?m)^#{1,6} +(.+?)\s*$")


def ancre(titre):
    """L'ancre que GitHub fabrique à partir d'un titre Markdown."""
    titre = titre.replace("`", "").strip().lower()
    garde = [c for c in titre if c.isalnum() or c in " -_"]
    return "".join(garde).strip().replace(" ", "-")


def ancres_de(chemin):
    return {ancre(x) for x in TITRE.findall(lire(chemin))}


def lire(chemin):
    return (RACINE / chemin).read_text(encoding="utf-8")


def developper(valeur, variables, profondeur=0):
    """Remplace les $(VAR) d'une recette de Makefile par leur valeur."""
    if profondeur > 10:
        return valeur
    for nom, brut in variables.items():
        marque = "$(%s)" % nom
        if marque in valeur:
            valeur = valeur.replace(marque, developper(brut, variables, profondeur + 1))
    return valeur


def variables_du_makefile(texte):
    variables = {}
    for ligne in texte.splitlines():
        trouve = re.match(r"^([A-Z_]+)\s*[:?]?=\s*(.*?)\s*$", ligne)
        if trouve:
            variables[trouve.group(1)] = trouve.group(2)
    return variables


def commandes_python_de_la_ci(texte):
    """Les commandes « run: python … » du workflow, sans l'interpréteur."""
    commandes = []
    for ligne in texte.splitlines():
        trouve = re.match(r"^\s*(?:-\s*)?run:\s*(python\S*)\s+(.+?)\s*$", ligne)
        if trouve:
            commandes.append(trouve.group(2))
    return commandes


class GouvernanceTests(unittest.TestCase):
    def test_fichiers_attendus_presents(self):
        for nom in GOUVERNANCE:
            with self.subTest(fichier=nom):
                chemin = RACINE / nom
                self.assertTrue(chemin.is_file(), "%s manque" % nom)
                self.assertGreater(chemin.stat().st_size, 0, "%s est vide" % nom)

    def test_documents_disent_quelque_chose(self):
        for nom in DOCUMENTS:
            with self.subTest(document=nom):
                self.assertGreater((RACINE / nom).stat().st_size, 500,
                                   "%s est trop court pour tenir sa promesse" % nom)

    def test_claude_md_renvoie_au_guide_commun(self):
        self.assertIn("@AGENTS.md", lire("CLAUDE.md"),
                      "CLAUDE.md doit appeler AGENTS.md plutôt que dupliquer les règles")

    def test_securite_ne_publie_aucune_adresse(self):
        # Le signalement passe par GitHub : aucune adresse personnelle ne doit figurer dans le dépôt.
        for nom in ("SECURITY.md", "SUPPORT.md", "CODE_OF_CONDUCT.md"):
            with self.subTest(fichier=nom):
                self.assertNotRegex(lire(nom), r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


class DocumentationTests(unittest.TestCase):
    def test_index_et_dossier_docs_concordent(self):
        index = lire("docs/README.md")
        presents = {p.name for p in (RACINE / "docs").glob("*.md")} - {"README.md"}
        for nom in sorted(presents):
            with self.subTest(document=nom):
                self.assertIn("(%s)" % nom, index, "docs/%s n'est pas dans l'index docs/README.md" % nom)
        cites = {c for c in LIEN.findall(index) if not c.startswith(("http", "#", "../"))}
        for cite in sorted(cites):
            with self.subTest(cite=cite):
                self.assertIn(cite.split("#")[0], presents | {"README.md"})

    def test_liens_relatifs_resolus(self):
        vus = 0
        for nom in DOCUMENTS_LIES:
            base = (RACINE / nom).parent
            for cible in LIEN.findall(lire(nom)):
                if cible.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                vus += 1
                fichier, _, fragment = cible.partition("#")
                chemin = (base / fichier).resolve() if fichier else (RACINE / nom)
                with self.subTest(fichier=nom, lien=cible):
                    self.assertTrue(chemin.exists(), "%s renvoie à %s, qui n'existe pas" % (nom, cible))
                    if fragment and chemin.suffix == ".md":
                        relatif = chemin.relative_to(RACINE).as_posix()
                        self.assertIn(fragment, ancres_de(relatif),
                                      "%s renvoie à l'ancre #%s de %s, qui n'a aucun titre correspondant"
                                      % (nom, fragment, relatif))
        self.assertGreater(vus, 20, "le contrôle des liens ne voit presque rien : vérifier l'expression")

    def test_ancres_internes_resolues(self):
        """Les renvois d'un document vers ses propres titres, comme le sommaire du README."""
        for nom in DOCUMENTS_LIES:
            disponibles = ancres_de(nom)
            for cible in LIEN.findall(lire(nom)):
                if not cible.startswith("#"):
                    continue
                with self.subTest(fichier=nom, ancre=cible):
                    self.assertIn(cible[1:], disponibles,
                                  "%s renvoie à %s, qui n'est pas un de ses titres" % (nom, cible))


class OutillageTests(unittest.TestCase):
    def test_makefile_et_ci_ne_divergent_pas(self):
        variables = variables_du_makefile(lire("Makefile"))
        recettes = developper(lire("Makefile"), variables)
        commandes = commandes_python_de_la_ci(lire(".github/workflows/tests.yml"))
        self.assertGreaterEqual(len(commandes), 4, "la CI doit garder ses étapes explicites")
        for commande in commandes:
            with self.subTest(commande=commande):
                self.assertIn(commande, recettes,
                              "la CI lance « %s » ; le Makefile ne le fait pas : make verify mentirait" % commande)

    def test_verify_enchaine_les_quatre_controles(self):
        texte = lire("Makefile")
        trouve = re.search(r"^verify:\s*(.*?)\s*(?:##.*)?$", texte, re.M)
        self.assertIsNotNone(trouve, "la cible verify doit exister")
        for cible in ("checklists", "test", "archive", "audit"):
            self.assertIn(cible, trouve.group(1).split(), "verify doit dépendre de %s" % cible)

    def test_archive_livree_marquee_binaire(self):
        self.assertRegex(lire(".gitattributes"), r"(?m)^dist/dan-cortex\.plugin\s+binary")

    def test_bibliotheque_marquee_vendorisee(self):
        attributs = lire(".gitattributes")
        for chemin in ("dan-cortex/bibliotheque/**", "dan-cortex/universel/**"):
            with self.subTest(chemin=chemin):
                self.assertIn(chemin, attributs)


if __name__ == "__main__":
    unittest.main()
