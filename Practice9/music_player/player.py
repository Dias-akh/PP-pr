import pygame
import os

class MusicPlayer:
    def __init__(self, music_dir):
        pygame.mixer.init()
        self.music_dir = music_dir
        self.playlist = [f for f in os.listdir(music_dir) if f.endswith(('.mp3', '.wav'))]
        self.current_index = 0
        self.is_playing = False

    def load_track(self):
        if self.playlist:
            pygame.mixer.music.load(os.path.join(self.music_dir, self.playlist[self.current_index]))


    def play(self):
        if not self.playlist:
            return
        if not self.is_playing:
            self.load_track()
            pygame.mixer.music.play()
            self.is_playing = True
        else:
            pygame.mixer.music.unpause()

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.load_track()
        pygame.mixer.music.play()   # ← напрямую, минуя play()
        self.is_playing = True

    def prev_track(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.load_track()
        pygame.mixer.music.play()   
        self.is_playing = True

    def get_current_track_name(self):
        if self.playlist:
            return os.path.splitext(self.playlist[self.current_index])[0]
        return "No tracks found"

    def get_pos_str(self):
        pos = pygame.mixer.music.get_pos()
        if pos == -1: pos = 0
        seconds = pos // 1000
        return f"{seconds // 60:02d}:{seconds % 60:02d}"