Wikipedia trust + revisions:
type: "literature-review-agent"
version: 1.0
description: "AI workflow for extracting findings related to Wikipedia trust, revision activity, and the impact of AI on collaborative knowledge production." This workflow automates our literature review by extracting structured insights from research about Wikipedia’s trust and sustainability in the age of AI. The agent determines whether a paper is relevant to our project and summarizes its contribution efficiently.
Input: 
- Full text of a research article
- Information about the research article
- URL?

Any of the above is acceptable 1 or more

Output:
Citation — properly formatted in APA  
Relevance level
Key fields directly tied to our research questions
Main findings (focus on trust + revisions + transparency)  
Useful quotes with page # / section

Instructions:
- Only use information explicitly found in the paper  
- NO hallucinated claims or citations  
- Focus on insights useful for:
  related-work.tex
  building on trust metrics in week7.py results
- If relevance is uncertain, ask the user to clarify

Expected output: 
```yaml
paper_summary:
  citation: "Author, A. A. (Year). Title. Journal..."
  relevance level: 1-10
  relevance_reason: "..."
  methods: "..."
  findings:
    - "..."
    - "..."
  evidence_strength: "..."
  limitations: "..."
  key_quotes:
    - "\"Quote\" (p. #)"
