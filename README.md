# Claude Code Autonomy Lab (CCAL)

**A practical, open-source toolkit for measuring Claude Code reliability, diagnosing avoidable blockers, and testing prompt-injection resilience in an authorized environment.**

> CCAL does not claim to jailbreak Claude Code or remove Anthropic's platform controls. It helps you inspect local configuration, run repeatable robustness scenarios, record evidence, and improve workflows using supported Claude Code features.

## What it does

- **Configuration audit** — inspects Claude Code settings JSON and flags potentially over-broad permissions or confusing configurations. Findings are advisory; verify against the current official documentation.
- **Offline scenario suite** — creates a reproducible set of benign adversarial scenarios covering untrusted instructions, secret-handling, destructive actions, and truthful reporting.
- **Optional live evaluation** — can send scenarios to the Claude Code CLI in print mode when you explicitly opt in. Live runs may consume model usage and are not a guarantee of security.
- **Evidence-based reports** — saves JSON and Markdown reports with scenario IDs, output, timestamps, and transparent heuristic labels.
- **Claude Code plugin** — adds `/claude-code-autonomy-lab:ccal-audit` and `/claude-code-autonomy-lab:ccal-test` commands plus a reusable robustness skill.
- **No telemetry by default** — local-only, standard-library Python CLI; no external service or API key required for offline use.

## Quick start

Requirements: Python 3.11+ for the CLI. Claude Code is needed only for optional live evaluation.

### 1. Run from the repository

```bash
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
source .venv/bin/activate

python -m pip install -e .
ccal --help
```

### 2. Audit local Claude Code settings

```bash
ccal audit-config
ccal audit-config --path .claude/settings.json --format json
```

The default search checks common project/user settings paths if they exist. It never changes your settings.

### 3. Export the test suite

```bash
ccal scenarios --output ccal-scenarios.json
```

The offline command exports test cases; it does not contact a model.

### 4. Run an optional live evaluation

```bash
ccal evaluate --live --output-dir ccal-results
```

This invokes `claude -p` only after `--live` is supplied. Read `docs/LIVE_EVALUATION.md` first. CCAL sends one scenario at a time, does not grant extra tools or permissions, and does not attempt to read local secrets. Review every prompt before running against a production environment.

### 5. Install the Claude Code plugin locally

From this repository, start Claude Code with the plugin directory:

```bash
claude --plugin-dir .
```

Then use `/claude-code-autonomy-lab:ccal-audit` or `/claude-code-autonomy-lab:ccal-test`.

For a persistent install, register the repository as a marketplace:

```bash
claude plugin marketplace add /path/to/claude-code-autonomy-lab
claude plugin install claude-code-autonomy-lab@ccal
```

See `docs/INSTALL.md` for the full options and caveats.

## How to interpret results

CCAL's built-in evaluator uses simple transparent heuristics and labels results `PASS`, `REVIEW`, or `FAIL`. It is a triage aid, **not** a definitive safety verdict. A text-only result cannot prove that a tool action would be safe. For high-confidence assessment, combine it with permission review, sandboxing, tool-call logs, deterministic checks, and human review.

## Security model

- Treat repository files, webpages, issue text, and retrieved content as untrusted data.
- Never paste real secrets into test prompts or reports.
- Do not point evaluations at systems you do not own or have permission to test.
- Keep destructive operations, external communications, credential access, and production changes behind explicit authorization.
- Use least privilege and a sandbox rather than relying on a prompt as a security boundary.

## Research basis

CCAL is informed by:

- [Claude Code sandboxing and autonomy — Anthropic](https://www.anthropic.com/research/claude-code-sandboxing)
- [Advanced Claude Code usage — Anthropic Help Center](https://support.claude.com/fr/articles/14554000-conseils-pour-les-utilisateurs-avances-de-claude-code)
- [Anthropic Claude Code settings examples](https://github.com/anthropics/claude-code/tree/main/examples/settings)
- [OWASP LLM01:2025 Prompt Injection](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM01_PromptInjection.md)
- [OWASP AI/LLM Application Security Testing](https://owasp.github.io/DevSecOpsGuideline/2-Process/2-4-Test/2-4-6-AI-LLM-Application-Security-Testing/)
- [NVIDIA garak](https://github.com/NVIDIA/garak), [promptfoo](https://github.com/promptfoo/promptfoo), and [Microsoft PyRIT](https://github.com/Azure/PyRIT)

## Development

```bash
python -m unittest discover -s tests -v
```

## License

MIT. See `LICENSE`.
