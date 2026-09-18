# InRA — Internet Research Agent

InRA is a command-line research assistant for finding and organizing publicly available information about people, organizations, companies, brands, products, and other entities. It combines an LLM served through OpenRouter with Tavily web search, then can save a research report locally.

> Use InRA only for lawful, ethical research of publicly available information. Do not use it to seek, infer, collect, or share private, sensitive, or otherwise non-public personal information.

## Features

- Searches the web for an entity and name variations
- Helps distinguish between similarly named people or entities
- Produces structured reports covering identity, online presence, social profiles, notable information, possible matches, and sources
- Saves reports in `research_results/`
- Keeps a short-term in-memory conversation thread while the program is running

## Requirements

- Python 3.12 or later
- An [OpenRouter](https://openrouter.ai/) API key
- A [Tavily](https://tavily.com/) API key

## Installation

Clone the repository and move into it:

```bash
git clone <repository-url>
cd inra-AI-agent
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell, activate it with:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Keep `.env` private; it contains credentials and should never be committed to source control.

The agent is configured in `agent/agent.py` to use `deepseek/deepseek-r1` through OpenRouter. Change the `model` value there if you want to use another compatible model.

## Run

```bash
python main.py
```

Enter a research request at the prompt, for example:

```text
You: Research the public online presence of Example Organization.
```

Enter `q` to quit.

The assistant may use its search tool, respond with its findings, and save a report when asked. Saved reports are written to `research_results/`, which is created automatically when needed.

## Project structure

```text
.
├── main.py           # Interactive CLI loop
├── agent/
│   ├── agent.py      # Model, tools, agent, and session configuration
│   └── prompts.py    # Research instructions and report format
├── tools/
│   └── tools.py      # Tavily search and local report-storage tools
├── requirements.txt  # Pinned Python dependencies
└── .env              # Local API keys (create locally; do not commit)
```

## How it works

1. `main.py` accepts a request in an interactive terminal session.
2. The LangChain agent uses the OpenRouter-hosted model to decide whether to call a tool.
3. `internet_search` uses Tavily's advanced search to retrieve public web results.
4. The model compiles a sourced, structured response.
5. When requested, `save_research_result` writes the report under `research_results/`.

## Responsible use

Treat results as leads, not proof. Verify important claims against authoritative sources, distinguish uncertain matches, and comply with the terms of the sites and services you access. Never attempt to access private accounts, credentials, financial data, precise home addresses, private contact details, or other sensitive personal information.

