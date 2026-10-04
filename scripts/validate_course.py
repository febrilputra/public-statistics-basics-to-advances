"""Validate links, notebook structure, execution, and scientific assertions.

    python scripts/validate_course.py --execute

Execution uses this Python interpreter in a fresh kernel for each notebook.
All published notebooks are rewritten with successful outputs only.
"""
import argparse
from pathlib import Path
import re
import sys
import time
import nbformat
from nbclient import NotebookClient
from jupyter_client import KernelManager
from build_notebooks import LAB_MARKER, SETUP, lab_cells

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--chapter", help="Only validate chapter prefix, e.g. 06 or AA")
    args = parser.parse_args()
    errors = []
    folders = sorted(p for p in ROOT.iterdir() if p.is_dir() and re.match(r"^(\d\d|AA)_", p.name))
    if args.chapter:
        folders = [p for p in folders if p.name.startswith(args.chapter + "_")]
        if not folders:
            parser.error("No chapter matches the requested prefix")
    if len(folders) != 13 and not args.chapter:
        errors.append(f"Expected 13 chapter directories, found {len(folders)}")
    for folder in folders:
        notebook_path = folder / f"{folder.name}.ipynb"
        try:
            nb = nbformat.read(notebook_path, as_version=4)
            nbformat.validate(nb)
            if args.execute:
                started = time.monotonic()
                km = KernelManager(kernel_name="python3")
                # Do not silently run a globally installed Python kernel.
                km.kernel_spec.argv[0] = sys.executable
                client = NotebookClient(nb, km=km, timeout=180,
                                        resources={"metadata": {"path": str(folder)}},
                                        allow_errors=False)
                client.execute(cleanup_kc=True)
                nbformat.write(nb, notebook_path)
                print(f"Executed {folder.name} in {time.monotonic()-started:.1f}s", flush=True)
            code_cells = [c for c in nb.cells if c.cell_type == "code"]
            if not code_cells:
                errors.append(f"No code cells: {notebook_path}")
            for c in code_cells:
                if c.execution_count is None:
                    errors.append(f"Unexecuted code cell: {notebook_path}")
                if any(o.output_type == "error" for o in c.get("outputs", [])):
                    errors.append(f"Error output: {notebook_path}")
            prose = (folder / f"{folder.name}.md").read_text(encoding="utf-8")
            labs = lab_cells(ROOT / "scripts" / "labs" / f"{folder.name[:2]}.py")
            expected_code = [SETUP.replace("__CHAPTER__", repr(folder.name))]
            expected_code += [labs[name] for name in LAB_MARKER.findall(prose)]
            if [c.source for c in code_cells] != expected_code:
                errors.append(f"Notebook code is stale: {folder.name}; rebuild before executing")
            for token in ["```mermaid", "##", "Practice", "Worked answers", "References"]:
                if token not in prose:
                    errors.append(f"Missing {token!r}: {folder.name}")
            notebook_prose = "\n".join(c.source for c in nb.cells if c.cell_type == "markdown")
            # Confirm every authored prose segment is present in its notebook.
            for segment in re.split(r"<!-- lab: [a-z_]+ -->", prose):
                if segment.strip() not in notebook_prose:
                    errors.append(f"Notebook prose is stale: {folder.name}")
                    break
        except Exception as exc:
            errors.append(f"{folder.name}: {type(exc).__name__}: {exc}")
    md_files = [p / f"{p.name}.md" for p in folders]
    if not args.chapter:
        md_files += list(ROOT.glob("*.md"))
    for source in md_files:
        if not source.exists():
            errors.append(f"Missing Markdown: {source}")
            continue
        text = source.read_text(encoding="utf-8")
        for link in re.findall(r"!?\[[^\]]*\]\(([^\s)]+)\)", text):
            if re.match(r"^(https?://|mailto:|#)", link):
                continue
            target = source.parent / link.split("#",1)[0]
            if not target.exists():
                errors.append(f"Broken local link in {source.relative_to(ROOT)}: {link}")
        for figure in re.findall(r"!\[[^\]]*\]\((figure/[^)]+)\)", text):
            target = source.parent / figure
            if target.exists() and target.stat().st_size < 5000:
                errors.append(f"Suspiciously small figure: {target}")
            if target.suffix == ".png" and not target.with_suffix(".svg").is_file():
                errors.append(f"Missing SVG companion: {target.with_suffix('.svg')}")
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {len(folders)} notebooks, synchronized prose, local links, and figures.")


if __name__ == "__main__":
    main()
