# What does it take to get hired? PolMeth/EPSS faculty ads, 2021–2026

## Pipeline
1. **Ads** (`data/ads_all.csv`, n=382): faculty ads from Gmail, deduplicated across lists. POLMETH covers Nov 2021–Nov 2026; EPSS-info covers only Jun 2025 onward (that's when the subscription starts); EPSA-info contained no job ads, only CFPs. Postdoc, PhD, visiting, adjunct and "faculty fellow" posts are excluded.
2. **Traced** (`data/ads_traced.csv`, n=231): tenure-track or permanent ads old enough for a hire to be visible (POLMETH before Jul 2025; EPSS before Mar 2026).
3. **Hires** (`data/hires_all_rows.csv`): research agents checked department staff pages, news posts and CVs to infer each hire, then coded the CV *as of the start year*. 101 of 231 ads (44%) have a high- or medium-confidence hire, giving 122 people; another 55 rows are low-confidence guesses. Counts are refereed journal articles only, published or forthcoming by the start year.

## Main result: junior and open-rank hires (n=110, high/medium confidence)
| | median | IQR |
|---|---|---|
| Peer-reviewed articles at start | **4** | 2–9 |
| Solo/first-authored | 2 | |
| Articles in top general/field journals | 1 (49% have ≥1) | |
| Years since PhD | 2 | |
| Share with a postdoc/VAP | 53% | |
| Share hired ABD or straight from the PhD | 21% | |

Only 2% were hired with zero publications; 29% had ≤2; 22% had ≥10. Publication counts rise with time since the PhD: median 3 at year 0, 2–5 at years 1–3, and 12 at year 4+.

**By subfield** (median articles / share with a top-journal article):
- IR 3.5 / 59%
- American 4 / 43%
- Comparative/PE 8 / 55%
- Computational social science 6 / 50%
- Methods 3 / 50%
- Open field 3 / 50%
- Policy/other 7 / 33%

Methods and American hires are the most likely to be hired straight out of the PhD (25–36%). CSS hires most often did a postdoc first (68%).

**By region** (n; median articles): US 84; 4 · Continental Europe 12; 4.5 · UK/Ireland 3; 4.5 · Canada 3; 9 · Asia/Middle East 7; 3. US hires are the ones most often taken straight from the PhD (23%). Outside the US, nearly everyone hired is post-PhD, typically 2–3 years out with a postdoc.

**Senior/lateral hires** (n=12): median 9 articles, 12 years post-PhD.

**Robustness:** including low-confidence matches (n=159 junior) gives the same medians (4 articles, 1 top, 2 years post-PhD). High-confidence-only hires look somewhat stronger (median 6 articles).

## Caveats (read before citing)
- **Selection by list:** 87% of traced ads came from POLMETH, so the sample is quant/methods-heavy and US-heavy. Even the European hires mostly hold US PhDs (9 of 12), because European departments that post on POLMETH want US-style quant candidates. This is *not* a picture of the typical European market. EPSS coverage starts only in mid-2025, too late for most hires to be visible.
- **Non-European cells are small:** the UK, Canada and Asia each have ≤7 hires, so treat those numbers as anecdotes.
- **Inference error:** 56% of ads have no identified hire. Searches fail, get re-run, or the department site was unreadable (the Wayback Machine was unreachable). A hire can come from a later re-run of the same search.
- **Coding error:** about 15% of hires have no publication count, and some counts come from Crossref rather than a CV, so they are likely undercounts. First-author counts are unreliable where author order is alphabetical (formal/methods).
- **Third-party data:** the files name real people and contain information from their public CVs. Keep this repo private.
