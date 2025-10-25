"""Test if memories were saved to Supermemory"""
from supermemory import Supermemory
import os
from dotenv import load_dotenv

load_dotenv()

client = Supermemory(
    api_key=os.getenv('SUPERMEMORY_API_KEY'),
    base_url=os.getenv('SUPERMEMORY_BASE_URL')
)

# Search for session end memories
print("Searching for 'supermemory-integration session end'...")
response = client.search.execute(q='supermemory-integration session end', limit=5)

print(f"\nResults found: {len(response.results)}\n")

if response.results:
    for i, result in enumerate(response.results, 1):
        print(f"{i}. Document ID: {result.document_id}")
        print(f"   Created: {result.created_at}")
        if result.chunks:
            print(f"   Content: {result.chunks[0].content[:200]}...")
        print()
else:
    print("No results found. The memory may not have been saved to Supermemory.ai")
    print("\nNote: Cascade's create_memory saves to Windsurf's local memory system,")
    print("NOT to your Supermemory.ai account. These are separate systems.")
