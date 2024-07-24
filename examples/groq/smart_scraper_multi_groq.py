"""
Basic example of scraping pipeline using SmartScraper
"""

import os
import json

from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperMultiGraph

load_dotenv()

# ************************************************
# Define the configuration for the graph
# ************************************************

groq_key = os.getenv(
    key="GROQ_API_KEY")

graph_config = {
    "llm": {
        "model": "groq/gemma-7b-it",
        "api_key": groq_key,
        "temperature": 0
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "temperature": 0,
        # "base_url": "http://localhost:11434",  # set ollama URL arbitrarily
    },
    "verbose": True,
    "headless": False
}
# *******************************************************
# Create the SmartScraperMultiGraph instance and run it
# *******************************************************

multiple_search_graph = SmartScraperMultiGraph(
    prompt="Scrape the website for any data you can get in a .json format.",
    source=[
        # "https://perinim.github.io/",
        # "https://perinim.github.io/cv/",
        " https://disclosures-clerk.house.gov/foreign-reports/2024q1jan09.pdf",
    ],
    schema=None,
    config=graph_config
)

result = multiple_search_graph.run()
print(json.dumps(obj=result, indent=4))
