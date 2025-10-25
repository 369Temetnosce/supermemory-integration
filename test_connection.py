"""
Quick test to verify your Supermemory connection is working.
"""

from supermemory import Supermemory
import os
from dotenv import load_dotenv

def test_connection():
    """Test the Supermemory API connection"""
    
    print("=" * 60)
    print("Testing Supermemory.ai Connection")
    print("=" * 60)
    
    # Load environment variables
    load_dotenv()
    
    api_key = os.getenv("SUPERMEMORY_API_KEY")
    base_url = os.getenv("SUPERMEMORY_BASE_URL", "https://api.supermemory.ai/")
    
    if not api_key:
        print("❌ ERROR: SUPERMEMORY_API_KEY not found in .env file")
        return False
    
    print(f"\n✓ API Key found: {api_key[:20]}...")
    print(f"✓ Base URL: {base_url}")
    
    try:
        # Initialize client
        client = Supermemory(
            api_key=api_key,
            base_url=base_url
        )
        print("\n✓ Client initialized successfully")
        
        # Test 1: Add a test memory
        print("\n[Test 1] Adding a test memory...")
        response = client.memories.add(
            content="This is a test memory created to verify the Supermemory API connection.",
            metadata={"type": "connection_test"}
        )
        print(f"✓ Memory added successfully!")
        print(f"  - ID: {response.id}")
        print(f"  - Status: {response.status}")
        
        # Test 2: Search
        print("\n[Test 2] Searching memories...")
        search_response = client.search.execute(
            q="test",
            limit=5
        )
        print(f"✓ Search completed successfully!")
        print(f"  - Results found: {len(search_response.results)}")
        
        if search_response.results:
            print("\n  First few results:")
            for idx, result in enumerate(search_response.results[:3], 1):
                content = str(result)[:100]
                print(f"    {idx}. {content}...")
        
        print("\n" + "=" * 60)
        print("✅ All tests passed! Your connection is working perfectly.")
        print("=" * 60)
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: {type(e).__name__}: {e}")
        print("\nPlease check:")
        print("  1. Your API key is correct")
        print("  2. You have internet connection")
        print("  3. The Supermemory API is accessible")
        return False

if __name__ == "__main__":
    test_connection()
