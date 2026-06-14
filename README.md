# Harsh Raje Portfolio

Static portfolio and writing site built with MkDocs Material.

## Why this setup

- Content lives in markdown, so new project pages and articles can be added quickly.
- GitHub Pages can deploy on every push.
- The site can link out to GitHub, LinkedIn, Blogspot, YouTube, and project repos without needing a backend.

## Local development

```bash
pip install mkdocs mkdocs-material
mkdocs serve
```

Open `http://127.0.0.1:8000`.

## Publish on GitHub Pages

1. Put this folder in its own GitHub repository.
2. Push to the default branch.
3. In GitHub Pages, set the source to `GitHub Actions`.
4. The workflow in `.github/workflows/deploy.yml` will build and publish the site.

## Content workflow

- Add or edit markdown files in `docs/`.
- Keep project deep-dives in `docs/projects/`.
- Keep articles and draft posts in `docs/writing/`.
- When you publish code to GitHub, update the matching project page with the repo link and any demo media.

## TODOs For Next Session

- Add the user’s YouTube channel link to [docs/contact.md](docs/contact.md).
- Add GitHub profile and final public repo links once the publishing repo is chosen.
- Create or connect the actual GitHub repository for this site.
- Push the site and enable GitHub Pages via the existing GitHub Actions workflow.
- Decide the final production URL and update `site_url` in [mkdocs.yml](mkdocs.yml).
- Review the left navigation hierarchy and confirm the final naming of project sections.
- Preview the site on desktop and mobile and tune layout issues if any show up.
- Clean up the collaborative transport report page formatting where PDF extraction still reads awkwardly.
- ~~Fix remaining mojibake and encoding artifacts in the collaborative transport report~~ — done: confirmed the file is clean UTF-8 with no corruption; normalized curly quotes to straight ASCII. The remaining non-ASCII characters (±, °, ¾, °C) are intentional and correct.
- Improve multi-image figure layouts on the collaborative transport report page so related images display more cleanly.
- Decide whether Figure 12 and Figure 13 from the collaborative transport report should be extracted or reconstructed more cleanly.
- Decide whether Appendix B code should stay summarized or whether a few representative code excerpts should be promoted into the webpage.
- Decide whether Appendix C/D/E need more visual treatment or if the PDF-only preservation is sufficient.
- Add absolute/clear captions where extracted appendix figures are currently context-light.
- Do one editorial pass on [docs/projects/collaborative_load_transport.md](docs/projects/collaborative_load_transport.md) now that the full report archive exists.
- Add the full report PDF link anywhere else it should appear, such as the main projects index if desired.
- Add more media to the collaborative transport project if original images or CAD screenshots are found outside the PDF.
- Consider placing the two cover-page images side by side for a cleaner intro section.
- Review all external links in the portfolio for validity: Blogspot, YouTube, LinkedIn, PDF download, and demo video.
- Add stronger cross-links between the main project page and the full report page.
- Decide whether the Blogspot pending posts should be migrated into `docs/writing/` one by one.
- Convert the next legacy project/post into the same portfolio-plus-archive pattern if desired.
- Add screenshots or figures for the other project pages: racecar benchmarking, shot peening ML, crack detection, and webcam streaming.
- ~~Expand the six writing-section stubs into full posts~~ — done.
- ~~Sync `projects.csv` with the actual project pages~~ — done (was listing imu_fusion / mujoco_sim, which no longer exist).
- ~~Add the Philips defibrillator-simulator patent to the Patents section~~ — done: WO2026087546A1, linked to Google Patents and WIPO PATENTSCOPE (EP + WO). Update if/when a US application or national grant issues.
- Add real GitHub repository links to each project page once repos are selected for public presentation.
- Do a final style/content consistency pass across all project pages so tone and structure are aligned.
