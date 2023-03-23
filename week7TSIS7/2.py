import pygame.mixer
import pygame.time
import keyboard

# Initialize mixer
pygame.mixer.init()

# Load music files
playlist = ["mockinbird.mp3",]
current_track = 0
pygame.mixer.music.load(playlist[current_track])

# Define keyboard control functions
def play():
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

def prev_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

# Map keyboard keys to control functions
keyboard.add_hotkey('space', play)
keyboard.add_hotkey('esc', stop)
keyboard.add_hotkey('right', next_track)
keyboard.add_hotkey('left', prev_track)

# Start event loop
while True:
    pygame.time.wait(100)
