# Dual-Memory Workflow Guide

## Overview

This project demonstrates how to use **TWO memory systems** together for maximum persistence and accessibility:

1. **Windsurf Memory** (Local) - For Cascade AI context
2. **Supermemory.ai** (Cloud) - For cross-device access

---

## 🧠 Understanding the Two Systems

### Windsurf Memory (Local)
- **What**: Built into Windsurf IDE
- **Where**: `C:\Users\User\.codeium\windsurf\memories\`
- **Access**: Cascade AI assistant reads automatically
- **Scope**: This computer only
- **Speed**: Instant
- **Use For**: AI assistant context, quick recall

### Supermemory.ai (Cloud)
- **What**: Cloud-based memory API
- **Where**: https://supermemory.ai
- **Access**: API calls from anywhere
- **Scope**: All devices, all locations
- **Speed**: ~300ms
- **Use For**: Cross-device persistence, searchable knowledge base

---

## 📝 When to Save to Both

**Always save to BOTH systems:**
- ✅ Session end summaries
- ✅ Important architectural decisions
- ✅ Project milestones
- ✅ Code standards and conventions
- ✅ Lessons learned
- ✅ TODOs and next steps

**Why both?**
- Windsurf Memory → Cascade knows context immediately
- Supermemory.ai → You can access from any computer/device

---

## 🚀 How to Use the Dual-Memory Helper

### Quick Start

```python
from dual_memory_helper import DualMemoryHelper

# Initialize for your project
helper = DualMemoryHelper("your-project-name")

# Save session end
helper.save_session_end(
    summary="What you accomplished",
    next_steps="What to do next",
    status="Current status",
    github_url="https://github.com/user/repo",  # optional
    commit_hash="abc1234"  # optional
)

# Save important decisions
helper.save_decision(
    decision="Use React for frontend",
    category="Architecture",
    reasoning="Team expertise and ecosystem"
)
```

### Session End Workflow

When you say **"save my work"**, Cascade should:

1. **Create session summary**
2. **Save to Windsurf Memory** (via `create_memory` tool)
3. **Save to Supermemory.ai** (via API)
4. **Git operations** (add, commit, push)
5. **Confirm both saves**

---

## 🔧 Setup for Your Projects

### 1. Copy the Helper

```bash
# Copy to your project
cp dual_memory_helper.py /path/to/your/project/
```

### 2. Configure Supermemory.ai

```bash
# In your project's .env file
SUPERMEMORY_API_KEY=your_api_key_here
SUPERMEMORY_BASE_URL=https://api.supermemory.ai/
```

### 3. Use in Your Workflow

```python
# At the end of your work session
from dual_memory_helper import DualMemoryHelper

helper = DualMemoryHelper("my-project")
helper.save_session_end(
    summary="Completed user authentication module",
    next_steps="Build dashboard UI",
    status="Auth working, needs testing"
)
```

---

## 📋 Manual Dual-Save Process

If you don't use the helper script:

### A. Save to Windsurf Memory
Tell Cascade:
```
Remember this: [PROJECT] - Session End: [summary]. Next: [steps]. Status: [status]. Last worked: [date/time].
```

Cascade will use `create_memory` tool to save locally.

### B. Save to Supermemory.ai

```python
from supermemory import Supermemory
import os

client = Supermemory(api_key=os.getenv('SUPERMEMORY_API_KEY'))

client.memories.add(
    content="Your session summary here",
    metadata={
        "project": "project-name",
        "type": "session_end",
        "date": "2025-10-25"
    }
)
```

---

## 🔍 Searching Memories

### Search Windsurf Memory
Ask Cascade:
```
"What do you remember about [topic]?"
"What did I work on last in [project]?"
```

### Search Supermemory.ai

```python
from supermemory import Supermemory
import os

client = Supermemory(api_key=os.getenv('SUPERMEMORY_API_KEY'))

results = client.search.execute(q="your search query")
for result in results.results:
    print(result)
```

---

## ✅ Benefits of Dual-Memory

| Feature | Windsurf Memory | Supermemory.ai | Both Together |
|---------|----------------|----------------|---------------|
| **Speed** | Instant | ~300ms | ✅ Best of both |
| **AI Context** | ✅ Yes | Manual | ✅ Automatic + Manual |
| **Cross-Device** | ❌ No | ✅ Yes | ✅ Yes |
| **Searchable** | Via Cascade | Via API | ✅ Both ways |
| **Persistence** | Local only | Cloud | ✅ Redundant |
| **Cost** | Free | Free tier | ✅ Free |

---

## 🎯 Best Practices

1. **Always save session ends to both** - Ensures continuity
2. **Use metadata in Supermemory.ai** - Makes searching easier
3. **Include GitHub URLs** - Link code to memories
4. **Format consistently** - Use `[PROJECT] - [CATEGORY]: [INFO]`
5. **Search before deciding** - Check past decisions first

---

## 🛠️ Automation

### Global Rules Integration

Your global rules now specify dual-memory saves. When you say:
- **"save my work"** → Saves to both systems + Git push
- **"remember that [info]"** → Saves to both systems
- **"start working"** → Loads from both systems

### Cascade Behavior

Cascade will automatically:
1. Save session summaries to Windsurf Memory
2. Prompt you to save to Supermemory.ai (or use helper)
3. Confirm both saves completed
4. Include memory status in confirmations

---

## 📚 Examples

### Example 1: Session End

```python
helper = DualMemoryHelper("my-app")

helper.save_session_end(
    summary="Implemented user login with JWT tokens. Added password reset flow.",
    next_steps="Add email verification. Write tests for auth module.",
    status="Auth module 80% complete, needs testing",
    github_url="https://github.com/user/my-app",
    commit_hash="a1b2c3d"
)
```

**Result:**
- ✅ Saved to Windsurf Memory (Cascade knows context)
- ✅ Saved to Supermemory.ai (accessible from anywhere)

### Example 2: Important Decision

```python
helper.save_decision(
    decision="Use PostgreSQL instead of MongoDB",
    category="Architecture",
    reasoning="Need ACID compliance for financial transactions"
)
```

**Result:**
- ✅ Saved to both systems
- ✅ Searchable by "PostgreSQL" or "database decision"
- ✅ Cascade will reference this in future database discussions

---

## 🎉 Summary

**Dual-memory workflow gives you:**
- 🚀 Fast AI context (Windsurf Memory)
- ☁️ Cross-device access (Supermemory.ai)
- 🔍 Powerful search (both systems)
- 💾 Redundant backups
- 🤖 Automated workflow

**Use the helper script** to make dual-saves easy and consistent!

---

**Next**: Try the `dual_memory_helper.py` script in your projects!
