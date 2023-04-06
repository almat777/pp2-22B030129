import pygame.mixer
import pygame.time
import keyboard

pygame.mixer.init()

playlist = ["music/mockinbird.mp3", ]
current_track = 0
pygame.mixer.music.load(playlist[current_track])

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
keyboard.add_hotkey('space', play)
keyboard.add_hotkey('esc', stop)
keyboard.add_hotkey('right', next_track)
keyboard.add_hotkey('left', prev_track)

while True:
    pygame.time.wait(100)
