# =============================
# VTUBER ADAPTER
# =============================

class VTuberAdapter:
    def __init__(self, core, responder):
        self.core = core
        self.responder = responder

    def on_chat_message(self, user, message):
        """
        Entry point for any chat message.
        """
        # Perception phase
        self.core.perceive(user, message)

        # Decision phase (currently informational)
        decision = self.core.decide()

        # Response generation
        response = self.responder.respond(
            user=user,
            message=message,
            emotion_state=self.core.emotion.state
        )

        return response