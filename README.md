# Project B — LLM Governance for SOC (Policy + Controls + Evaluation)

This package includes:
- Streamlit SOC assistant (`app.py`) using Llama Guard 3 + Llama 3 Instruct
- Evaluation suite in `evaluation/`
- Policy PDFs in `report/`

Run locally:
```bash
pip install -r requirements.txt
streamlit run app.py
```


### Added model option
- `Qwen/Qwen2.5-Coder-32B-Instruct` is available as a selectable assistant model in the Streamlit sidebar.


## Qwen-only mode
This build uses **Qwen/Qwen2.5-Coder-32B-Instruct** for both the policy decision and the SOC response generation (no Meta models).
