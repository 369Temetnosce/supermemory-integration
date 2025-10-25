"""Save session summary to actual Supermemory.ai"""
from supermemory import Supermemory
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

client = Supermemory(
    api_key=os.getenv('SUPERMEMORY_API_KEY'),
    base_url=os.getenv('SUPERMEMORY_BASE_URL')
)

# Session summary
session_summary = """
supermemory-integration - Session End: Successfully created complete Supermemory.ai integration project with official Python SDK. 

Implemented:
- Wrapper client (supermemory_client.py)
- 3 working examples (simple, basic, advanced)
- Connection test
- Full documentation (README, QUICKSTART, PROJECT_SUMMARY)

API key configured and tested successfully. All examples running correctly.

GitHub CLI installed and authenticated as 369Temetnosce.
Repository created and pushed to GitHub: https://github.com/369Temetnosce/supermemory-integration
Git commit: 5e74744

Next: User can clone from any computer and start building AI applications with persistent memory.
Status: Production ready and live on GitHub.
Last worked: 2025-10-25 5:30 PM EDT
"""

# Save to Supermemory.ai
print("Saving session summary to Supermemory.ai...")
response = client.memories.add(
    content=session_summary,
    metadata={
        "project": "supermemory-integration",
        "type": "session_end",
        "github_url": "https://github.com/369Temetnosce/supermemory-integration",
        "commit": "5e74744",
        "date": "2025-10-25",
        "status": "complete"
    }
)

print(f"✅ Session summary saved to Supermemory.ai!")
print(f"   Memory ID: {response.id}")
print(f"   Status: {response.status}")
