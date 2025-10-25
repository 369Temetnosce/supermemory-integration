"""
Supermemory.ai API Client
A Python wrapper using the official Supermemory SDK.
"""

import os
from typing import Dict, List, Optional, Any
from dotenv import load_dotenv
from supermemory import Supermemory


class SupermemoryClient:
    """Client for interacting with Supermemory.ai API using the official SDK"""
    
    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        """
        Initialize the Supermemory client.
        
        Args:
            api_key: Your Supermemory API key. If not provided, will look for
                    SUPERMEMORY_API_KEY environment variable.
            base_url: Base URL for the API. If not provided, will look for
                     SUPERMEMORY_BASE_URL environment variable or use default.
        """
        load_dotenv()
        self.api_key = api_key or os.getenv("SUPERMEMORY_API_KEY")
        self.base_url = base_url or os.getenv("SUPERMEMORY_BASE_URL", "https://api.supermemory.ai/")
        
        if not self.api_key:
            raise ValueError(
                "API key is required. Either pass it directly or set "
                "SUPERMEMORY_API_KEY environment variable."
            )
        
        self.client = Supermemory(
            api_key=self.api_key,
            base_url=self.base_url
        )
    
    def add_memory(
        self, 
        content: str,
        metadata: Optional[Dict[str, Any]] = None,
        user_id: Optional[str] = None,
        container_tags: Optional[List[str]] = None,
        custom_id: Optional[str] = None,
        **kwargs
    ) -> Any:
        """
        Add a new memory to Supermemory.
        
        Args:
            content: The content to store as a memory (text or URL)
            metadata: Optional metadata dict to attach to the memory
            user_id: Optional user ID for partitioning memories
            container_tags: Optional list of tags for grouping memories
            custom_id: Optional custom ID for the memory
            **kwargs: Additional arguments to pass to the API
            
        Returns:
            Response from the API containing the created memory details
        """
        params = {"content": content}
        
        if metadata:
            params["metadata"] = metadata
        if user_id:
            params["userId"] = user_id
        if container_tags:
            params["containerTags"] = container_tags
        if custom_id:
            params["customId"] = custom_id
        
        params.update(kwargs)
        
        return self.client.memories.add(**params)
    
    def search_memories(
        self,
        query: str,
        limit: Optional[int] = None,
        **kwargs
    ) -> Any:
        """
        Search through your memories.
        
        Args:
            query: The search query
            limit: Maximum number of results to return
            **kwargs: Additional arguments to pass to the API
            
        Returns:
            Search results from the API
        """
        params = {"q": query}
        
        if limit:
            params["limit"] = limit
        
        params.update(kwargs)
        
        return self.client.search.execute(**params)
    
    def get_raw_client(self) -> Supermemory:
        """
        Get the underlying Supermemory client for advanced usage.
        
        Returns:
            The Supermemory client instance
        """
        return self.client
