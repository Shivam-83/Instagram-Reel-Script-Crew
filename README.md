# Instagram Reel Script Crew

A small Streamlit app that generates Instagram Reel concepts, shot-by-shot scripts, captions, and hashtags using a multi-agent CrewAI workflow with Gemini LLM.

## Features

- Generate 3 viral reel concepts from a theme and pick the best
- Produce a 15–30s shot-by-shot script with timing, text overlays, and CTA
- Optimize caption, hashtags, and recommended posting time

## Requirements

- Python 3.10+ recommended
- See `requirements.txt` for runtime dependencies

## Setup

1. Clone or download this project.
2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file (in the project root) and add your Gemini API key:

```text
GEMINI_API_KEY=your_gemini_api_key_here
```

## Running the app

Recommended (Streamlit):

```bash
streamlit run app.py
```

Or run directly with Python:

```bash
python app.py
```

Open the Streamlit UI in your browser (the command above prints the local URL).

## Files

- `app.py` — Streamlit front-end that collects the reel theme and displays results
- `crew_reel.py` — CrewAI agents and tasks that generate and optimize reel content
- `requirements.txt` — Python dependencies

## Environment

The app reads `GEMINI_API_KEY` from environment variables (via `python-dotenv`). Ensure the key is set before running.

## Notes

- The project uses the `crewai` package to orchestrate agents and tasks with a Gemini LLM backend.
- Tailor prompts, agent backstories, or the LLM config in `crew_reel.py` to fit your target audience or style.

If you want, I can add a quick example theme and screenshot, or prepare a `Procfile` / GitHub Actions workflow for deployment.
