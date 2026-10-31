import json
from pathlib import Path

CONVERSATION_DIR = Path("conversations")
HISTORY_FILE = CONVERSATION_DIR / "chat_history.json"

def save_conversation(messages):
    # Ensure the folder exists
    CONVERSATION_DIR.mkdir(exist_ok=True)
    
    # Print absolute path so you can find it easily
    print(f"[DEBUG] Saving file to: {HISTORY_FILE.resolve()}")

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(messages, file, indent=4, ensure_ascii=False)

    return True

def load_conversation():
    if not HISTORY_FILE.exists():
        print(f"[DEBUG] File not found at: {HISTORY_FILE.resolve()}")
        return None
        
    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)