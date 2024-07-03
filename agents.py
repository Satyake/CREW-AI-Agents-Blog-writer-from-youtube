from crewai import Agent
from tools import tool
from dotenv import load_dotenv
import os 

load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')
os.environ['OPENAI_MODEL_NAME']="gpt-4-0125-preview"
#print(os.getenv('OPENAI_API_KEY'))


blog_research_agent=Agent(
    role="Blog Researcher from youtube videos",
    goal="Get the relevant video transcription for the {topic}",
    verbose=True,
    memory=True,
    backstory=(
        'Expert in understanding videos related to stocks'
    ),
    tools=[tool],
    allow_delegation=True
)



blog_writer_agent=Agent(
    role="Blog writer",
    goal="Narrate compelliong stories about the {topic}",
    verbose=True,
    memory=True,
    backstory=(
        'Simplifying complex content'
    ),
    tools=[tool],
    allow_delegation=False
)
