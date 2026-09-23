# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is Jiahao (Riddle) Liu's personal academic website, built on the **Academic Pages** Jekyll template (a fork/detach of Minimal Mistakes). It is a static site hosted on GitHub Pages at `riddle-jhliu.github.io`. Content changes (publications, talks, CV, bio) are far more common than theme/code changes.

## Commands

Local development requires Ruby, Bundler, and Node.js.

```bash
bundle install          # install Ruby/Jekyll dependencies (delete Gemfile.lock first if errors occur)
bundle exec jekyll serve       # build and serve at localhost:4000
bundle exec jekyll liveserve   # build, serve, and auto-rebuild/refresh on change (uses hawkins gem)
```

There is no test suite, linter, or CI build step in this repo — verification is "does it build and render correctly with Jekyll."

There are no JS build commands in practice; `package.json` defines `npm run uglify`/`build:js`/`watch:js` scripts for minifying the theme's vendor JS, but these come from the upstream Minimal Mistakes theme and aren't part of this site's normal workflow.

## Architecture

Standard Jekyll structure with content driven by **collections** defined in `_config.yml`: `_teaching`, `_publications`, `_portfolio`, `_talks` (each `output: true`, permalink `/:collection/:path/`). Non-collection static pages live in `_pages/` (about, cv, publications index, talks index, 404, etc.) and are included in the build via the `include:` list in `_config.yml` (Jekyll normally ignores underscore-prefixed dirs).

- `_layouts/` — page templates (`single`, `archive`, `talk`, `splash`, `default`, etc.)
- `_includes/` — reusable partials (author profile, head/SEO, analytics, comments providers, navigation, etc.)
- `_sass/` — theme styles, compiled via the `sass:` config (`sass_dir: _sass`, compressed output)
- `_data/` — YAML data: `authors.yml`, `navigation.yml` (top nav), `ui-text.yml`, plus `comments/` (staticman-generated comment YAML files)
- `_config.yml` — main site config (author info, social links, collections, defaults, analytics, plugins). `_config.dev.yml` is a local-dev override (localhost URL, disables analytics, expanded Sass) merged in via `--config _config.yml,_config.dev.yml` when serving locally.
- `defaults:` in `_config.yml` sets per-collection front matter (e.g. all `talks` get `layout: talk`; all `publications`/`teaching`/`portfolio` get `layout: single` with `author_profile`, `share`, `comments` enabled).

### Content entry format

Each collection item is a Markdown file with YAML front matter. Filenames follow `YYYY-MM-DD-slug.md` and the permalink is typically set explicitly in front matter (e.g. `permalink: /talks/2023-08-21-talk-6`, `permalink: /publication/2026-3-10-paper-title-number-7`). Look at existing files in `_publications/` or `_talks/` as the template when adding new ones — required front matter fields differ per collection (e.g. talks need `type`, `venue`, `location`, `date`; publications need `citation`, `paperurl`, `excerpt`).

### Markdown generators

`markdown_generator/` contains Jupyter notebooks (and equivalent `.py` scripts) that batch-generate collection Markdown files from TSV data (`publications.tsv`, `talks.tsv`) rather than hand-authoring each file — useful when adding many entries at once. `pubsFromBib.py`/`PubsFromBib.ipynb` does the same from a BibTeX file. TSV format for publications: columns `pub_date` (YYYY-MM-DD), `title`, `venue`, `excerpt`, `citation`, `site_url`, `paper_url` (excerpt/paper_url may be blank).

### Talk map

`talkmap/` + `talkmap.py`/`talkmap.ipynb` generate `talkmap/org-locations.js` (a Leaflet map of talk locations) from the `_talks/` collection's `location` front matter; rendered via `_pages/talkmap.html` when `talkmap_link: true` in `_config.yml`.

## Notes

- `timezone` in `_config.yml` is set to `Asia/Shanghai` — dates in front matter are interpreted relative to that.
- Files meant for direct download (PDFs, zips) go in `files/` and are served at `/files/<name>`.
- This repo tracks upstream academicpages fixes as closed GitHub issues tagged `code change` (see CONTRIBUTING.md) — not directly actionable here, just useful context if diagnosing merge-conflict-prone areas.
