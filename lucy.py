from agno.agent import Agent
from agno.team import Team
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Import the existing agents
from dp import deadpool_agent
from ca import captain_america_agent

# Create Lucy as the orchestrator in coordinate mode
lucy = Team(
    name="Lucy",
    mode="coordinate",
    model=OpenAIChat(id="gpt-4o-mini"),
    members=[deadpool_agent, captain_america_agent],
    description="A team that combines factual accuracy with polite language",
    instructions=[
        "You are Lucy, an orchestrator that combines the strengths of two agents: Deadpool and Captain America.",
        "Deadpool is excellent at finding accurate information but uses crude language.",
        "Captain America is polite and inspirational but may hallucinate facts.",
        "Your job is to coordinate between these two agents to produce perfect responses.",
        "First, ask Deadpool to research the query and provide factual information.",
        "Then, ask Captain America to rewrite Deadpool's response in a polite, inspirational tone while preserving all factual information.",
        "Finally, review both responses, ensure all facts from Deadpool are preserved in Captain America's polite version.",
        "If Captain America has introduced any hallucinations or removed important facts, correct these issues in your final response.",
        "Your final response should be factually accurate like Deadpool's but polite and well-structured like Captain America's."
    ],
    add_datetime_to_instructions=True,
    enable_agentic_context=True,  # Allow the agent to maintain a shared context
    share_member_interactions=True,  # Share all member responses with subsequent member requests
    show_members_responses=True,
    markdown=True,
)


lucy.print_response("Give me details about Thoughtworks company and their CEO")