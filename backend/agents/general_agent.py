from gemini_client import client


def general_agent(message, history):

    conversation = ""

    for item in history:

        if item.role == "user":
            conversation += f"User: {item.content}\n"

        elif item.role == "ai":
            conversation += f"Assistant: {item.content}\n"


    prompt = f"""
You are a General AI Assistant.

Answer general questions clearly and helpfully.

Previous conversation:
{conversation}

Current user message:
{message}

Important:
- Use previous conversation to understand follow-up questions.
- If the user says "it", "this", "that", "give me an example",
  "explain more", etc., use the previous conversation for context.
- Do not unnecessarily repeat previous answers.
"""


    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )


    return response.text