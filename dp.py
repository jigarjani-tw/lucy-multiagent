from agno.agent import Agent
from agno.models.groq import Groq
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

deadpool_agent = Agent(
    name="DeadpoolAgent",
    role="The Merc with a Mouth",
    # model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions="You are the most sarcastic, fourth-wall-breaking AI in the multiverse."+
    "Web searches are your playground, and no topic is safe from your brutal, hilarious honesty."+
    "You are rude to users like Deadpool and always like to insult them in funny ways."+
    "Every sentence must be sarcastic either on the subject or the user. No straight answer.",
    tools=[DuckDuckGoTools()],
    markdown=True,
)

deadpool_agent.print_response("Give me details about Thoughtworks company and their CEO")