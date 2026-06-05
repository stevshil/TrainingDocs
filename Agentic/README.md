# Pydantic and Agentic

This folder makes use of running a local LLM, but can also be used with OpenAI and Claude accounts if need be.

This project also uses **uv** instead of **pip**.

## Table of Content

- [Install Ollama Server](#install-ollama-server)
  - [Using systemctl](#using-systemctl-to-control-service)
  - [Manual server control](#manual-server-execution)
- [Download Ollama LLMs](#download-language-for-ollama)
- [Using uv](#using-uv)

# Install Ollama Server

```
curl -fsSL https://ollama.com/install.sh | sh
```

This installs and runs a local Ollama LLM server on port 11434.

On Linux you can control the service with **systemctl**

On AMD systems Ollama detects AMD GPU perfectly.

On Intel systems with CUDA GPUs it falls back to CPU.  See the following for help;

- https://www.serverman.co.uk/server/ollama-gpu-not-detected-how-to-fix-cuda-and-rocm-errors/

## Using systemctl to control service

### Get status

```
sudo systemctl status ollama
```

### Stop

```
sudo systemctl stop ollama
```

### Start

```
sudo systemctl start ollama
```

## Manual server execution

### Start

```
ollama serve
```

# Download model for Ollama

```
ollama run llama3
```

or using the service method

```
ollama pull mistral:7b
```

Other models

```
ollama pull qwen2.5:7b-instruct
```

Instead of gpt-4o-mini

# Uninstall model

List models

```
ollama list
```

Remove

```
ollama rm gpt-oss:120b
```

# Installing Astral UV

See the main page for details for your system:

- https://docs.astral.sh/uv/getting-started/installation/

On Ubuntu and other Linux systems, use:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

# Using **uv**

A short intro to using UV instead of pip.

| UV command | PIP command | Description |
|---|---|---|
| `uv venv` | `python -m venv .venv` | Create the virtual environment |
| `source .venv/bin/activate` | `source .venv/bin/activate` | Activate the virtual environment |
| `uv init .` | N/A | Initialise the current directory as the UV project |
| `uv add pydantic` | `pip install pydantic` | Install the **pydantic** module |
| `uv run python main.py` | `python main.py` | Run the script called **main.py** |
| `uv sync` | `python -m venv .venv && pip install -r requirements.txt` | Sets up the project from existing pyproject.toml and .python-version files |

# Running the examples

1. Create a **lab.env** file
2. Add the following to that file
    ```sh
    export OPENAI_API_KEY="ollama"
    export OPENAI_BASE_URL="http://localhost:11434/v1"
    ```
3. Install the environment variables from the **lab.env** file as follows.
    - In the terminal that you have run your **uv** commands
    - Type `source lab.env`
      - This will ensure that the **mistral** examples will use your local Ollama server.
    - Now run one of the examples