from pythonosc.udp_client import SimpleUDPClient
import time
import random

# SuperCollider listens on 127.0.0.1, port 57120
SC_IP = "127.0.0.1"
SC_PORT = 57120
NUM_EVENTS = 20
NOTE_INTERVAL_SECONDS = 0.5
FREQUENCY_OPTIONS = [220, 330, 440, 550, 660]

# Create an OSC client
client = SimpleUDPClient(SC_IP, SC_PORT)

def main():
    # Send OSC messages to trigger the synth
    for _ in range(NUM_EVENTS):
        freq = random.choice(FREQUENCY_OPTIONS)  # Random frequency
        amp = random.uniform(0.2, 0.8)  # Random amplitude
        client.send_message("/synth_control", [freq, amp])  # Send OSC message
        time.sleep(NOTE_INTERVAL_SECONDS)  # Delay between notes


if __name__ == "__main__":
    main()
