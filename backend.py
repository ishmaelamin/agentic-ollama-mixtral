# backend.py

from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.llms import Ollama
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate
from langchain import hub
from langchain.tools import tool

# Define a placeholder tool (or your real tool)
@tool
def search(query: str) -> str:
    """Performs a web search for the given query."""
    # For a real app, this would perform a real search
    return f"Search result for '{query}': Example information."

# Initialize the Ollama model
llm = Ollama(model="mixtral")

# Get the prompt from the LangChain Hub
prompt = hub.pull("hwchase17/react")

# Create the agent
tools = [search]
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# FastAPI setup
app = FastAPI(title="Mixtral Agent API")

# Pydantic model for request validation
class PromptRequest(BaseModel):
    prompt: str

@app.post("/ask/")
async def run_agent(request: PromptRequest):
    response = agent_executor.invoke({"input": request.prompt})
    return {"response": response["output"]}
