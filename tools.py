from crewai_tools import YoutubeChannelSearchTool
from dotenv import load_dotenv
import os 
load_dotenv()
os.environ['OPENAI_API_KEY']=os.getenv('OPENAI_API_KEY')
tool = YoutubeChannelSearchTool(youtube_channel_handle='@EverythingMoney')