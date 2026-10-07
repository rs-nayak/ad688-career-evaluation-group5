import pandas as pd

df = pd.read_csv("data/jobs.csv", low_memory=False)

cols = [
    "POSTED", "SALARY", "SALARY_FROM", "SALARY_TO", "STATE_NAME", "MSA_NAME",
    "TITLE_NAME", "SKILLS_NAME", "SPECIALIZED_SKILLS_NAME",
    "SOFTWARE_SKILLS_NAME", "LOT_V6_CAREER_AREA_NAME", "ONET_NAME",
    "EMPLOYMENT_TYPE_NAME", "REMOTE_TYPE_NAME", "MIN_YEARS_EXPERIENCE",
]

print("=== % missing ===")
print((df[cols].isna().mean() * 100).round(1).to_string())

print("\n=== SKILLS_NAME sample (3 rows) ===")
for v in df["SKILLS_NAME"].dropna().head(3):
    print(repr(v)[:300])

print("\n=== SOFTWARE_SKILLS_NAME sample (3 rows) ===")
for v in df["SOFTWARE_SKILLS_NAME"].dropna().head(3):
    print(repr(v)[:300])

print("\n=== SALARY summary ===")
print(df["SALARY"].describe().to_string())

print("\n=== Top 15 career areas ===")
print(df["LOT_V6_CAREER_AREA_NAME"].value_counts().head(15).to_string())

print("\n=== Top 25 ONET_NAME ===")
print(df["ONET_NAME"].value_counts().head(25).to_string())

print("\n=== POSTED range ===")
posted = pd.to_datetime(df["POSTED"], errors="coerce")
print(posted.min(), "to", posted.max())