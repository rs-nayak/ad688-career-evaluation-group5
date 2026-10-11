   # AD688 Career Evaluation Product: Group 5

   Team project for AD688 O1 Fall '26 (Boston University MET). We evaluate career prospects for Data Scientists in Scientific Research and Development Services (NAICS 5417) using the MET Career Compass 2026 job-posting data (760 postings, January 6 to August 23, 2026).

   **Team:** Richa Nayak, Benjamin Nagle, James Lillis, Victoria Loukas

   **Website:** https://rs-nayak.github.io/ad688-career-evaluation-group5/

   ## Contents
   - `index.qmd` to `final_recommendations.qmd`: the pages of the project website
   - `final_report.qmd`: the written report, rendered to Word
   - `output/career_market_panel.csv`: the cleaned posting panel; `output/data_dictionary.csv` describes its columns
   - `theme.py`: shared Plotly chart theme

   ## Setup
   1. Create a `.env` file from `.env.example` and add your API key. Never commit `.env`.
   2. Install packages: `pip install -r requirements.txt`
   3. Render the site: `quarto render`
   4. Render the report: `quarto render final_report.qmd --to docx`
