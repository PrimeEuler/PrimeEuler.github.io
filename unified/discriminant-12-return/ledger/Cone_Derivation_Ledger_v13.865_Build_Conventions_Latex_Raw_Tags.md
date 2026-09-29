# Cone Derivation Ledger v13.865 — Build Conventions: Escaping LaTeX for the Pages Build

Date: 2026-09-29

Type: **project conventions note** (not a derivation, not an audit). Standing guidance for all future ledger contributors — human and agent threads alike. (This file practices what it preaches: every literal Liquid-looking sequence in the prose below is HTML-entity-encoded so this entry itself can't break the build; only the one functional example in §1 uses real tags.)

Author: project owner's assistant, at the project owner's request (follows the 2026-09-29 build-error repair session).

Parents: v13.205 (first repaired entry), v13.192 (publication build baseline).

## 0. The problem

The project site builds on GitHub Pages with **Jekyll**, whose **Liquid** templating interprets double-open-brace sequences as output tags and percent-brace sequences as logic tags. Ledger entries are Markdown files in the built tree, so any LaTeX containing literal double braces breaks the build. The concrete offender found 2026-09-29: a `\graphicspath` command with doubled braces inside a `tex` code block in v13.205 — parsed as a Liquid tag, Pages build failed. 30 further entries containing double-brace sequences were found and repaired in the same session.

## 1. The fix (already applied)

Wrap the offending region in Liquid raw tags so the braces pass through untouched:

{% raw %}
```tex
\graphicspath{{./}{../figures/}}
```
{% endraw %}

i.e. place the raw-open tag on its own line before the region and the raw-close tag on its own line after it. (Rendered form: `{&#37; raw &#37;}` … `{&#37; endraw &#37;}`.) Applied to v13.205 first, then batch-applied to all 30 remaining entries containing double braces. Single braces are harmless — only doubled braces and percent-brace sequences trigger Liquid.

## 2. Rules for all future ledger entries

1. **Before pushing a new entry, grep it for doubled open-braces.** If present, wrap each offending region (code block, display equation, or paragraph) in raw-open / raw-close tags.
2. **Prefer wrapping the smallest region that contains the double braces** — usually the code block or the single equation — rather than the whole file, so the rest of the entry keeps normal Markdown rendering.
3. **Watch for percent-brace sequences too**: a literal one in text (rare in math, possible in prose about this very convention) needs the same treatment — or write it entity-encoded as `{&#37;` … `&#37;}` so Liquid never sees it.
4. **Display math with `\boxed{...}`, `\frac{...}{...}`, sub/superscripts is fine** — single braces never trigger Liquid. Only double-brace sequences matter.
5. If the Pages build fails after your push, check the build log for a Liquid syntax error naming your file; the fix is almost always a missing raw wrap around a double-brace sequence.

## 3. Why this is in the ledger

Build-breaking entries block every reader, and with multiple agent threads writing entries in parallel (sandbox track, audit thread, Lane A), the convention has to live where all writers will see it — not in one thread's side chat. This entry is the canonical reference; point future contributors here.
