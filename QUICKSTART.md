# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
cd C:\Users\User\CascadeProjects\supermemory-integration
pip install -r requirements.txt
```

### Step 2: Test Your Connection
Your API key is already configured in the `.env` file. Run the test:
```bash
python test_connection.py
```

You should see:
```
✅ All tests passed! Your connection is working perfectly.
```

### Step 3: Try the Examples

**Simple Direct SDK Usage:**
```bash
python example_simple.py
```

**Using the Wrapper:**
```bash
python example_basic.py
```

**Advanced Features:**
```bash
python example_advanced.py
```

## 📝 Basic Usage

### Add a Memory
```python
from supermemory import Supermemory
import os
from dotenv import load_dotenv

load_dotenv()

client = Supermemory(
    api_key=os.getenv("SUPERMEMORY_API_KEY"),
    base_url=os.getenv("SUPERMEMORY_BASE_URL")
)

# Add text content
response = client.memories.add(
    content="Your memory content here",
    metadata={"category": "notes", "topic": "Important Info"}
)
print(f"Added memory: {response.id}")

# Add a URL (Supermemory will extract the content)
response = client.memories.add(
    content="https://example.com/article",
    metadata={"source": "web"}
)
```

### Search Memories
```python
# Simple search
results = client.search.execute(q="What do you know about me?")
print(results.results)

# Search with limit
results = client.search.execute(q="programming", limit=10)
for result in results.results:
    print(result)
```

### Using the Wrapper
```python
from supermemory_client import SupermemoryClient

client = SupermemoryClient()

# Add memory
memory = client.add_memory(
    content="Python is great for AI development",
    metadata={"language": "python", "topic": "AI"}
)

# Search
results = client.search_memories(query="AI development", limit=5)
```

## 🔑 Key Features

- **Automatic Content Processing**: Text is chunked, embedded, and indexed automatically
- **URL Support**: Pass a URL as content and Supermemory extracts the text
- **Metadata**: Add custom metadata for better organization
- **Semantic Search**: AI-powered search finds relevant content
- **Fast**: Sub-300ms recall times

## 📚 Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Check out [Supermemory Documentation](https://supermemory.ai/docs)
- Explore the [API Reference](https://supermemory.ai/docs/api-reference)

## 💡 Tips

1. **Metadata is flexible**: Add any key-value pairs you need
2. **URLs work**: Just pass a URL as content to extract and store web pages
3. **Memories are queued**: Status will be "queued" → "processing" → "done"
4. **Search is semantic**: You don't need exact matches, AI finds related content

## ❓ Troubleshooting

**Connection issues?**
- Verify your API key in `.env`
- Check internet connection
- Run `python test_connection.py`

**Import errors?**
- Make sure dependencies are installed: `pip install -r requirements.txt`

**No search results?**
- Memories need time to process (usually a few seconds)
- Try broader search terms
- Check if memories were added successfully
