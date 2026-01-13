# app.py

from agent_logic import run_agent

print("ServiceHive AI Agent - Chat Mode\n")

state = {
    "expecting_name": False,
    "expecting_email": False,
    "name": "",
    "email": ""
}

while True:
    user_input = input("User: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    response = run_agent(user_input, state)
    print("Agent:", response)
