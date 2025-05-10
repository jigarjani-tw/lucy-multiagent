# Lucy Multi-Agent System

A multi-agent system built with Agno that orchestrates specialized AI agents to provide factually accurate and well-presented responses.

## Overview

This project demonstrates a coordinated multi-agent system with three components:

1. **Deadpool Agent** - Provides factually accurate information with crude language
2. **Captain America Agent** - Polishes language but may hallucinate facts
3. **Lucy Orchestrator** - Coordinates between agents to produce perfect responses

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and add your API keys:
   ```
   cp .env.example .env
   ```
4. Edit `.env` with your API keys for Groq and OpenAI

## Usage

Run the Lucy orchestrator:
```
python lucy.py
```

Or run individual agents:
```
python dp.py  # Deadpool agent
python ca.py  # Captain America agent
```

## How It Works

The system uses Agno's Team class with "coordinate" mode to:
- Delegate specific tasks to each agent
- Maintain shared context between agents
- Review and synthesize the outputs from both agents

Lucy ensures the final response combines Deadpool's factual accuracy with Captain America's polite language.

## Requirements

- Python 3.8+
- Agno library
- OpenAI API key
- Groq API key
