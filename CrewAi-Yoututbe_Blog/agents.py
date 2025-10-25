from crewai import Agent
from tools import yt_tool
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

llm = ChatGroq(model="llama-3.1-8b-instant")


##Create a senior blog content

blog_researcher = Agent(
    role="Blog Researcher from Youtube Videos",
    goal = "get the relevant video content for the topic {topic} from Yotube Channel",
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos i AI,Data Science,ML and GenAI and Providing Suggestion"
    ),
    tools=[yt_tool],
    llm=llm,
    allow_delegation=True #means whatever work this agent do will be transfer to someone else
)

##Create a senior Blog writer agent with YT Tool

blog_writer = Agent(
    role="Blog Writer",
    goal="Narrate compelling tech stories about the video {topic} from Youtube Channel",
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and eduacte, bringing new"
        "discoveries to light in an accessible manner"
    ),
    tools=[],
    allow_delegation=False
)