from phi.agent import Agent
from phi.model.ollama import Ollama
from phi.tools.duckduckgo import DuckDuckGo
from phi.storage.agent.sqlite import SqlAgentStorage
import time

agent = Agent(
    name="Web Agent",
    model=Ollama(id='llama3.2'),
    tools=[DuckDuckGo()],
    instructions=[''],
    show_tool_calls=True,
    markdown=True,
    storage=SqlAgentStorage(table_name="agent_sessions", db_file="tmp/agent_storage.db"), # permanent memory
    add_chat_history_to_messages=True,
    num_history_responses=3
)

while True:
    prompt = input('enter your prompt: ')

    try:
        time.sleep(1)
        agent.print_response(prompt, stream=True)
    except Exception as e:
        print(e)