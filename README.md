# Portfolio (IS 373 Deliverable 1)

My class portfolio for IS 373 at NJIT: a single static page with my introduction, target direction (UX research on AI products), my featured projects and contact links.

- **Live site:** published with GitHub Pages from `main`
- **Planning record:** [is373-individual-planning, section 1](https://github.com/mcbridgeee/is373-individual-planning/blob/main/1-portfolio-career.md)
- **Status:** Build stage. The two featured case studies (Throughline and the group project) are labeled in progress on the page.

## Why a static page

The portfolio is public content with no logins or data, so plain HTML and CSS is the simplest thing that works. Reusing my App Studio FastAPI app would have added accounts and a server deploy the site doesn't need.

## Checks

CI runs on every pull request: HTML validation (`html-validate`) and a script that confirms every local link, image and anchor exists (`scripts/check_links.py`).

To run them locally:

```
npx html-validate index.html
python3 scripts/check_links.py
```
