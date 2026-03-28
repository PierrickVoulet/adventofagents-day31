# Advent of Agents - Day 31: A2UI Weather Agent Showcase

Welcome to **Day 31** of the [Advent of Agents](https://adventofagents.com/)! 

This repository demonstrates how to build an Agent-to-Agent (A2A) weather assistant using the **Google Agent Development Kit (ADK)**, **Gemini Enterprise (gemini-2.5-flash)**, and **A2UI** for rich, interactive rendering.

## Project Structure

This repository has been refactored into two versions to demonstrate the progression of A2UI capabilities:

### [Version 1](./version-1/)
The original code base. It features a basic A2A weather agent that returns standard A2UI rendering schemas using simple Rows and Columns to build weather and forecast cards.

### [Version 2](./version-2/)
The enhanced "Colorful Weather App". This version pushes A2UI to its limits using:
- **Dynamic Data Binding (`valueStruct`)**: Decoupling the UI structure from the data model.
- **Looping Lists**: Using the `List` component and templates to render multi-day forecasts.
- **Dynamic Theming**: The agent automatically updates the `primaryColor` of the UI (e.g., Amber for Sunny, Deep Purple for Stormy) based on real-time weather conditions.
- **Interactive Buttons & Unit Toggles**: Actionable buttons (`sendText`) that allow users to query new locations or instantly toggle between **°C** and **°F** directly on the card.
- **Multi-modal Soundscapes**: Integration of the `AudioPlayer` component to play ambient weather sounds (rain, wind, chimes) based on current conditions.
- **Rich Media**: Dynamically loaded images and polished visual styles.

## Technologies Demonstrated

- **Gemini Enterprise**: Utilizing the powerful reasoning of Gemini 2.5 Flash.
- **Agent-to-Agent (A2A) Protocol**: Standardizing how agents communicate and discover each other via `.well-known/agent-card.json` and JSON-RPC.
- **A2UI**: Moving beyond plain text responses to deliver rich, interactive UI components natively rendered by Gemini Enterprise.

## Prerequisites

- An existing [Google Cloud Project](https://console.cloud.project/).
- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install).
- [Python 3.11+](https://www.python.org/downloads/).
- The `uv` package manager (recommended) or standard `pip`.

## Installation & Running Locally

1. Clone the repository and navigate to either `version-1` or `version-2`:
    ```bash
    cd version-1  # or version-2
    ```

2. Create a Python virtual environment and activate it:
    ```bash
    uv venv .venv
    source .venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set your `GOOGLE_API_KEY` in your environment (or create a `.env` file).

5. Start the agent server:
    ```bash
    uvicorn main:app --port 8001
    ```

The agent will run on `http://localhost:8001`.

## Deployment

### Deploy Both Versions (Recommended)
You can deploy both versions sequentially using the root `deploy_all.sh` script. Version 2 will automatically be named with a `-v2` suffix.

```bash
bash deploy_all.sh <YOUR_PROJECT_ID> <BASE_SERVICE_NAME> [MODEL_NAME]
```

### Deploy Individually
To deploy a specific version, use the `deploy.sh` script within that directory:

```bash
cd version-2
bash deploy.sh <YOUR_PROJECT_ID> <YOUR_SERVICE_NAME> [MODEL_NAME]
```

*Note: The default model is `gemini-2.5-flash`.*

## Presentation

A polished presentation deck explaining the A2A and A2UI architecture is available in the `slides/` directory. 
- `slides/presentation.html`: The interactive slide deck featuring SVG animations and live UI mockups.

## Disclaimer

This is not an officially supported Google product. Code and data from this repository are intended for demonstration purposes only.
