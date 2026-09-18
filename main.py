from langchain.messages import HumanMessage, AIMessage
from agent.agent import run
import os

# clear the terminal screen
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


user_request_count = 0

if __name__ == "__main__":
    while True:
        user_input = input("\nYou: ")

        if user_input == "q":
            print("Byeeeee")
            quit()

        user_request_count += 1

        if user_request_count == 1:
            clear_terminal()

        response = run(user_input)