import pandas as pd
from groq import Groq


class AIEngine:

    def __init__(self, api_key):
        self.client = Groq(api_key=api_key)
        self.model = "openai/gpt-oss-120b"

    def build_dataset_summary(self, df):

        summary = f"""
You are analyzing a business dataset.

DATASET OVERVIEW
----------------
Total Rows: {len(df)}
Total Columns: {len(df.columns)}

COLUMN INFORMATION
------------------
"""

        for col in df.columns:
            summary += f"\n- {col} ({df[col].dtype})"

        summary += f"""

DATA QUALITY
------------
Missing Values: {df.isnull().sum().sum()}
Duplicate Rows: {df.duplicated().sum()}

NUMERICAL SUMMARY
-----------------
{df.describe().to_string()}

SAMPLE DATA
-----------
{df.head(10).to_string()}

Analyze this dataset as a Senior Business Intelligence Consultant.

Provide a professional business report using these sections:

1. Executive Summary
2. Key Insights
3. Business Risks
4. Recommended Visualizations
5. Business Recommendations

Make your analysis specific to the actual dataset.
Avoid generic recommendations.
Use clear headings and bullet points.
"""

        return summary

    def analyze_dataset(self, df):

        prompt = self.build_dataset_summary(df)

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a Senior Business Intelligence "
                        "Consultant specializing in data analytics, "
                        "business intelligence and strategic insights."
                    )
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content