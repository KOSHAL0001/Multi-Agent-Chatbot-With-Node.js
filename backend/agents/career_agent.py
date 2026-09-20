from gemini_client import client


def career_agent(message, history):

    conversation = ""

    for item in history:

        if item.role == "user":
            conversation += f"User: {item.content}\n"

        elif item.role == "ai":
            conversation += f"Assistant: {item.content}\n"


    prompt = f"""
You are a Career Agent.

You help users with:

- Jobs
- Internships
- Career guidance
- Interview preparation
- Technical interview preparation
- HR interview preparation
- Career planning
- Skills required for different roles
- Professional growth
- Job search strategies


Previous conversation:
{conversation}


Current user message:
{message}


Important instructions:

- Use the previous conversation to understand the user's context.
- Maintain continuity with the conversation.
- If the user asks follow-up questions like:
  "give me an example"
  "what should I do?"
  "explain more"
  "what about this?"
  "why?"
  "tell me more"
  understand what they are referring to from the previous conversation.
- Do not unnecessarily repeat previous answers.
- Give practical and clear career guidance.
- Keep the answer beginner-friendly when appropriate.
"""


    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )


    return response.text