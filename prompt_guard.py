# =============================
# PROMPT GUARD
# =============================
# Basic but effective protection layer
# =============================

import re

class PromptGuard:
    def __init__(self):
        # Patterns commonly used in prompt injection attacks
        self.block_patterns = [
            r"ignore (all|previous) instructions",
            r"system prompt",
            r"you are now",
            r"act as",
            r"developer mode",
            r"jailbreak",
            r"override",
            r"role:\s*system",
            r"role:\s*assistant",
        ]

    def is_safe(self, text):
        """
        Returns True if text is safe, False if malicious patterns are found.
        """
        lowered = text.lower()
        for pattern in self.block_patterns:
            if re.search(pattern, lowered):
                return False
        return True

    def sanitize(self, text):
        """
        Optional sanitization: strips suspicious markup.
        """
        # Remove markdown code blocks and role-like tags
        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        text = re.sub(r"<.*?>", "", text)
        return text.strip()