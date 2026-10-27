# Contributing

1. Open an issue describing the reliability or security gap and a reproducible example.
2. Keep tests local by default; any live test must be opt-in and clearly documented.
3. Do not add real credentials, private prompts, personal data, or payloads designed to attack third-party systems.
4. Prefer deterministic checks and clearly label heuristic grading.
5. Run `python -m unittest discover -s tests -v` before submitting a pull request.
6. Document supported Python/Claude Code versions and limitations.
