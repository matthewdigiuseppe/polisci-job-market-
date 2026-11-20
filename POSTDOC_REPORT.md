# What does it take to get a postdoc? PolMeth/EPSS postdoc ads, 2021–2026

## Pipeline
- **Ads** (`data/postdoc/ads_all.csv`, n=344): postdoc ads from POLMETH (Nov 2021–Nov 2026) and EPSS (Jun 2025–Nov 2026), deduplicated. Includes project postdocs, centre fellowships, data-science fellowships, independent fellowships and teaching postdocs. PhD, predoc and RA posts are excluded.
- **Traced** (`data/postdoc/ads_traced.csv`, n=252): ads posted before March 2026. These come from the US 109, Germany 33, UK 25, Switzerland 15, France 10 and elsewhere.
- **Hires:** research agents used project and centre team pages, fellow-cohort pages, PI lab pages and CVs to name the people hired. A second pass coded each person's CV *as of the postdoc's start year*, downloading CV PDFs directly where possible.
- **Coverage:** 57 of 252 ads (23%) have a high- or medium-confidence hire, giving **73 people**, 70 of them with publication counts. Another 34 rows are low-confidence guesses. Two misidentified hires were dropped.

## Main result (n=73, high/medium confidence)
| At start of postdoc | |
|---|---|
| Peer-reviewed articles, median (IQR) | **2** (0–3) |
| Share with zero articles | 26% |
| Share with ≤1 article | 49% |
| Share with ≥5 articles | 13% |
| Has ≥1 top general/field-journal article | 25% |
| Years since PhD, median | **0**; 70% start ABD or in the year they defend |
| Already did a previous postdoc | 14% |
| US PhD | 63% |

**What came next** (32 people whose next job is known): 66% moved to an assistant professor or lecturer post. That figure includes a few teaching-track and non-political-science posts. The rest took a second postdoc, a Marie Curie or Leverhulme fellowship, or a non-academic research job. Outcomes are known mostly for US centre and data-science fellows; most 2024–25 starters are still in post.

**By type** (n; median articles; share with a top-journal article; share whose next job, where known, was an assistant professorship or lectureship):
- Centre fellowships (23): 1 article, 26%, 83% (10 of 12)
- Data-science fellowships (5): 1, 20%, 4 of 4
- Project postdocs (41): 2, 24%, 40% (6 of 15)

Centre fellowships are the most selective by outcome: 83% of fellows whose next job is known moved to a tenure-track post. They are *not* the most demanding by publication count, because they mainly hire straight from the PhD, judging on the job-market paper and pedigree. 83% of centre fellows have US PhDs.

**By region** (n; median articles; share with zero articles):
- US (40): 1.5, 18%
- German-speaking countries (11): 3, 36%
- France/Southern Europe (8): 1, 38%
- UK/Ireland (8): 0, 50%

European project postdocs look bimodal: they hire either fresh PhDs with nothing published or people who already have 3–4 articles. Most European hires (62–73%) hold non-US PhDs, unlike the faculty sample.

**By subfield** (median articles): American 3, methods 3, CSS 2, comparative/PE 1, IR 1. These cells are small.

## Postdoc vs. faculty hires in the same lists
| | Postdoc start | Junior faculty start |
|---|---|---|
| Median articles | 2 | 4 |
| Share with a top-journal article | 25% | 49% |
| Median years since PhD | 0 | 2 |
| Share with a prior postdoc | 14% | 53% |

Read across, the typical path is about two years of postdoc in which a candidate roughly doubles their article count and gets a first top-journal hit.

## Caveats
- **Low coverage:** only 23% of ads have a traced hire. Project postdocs are often invisible online: team pages are JavaScript-rendered, list only current staff, or were blocked, and the Wayback Machine was unreachable. Ads from late 2025 to early 2026 mostly have no posted hire yet.
- **Small cells:** by region and subfield the samples are small (n=3–11 outside the US). Treat those numbers as illustrative.
- **Coding sources:** about a third of CVs were coded from profile pages or databases (ORCID, Crossref) rather than a dated CV, so counts are probably undercounts. Several hires in cross-disciplinary posts (public health, CS, sociology) are not political scientists.
- **"Next position" is selected:** it's known mainly for people who already moved on. Successful movers are probably over-represented.
- **Low-confidence robustness:** adding low-confidence matches (n=107) gives the same medians (2 articles, 0 years post-PhD), with somewhat fewer top-journal articles (18%).
- **Third-party data:** the files name real people and contain information from their public CVs. Keep the repo private.
