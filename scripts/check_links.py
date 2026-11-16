"""Check that every local link and image in the notes points to a file that exists.

    python scripts/check_links.py

Scans the root Markdown files and every lesson in the numbered chapter folders
(and old_chapters/). Web links and in-page anchors are skipped. For figures made
by a chapter's figures/make_figures.py, it also checks the SVG companion exists.
"""
from pathlib import Path
import re
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?\[[^\]]*\]\(([^\s)]+)\)")


def markdown_files():
    yield from ROOT.glob("*.md")
    for folder in sorted(ROOT.iterdir()):
        if folder.is_dir() and (re.match(r"^\d\d_", folder.name) or folder.name == "old_chapters"):
            yield from folder.rglob("*.md")


def main():
    errors, checked = [], 0
    for md in markdown_files():
        checked += 1
        for link in LINK.findall(md.read_text(encoding="utf-8")):
            if re.match(r"^(https?://|mailto:|#)", link):
                continue
            target = md.parent / unquote(link.split("#", 1)[0])
            if not target.exists():
                errors.append(f"{md.relative_to(ROOT)}: broken link {link}")
            elif target.suffix == ".png" and (target.parent / "make_figures.py").exists() \
                    and not target.with_suffix(".svg").exists():
                errors.append(f"{md.relative_to(ROOT)}: missing SVG for {link}")
    for e in errors:
        print(e, file=sys.stderr)
    print(f"{checked} Markdown files checked, {len(errors)} problem(s).")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
