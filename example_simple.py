"""
Simple example using the Supermemory SDK directly (as shown in your account).
"""

from supermemory import Supermemory
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize client with your credentials
client = Supermemory(
    api_key=os.getenv("SUPERMEMORY_API_KEY"),
    base_url=os.getenv("SUPERMEMORY_BASE_URL", "https://api.supermemory.ai/")
)

# Search example
response = client.search.execute(
    q="What do you know about me?",
)
print("Search Results:")
print(response.results)

# Add a memory example
print("\nAdding a new memory...")
add_response = client.memories.add(
    content="I love building AI applications with Python and exploring new technologies."
)
print(f"Memory added: {add_response}")

# Search again
print("\nSearching for 'AI applications'...")
search_response = client.search.execute(
    q="AI applications",
    limit=5
)
print(f"Found {len(search_response.results)} results:")
for idx, result in enumerate(search_response.results, 1):
    print(f"{idx}. {result}")
