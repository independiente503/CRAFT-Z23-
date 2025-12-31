# =============================
# WATCHDOG MODULE
# =============================
# Monitors system heartbeat
# =============================

import threading
import time

class Watchdog:
    def __init__(self, interval=5):
        """
        interval: seconds between health checks
        """
        self.interval = interval
        self._running = False
        self._thread = None
        self._last_heartbeat = time.time()

    def start(self):
        """
        Start watchdog monitoring.
        """
        self._running = True
        self._thread = threading.Thread(target=self._monitor, daemon=True)
        self._thread.start()
        print("🐶 Watchdog started")

    def stop(self):
        """
        Stop watchdog safely.
        """
        self._running = False
        print("🐶 Watchdog stopped")

    def heartbeat(self):
        """
        Update heartbeat timestamp.
        Call this periodically from the main loop.
        """
        self._last_heartbeat = time.time()

    def _monitor(self):
        """
        Internal monitoring loop.
        """
        while self._running:
            now = time.time()
            if now - self._last_heartbeat > self.interval * 3:
                self._on_failure()
            time.sleep(self.interval)

    def _on_failure(self):
        """
        Handle detected failure.
        """
        print("🚨 WATCHDOG ALERT: System heartbeat lost!")
        # Here you could:
        # - Restart components
        # - Write audit logs
        # - Trigger safe shutdown