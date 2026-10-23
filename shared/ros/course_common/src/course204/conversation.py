"""Use the actual PyAIML-compatible interpreter, not a simulated model."""
import threading
from .commands import normalize, intent


class Conversation:
    def __init__(self, path):
        import aiml
        self.kernel = aiml.Kernel()
        self.kernel.learn(str(path))
        self.lock = threading.Lock()

    def respond(self, text):
        if not isinstance(text, str) or len(text) > 500:
            raise ValueError("Text must contain at most 500 characters")
        cleaned = normalize(text)
        with self.lock:
            reply = self.kernel.respond(cleaned) if cleaned else "اكتب أو قل عبارة أولًا."
        return reply or "لم أفهم الطلب.", intent(cleaned) or ""
