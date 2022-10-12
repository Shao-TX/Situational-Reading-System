from playsound import playsound
import random
import os

def Play_Music(song_dir_path):
    music_len = len(os.listdir(song_dir_path))
    music_num = random.randint(1, music_len)
    music_path = str(music_num) + ".mid"
    music_path = os.path.join(song_dir_path, music_path)
    playsound(music_path)