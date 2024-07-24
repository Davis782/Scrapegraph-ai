from scrapegraphai.graphs import SmartScraperGraph
from scrapegraphai.utils import prettify_exec_info

# Define the configuration for the graph
graph_config = {
    "llm": {
        "model": "ollama/llava-llama3",
        "temperature": 0,
        "format": "json",
        "base_url": "http://localhost:11434",
    },
    "embeddings": {
        "model": "ollama/nomic-embed-text",
        "temperature": 0,
        "base_url": "http://localhost:11434",
    },
    "verbose": True,
    "headless": False
}

# Create the SmartScraperGraph instance and run it
smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the titles",
    source="https://www.shopify.com/blog/best-ecommerce-books",
    # source="https://sport.sky.it/nba?gr=www",
    config=graph_config
)

try:
    result = smart_scraper_graph.run()
    if result is None:
        print("No result was returned from the run.")
    else:
        print(result)
except Exception as e:
    print(f"An error occurred while running the SmartScraperGraph: {e}")

# Get graph execution info
try:
    graph_exec_info = smart_scraper_graph.get_execution_info()
    if 'error' in graph_exec_info:
        print(
            f"An error occurred during execution: {graph_exec_info['error']}")
    else:
        print(prettify_exec_info(complete_result=graph_exec_info))
except Exception as e:
    print(f"An error occurred while getting the execution info: {e}")
