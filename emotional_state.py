# =============================
# EMOTIONAL STATE MACHINE
# =============================

class EmotionalState:
    def __init__(self):
        self.state = "Calm"

    def update(self, stimulus):
        """
        Update emotional state based on stimulus.
        """
        transitions = {
            "positive": "Engaged",
            "negative": "Defensive",
            "creative": "Creative",
            "fatigue": "Fatigued",
            "neutral": "Calm"
        }

        self.state = transitions.get(stimulus, self.state)

    def snapshot(self):
        """
        Return current emotional state.
        """
        return self.state