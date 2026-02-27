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

### Phase 1: Foundation (DONE / In Progress)

- [x] Visa route clarified — non-monetised project, British co-founder handles any formal registration
- [x] Journal identity defined: AI-Driven Energy Research (AIDER)
- **Scope:** AI applications in energy systems — including but not limited to: ML for CFD, AI-driven grid optimisation, autonomous energy system design, reinforcement learning for control, generative models for materials discovery, LLM-assisted research workflows
- **Differentiator:** Mandatory open-source code + data + documented AI-assisted research process

---

### Phase 2: Set Up the GitHub Organisation ← YOU ARE HERE

This is the backbone of AIDER. The journal effectively lives on GitHub.

#### 2.1 Create the GitHub Org
- [ ] Go to https://github.com/organizations/plan and create a **free** organisation
- Suggested name: `aider-journal` or `ai-driven-energy-research`
- Add a profile README explaining what AIDER is

#### 2.2 Create the Journal Website Repo
- [ ] Create repo: `aider-journal/aider-journal.github.io`
- Use GitHub Pages (free) with a static site generator (Hugo or Jekyll)
- Pages needed:
  - **Home** — what is AIDER, the manifesto
  - **Scope** — what topics are covered
  - **Submit** — how to submit (link to GitHub Issues template)
  - **Papers** — list of published papers with links to their repos
  - **Editorial Board** — who is involved
  - **Process** — explanation of the open-process requirement
- No domain purchase needed — `aider-journal.github.io` works fine and costs nothing

#### 2.3 Create Submission Template Repo
- [ ] Create repo: `aider-journal/paper-template`
- This is a template repository that authors fork to start a submission
- Structure:
  ```
  paper-title/
  ├── paper/
  │   ├── main.tex           # or main.md — the manuscript
  │   └── figures/
  ├── code/
  │   ├── README.md           # How to set up and run
  │   ├── requirements.txt    # or environment.yml / Dockerfile
  │   └── src/                # All source code
  ├── data/
  │   └── README.md           # Data description, links, license
  ├── process-log/
  │   ├── README.md           # Overview of how paper was produced
  │   ├── ai-sessions/        # AI agent logs, transcripts, prompts
  │   └── human-decisions/    # Timestamped log of human interventions
  ├── results/
  │   └── reproduce.sh        # Script that regenerates all figures/tables
  ├── REPRODUCIBILITY.md      # Checklist (does code run? data available? results match?)
  ├── LICENSE                  # CC-BY 4.0 for paper, MIT for code
  └── README.md               # Paper title, abstract, how to cite, how to run
  ```

