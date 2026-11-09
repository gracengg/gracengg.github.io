# Grace Ngo — Portfolio

A static HTML, CSS and JavaScript portfolio for business analytics, financial operations and applied research.

Live portfolio: https://gracengg.github.io/

This is the canonical source for the public portfolio at https://gracengg.github.io/.

## Structure

- `index.html`: introduction, resume-aligned experience, selected work, research and contact.
- `case-studies/`: project briefs and the three-stage NSDUH dashboard gallery.
- `css/style.css`: shared tokens, components and responsive layouts.
- `css/case-study.css`: case-study page layout only.
- `js/script.js`: optional navigation, section tracking, reveal, image fallback and email-draft enhancements.
- `images/projects/`: original dashboard exports.
- `publications/`: public academic PDF attachments.
- `scripts/check_site.py`: offline checks for HTML structure, labels, local assets and anchors.

## Selected work

| Work | Focus | Published materials |
| --- | --- | --- |
| 1Matrix | Budget availability and procurement controls | Linked Excel model, dashboard prototype scope and control framework |
| Dickinson / CCLA | Institutional reporting and engagement analysis | Ten-dashboard suite summary and separate CCLA prototype brief |
| New-to-credit | Missing credit information, model comparison and review thresholds | Verified source access, executed research notebook, reproduced results, Python workflow and Tableau template |
| NSDUH | Age-group comparisons and accumulated distress indicators | Redesigned age-group overview, labeled-value JSON, original Power BI exports and analytical brief |
| Apple equity risk | Historical performance, drawdowns and macroeconomic context | Case, Python package, six data snapshots, notebook and rebuilt risk tables |
| IMDb catalogue selection | Coverage trade-offs across four vote thresholds on 88,601 movies | Official-data results, aggregate chart, SQL, source fingerprints and reproduction guide |
| Retail revenue | Category growth reconciliation and data quality | Case, SQL queries, executable loader and aggregate identity audit |
| Campus energy | Metering and investment reporting | Proposal brief and phased implementation recommendations |
| Credit and hiring ethics | Financial history as a proxy in hiring | Original essay PDF |
| Beauty and wages | Econometric replication and distributional analysis | [Research brief](case-studies/beauty-labor-market.html) and [full 21-page paper](publications/beauty-labor-market.pdf) |
| Helping behavior | Time pressure, reciprocity and experimental design | Original research paper PDF |

Selected work leads with NSDUH, New-to-Credit and IMDb, followed by Apple, Retail, 1Matrix and Dickinson. The featured research section highlights labor-market econometrics and the campus-energy proposal; additional papers remain accessible through More research & writing.

Case studies identify their analytical setting, methods and deliverables. Linked project repositories contain detailed methods and data documentation. Institutional source workbooks remain outside this public repository.

## Checks

Run from the repository root:

```sh
python3 scripts/check_site.py
node --check js/script.js
git diff --check
```

Also review the homepage and case-study pages in a browser at phone, tablet and desktop widths. Check mobile menu keyboard behavior, native disclosures, image loading and contact validation. The contact form opens a draft in the visitor's email application; it does not send through a server.

## Deployment

GitHub Pages builds from this repository's configured branch. Publishing here updates the final portfolio at the root URL. Canonical and social metadata use https://gracengg.github.io/.

## Independent project source

[New-to-Credit Consumer Risk Analysis](https://github.com/gracengg/New_to_Credit_Consumer_Risk_Analysis) is maintained as a standalone project, outside this website repository.



## Visual assets

Featured cards share a 3:2 cover ratio, equal card structure and visible headline measures. Credit and IMDb covers were supplied for this portfolio; analytical charts remain in the case studies. Experience panels use a consistent typographic company-name treatment. The clean public LinkedIn portrait is stored locally.

The NSDUH overview uses four percentages transcribed from the labels in the original report export. It does not reproduce the underlying survey calculation. Run `python3 scripts/build_nsduh_overview.py` to rebuild the SVG from `data/nsduh-display-summary.json`. The original report exports remain available from the case-study disclosure.

The social preview can be rebuilt with `python3 scripts/build_social_preview.py` after installing Matplotlib; this is an optional asset-generation dependency, not a website runtime dependency.
