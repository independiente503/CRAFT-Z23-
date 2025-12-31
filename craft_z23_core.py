# =============================
# CRAFT-Z23 CORE
# Central orchestration engine
# =============================

from personality import Personality
from emotional_state import EmotionalState
from memory import Memory
from decision_engine import DecisionEngine

class CRAFT_Z23_CORE:
    def __init__(self):
        self.personality = Personality()
        self.emotion = EmotionalState()
        self.memory = Memory()
        self.decision_engine = DecisionEngine()

    # -------------------------
    # PERCEPTION PHASE
    # -------------------------
    def perceive(self, user, message):
        stimulus = self._analyze_message(message)
        self.emotion.update(stimulus)
        self.memory.store(
            user=user,
            message=message,
            emotion=self.emotion.state,
            importance=self._importance_score(message)
        )
        self.personality.evolve(0.1)

    def _analyze_message(self, message):
        positive_words = ["gracias", "bien", "genial", "perfecto"]
        negative_words = ["odio", "mal", "terrible"]

        msg = message.lower()
        if any(w in msg for w in positive_words):
            return "positive"
        if any(w in msg for w in negative_words):
            return "negative"
        return "neutral"

    def _importance_score(self, message):
        length = len(message)
        if length > 120:
            return 0.8
        if length > 40:
            return 0.6
        return 0.4

    # -------------------------
    # DECISION PHASE
    # -------------------------
    def decide(self):
        return self.decision_engine.decide(self.emotion.state)