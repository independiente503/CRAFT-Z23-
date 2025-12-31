# =============================
# DECISION ENGINE
# =============================

class DecisionEngine:
    def decide(self, emotion_state):
        """
        Decide behavior based on emotional state.
        """
        if emotion_state == "Engaged":
            return "respond"
        elif emotion_state == "Defensive":
            return "limit"
        elif emotion_state == "Creative":
            return "improvise"
        elif emotion_state == "Fatigued":
            return "slow"
        else:
            return "neutral"