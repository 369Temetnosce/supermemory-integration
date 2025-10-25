"""
Advanced example demonstrating more features of the Supermemory client.
"""

from supermemory_client import SupermemoryClient
import json


def main():
    # Initialize the client
    client = SupermemoryClient()
    
    print("=== Advanced Supermemory.ai Examples ===\n")
    
    # Example 1: Add multiple memories with rich metadata
    print("1. Adding multiple memories with metadata...")
    
    memories_data = [
        {
            "content": "Machine learning is a subset of AI that enables systems to learn from data.",
            "metadata": {"category": "AI", "difficulty": "intermediate", "topic": "Machine Learning Basics"}
        },
        {
            "content": "Neural networks are computing systems inspired by biological neural networks.",
            "metadata": {"category": "AI", "difficulty": "advanced", "topic": "Neural Networks"}
        },
        {
            "content": "REST APIs use HTTP methods like GET, POST, PUT, and DELETE for CRUD operations.",
            "metadata": {"category": "web-development", "difficulty": "beginner", "topic": "REST API Fundamentals"}
        }
    ]
    
    added_memories = []
    for mem_data in memories_data:
        memory = client.add_memory(**mem_data)
        added_memories.append(memory)
        print(f"✓ Added: {mem_data['metadata']['topic']}")
    print()
    
    # Example 2: Advanced search with specific queries
    print("2. Searching with specific queries...")
    
    search_queries = [
        "artificial intelligence",
        "web development",
        "neural networks"
    ]
    
    for query in search_queries:
        response = client.search_memories(query=query, limit=3)
        print(f"\n   Query: '{query}'")
        
        # Handle response object
        if hasattr(response, 'results'):
            results = response.results
            print(f"   Results: {len(results)}")
            for result in results[:2]:
                result_str = str(result)
                print(f"   - {result_str[:80]}...")
        else:
            print(f"   Response: {response}")
    print()
    
    # Example 3: Using the raw SDK client for advanced features
    print("\n3. Using the raw SDK client for advanced operations...")
    raw_client = client.get_raw_client()
    
    # Direct search using the SDK
    direct_response = raw_client.search.execute(
        q="What technologies are mentioned?",
        limit=5
    )
    print(f"✓ Direct SDK search completed")
    print(f"   Results: {direct_response.results}")
    print()
    
    # Example 4: Batch operations
    print("4. Demonstrating batch memory additions...")
    batch_contents = [
        "Docker is a platform for developing, shipping, and running applications in containers.",
        "Kubernetes is an open-source container orchestration platform.",
        "GraphQL is a query language for APIs and a runtime for executing those queries."
    ]
    
    for content in batch_contents:
        client.add_memory(content=content)
        print(f"✓ Added: {content[:50]}...")
    print()
    
    print("=== Advanced examples completed! ===")


if __name__ == "__main__":
    main()
