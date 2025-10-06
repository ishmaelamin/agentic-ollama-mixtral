# agentic-ollama-mixtral

![AI Agent Banner](https://img.shields.io/badge/AI%20Engineering-Portfolio%20Project-blue?style=for-the-badge&logo=github)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME/ci-cd.yml?branch=main&label=CI/CD&style=for-the-badge)
![License: MIT](https://img.shields.io/github/license/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME?style=for-the-badge)

## 📖 Overview

This project demonstrates the setup and execution of a local AI agent using **Ollama**, the powerful **Mixtral** model, and the **LangChain** framework. The agent is configured with tools that enable it to perform multi-step reasoning and interact with the real world (e.g., performing web searches). The entire workflow, from code changes to testing, is automated using a **GitHub Actions CI/CD pipeline**.

This project serves as a comprehensive portfolio piece, showcasing skills in:
*   Local LLM deployment and management with Ollama.
*   Integrating language models with agent frameworks like LangChain.
*   Building end-to-end CI/CD pipelines using GitHub Actions.
*   Managing Python dependencies and virtual environments.

## ✨ Features

*   **Local Inference:** Uses Ollama to run the Mixtral model directly on a local machine, ensuring data privacy and reducing reliance on cloud-based APIs.
*   **Web Search Capability:** The agent is equipped with a web search tool (`duckduckgo-search`) to access and summarize up-to-date, external information.
*   **Automated CI/CD:** A GitHub Actions workflow automates the build, dependency installation, and testing process for continuous integration.
*   **Dependency Management:** Utilizes a Python virtual environment to create an isolated, reproducible environment for the project's dependencies.

## 🚀 Installation

### Prerequisites

*   **Git:** To clone the repository.
*   **Python 3.10+:** The agent script is written in Python.
*   **Ollama:** The Ollama service must be installed and running on your Windows 11 machine. You can download the installer from the [official Ollama website](https://ollama.com/).
*   **WSL (Windows Subsystem for Linux):** This project assumes you are running commands from a Linux-based terminal within WSL.

### Step-by-step setup

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/YOUR_GITHUB_USERNAME/YOUR_REPOSITORY_NAME.git
    cd YOUR_REPOSITORY_NAME
    ```
2.  **Create and activate a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```
    *Note: A `requirements.txt` file is not included in the provided prompt but is a standard best practice. See the "Dependencies" section below for details.*
4.  **Pull the Mixtral model using Ollama:**
    ```sh
    ollama pull mixtral
    ```
    This may take some time depending on your internet connection.

## 🛠️ Usage

After following the installation steps, ensure your virtual environment is active and the Ollama service is running.

To run the agent, execute the `agent.py` script from your terminal:
```sh
python agent.py
