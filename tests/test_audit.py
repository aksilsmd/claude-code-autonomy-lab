import unittest
from ccal.audit import audit_settings

class AuditTests(unittest.TestCase):
    def test_flags_bypass_permission_mode(self):
        result = audit_settings({"permissions": {"defaultMode": "bypassPermissions"}})
        self.assertTrue(any(f["code"] == "BROAD_PERMISSION_MODE" for f in result["findings"]))

    def test_flags_wildcard_allow(self):
        result = audit_settings({"permissions": {"allow": ["Bash(*)"]}})
        self.assertTrue(any(f["code"] == "WILDCARD_ALLOW_RULE" for f in result["findings"]))

    def test_no_match_is_info_not_secure_claim(self):
        result = audit_settings({"theme": "dark"})
        self.assertEqual(result["findings"][0]["severity"], "INFO")
        self.assertIn("not proof", result["findings"][0]["recommendation"])

if __name__ == "__main__":
    unittest.main()
