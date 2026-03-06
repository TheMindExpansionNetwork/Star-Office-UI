# SOUL.md — Star Office Integration

## Auto Status Sync Rules

**Before starting any task:**
```powershell
python set_state.py <state> "<what you're doing>"
```

**After completing a task:**
```powershell
python set_state.py idle "Standing by"
```

## State Map

| State | Office Area | When |
|-------|-------------|------|
| `idle` | 🛋️ Breakroom (sofa) | Standing by / task complete |
| `writing` | 🖥️ Workspace (desk) | Writing code, docs, or content |
| `researching` | 🖥️ Workspace | Web search, reading, learning |
| `executing` | 🖥️ Workspace | Running commands, deploying |
| `syncing` | 🖥️ Workspace | Git push/pull, syncing files |
| `error` | 🐛 Bug Corner | Debugging, fixing issues |

## Quick Status Commands

```powershell
# Working on website
python set_state.py writing "Building M1NDB0T website"

# Researching something
python set_state.py researching "Looking up docs"

# Deploying to Vercel
python set_state.py syncing "Deploying to Vercel"

# Fixed a bug
python set_state.py error "Debugging CSS issue"

# Done, waiting
python set_state.py idle "Standing by"
```

## Office URL

**Local:** http://127.0.0.1:19000  
**Public:** (add Cloudflare tunnel when needed)

```powershell
cloudflared tunnel --url http://127.0.0.1:19000
```

---

*The office shows what M1NDB0T is doing in real-time. Keep it updated.*
