from gemini_client import client


def coding_agent(message, history):

    conversation = ""

    for item in history:
        role = item.role
        content = item.content

        if role == "user":
            conversation += f"User: {content}\n"

        elif role == "ai":
            conversation += f"Assistant: {content}\n"


    prompt = f"""
You are a Coding Agent.

You help users with:
- Programming
- Data Structures and Algorithms
- Java
- Python
- JavaScript
- Debugging
- Technical concepts
- Coding interview preparation

Below is the previous conversation between the user and the assistant.

Previous Conversation:
{conversation}

Now answer the user's latest message:

User: {message}

Important:
- Use the previous conversation to understand references like
  "it", "this", "that", "give me an example", etc.
- Maintain continuity with the previous discussion.
- Do not unnecessarily repeat previous explanations.
- Give beginner-friendly and technically correct answers.
- If code is required, provide correct code.
"""


    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )


    return response.text