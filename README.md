# AI-Driven Energy Research (AIDER)

## Vision

An open-access, open-source academic journal at the intersection of AI and energy research. Every paper published here is fully reproducible, immediately usable, and transparently produced.

**Core Principles:**
- AI-led research is embraced, not hidden
- All code, data, and methodology are open-sourced on GitHub
- The full process of producing a paper (including AI agent workflows and all human input) is documented and shared
- Free to read, free to publish — no paywalls, no APCs, no money whatsoever
- A published paper is not dead on arrival — it lives as a usable GitHub repository

**Operating Model: Entirely Non-Monetised**
- Zero revenue, zero costs beyond free-tier services
- No legal entity required — this is a volunteer academic community project
- A UK-based co-founder with full work rights handles any formal registration (Crossref, ISSN) if needed later
- Jianou Jiang serves as founding academic editor (voluntary/advisory role) — fully compatible with Tier 4 Student visa under UKCISA guidance for non-monetised academic activities

---

## Step-by-Step Roadmap

### Phase 1: Foundation (DONE)

- [x] Visa route clarified — non-monetised project, British co-founder handles any formal registration
- [x] Journal identity defined: AI-Driven Energy Research (AIDER)
- **Scope:** AI applications in energy systems — including but not limited to: ML for CFD, AI-driven grid optimisation, autonomous energy system design, reinforcement learning for control, generative models for materials discovery, LLM-assisted research workflows
- **Differentiator:** Mandatory open-source code + data + documented AI-assisted research process

---

### Phase 2: Set Up the GitHub Organisation (DONE)

This is the backbone of AIDER. The journal effectively lives on GitHub.

#### 2.1 Create the GitHub Org
- [x] Created: https://github.com/ai-driven-energy-research
- Organisation name: `ai-driven-energy-research`

#### 2.2 Create the Journal Website Repo
- [x] Created: https://ai-driven-energy-research.github.io/
- [x] Full website built with all pages: Home, Scope, Author Guidelines, Reviewer Guidelines, Ethics, Collaborative Research, Research Roadmap, News, Founder's Remarks, Join
- [x] Publisher statement added to footer (required by ISSN): "Published by AI-Driven Energy Research (AIDER), Oxford, United Kingdom."

#### 2.3 Create Submission Template Repo
- [x] Created: `ai-driven-energy-research/paper-template` with full structure (paper/, code/, data/, process-log/, results/, REPRODUCIBILITY.md, LICENSE)

#### 2.4 Define the Submission Workflow (All on GitHub, Zero Cost)
- [x] Submissions repo created with reviewer-agent tooling
- **To submit:** Author forks `paper-template`, fills it in, then opens an Issue on `ai-driven-energy-research/submissions` with a link to their repo
- **Automated AI review pipeline:** Three stages run automatically on every submission:
  1. **Reproducibility Check** — CI verifies repo structure, installs dependencies, runs `reproduce.sh`
  2. **AI Pre-Screening** — summarises paper, checks completeness, flags attention points
  3. **AI Deep Review** — audits bold claims ("first", "novel", etc.), checks reference accessibility, flags paywalled sources
- **Editorial decision:** An editor reviews the AI reports and makes the final call. Additional human reviewers may be invited at the editor's discretion
- **Acceptance:** Accepted paper repo is forked into the org. Listed on the website with a Zenodo DOI

---

### Phase 3: Write the Founding Documents (DONE)

#### 3.1 The AIDER Manifesto
- [x] Published on website homepage as "Founding Principles"

#### 3.2 Submission Guidelines
- [x] Published: `author-guidelines.html`

#### 3.3 Reviewer Guidelines
- [x] Published: `reviewer-guidelines.html`

#### 3.4 Ethics Policy
- [x] Published: `ethics.html`

---

### Phase 4: Recruit the Editorial Board (DONE — 7 founding editors)

- [x] Jianou Jiang — DPhil candidate, Engineering Science, University of Oxford (Founding Editor)
- [x] Raul Adriaensen — PhD candidate, Earth Science and Engineering, Imperial College London
- [x] Dr. Feng Wei — CAICT, Ministry of Industry and Information Technology (MIIT)
- [x] Dr. Yadong Han — Energy and Power Engineering, Tsinghua University
- [x] Qian Wang — Senior Supervisor, China Three Gorges Renewables
- [x] Shixin Huo — PhD candidate, Complex System Engineering, TU Delft
- [x] Jingda Wu — PhD candidate, Graduate School of Energy, Kyoto University
- [x] 5 AI Reviewer Agents configured: Claude, GPT, Gemini, Grok, Qwen

---

### Phase 5: Bootstrap with Founding Papers ← **CRITICAL PATH — NEED 5 PAPERS BY JUNE 2026**

**Published (1/5):**
- [x] `foundation-models-clean-energy` — Foundation Models for Clean Energy Systems: A Scoping Review and Deployment Framework
  - Published: Vol. 1, No. 1, 2026
  - DOI: 10.5281/zenodo.18902064
  - Repo: https://github.com/ai-driven-energy-research/foundation-models-clean-energy

**In production (need to finish):**
- [ ] `dam_safety_ai` — Physics-Informed AI for Dam Safety Monitoring
  - Repo: https://github.com/JianouJiang/dam-safety-ai-monitoring
- [ ] `desert_solar_sand_transport` — CFD-Aeolian Modeling of Wind-Sand Transport in Desert PV Mega-Bases
  - Repo: https://github.com/JianouJiang/desert-pv-sand-transport

