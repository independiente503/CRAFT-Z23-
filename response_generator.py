# =============================
# RESPONSE GENERATOR
# =============================

class ResponseGenerator:
    def __init__(self, llm, memory):
        self.llm = llm
        self.memory = memory

    def _build_history(self, user):
        """
        Build short conversation history from memory.
        """
        past_memories = self.memory.recall(user, limit=3)
        lines = []
        for m in past_memories:
            lines.append(f"{m['user']}: {m['message']}")
        return "\n".join(lines)

    def build_prompt(self, user, message, emotion_state):
        """
        Build prompt sent to the LLM.
        """
        history = self._build_history(user)

        prompt = f"""
You are CRAFT-Z23, an autonomous VTuber AI.
You have a consistent personality and memory.

Current emotional state: {emotion_state}

Recent conversation:
{history}

User message:
{message}

Respond naturally, concisely, and in character.
"""
        return prompt.strip()

    def respond(self, user, message, emotion_state):
        """
        Generate final response using the LLM.
        """
        prompt = self.build_prompt(user, message, emotion_state)
        return self.llm.generate(prompt)