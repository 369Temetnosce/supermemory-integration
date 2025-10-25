"""
Dual-Memory Helper for Session Management
Saves session summaries to BOTH Windsurf Memory and Supermemory.ai
"""

from supermemory import Supermemory
import os
from dotenv import load_dotenv
from datetime import datetime

class DualMemoryHelper:
    """Helper class to save memories to both Windsurf and Supermemory.ai"""
    
    def __init__(self, project_name, supermemory_api_key=None, supermemory_base_url=None):
        """
        Initialize the dual-memory helper.
        
        Args:
            project_name: Name of the project
            supermemory_api_key: Supermemory.ai API key (or from env)
            supermemory_base_url: Supermemory.ai base URL (or from env)
        """
        load_dotenv()
        self.project_name = project_name
        
        # Initialize Supermemory.ai client
        api_key = supermemory_api_key or os.getenv('SUPERMEMORY_API_KEY')
        base_url = supermemory_base_url or os.getenv('SUPERMEMORY_BASE_URL', 'https://api.supermemory.ai/')
        
        if api_key:
            self.supermemory_client = Supermemory(
                api_key=api_key,
                base_url=base_url
            )
            self.has_supermemory = True
        else:
            self.supermemory_client = None
            self.has_supermemory = False
            print("⚠️  Supermemory.ai API key not found. Only Windsurf Memory will be used.")
    
    def save_session_end(self, summary, next_steps, status, github_url=None, commit_hash=None):
        """
        Save session end summary to BOTH memory systems.
        
        Args:
            summary: What was accomplished
            next_steps: What to do next
            status: Current project status
            github_url: Optional GitHub repository URL
            commit_hash: Optional Git commit hash
            
        Returns:
            dict with results from both systems
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %I:%M %p %Z")
        
        # Format the memory content
        memory_content = f"{self.project_name} - Session End: {summary}. Next: {next_steps}. Status: {status}. Last worked: {timestamp}."
        
        results = {
            'windsurf': None,
            'supermemory': None
        }
        
        # 1. Save to Windsurf Memory (via Cascade create_memory tool)
        print("\n📝 Windsurf Memory:")
        print(f"   Content: {memory_content}")
        print("   ℹ️  Use Cascade's create_memory tool to save this to Windsurf Memory")
        results['windsurf'] = 'manual_save_required'
        
        # 2. Save to Supermemory.ai
        if self.has_supermemory:
            print("\n☁️  Supermemory.ai:")
            try:
                # Build detailed content for Supermemory
                detailed_content = f"""
{self.project_name} - Session End

Summary: {summary}

Next Steps: {next_steps}

Status: {status}

Last Worked: {timestamp}
"""
                if github_url:
                    detailed_content += f"\nGitHub: {github_url}"
                if commit_hash:
                    detailed_content += f"\nCommit: {commit_hash}"
                
                # Build metadata
                metadata = {
                    "project": self.project_name,
                    "type": "session_end",
                    "date": datetime.now().strftime("%Y-%m-%d"),
                    "status": status
                }
                if github_url:
                    metadata["github_url"] = github_url
                if commit_hash:
                    metadata["commit"] = commit_hash
                
                # Save to Supermemory.ai
                response = self.supermemory_client.memories.add(
                    content=detailed_content,
                    metadata=metadata
                )
                
                print(f"   ✅ Saved to Supermemory.ai")
                print(f"   Memory ID: {response.id}")
                print(f"   Status: {response.status}")
                results['supermemory'] = {
                    'id': response.id,
                    'status': response.status
                }
                
            except Exception as e:
                print(f"   ❌ Error saving to Supermemory.ai: {e}")
                results['supermemory'] = f'error: {e}'
        
        return results
    
    def save_decision(self, decision, category, reasoning=None):
        """
        Save an important decision to both memory systems.
        
        Args:
            decision: The decision made
            category: Category (Architecture, Code Standard, etc.)
            reasoning: Optional reasoning for the decision
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %I:%M %p %Z")
        
        memory_content = f"{self.project_name} - {category}: {decision}"
        if reasoning:
            memory_content += f" Reason: {reasoning}"
        memory_content += f" Saved: {timestamp}."
        
        print(f"\n📝 Decision to save: {memory_content}")
        
        # Save to Supermemory.ai
        if self.has_supermemory:
            try:
                content = f"{self.project_name} - {category}\n\nDecision: {decision}"
                if reasoning:
                    content += f"\n\nReasoning: {reasoning}"
                content += f"\n\nSaved: {timestamp}"
                
                response = self.supermemory_client.memories.add(
                    content=content,
                    metadata={
                        "project": self.project_name,
                        "type": "decision",
                        "category": category.lower().replace(" ", "_"),
                        "date": datetime.now().strftime("%Y-%m-%d")
                    }
                )
                print(f"   ✅ Saved to Supermemory.ai (ID: {response.id})")
            except Exception as e:
                print(f"   ❌ Error: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize helper for your project
    helper = DualMemoryHelper("supermemory-integration")
    
    # Save session end
    helper.save_session_end(
        summary="Created complete Supermemory.ai integration with SDK wrapper, examples, and documentation",
        next_steps="User can start building AI applications with persistent memory",
        status="Production ready and live on GitHub",
        github_url="https://github.com/369Temetnosce/supermemory-integration",
        commit_hash="5e74744"
    )
