# agent/intent.py

def detect_intent(user_message: str) -> str:
    """
    Detects the intent of the user message.

    Returns:
        'sales_intent' -> if user shows buying interest
        'product_query' -> normal product-related question
    """

    sales_keywords = [
        "price",
        "pricing",
        "demo",
        "buy",
        "contact",
        "trial",
        "subscription"
    ]

    message = user_message.lower()

    for keyword in sales_keywords:
        if keyword in message:
            return "sales_intent"

    return "product_query"
