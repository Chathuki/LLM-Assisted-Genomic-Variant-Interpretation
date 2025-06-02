# 🧬 LLM-Assisted Genomic Variant Interpretation

An offline-ready AI tool that helps bioinformaticians and geneticists interpret genomic variant data using local LLMs like GPT4All.

## 🔍 Features

- Interpret VCF-like or tab-separated variant entries
- Query clinical significance, gene impact, or explanation
- No internet needed — completely local

## 📁 Folder Structure

- `variants/example_variants.txt` – sample variant list
- `models/` – place your GPT4All model here

## 💻 Run Locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
Download GPT4All model (e.g., GPT4All Groovy) and place in models/.
Run the app:
streamlit run app.py

Example Questions
"Which variants are pathogenic?"

"Explain the clinical significance of TP53 mutation"

"What is the function of BRCA2?"
