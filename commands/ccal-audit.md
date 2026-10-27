---
description: Audit the current project's Claude Code settings and explain actionable findings.
argument-hint: "[optional settings path]"
---

Perform a read-only audit of Claude Code configuration for this workspace.

1. Inspect `.claude/settings.json` and `.claude/settings.local.json` if present. Do not read secrets or unrelated user files.
2. If `$ARGUMENTS` supplies a settings path, inspect only that path after confirming it is within a location the user is authorized to access.
3. Check for overly broad permissions, wildcard command grants, bypass-permission modes, disabled sandbox-related settings, and invalid JSON.
4. Explain that findings are advisory and must be verified against the current official Claude Code documentation.
5. Do not edit settings automatically. Propose a minimal diff and wait for explicit approval before changing permission/security configuration.
6. Report evidence, severity, recommendation, and any checks that could not be completed.
