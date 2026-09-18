import os

from langchain_openai import ChatOpenAI
from langchain.messages import AIMessage, HumanMessage
from langchain.agents import create_agent
from tools.tools import internet_serach, save_research_result, list_of_saved_research_results
from agent.prompts import SYSTEM_PROMPT
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
   

llm = ChatOpenAI(
    model="deepseek/deepseek-r1",
    temperature=0,
    max_tokens=2048,
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

tools = [internet_serach, save_research_result, list_of_saved_research_results]

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=SYSTEM_PROMPT,
    checkpointer=InMemorySaver()
)

config = {"configurable": {"thread_id": "InRA-140505"}}

def run(user_input: str) -> str:
    response = agent.stream(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        },
        config=config,
        stream_mode="values"
        )

    print("\nInRA: ", response, "\n")

    for res in response:
        latest_message = res["messages"][-1]
        
        if latest_message.content:
            if isinstance(latest_message, HumanMessage):
                print(f"You: {latest_message.content}\n")
                print("="*50)

            elif isinstance(latest_message, AIMessage):
                print(f"InRA: {latest_message.content}\n")

        elif latest_message.tool_calls:
            print(
                f"Calling tools: "
                f"{[tc['name'] for tc in latest_message.tool_calls]}\n"
            )
