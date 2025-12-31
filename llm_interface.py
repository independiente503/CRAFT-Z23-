# =============================
# LLM INTERFACE
# =============================
# Compatible with:
# - OpenAI
# - Ollama
# - LM Studio
# - Local models
# =============================

class LLMInterface:
    def __init__(self, client=None):
        """
        client: external LLM client (OpenAI, Ollama, etc.)
        """
        self.client = client

    def generate(self, prompt):
        """
        Generate text from LLM.
        Replace this method with real API calls.
        """
        if self.client:
            # Example:
            # return self.client.generate(prompt)
            pass

        # Fallback (safe default)
        return f"[LLM OUTPUT]: {prompt[:200]}"