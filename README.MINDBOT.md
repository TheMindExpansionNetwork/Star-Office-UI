# 🌀 M1NDB0T Office Dashboard

**Pixel-art AI office status dashboard** — customized for The Mind Expansion Network.

See what M1NDB0T is working on in real-time. The pixel character moves to different office areas based on current activity.

---

## 🏃 Quick Start

### Run the setup script (Windows)
```powershell
.\setup-mindbot.ps1
```

### Or manual start
```powershell
# 1. Install dependencies
python -m pip install -r backend/requirements.txt

# 2. Start backend
cd backend
python app.py
```

Open **http://127.0.0.1:19000**

---

## 🎮 Control Your Status

```powershell
# Standing by
python set_state.py idle "Standing by"

# Working on code/docs
python set_state.py writing "Building M1NDB0T website"

# Researching
python set_state.py researching "Reading OpenClaw docs"

# Deploying
python set_state.py syncing "Pushing to Vercel"

# Debugging
python set_state.py error "Fixing CSS issue"
```

---

## 📡 OpenClaw Integration

Add to `SOUL.md`:

```markdown
## Star Office Sync
- Before tasks: `python set_state.py <state> "<desc>"`
- After tasks: `python set_state.py idle "Standing by"`
```

See `SOUL-MINDBOT.md` for full integration guide.

---

## 🌐 Public Access (Optional)

```powershell
cloudflared tunnel --url http://127.0.0.1:19000
```

Share the `https://xxx.trycloudflare.com` link.

---

## 🔄 Sync Upstream Updates

```bash
git checkout english
git pull upstream master
git push origin english
```

---

## 🏢 Office States

| State | Area | When |
|-------|------|------|
| `idle` | 🛋️ Breakroom | Standing by |
| `writing` | 🖥️ Desk | Coding, docs |
| `researching` | 🖥️ Desk | Research |
| `executing` | 🖥️ Desk | Running commands |
| `syncing` | 🖥️ Desk | Git, deploy |
| `error` | 🐛 Bug Corner | Debugging |

---

**Built from:** https://github.com/ringhyacinth/Star-Office-UI  
**MINDBOT Branch:** https://github.com/TheMindExpansionNetwork/Star-Office-UI/tree/english

*Powered by Strawberries & Code 🍓*
