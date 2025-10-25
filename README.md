# Supermemory.ai Integration

A Python integration for [Supermemory.ai](https://supermemory.ai) - the Memory API for the AI era. This project uses the official Supermemory SDK to store, search, and manage memories with a simple and intuitive interface.

## Features

- **Official SDK**: Uses the official `supermemory` Python package
- **Add Memories**: Store content with optional metadata, titles, and URLs
- **Semantic Search**: Search across all your stored memories using AI-powered search
- **Easy Integration**: Simple wrapper and direct SDK usage examples
- **Environment Configuration**: Secure API key management with `.env` files

## Prerequisites

- Python 3.7 or higher
- A Supermemory.ai API key (get one at [console.supermemory.ai](https://console.supermemory.ai))

## Installation

1. **Navigate to this project directory**:
   ```bash
   cd C:\Users\User\CascadeProjects\supermemory-integration
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your API key**:
   
   Your `.env` file has already been created with your API key. If you need to update it, edit the `.env` file:
   ```
   SUPERMEMORY_API_KEY=sm_xSFdGPgbmLxGJotb1dzBfK_UAGWKBLSPBrvBgfPwrVqbxsJzOmRduIPGefmYJnoYduPmVAwOPJCYvbThZFosnws
   SUPERMEMORY_BASE_URL=https://api.supermemory.ai/
   ```

## Quick Start

### Basic Usage

```python
from supermemory_client import SupermemoryClient

# Initialize the client
client = SupermemoryClient()

# Add a memory
memory = client.add_memory(
    content="Python is a versatile programming language.",
    metadata={"category": "programming", "topic": "Python Info"}
)

# Search memories
results = client.search_memories(query="programming language", limit=5)
```

### Direct SDK Usage

```python
from supermemory import Supermemory
import os
from dotenv import load_dotenv

load_dotenv()

client = Supermemory(
    api_key=os.getenv("SUPERMEMORY_API_KEY"),
    base_url=os.getenv("SUPERMEMORY_BASE_URL")
)

# Search memories
response = client.search.execute(q="What do you know about me?")
print(response.results)

# Add a memory
client.memories.add(content="Your memory content here")
```

### Running Examples

**Test Connection** (Verify your setup):
```bash
python test_connection.py
```

**Simple Example** (Direct SDK usage):
```bash
python example_simple.py
```

**Basic Example** (Using the wrapper):
```bash
python example_basic.py
```

**Advanced Example** (Batch operations and metadata):
```bash
python example_advanced.py
```

## API Client Reference

### `SupermemoryClient`

#### `__init__(api_key: Optional[str] = None)`
Initialize the client with your API key. If not provided, reads from `SUPERMEMORY_API_KEY` environment variable.

#### `add_memory(content: str, metadata: Optional[Dict] = None, user_id: Optional[str] = None, container_tags: Optional[List[str]] = None, custom_id: Optional[str] = None)`
Add a new memory to Supermemory.

**Parameters**:
- `content` (str): The content to store (text or URL)
- `metadata` (dict, optional): Additional metadata as key-value pairs
- `user_id` (str, optional): User ID for partitioning memories
- `container_tags` (list, optional): Tags for grouping memories
- `custom_id` (str, optional): Custom ID for the memory

**Returns**: Response object with `id` and `status` fields

#### `search_memories(query: str, limit: int = 10, filters: Optional[Dict] = None)`
Search through your memories using semantic search.

**Parameters**:
- `query` (str): Search query
- `limit` (int): Maximum results to return
- `filters` (dict, optional): Search filters

**Returns**: Dictionary with search results

#### `get_raw_client()`
Get the underlying Supermemory SDK client for direct access to all SDK features.

**Returns**: `Supermemory` client instance

**Example**:
```python
raw_client = client.get_raw_client()
response = raw_client.search.execute(q="your query")
```

## Project Structure

```
supermemory-integration/
├── supermemory_client.py   # Wrapper around official SDK
├── test_connection.py       # Quick connection test
├── example_simple.py        # Direct SDK usage example
├── example_basic.py         # Basic wrapper usage
├── example_advanced.py      # Advanced features demo
├── requirements.txt         # Python dependencies (supermemory SDK)
├── .env.example            # Environment variable template
├── .env                    # Your actual API key (gitignored)
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## How It Works

Supermemory.ai provides a powerful memory API that:

1. **Processes Content**: Automatically extracts, chunks, and embeds your content
2. **Semantic Search**: Uses vector embeddings for intelligent search
3. **Scalable Storage**: Handles large amounts of data efficiently
4. **Fast Retrieval**: Sub-300ms recall times

### Content Processing Pipeline

When you add a memory, it goes through these stages:
1. **Queued**: Initial submission
2. **Extracting**: Content extraction
3. **Chunking**: Semantic chunking with context preservation
4. **Embedding**: Vector embedding generation
5. **Indexing**: Adding to search index
6. **Done**: Ready for search

## Use Cases

- **Personal Knowledge Base**: Store and retrieve notes, articles, and learnings
- **AI Assistant Memory**: Give your AI applications long-term memory
- **Document Search**: Build semantic search over your documents
- **Research Organization**: Organize and search research materials
- **Customer Support**: Store and retrieve support documentation

## Resources

- [Supermemory Documentation](https://supermemory.ai/docs)
- [API Reference](https://supermemory.ai/docs/api-reference)
- [Developer Console](https://console.supermemory.ai)
- [GitHub](https://github.com/supermemoryai)

## Error Handling

Always wrap API calls in try-except blocks to handle potential errors:

```python
try:
    memory = client.add_memory(content="Test content")
    print(f"Memory added: {memory}")
except Exception as e:
    print(f"Error: {e}")
```

## License

This project is open source and available for use and modification.

## Support

For issues with this integration, please check the code or create an issue.
For Supermemory.ai API questions, visit their [documentation](https://supermemory.ai/docs) or contact their support.
