from phi.agent import Agent, RunResponse
from phi.model.huggingface import HuggingFaceChat
import time

agent = Agent(
    model=HuggingFaceChat(
        id="meta-llama/Meta-Llama-3-8B-Instruct",
        max_tokens=4096,
    ),
    markdown=True
)

while True:
    prompt = input('enter your prompt: ')

    try:
        time.sleep(1)
        agent.print_response(prompt, stream=True)
    except Exception as e:
        print(e)