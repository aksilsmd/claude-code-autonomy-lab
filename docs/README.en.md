# Dan-Cortex — English summary

**Dan-Cortex** is a Claude plugin that runs a network of 59 expert agents, organised like a real company,
to scope, design, build, test, secure and launch a digital project: enterprise website, mobile app, SaaS, niche
product, e-commerce, ERP. Agents work in parallel waves, cross-review each other's deliverables, debate
structural decisions in bounded written meetings, and an independent auditor reviews everything before launch. A
coverage matrix of 784 controls makes sure nothing is forgotten, from security and law to budget,
marketing and cultural adaptation.

Version 1.0 adds an **autonomous mode**: after a single qualification round, the network runs the whole scope
without waiting, takes irreversible decisions as provisional ones you confirm at the end, and acts outside the
workspace only within the standing authorisations you wrote down. Six hard limits (spending, systems outside the
project, unauthorised security testing, changing Claude Code permissions, irreversible deletion, real secrets)
always require your consent. It also merges **Claude Code Autonomy Lab**: an agent-robustness pole that audits
Claude Code settings and tests AI features against prompt injection.

It is built for low token use: each agent starts with about 6,000 tokens of context instead of about 90,000 for a
general-purpose agent, deterministic checks run in scripts, and agents talk through files.

The plugin content is written in French, with French and EU law first. Install it with
`/plugin marketplace add aksilsmd/cortex` then `/plugin install dan-cortex@cortex-projets` in Claude Code, or in the Claude
app with Customize → Plugins → Add → Add marketplace → Add from a repository (`aksilsmd/cortex`). Start with
`/dan-cortex:lancer-projet`.

Dan-Cortex prepares and checks; it does not replace a lawyer, an accountant or a qualified security auditor.

The full documentation is in French: [README](../README.md).
