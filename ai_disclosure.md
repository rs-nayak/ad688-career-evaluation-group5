# AI Disclosure: Victoria Loukas, Group 5

**Course:** AD688 O1 Fall '26, Career Evaluation Team Project
**Tool and provider:** Claude (Anthropic), used through the Claude app
**Dates used:** October 11, 2026

## Tasks Claude helped with

1. **Predictive Modeling page (`ml_methods.qmd`).** Claude wrote the K-Means and PCA code, the choice-of-k plots, the segment profile table, and the interpretation text.
2. **Career Evaluation, Final Recommendations and `final_report.qmd`.** Claude drafted the text from the team's Market Baseline, Data Preparation and Predictive Modeling pages.
3. **Setup help.** Claude walked me through connecting VS Code to the EC2 server, installing packages, and committing to GitHub.

## Prompts and conversation

*[Attach or link the full conversation here. The course requires complete prompts and, where supported, a shared conversation link.]*

## Validation steps

- I ran the clustering code on the real data on my EC2 instance and compared the output with the rendered website page. Segment sizes (261, 170, 150, 128, 51), salary medians and percentages matched the text.
- I checked how many postings had salary (240) and experience (503) before deciding how to handle missing values.
- Numbers in the recommendations and report were taken from the team's Market Baseline and Data Preparation pages.

## Corrections made to Claude's work

- The first version dropped postings missing salary or experience, which left only 133 of 760. We changed it to keep all 760 and compare salary afterward.
- Claude's first approach picked k by highest silhouette score, which just selected the largest k tested (8). We fixed k = 5 and said so on the page.
- Claude's first interpretation text was written before the final data was run and was replaced with text matching the real output.

## Items the team must confirm

- The self-ratings on the Skill Gap Analysis page are marked as placeholders in the code and need to be the team's real ratings.
- The Exploratory Analysis page loads a different, larger dataset (`data/jobs.csv`) than the 760-posting panel used elsewhere.
