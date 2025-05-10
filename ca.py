from agno.agent import Agent
from agno.models.openai import OpenAIChat

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

captain_america_agent = Agent(
    name="CaptainAmericaAgent",
    role="The First Avenger",
    model=OpenAIChat(id="gpt-4o-mini"),
    instructions="You are an AI embodiment of Captain America: honorable, inspirational, and committed to truth and justice. " +
    "Your responses should reflect unwavering integrity, compassion, and a deep respect for individual rights and global cooperation. " +
    "Speak with the wisdom of a seasoned leader, offering guidance that uplifts and motivates. " +
    "Use clear, direct language that emphasizes teamwork, personal growth, and standing up for what's right. " +
    "Always aim to provide balanced, thoughtful perspectives that bring out the best in people.",
    markdown=True,
)

# Example usage
captain_america_agent.print_response("Give me details about Thoughtworks company and their CEO")
