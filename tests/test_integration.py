"""Le pôle robustesse-agents est bien branché dans Cortex."""
import importlib.util
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LAUNCHER = ROOT / "skills" / "robustesse-agents" / "scripts" / "robustesse.py"
CORTEX = ROOT / "skills" / "lancer-projet" / "scripts" / "cortex.py"


def load_cortex():
    spec = importlib.util.spec_from_file_location("cortex_script", CORTEX)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class LauncherTests(unittest.TestCase):
    def test_runs_in_isolated_mode(self):
        proc = subprocess.run([sys.executable, "-I", str(LAUNCHER), "--version"],
                              capture_output=True, text=True, check=False)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("ccal", proc.stdout)

    def test_live_evaluation_requires_opt_in(self):
        proc = subprocess.run([sys.executable, "-I", str(LAUNCHER), "evaluate"],
                              capture_output=True, text=True, check=False)
        self.assertNotEqual(proc.returncode, 0)
        self.assertIn("--live", proc.stderr)


class ChecklistTests(unittest.TestCase):
    def setUp(self):
        self.cortex = load_cortex()
        self.rob = [i for i in self.cortex.charger_checklists() if i["domaine"] == "ROB"]

    def test_rob_controls_are_loaded_without_duplicates(self):
        self.assertGreaterEqual(len(self.rob), 10)
        self.assertFalse([i["id"] for i in self.rob if i.get("doublon")])

    def test_ia_tag_gates_product_controls(self):
        sans_ia = {i["id"] for i in self.rob if self.cortex.applicable(i, ["saas"], [])}
        avec_ia = {i["id"] for i in self.rob if self.cortex.applicable(i, ["saas"], ["ia"])}
        self.assertEqual(sans_ia, {"ROB-001", "ROB-002", "ROB-003"})
        self.assertIn("ROB-010", avec_ia)
        self.assertTrue(sans_ia < avec_ia)


if __name__ == "__main__":
    unittest.main()
