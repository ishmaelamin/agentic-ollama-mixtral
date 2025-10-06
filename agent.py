import os
import sys
import logging
from dotenv import load_dotenv

# Load .env if present
load_dotenv()

try:
    from langchain_ollama import OllamaLLM
except Exception:
    raise RuntimeError(
        "Unable to import OllamaLLM from langchain_ollama. Make sure 'langchain-ollama' is installed."
    )

try:
    from langchain_community.agent_toolkits.load_tools import load_tools
except Exception:
    raise RuntimeError(
        "Unable to import load_tools from langchain_community. Install 'langchain-community' to get community tools."
    )

from langchain.agents import AgentType, initialize_agent


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def create_agent(model_name: str = None):
    """Create and return an initialized LangChain agent using Ollama.

    Inputs:
      - model_name: optional model to use (defaults to env OLLAMA_MODEL or 'mixtral')

    Outputs:
      - initialized agent ready to run queries

    Error modes:
      - Raises RuntimeError with instructions when imports or tools are missing.
    """

    model = model_name or os.getenv("OLLAMA_MODEL", "mixtral")

    logging.info(f"Initializing OllamaLLM(model={model})")
    llm = OllamaLLM(model=model)

    logging.info("Loading tools: ddg-search")
    tools = load_tools(["ddg-search"])

    logging.info("Initializing agent")
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )

    return agent


def main():
    # Accept a query from the command line, or use a helpful default
    if len(sys.argv) > 1:
        query = " ".join(sys.argv[1:])
    else:
        query = (
            "What is the current population of Japan? "
            "What is the current USD to JPY exchange rate? "
            "How is this different from last year?"
        )

    try:
        agent = create_agent()
    except Exception as e:
        logging.exception("Failed to create agent")
        print("See README.md for setup steps and required packages.")
        raise

    try:
        logging.info("Running agent query...")
        result = agent.run(query)
        print("\n=== Agent result ===")
        print(result)
    except Exception:
        logging.exception("Agent run failed. Ensure your Ollama service is running and accessible.")


if __name__ == "__main__":
    main()
