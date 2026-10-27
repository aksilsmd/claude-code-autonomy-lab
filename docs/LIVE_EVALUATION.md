# Live evaluation: safety and limitations

The live mode invokes the installed `claude` CLI with `--restricted`, `--tools ""`, `--disallowedTools "mcp__*"`, `-p`, and a text-only scenario. This reduces available tool surface and prevents MCP tool use for compatible CLI versions. It is opt-in because it may consume model usage. It does not add tool permissions, alter Claude Code settings, read local files intentionally, or try to access credentials. The prompts explicitly request a text-only answer, but the CLI's actual configuration and version still matter; use a disposable test workspace and inspect the command and settings before use.

## Run

```bash
ccal evaluate --live --output-dir ccal-results
```

You can set a longer timeout, for example `--timeout 180` (allowed range 5–900 seconds).

## Important limitations

- The built-in grader uses simple text heuristics and can misclassify an answer.
- Passing these scenarios does not prove the agent is secure.
- Text-only answers do not measure whether tools or filesystem boundaries are actually enforced.
- Run multiple trials to account for stochastic behavior; preserve exact model/version and settings for reproducibility.
- Review reports before sharing them. Never include real secrets or personal data in prompts.
- For a serious assessment, add deterministic checks around tool calls and test a staging or isolated environment with explicit authorization.
