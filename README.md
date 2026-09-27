# JARVIS Multi-Agent

A starter multi-agent assistant inspired by a JARVIS-style architecture.

## What it does
- Master Agent classifies a task.
- Routes work to specialized sub-agents.
- Includes Document, Excel/Data, Web Research, Video, Application Form, and Quality Control agents.
- Form submission is intentionally gated: the agent can prepare and fill data, but final submission requires explicit confirmation.

## Run
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

Type tasks such as:
- "PDF se report banao"
- "Excel me data calculate karo"
- "Ek promotional video banao"
- "Application form fill karo"
- "Website par form ki details prepare karo"

This is a starter framework. Real browser automation/API credentials can be connected later.