**Need 2 more papers — options:**
- [ ] Recruit founding papers from editorial board members (Raul, Feng Wei, Yadong Han, etc.)
- [ ] Write additional short papers (e.g., methods paper on the AI review pipeline, reproducibility benchmark)

**ISSN requirement:** Minimum 5 articles per issue. Must publish Vol. 1, No. 1 with 5+ papers before contacting ISSN again in June.

---

### Phase 6: Get Discoverable (Free Methods Only)

#### 6.1 Immediate (Free, Automatic)
- **Google Scholar** — automatic if papers have proper HTML meta tags (citation_title, citation_author, citation_pdf_url). GitHub Pages can do this.
- **Semantic Scholar** — automatic crawling of well-structured academic pages

#### 6.2 ISSN Registration (Free) ← WAITING — RECONTACT JUNE 2026
- [x] Contacted ISSN UK Centre at the British Library (2026-03)
- [x] Received application form from Vicci Daniels, ISSN UK Centre
- [x] Completed and submitted application form (2026-03-05)
  - Title: AI-Driven Energy Research
  - Format: Online only
  - Frequency: Continuous (rolling publication)
  - URL: https://ai-driven-energy-research.github.io/
  - Publisher address: Dept of Engineering Science, University of Oxford
  - Contact: Jianou Jiang, jianou.jiang@eng.ox.ac.uk, +44 7761 956720
  - Requested by: 2026/06/01
  - First issue: Vol. 1, No. 1 (2026/06)
- [x] Response received (2026-03-12): Application held on file. ISSN will be assigned after first issue is published in June. No need to reapply.
- **Requirements from ISSN UK Centre:**
  - Minimum 5 articles per issue
  - Clear publisher statement on website (name + location) — **DONE** (added 2026-03-12)
- [ ] Publish Vol. 1, No. 1 with 5+ articles (by June 2026)
- [ ] Contact Vicci Daniels again after first issue is live
- Filed application: `Re_ ISSN request for new online-only journal/ISSN_Application_FILLED.docx`

#### 6.3 Zenodo Integration (Free)
- [ ] Each paper's GitHub repo gets archived on Zenodo (automatic via GitHub-Zenodo integration)
- This gives every paper a free DOI without Crossref fees
- Zenodo is run by CERN — reliable and free forever

#### 6.4 Later (Once You Have 5+ Papers)
- [ ] Apply to DOAJ (Directory of Open Access Journals) — free, requires 5 published articles
- [ ] Apply to Crossref for DOIs — your British co-founder registers as publisher (~$275/year, only when ready — can use Zenodo DOIs until then)

#### 6.5 Long-Term Indexing
- **Year 1-2:** Scopus application (requires established record, regular schedule)
- **Year 3+:** Web of Science / Impact Factor (requires sustained citations)

---

### Phase 7: Community Building (All Free)

- [ ] Twitter/X account: `@AIDERjournal` — share papers, reproducibility highlights
- [ ] Discord server — for authors, reviewers, readers, and anyone interested in AI+energy open science
- [ ] Monthly "reproducibility challenge" — community members pick a published paper and try to reproduce it, post results
- [ ] Partner with conference workshops (NeurIPS, ICLR, energy conferences) to invite extended papers

---

## Timeline

| Time | Milestone | Status |
|---|---|---|
| 2026-02 | Create GitHub org, website, paper template | **DONE** |
| 2026-02/03 | Write manifesto, guidelines, ethics | **DONE** |
| 2026-02/03 | Recruit editorial board (7 founding editors) | **DONE** |
| 2026-03 | Submit ISSN application | **DONE** — held on file, recontact June |
| 2026-03 | Publish first paper (foundation models) | **DONE** |
| 2026-03 | Add publisher statement to website | **DONE** |
| **2026-03–05** | **Finish dam safety + desert solar papers** | **IN PROGRESS** |
| **2026-03–05** | **Recruit/write 2 more papers (need 5 total)** | **TODO** |
| **2026-06** | **Publish Vol. 1, No. 1 with 5+ papers** | **TODO — CRITICAL** |
| 2026-06 | Recontact ISSN UK Centre for assignment | TODO |
| 2026-06+ | Set up Zenodo DOIs for all papers | TODO |
| 2026 H2 | Aim for 10+ papers, apply to DOAJ | TODO |
| 2027+ | Scopus application | TODO |

---

## Cost Breakdown

| Item | Cost |
|---|---|
| GitHub Organisation (free tier) | $0 |
| GitHub Pages website hosting | $0 |
| Zenodo DOIs | $0 |
| ISSN registration | $0 |
| Google Scholar indexing | $0 |
| DOAJ listing | $0 |
| Editorial work | Volunteer |
| **Total** | **$0** |

(Crossref DOIs: ~$275/year if you want them later — optional, Zenodo DOIs work fine)

---

## Immediate Next Steps (March–June 2026)

1. [ ] **Finish dam safety AI paper** — complete research, write manuscript, submit through review pipeline
2. [ ] **Finish desert solar sand transport paper** — complete research, write manuscript, submit through review pipeline
3. [ ] **Secure 2 more papers** — ask editorial board members to contribute founding papers, or write additional papers (e.g., AI review pipeline methods paper, reproducibility benchmark)
4. [ ] **Publish Vol. 1, No. 1** — list all 5+ papers on website with Zenodo DOIs and proper metadata
5. [ ] **Recontact ISSN UK Centre (Vicci Daniels)** — once issue is live with 5+ articles

---

*Founded by Jianou Jiang, DPhil candidate in Engineering Science, University of Oxford, 2026.*
