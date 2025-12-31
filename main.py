# =============================
# CRAFT-Z23 MAIN ENTRYPOINT
# Based on Open-LLM-VTuber
# =============================

import time
from craft_z23_core import CRAFT_Z23_CORE
from llm_interface import LLMInterface
from response_generator import ResponseGenerator
from vtuber_adapter import VTuberAdapter
from watchdog import Watchdog

def main():
    print("🚀 Booting CRAFT-Z23...")

    # Initialize core systems
    core = CRAFT_Z23_CORE()
    llm = LLMInterface()
    responder = ResponseGenerator(llm, core.memory)
    adapter = VTuberAdapter(core, responder)

    # Start watchdog
    watchdog = Watchdog()
    watchdog.start()

    print("✅ CRAFT-Z23 ONLINE AND STABLE")

    # Simple CLI loop (replace with Twitch / YT chat later)
    while True:
        try:
            user = input("User: ")
            message = input("Message: ")

            response = adapter.on_chat_message(user, message)
            print("CRAFT-Z23:", response)

            time.sleep(0.3)

        except KeyboardInterrupt:
            print("\n🛑 Shutting down CRAFT-Z23 safely...")
            watchdog.stop()
            break

        except Exception as e:
            print(f"⚠️ Runtime error: {e}")

if __name__ == "__main__":
    main()