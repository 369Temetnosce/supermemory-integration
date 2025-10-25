"""
Basic example of using the Supermemory client.
"""

from supermemory_client import SupermemoryClient


def main():
    # Initialize the client (reads API key from .env file)
    client = SupermemoryClient()
    
    print("=== Supermemory.ai Integration Example ===\n")
    
    # 1. Add a memory
    print("1. Adding a new memory...")
    memory = client.add_memory(
        content="Python is a high-level programming language known for its simplicity and readability.",
        metadata={
            "category": "programming",
            "language": "python",
            "topic": "Python Programming"
        }
    )
    print(f"✓ Memory added successfully!")
    print(f"   Response: {memory}\n")
    
    # 2. Search for memories
    print("2. Searching for 'programming language'...")
    response = client.search_memories(
        query="programming language",
        limit=5
    )
    
    # Access results from the response object
    if hasattr(response, 'results'):
        results = response.results
        print(f"✓ Found {len(results)} results")
        for idx, result in enumerate(results, 1):
            # Result objects have various attributes, convert to string for display
            result_str = str(result)
            print(f"   {idx}. {result_str[:100]}...")
    else:
        print(f"✓ Search response: {response}")
    print()
    
    # 3. Example of direct SDK usage
    print("3. Using the SDK directly...")
    raw_client = client.get_raw_client()
    direct_response = raw_client.search.execute(q="What do you know about me?")
    print(f"✓ Direct search results: {direct_response.results}")
    print()
    
    print("=== Example completed successfully! ===")


if __name__ == "__main__":
    main()
