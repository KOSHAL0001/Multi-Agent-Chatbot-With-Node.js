from gemini_client import client


def route_message(message, history):

    conversation = ""

    for item in history:

        if item.role == "user":
            conversation += f"User: {item.content}\n"

        elif item.role == "ai":
            conversation += f"Assistant: {item.content}\n"


    prompt = f"""
You are an AI router for a multi-agent chatbot.

Available agents:

1. coding
   - Programming
   - Java
   - Python
   - DSA
   - Debugging
   - Technical concepts

2. career
   - Jobs
   - Internships
   - Career guidance
   - Interview preparation

3. resume
   - Resume
   - CV
   - ATS
   - Resume improvement

4. general
   - General knowledge
   - Casual questions
   - Topics that do not belong to the other agents


Previous conversation:
{conversation}


Current user message:
{message}


Important:
- Understand the user's intent using both the current message and previous conversation.
- If the current message is a follow-up such as:
  "give me an example"
  "explain it more"
  "what about this?"
  "why?"
  "show me code"
  then use the previous conversation to determine the correct agent.
- Return ONLY one word:
  coding
  career
  resume
  general
"""


    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )


    agent = response.text.strip().lower()


    if agent not in ["coding", "career", "resume", "general"]:
        return "general"


    return agent