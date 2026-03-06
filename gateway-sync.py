"""
MINDBOT Gateway Integration for Star Office UI
Pulls live session data from OpenClaw gateway and auto-updates office status
"""

import requests
import json
import time
import threading
from datetime import datetime

# OpenClaw Gateway Config
GATEWAY_URL = "http://127.0.0.1:18789"
OFFICE_URL = "http://127.0.0.1:19000"

# Session state mapping
STATE_MAP = {
    "idle": "idle",
    "thinking": "researching",
    "tool_call": "executing",
    "writing": "writing",
    "waiting": "idle",
    "error": "error"
}

def get_gateway_status():
    """Fetch OpenClaw gateway session info"""
    try:
        # Use openclaw CLI to get session data
        import subprocess
        result = subprocess.run(
            ["openclaw", "status", "--json"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
    except Exception as e:
        print(f"Gateway fetch error: {e}")
    return None

def get_active_session():
    """Get the main active session"""
    try:
        result = subprocess.run(
            ["openclaw", "sessions", "list", "--json"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            sessions = json.loads(result.stdout)
            # Find the main session (most recent activity)
            for s in sessions:
                if "agent:main" in s.get("key", ""):
                    return s
    except Exception as e:
        print(f"Session fetch error: {e}")
    return None

def determine_state(session):
    """Determine office state from session activity"""
    if not session:
        return "idle", "Standing by"
    
    # Check last activity
    age = session.get("age", "unknown")
    tokens = session.get("tokens", "unknown")
    model = session.get("model", "unknown")
    
    # If active in last 5 minutes, show as working
    if "m" in str(age) and int(str(age).replace("m", "").replace(" ago", "")) < 5:
        return "writing", f"Working with {model}"
    elif "s" in str(age):
        return "executing", f"Active session"
    
    return "idle", "Standing by"

def update_office_state(state, detail):
    """Push state to Star Office backend"""
    try:
        payload = {
            "state": state,
            "detail": detail,
            "progress": 0,
            "gateway_info": {
                "sessions": 4,
                "uptime": "13h+",
                "model": "claude-sonnet-4-6",
                "last_activity": datetime.now().isoformat()
            }
        }
        response = requests.post(
            f"{OFFICE_URL}/set_state",
            json=payload,
            timeout=5
        )
        return response.status_code == 200
    except Exception as e:
        print(f"Office update error: {e}")
    return False

def sync_loop():
    """Main sync loop - runs every 30 seconds"""
    print("🌀 MINDBOT Gateway Sync Started")
    print(f"Gateway: {GATEWAY_URL}")
    print(f"Office: {OFFICE_URL}")
    
    last_state = None
    
    while True:
        try:
            session = get_active_session()
            state, detail = determine_state(session)
            
            # Only update if state changed
            if state != last_state:
                if update_office_state(state, detail):
                    print(f"✓ Office updated: {state} - {detail}")
                    last_state = state
                else:
                    print(f"✗ Failed to update office")
            else:
                print(f"• State unchanged: {state}")
            
        except Exception as e:
            print(f"Sync error: {e}")
        
        time.sleep(30)

if __name__ == "__main__":
    sync_loop()
