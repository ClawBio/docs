# ClawBio Documentation

Source for [docs.clawbio.ai](https://docs.clawbio.ai) — the documentation site for [ClawBio](https://github.com/ClawBio/ClawBio), the bioinformatics AI agent skill library.

## Structure

```
mkdocs.yml          # MkDocs Material configuration
docs/
  start/            # Getting started guides
  skills/           # Individual skill documentation
  hackathon/        # Hackathon tutorials and submission guide
  reference/        # SKILL.md spec, CLI, API, security
  roadmap/          # 2026 strategic roadmap
  contributing/     # Contributor guides
  assets/           # Logo, favicon
```

## Local development

```bash
pip install mkdocs-material
mkdocs serve
```

Site builds at `http://127.0.0.1:8000`.

## Deployment

Pushes to `main` trigger GitHub Actions, which runs `mkdocs gh-deploy` to publish to GitHub Pages at `docs.clawbio.ai`.

## Contributing

Edit or add markdown files under `docs/`, then open a PR. The site rebuilds automatically on merge.
