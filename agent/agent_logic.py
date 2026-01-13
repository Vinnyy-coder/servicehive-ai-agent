# agent_logic.py

from intent import detect_intent
from tools.lead_capture import save_lead


def run_agent(user_message, state):

    if state["expecting_name"]:
        state["name"] = user_message
        state["expecting_name"] = False
        state["expecting_email"] = True
        return "Thanks! Please share your email."

    if state["expecting_email"]:
        state["email"] = user_message
        save_lead(state["name"], state["email"])
        state["expecting_email"] = False
        return "✅ Your details are saved. Our team will contact you."

    intent = detect_intent(user_message)

    if intent == "sales_intent":
        state["expecting_name"] = True
        return "Sure! May I know your name?"

    return "ServiceHive AI CRM helps sales teams convert visitors into leads."
