# Tools for the Agent to use
from langchain.tools import tool
from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file


@tool("internet_search", description="Use this tool to search the internet for publicly available information about a given name or entity.")
def internet_serach(query:str) -> str:
  client = TavilyClient(os.getenv("TAVILY_API_KEY"))
  tavily_response = client.search(
      query=query,
      search_depth="advanced"
  )
  return tavily_response


@tool("save_research_result", description="Use this tool to save the research result and give the file a name")
def save_research_result(filename:str, research_result:str) -> str:
    with open(f"{filename}", 'w', encoding="utf-8") as file:
      os.chmod(f"{filename}", 0o777)  # Set file permissions to be readable and writable by everyone

      # save in the research_results folder
      research_results_folder = "research_results"
      if not os.path.exists(research_results_folder):
          os.makedirs(research_results_folder)
      with open(os.path.join(research_results_folder, f"{filename}"), 'w', encoding="utf-8") as file:
          file.write(research_result)

@tool("list_of_saved_research_results", description="Use this tool to list all the research results that have been saved in the research_results folder")
def list_of_saved_research_results() -> list:
    research_results_folder = "research_results"
    if not os.path.exists(research_results_folder):
        return []
    return os.listdir(research_results_folder)