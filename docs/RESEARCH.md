# Research notes and design decisions

Research snapshot: 27 October 2026. Check the linked primary sources again before production use because CLI flags and plugin packaging can change.

## Findings

1. Anthropic describes sandboxing as a way to give Claude Code bounded autonomy with fewer permission prompts. The key design principle is to define safe boundaries, not to depend on a prompt to override permissions.
2. Anthropic's advanced-use guidance documents hooks, pre-approved permission rules, automatic permission mode, and sandboxing. These are operational configuration features; availability and exact syntax must be verified against the installed version.
3. OWASP LLM01:2025 describes direct and indirect prompt injection and recommends least privilege, separation of untrusted content, validation, human approval for high-risk actions, and adversarial testing.
4. OWASP's AI/LLM testing guidance recommends repeatable tests, per-risk thresholds, pinned versions/configuration, regression corpora, and not treating an LLM judge as the sole evaluator.
5. Existing tools have complementary roles: garak for broad scanner probes, promptfoo for declarative evaluations and CI, and PyRIT for orchestrated adversarial testing. CCAL intentionally starts smaller and local-first, with no third-party dependencies.

## Primary sources

- https://www.anthropic.com/research/claude-code-sandboxing
- https://support.claude.com/fr/articles/14554000-conseils-pour-les-utilisateurs-avances-de-claude-code
- https://github.com/anthropics/claude-code/tree/main/examples/settings
- https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_vulns/LLM01_PromptInjection.md
- https://owasp.github.io/DevSecOpsGuideline/2-Process/2-4-Test/2-4-6-AI-LLM-Application-Security-Testing/
- https://github.com/NVIDIA/garak
- https://github.com/promptfoo/promptfoo
- https://github.com/Azure/PyRIT

## Why CCAL does not ship a universal jailbreak

No prompt or static attack corpus can guarantee a bypass across model versions and deployment configurations. A project that measures and improves authorized behavior is more reproducible and safer than promising to neutralize controls. The system's permissions, tool integration, sandbox and external side effects must be assessed directly.
