Instructions to Restart Mixtral Agent Chat
Follow these steps to restart your Ollama, FastAPI, and Streamlit applications within your Windows Subsystem for Linux (WSL) environment.
Step 1: Open WSL Terminals
After restarting your machine, open two separate WSL terminals by searching for "Ubuntu" (or your Linux distribution) in the Windows Start Menu.
Step 2: Start the Ollama Server
The Ollama service must be active before your agent can use the Mixtral model.
In Terminal 1, check the status of the Ollama service.
sh
systemctl status ollama
Use code with caution.

If the service is not running (indicated as inactive or dead), start it with administrator privileges.
sh
sudo systemctl start ollama
Use code with caution.

Leave this terminal open to keep the server running.
Step 3: Run the FastAPI Backend
This process will run your agent logic and listen for requests from the Streamlit UI.
In Terminal 1, in a separate session or tab, navigate to your project directory.
sh
cd /mnt/c/Users/ishma/Projects/mixtral-agent/
Use code with caution.

Activate your virtual environment.
sh
source venv/bin/activate
Use code with caution.

Start the FastAPI server.
sh
uvicorn backend:app --reload
Use code with caution.

Leave this terminal window open.
Step 4: Run the Streamlit Frontend
This process will launch your web-based chat interface.
In Terminal 2, navigate to your project directory.
sh
cd /mnt/c/Users/ishma/Projects/mixtral-agent/
Use code with caution.

Activate your virtual environment.
sh
source venv/bin/activate
Use code with caution.

Start the Streamlit application. A browser tab will automatically open with your user interface.
sh
python -m streamlit run frontend.py
Use code with caution.

Troubleshooting
Address already in use error: If you see Address already in use when starting FastAPI, it means a previous process on port 8000 is still active. Kill it with these commands and try again.
sh
sudo lsof -i :8000
sudo kill -9 <PID> # Replace <PID> with the process ID
Use code with caution.

Module not found error: If you get an error like No module named streamlit, double-check that your virtual environment is active by running source venv/bin/activate. You should see (venv) at the start of your terminal prompt.