#### 2.4 Define the Submission Workflow (All on GitHub, Zero Cost)
- **To submit:** Author forks `paper-template`, fills it in, then opens an Issue on `aider-journal/submissions` with a link to their repo
- **Review:** Editor assigns 2 reviewers. Review happens as GitHub Issues / PR comments on the author's repo — fully public
- **Two-track review:**
  - **Track A: Scientific merit** — is the research sound, novel, and well-presented?
  - **Track B: Reproducibility** — can a reviewer clone the repo, run `reproduce.sh`, and get the claimed results? (Hard gate — if code doesn't run, paper is not accepted)
- **Acceptance:** Accepted paper repo is forked into the `aider-journal` org. Listed on the website.
- **AI-assisted review is allowed** — reviewers may use AI tools but must disclose how

---

### Phase 3: Write the Founding Documents

#### 3.1 The AIDER Manifesto
- [ ] Write and publish in the website repo. Key messages:

1. **"Open process, not just open access."** — We don't just share the paper. We share how it was made.
2. **"AI is a collaborator, not a secret."** — Using AI to write, code, or analyse is encouraged and must be disclosed. There is no shame in working with AI.
3. **"If it can't be reproduced, it doesn't count."** — Code must run. Data must be available. Results must match.
4. **"A paper should be a living product."** — Published papers live on GitHub. They can be forked, improved, and extended by anyone.
5. **"Free as in freedom, free as in beer."** — No paywalls. No author charges. No money changes hands. Ever.

#### 3.2 Submission Guidelines
- [ ] Write clear author guidelines covering:
  - What must be included (code, data, process log)
  - Process log requirements — what counts as sufficient documentation
  - Licensing: papers CC-BY 4.0, code MIT or Apache 2.0, data CC0 or CC-BY 4.0
  - How the review process works
  - Timeline expectations

#### 3.3 Reviewer Guidelines
- [ ] Write reviewer instructions:
  - How to assess scientific merit
  - How to assess reproducibility (clone, install, run, compare)
  - That reviews are public and signed
  - That AI-assisted review is fine but must be disclosed

---

### Phase 4: Recruit the Editorial Board

You need 5-10 people to give this credibility. Target:

- [ ] **Your PhD supervisor(s)** — approach first, they are your anchor
- [ ] **2-3 Oxford academics** in CFD, ML, or energy
- [ ] **2-3 external academics** — people active in open science, Papers With Code, or reproducibility initiatives
- [ ] **1-2 early-career researchers** — PhD students or postdocs who are enthusiastic about AI-driven research

**How to recruit:**
- Write a 1-page pitch document (can reuse the manifesto + scope)
- Email individually — don't mass-email. Personal approach works better
- Emphasise: this is voluntary, no time commitment beyond occasional reviews, and they get to shape a new kind of journal

---

### Phase 5: Bootstrap with Your Own Papers

- [ ] Publish your paper-factory outputs as the founding articles of AIDER
  - `demand_forecasting` — ML demand forecasting
  - `draft_tube_cavitation` — CFD draft tube
  - `fowt_hydro_coupled` — Floating wind turbine
- [ ] For each, create the full submission package: paper + code + data + process-log (your paper-factory logs are the process log)
- [ ] Run them through the review process with your editorial board — this tests the whole system
- These founding papers demonstrate what AIDER submissions look like in practice

---

### Phase 6: Get Discoverable (Free Methods Only)

#### 6.1 Immediate (Free, Automatic)
- **Google Scholar** — automatic if papers have proper HTML meta tags (citation_title, citation_author, citation_pdf_url). GitHub Pages can do this.
- **Semantic Scholar** — automatic crawling of well-structured academic pages

#### 6.2 ISSN Registration (Free)
- [ ] Apply for an ISSN (International Standard Serial Number) at https://www.issn.org/
- Free to obtain, gives the journal a formal identity
- Your British co-founder can be the applicant if needed

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

| Time | Milestone |
|---|---|
| **This week** | Create GitHub org, website repo, paper template repo |
| **Week 2-3** | Write manifesto, submission guidelines, reviewer guidelines |
| **Week 3-4** | Recruit editorial board (start with supervisor) |
| **Month 2** | Package your 3 paper-factory papers as founding submissions |
| **Month 2-3** | Run founding papers through review process |
| **Month 3** | **Official launch** — publish founding papers, announce on Twitter/X |
| **Month 3-6** | Apply for ISSN, set up Zenodo DOIs, invite external submissions |
| **Month 6-12** | Aim for 10+ papers, apply to DOAJ |
| **Year 2+** | Scopus application |

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

## Immediate Next Steps (Do Now)

1. [ ] **Create GitHub org** — `github.com/aider-journal`
2. [ ] **Create `aider-journal.github.io` repo** — basic landing page with the vision
3. [ ] **Create `paper-template` repo** — the standardised submission structure
4. [ ] **Write the manifesto** — publish it on the website
5. [ ] **Talk to your supervisor** — show them this plan, get their backing
6. [ ] **Find your British co-founder** — for any future formal registration needs

---

*Founded by Jianou Jiang, DPhil candidate in Engineering Science, University of Oxford, 2026.*
