# Installation

## Python CLI

Install Python 3.11 or newer, then from the repository root:

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -e .
ccal --help
```

## Claude Code plugin — local testing

From the repository root, run:

```bash
claude --plugin-dir .
```

Inside Claude Code, try `/claude-code-autonomy-lab:ccal-audit` and `/claude-code-autonomy-lab:ccal-test`. Verify plugin discovery against the current Claude Code release because plugin packaging and installation options can evolve.

## Claude Code plugin — persistent installation

The repository ships `.claude-plugin/marketplace.json`, so it can be registered as a
marketplace and installed persistently:

```bash
claude plugin marketplace add /path/to/claude-code-autonomy-lab
claude plugin install claude-code-autonomy-lab@ccal
claude plugin details claude-code-autonomy-lab@ccal
```

A GitHub checkout works as a source too (`claude plugin marketplace add <owner>/<repo>`).
Remove it again with `claude plugin uninstall claude-code-autonomy-lab@ccal` and
`claude plugin marketplace remove ccal`.

## Team or persistent installation

Use the official Claude Code plugin/marketplace installation process documented by Anthropic. Review the repository and permissions before installing a third-party plugin. Do not run unknown hooks or scripts blindly. This project currently uses prompt commands and a skill; it does not install background telemetry or automatic permission changes.
