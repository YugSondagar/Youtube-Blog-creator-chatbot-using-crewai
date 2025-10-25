from crewai_tools import YoutubeChannelSearchTool
from langchain_community.embeddings import HuggingFaceEmbeddings
import os

embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

import os
from dotenv import load_dotenv
load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

yt_tool = YoutubeChannelSearchTool(youtube_channel_handle="https://www.youtube.com/user/krishnaik06",
embedding_function=embeddings
)