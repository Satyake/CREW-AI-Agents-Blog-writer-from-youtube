#from crew import Task 
from tools import tool
from agents import blog_research_agent, blog_writer_agent

research=Task(
    description=(
        "Identify the video {topic}"
        "Get detailed information about the video from the channel video"

    ),
    expected_output=" A comprehensive 3 paragraph long report based on the {topic}",
    tolls=[tool],
    agent=blog_research_agent

)

write=Task(
    description=(
        "Get the information from the youtube channel about the {topic}"

    ),
    expected_output=" Summarize the info on the{topic} and create the content",
    tolls=[tool],
    async_execution=False,
    output_file='new-blog-post.md',
    agent=blog_writer_agent

)