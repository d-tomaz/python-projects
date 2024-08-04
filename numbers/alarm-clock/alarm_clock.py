import time
from playsound import playsound

def play_sound_after_delay(sound_file, delay):
    time.sleep(delay)
    playsound(sound_file)

def play_sound_at_time(sound_file, target_time):
    current_time = time.strftime("%H:%M:%S")
    while current_time != target_time:
        time.sleep(1)
        current_time = time.strftime("%H:%M:%S")
    playsound(sound_file)

sound_file = "sound.mp3"
choice = input("Do you want to play the sound after a delay (D) or at a specific time (T)? ").strip().upper()

if choice == "D":
    delay = int(input("Enter the delay in seconds: "))
    play_sound_after_delay(sound_file, delay)
elif choice == "T":
    target_time = input("Enter the target time in HH:MM:SS format: ")
    play_sound_at_time(sound_file, target_time)
else:
    print("Invalid choice. Please, enter 'D' for delay or 'T' for target time.")
