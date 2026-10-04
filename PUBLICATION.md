# Attribution, source handling, and publication

The course consists of original explanations, new synthetic examples, new exercises and answers, and figures generated from the accompanying Python code. It follows the subject sequence of Josh Starmer's *The StatQuest Illustrated Guide to Statistics* and cites that reading in every chapter and in [References](Reference.md). It does not distribute the book's pages, screenshots, cartoons, or extracted text as course content.

The study PDFs and extracted reading files remain in the ignored `sources/` directory. The private task brief remains in the ignored `plan/` directory. Neither is required to run a notebook. The `.venv/`, notebook checkpoints, and local QA artifacts are also ignored. These exclusions keep supporting local material out of ordinary additions to Git; they do not remove anything that was already tracked.

## Existing Git history needs a separate review

Older source PDFs remain in this repository's existing Git commits, even though no PDF paths were tracked in the current index at the final review. Creating new course files or ignoring `sources/` does not remove those older PDFs from existing commits, branches, tags, or a remote repository. The pre-existing removal of those files from the working tree was preserved.

Before making a private repository public, inspect both the pending changes and the history. These commands only read repository state:

```bash
git status --short
git diff --name-status
git ls-files '*.pdf'
git log --all --name-only --format=oneline -- '*.pdf'
```

If copyrighted source files are present in commits that would become public, resolve that distribution issue before publishing. Depending on the intended history, options include preparing a clean repository containing only the original course, or deliberately removing the files from the relevant history with appropriate coordination and backups. A deletion commit by itself leaves earlier versions available. No history rewrite, commit, or push was performed while preparing these notes.

## Attribution and reuse

Attribution identifies the source of ideas and directs readers to the author. It is not, by itself, permission to redistribute protected material or a guarantee of legal clearance. Fair-use and similar exceptions depend on the circumstances and jurisdiction; the [U.S. Copyright Office's guidance](https://www.copyright.gov/help/faq/faq-fairuse.html) explains this for U.S. law. Readers should obtain the source book from its [official author page](https://statquest.org/statquest-store/).

No repository-wide reuse license has been selected on the owner's behalf. Before inviting others to reuse the course, choose an appropriate license for material you are entitled to license, distinguishing prose and figures from code if desired. Any third-party works and software retain their own terms. Making a repository visible publicly does not itself supply a reuse license for its contents.

For future contributions, write explanations in your own words, construct fresh examples, create or properly license figures, record sources, and keep any private reading material outside the public course. Replacing names or numbers in copied passages is not an adequate substitute for original authorship.
