# =============================
# PERSONALITY MODULE
# =============================

class Personality:
    def __init__(self):
        # Personality traits range from 0.0 to 1.0
        self.traits = {
            "openness": 0.65,
            "emotional_reactivity": 0.4,
            "curiosity": 0.8,
            "social_attachment": 0.6,
            "risk_tolerance": 0.3
        }

    def evolve(self, weight):
        """
        Slowly evolve personality based on interaction weight.
        """
        self.traits["openness"] = min(
            1.0, self.traits["openness"] + weight * 0.01
        )
        self.traits["social_attachment"] = min(
            1.0, self.traits["social_attachment"] + weight * 0.02
        )

    def snapshot(self):
        """
        Returns current personality state.
        """
        return self.traits.copy()