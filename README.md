# What does it take to get hired in political science? (2021–2026)

Evidence from **726 job ads** circulated on the POLMETH and EPSS mailing lists, tracing **195 people** who were hired and coding their CVs *as of the start of the job*.

## Headline results

| At start of job | Postdoc (n=73) | Junior / open-rank faculty (n=110) | Senior / lateral faculty (n=12) |
|---|---|---|---|
| Peer-reviewed articles, median (middle 50%) | **2** (0–3) | **4** (2–9) | 9 (5–13) |
| Has ≥1 top general/field-journal article | 25% | 49% | 33% |
| Years since PhD, median | **0** | **2** | 12 |
| Hired ABD / in year of PhD | 70% | 21% | 0% |
| Did a postdoc first | 14% | 53% | 42% |

Top journals counted: APSR, AJPS, JOP, IO, BJPolS, WP, CPS, Political Analysis, ISQ, JCR, EJPR, QJPS, PSRM, Political Behavior, JEPP.

**1. The typical path is PhD → about 2-year postdoc → tenure track.** Postdocs mostly hire straight out of the PhD with about 2 articles. Junior faculty hires are typically 2 years out with about 4 articles and a first top-journal piece. Of the 32 postdocs whose next job is known, 66% moved into an assistant professor or lecturer post.

**2. The faculty bar is about 4 articles, but the spread is wide.** Only 2% of junior faculty hires had no publications, 29% had ≤2, and 22% had ≥10. Publication counts track time since PhD: about 3 at year 0, 2–5 in years 1–3, and about 12 from year 4 on.

**3. By subfield (junior faculty, median articles / share with a top-journal article):**
- Comparative/PE 8 / 55%
- Policy/other 7 / 33%
- Computational social science 6 / 50%
- American 4 / 43%
- IR 3.5 / 59%
- Methods 3 / 50%
- Open field 3 / 50%

Methods and American hires are the most likely to come straight from the PhD. CSS hires most often did a postdoc first (68%).

**4. By country:**
- **Faculty:** the US (84 hires) and continental Europe (12) are both at a median of about 4–4.5 articles. Europe almost never hires straight from the PhD; its junior hires are typically 3 years out, after a postdoc. The UK, Canada and Asia have too few hires to say.
- **Postdocs:** the US (40) median is 1.5 articles. German-speaking countries (11) have a median of 3, but 36% of hires had none; European project postdocs seem to hire either fresh PhDs or people with 3–4 articles. UK/Ireland (8) median is 0.

**5. Centre fellowships are the most selective postdocs by outcome, not by publications.** Fellows had a median of 1 article, but 10 of the 12 whose next job is known moved to tenure track. Project postdocs: 6 of 15.

**Biggest caveat:** the faculty sample comes from POLMETH (92% of traced ads), so it is quant-leaning and US-heavy. 9 of the 12 European faculty hires hold US PhDs. It does not describe the typical European market. The postdoc sample is more European (57% of traced postdoc ads are outside the US).

Full write-ups: [`REPORT.md`](REPORT.md) (faculty) · [`POSTDOC_REPORT.md`](POSTDOC_REPORT.md) (postdocs).

## Methodology

**1. Ad collection (Gmail).**
- **Sources:** all messages from the POLMETH list (`polmeth@listserv.wustl.edu`, later `@lists.psu.edu`; Nov 2021–Nov 2026) and the EPSS-info list (from June 2025, when the subscription began). The EPSA-info list was also searched but carried no job ads.
- **Search:** subject-keyword queries (rank and post terms, plus a second pass on "job/position/hiring/search"), paged in date windows. EPSS threads were classified by hand because many subjects contain no keywords.
- **Cleaning:** cross-posts and reposts within about 60 days were merged.
- **Result:** 382 faculty ads and 344 postdoc ads. Excluded from both: PhD/predoc, RA, visiting, adjunct, and calls for papers or summer schools. NYU-style "Faculty Fellow" posts are counted as postdocs.

**2. Choosing ads to trace.**
- **Faculty:** tenure-track or permanent ads old enough for a hire to have started: POLMETH before Jul 2025 and EPSS before Mar 2026 (n=231).
- **Postdocs:** ads before Mar 2026 (n=252).

**3. Inferring the hire.** Research agents searched for each ad's hire on:
- department staff pages and "welcome new faculty" posts
- project, ERC and centre team pages, and fellowship cohort pages
- PI lab pages
- candidates' own CVs and websites

A hire was matched on unit, rank, subfield and a start date 6–18 months after the ad. Each match was graded:
- **high:** explicit evidence tying the person to the post
- **medium:** right unit, rank, subfield and timing
- **low:** plausible guess

The results above use high and medium only; adding low leaves the medians unchanged. Rumour forums were not accepted as evidence.

**4. CV coding (as of start year).**
- **Coded:** PhD institution, country and year; years since PhD; prior postdocs; refereed journal articles published or forthcoming by the start year (no chapters or working papers); solo/first-authored articles; top-journal articles; books; and for postdocs, the next position.
- **Sources:** dated CV PDFs first, then profile and Scholar pages, then ORCID or Crossref.

**5. Coverage.** Hires identified (high/medium) for 44% of faculty ads (122 people) and 23% of postdoc ads (73 people). Main reasons for misses:
- failed or re-run searches
- JavaScript-only or blocked department sites
- team pages listing only current staff
- the Wayback Machine being unreachable
- ads too recent for a hire to appear

**6. Known biases.**
- **Sample:** list-based and POLMETH-dominated.
- **Counts:** probably undercounted where coding relied on databases. First-author counts are unreliable where author order is alphabetical.
- **Matching:** some faculty hires may come from a later re-run of the same search.
- **Postdoc outcomes:** known mainly for people who already moved, which flatters success rates.
- **Small cells:** subgroups outside the US are small (n=3–12).

## Repository contents
- `data/ads_all.csv`, `data/ads_traced.csv`: faculty ads.
- `data/hires_all_rows.csv`: every faculty tracing row, including misses, with evidence URLs.
- `data/hires_identified_highmed.csv`: the faculty analysis sample.
- `data/postdoc/`: the same files for postdocs.
- `data/summary_*.txt`, `data/postdoc/summary_*.txt`: full summary tables, with and without low-confidence matches.
- `scripts/analyze.py`, `scripts/pd_analyze.py`: the analysis code.

*Privacy note: the data name real people and record details from their public CVs. Keep this repository private.*
