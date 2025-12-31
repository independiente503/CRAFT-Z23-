# =============================
# MEMORY SYSTEM (PERSISTENT)
# =============================

import json
from datetime import datetime
from pathlib import Path

class Memory:
    def __init__(self, file="craft_z23_memory.json"):
        self.file = Path(file)
        self.data = self._load()

    def _load(self):
        if self.file.exists():
            try:
                with open(self.file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def store(self, user, message, emotion, importance=0.5):
        """
        Store a memory entry persistently.
        """
        record = {
            "user": user,
            "message": message,
            "emotion": emotion,
            "importance": importance,
            "timestamp": datetime.utcnow().isoformat()
        }
        self.data.append(record)
        self._save()

    def recall(self, user, limit=10):
        """
        Recall recent memories for a given user.
        """
        memories = [m for m in self.data if m["user"] == user]
        return memories[-limit:]

    def _save(self):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)