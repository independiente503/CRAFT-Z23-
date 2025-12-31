# =============================
# RATE LIMITER
# =============================

import time
from collections import defaultdict, deque

class RateLimiter:
    def __init__(self, max_messages=5, window_seconds=10):
        """
        max_messages: number of allowed messages
        window_seconds: time window in seconds
        """
        self.max_messages = max_messages
        self.window = window_seconds
        self.user_messages = defaultdict(deque)

    def allow(self, user_id):
        """
        Check if a user is allowed to send a message.
        """
        now = time.time()
        queue = self.user_messages[user_id]

        # Remove old messages
        while queue and now - queue[0] > self.window:
            queue.popleft()

        if len(queue) < self.max_messages:
            queue.append(now)
            return True

        return False