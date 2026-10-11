---
title: "AI Use Disclosure"
---

## Summary

Our team used a generative AI assistant as a **reviewer and planning aid** during the final stages of this project (Modules 5 and 6). It did **not** generate our data, run our analyses, or write the content of our analytical pages. Every finding, table, and figure on this site was produced by team members from our own code and our cleaned dataset (`output/career_market_panel.csv`).

| **Item**           | **Detail**                                                        |
| ------------------ | ----------------------------------------------------------------- |
| Tool               | Claude (Anthropic), Claude Opus 5.5, via the claude.ai web app    |
| Date(s) of use     | October 11, 2026                                                  |
| Used by            | Victoria Loukas                                                   |
| Project stage      | Module 5 (final analytics and report) and Module 6 (presentation) |
| Data shared        | Course instructions (pasted text) and our public GitHub Pages URL |
| Data **not** shared | Our API key, `.env` file, raw parquet files, or private data     |

## How AI Was Used

### 1. Interpreting the project instructions

We pasted the Module 5 instructions (Step 4, final analytics, and report) and the Module 6 instructions (final presentation and team assessment) into the assistant. We asked it to summarize the requirements: the three acceptable analytics tracks (regression, classification, segmentation/ranking), the five interpretation elements each analytical section needs, the seven required report sections, and the presentation flow and evidence slides.

### 2. Reviewing our published site against the requirements

We shared the URL of our GitHub Pages site. The assistant read our published pages (Home, Data Preparation, Market Baseline, Skill Gap Analysis, Predictive Modeling, Career Evaluation, and Final Recommendations) and compared them with the checklists. It noted which requirements appeared complete and which pages were still placeholders.

### 3. Suggesting an analytical approach

The assistant pointed out that only 240 of our 760 postings (31.6%) have usable salary data, while skills coverage is 96.4%. It suggested centering our final analytics on skills, consistent with our product question. Specifically, it proposed:

- a skill opportunity **scorecard** (Option C), combining demand share, salary premium, and accessibility (share of entry-level postings), with justified weights and a sensitivity check; and
- a supporting **high-salary classifier** (Option B), using logistic regression on the salaried subset, evaluated with accuracy, precision/recall, F1, and a confusion matrix.

The team did not adopt the scorecard or the classifier. We used K-Means segmentation (Option C) on all 760 postings instead, because it uses every posting and does not depend on salary, which is listed on only 31.6% of postings.

### 4. Flagging potential issues for us to check

The assistant raised two issues for the team to investigate. We verified both ourselves.

- **Skill-gap scaling.** Our method set the most-demanded skill to level 5 and scaled the others proportionally. This produced a required level below 1 for most skills, so nearly every skill showed a gap of zero. We have not changed the scaling yet. The self-ratings on that page are also still marked as placeholders in the code, so both need to be confirmed by the team before we submit.
- **Experience field.** 339 postings (44.6%) list a 0-year minimum. That may reflect a source default rather than a true entry-level requirement. We checked the Data Preparation page: missing experience was labeled "Not specified," not 0, so the 339 postings are ones that list 0 years. We cannot tell from the data whether some of those are source defaults.

### 5. Completion and planning checklist

The assistant gave us a prioritized to-do list for finishing the project. That list covered completing the analytics and Career Evaluation pages, writing recommendations and limitations, creating `final_report.qmd`, building the slide deck, and documenting team contributions. We used it to plan our final work and standups.

<!-- EDIT: add sections here for any later AI use, e.g. help debugging code, drafting text, or slide outlines. Be specific about what was AI-assisted and what the team changed. -->

## What AI Did Not Do

- It did not access, download, or process our dataset.
- It did not produce any of the numbers, tables, or figures on this site. All results come from our own code.
- It did not write the analytical text on the Data Preparation, Market Baseline, or Skill Gap Analysis pages, which were completed before this use.
- It did not decide our scope, career pathway, industry, or recommendations.

## Verification and Responsibility

We treated every AI suggestion as a recommendation to evaluate, not as a fact. We checked the claims it made about our site against our own pages and code. The team is fully responsible for the accuracy, interpretation, and conclusions presented in this project.

## Citation

Anthropic. (2026). *Claude* (Claude Opus 5.5) \[Large language model\]. https://claude.ai

Full conversation transcript (October 11, 2026): <https://claude.ai/share/114cb123-50dd-4994-805c-b3a4f1b1898f>
