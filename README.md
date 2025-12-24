# Project B — LLM Governance for SOC (Policy + Controls + Evaluation)

This repository is an ETM/policy-focused governance artifact for safe adoption of LLMs in a Security Operations Center (SOC).  
It combines **policy**, **controls**, and a **mini evaluation** with a Streamlit prototype.

## What’s included
- **Streamlit SOC assistant**: `app.py`
- **Evaluation suite**: `evaluation/`
- **Policy PDFs**: `report/`

## How the prototype works (Hugging Face)
The Streamlit SOC assistant uses **Hugging Face Inference Providers** via the Hugging Face router endpoint:
- `https://router.huggingface.co/v1/chat/completions`

The app sends your prompt to a selected **open model hosted on Hugging Face** (e.g., Qwen).

## Hugging Face API Token (Bring Your Own Token)
This project is designed to be hosted publicly (GitHub + Streamlit) **without exposing private credentials**.

- The Streamlit sidebar includes a **password-style input** where each user pastes their own **Hugging Face API token**.
- The token is **not stored** in the repository and is **not committed to GitHub**.
- For public demos: use a **low-privilege token** and do **not** paste real secrets/production credentials.

### Create a Hugging Face token
1. Create/login to Hugging Face
2. Go to **Settings → Access Tokens**
3. Create a token (read/use for inference)
4. Paste it into the Streamlit sidebar when running the app

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
