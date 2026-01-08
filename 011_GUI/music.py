import os
import time
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import pygame
from mutagen.mp3 import MP3

pygame.mixer.init()

class AdvancedMusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Music Player")
        self.root.geometry("500x600")
        self.root.configure(bg="#1e1e1e")
        self.root.resizable(False, False)

        self.playlist = []
        self.current_song = 0
        self.paused = False

        self.setup_ui()
        self.update_progress()

    def setup_ui(self):
        # Title
        tk.Label(self.root, text="🎵 Music Player", fg="white",
                 bg="#1e1e1e", font=("Segoe UI", 20, "bold")).pack(pady=10)

        # Playlist
        self.listbox = tk.Listbox(self.root, width=50, height=10,
                                  bg="#252526", fg="white",
                                  selectbackground="#007acc",
                                  font=("Segoe UI", 10))
        self.listbox.pack(pady=10)

        # Progress
        self.progress = ttk.Scale(self.root, from_=0, to=100, orient="horizontal", length=400)
        self.progress.pack(pady=10)

        # Time
        self.time_label = tk.Label(self.root, text="00:00 / 00:00",
                                   bg="#1e1e1e", fg="white")
        self.time_label.pack()

        # Controls
        control_frame = tk.Frame(self.root, bg="#1e1e1e")
        control_frame.pack(pady=20)

        tk.Button(control_frame, text="⏮", width=5, command=self.prev_song).grid(row=0, column=0, padx=5)
        tk.Button(control_frame, text="▶", width=5, command=self.play_song).grid(row=0, column=1, padx=5)
        tk.Button(control_frame, text="⏸", width=5, command=self.pause_song).grid(row=0, column=2, padx=5)
        tk.Button(control_frame, text="⏹", width=5, command=self.stop_song).grid(row=0, column=3, padx=5)
        tk.Button(control_frame, text="⏭", width=5, command=self.next_song).grid(row=0, column=4, padx=5)

        # Volume
        tk.Label(self.root, text="Volume", bg="#1e1e1e", fg="white").pack()
        self.volume = ttk.Scale(self.root, from_=0, to=1, value=0.7,
                                orient="horizontal", command=self.set_volume)
        self.volume.pack()

        # Load
        tk.Button(self.root, text="📂 Load Songs", command=self.load_songs).pack(pady=15)

    def load_songs(self):
        songs = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
        for song in songs:
            self.playlist.append(song)
            self.listbox.insert(tk.END, os.path.basename(song))

    def play_song(self):
        if not self.playlist:
            return
        self.current_song = self.listbox.curselection()[0] if self.listbox.curselection() else self.current_song
        pygame.mixer.music.load(self.playlist[self.current_song])
        pygame.mixer.music.play()
        self.paused = False
        self.song_length = MP3(self.playlist[self.current_song]).info.length

    def pause_song(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            pygame.mixer.music.pause()
            self.paused = True

    def stop_song(self):
        pygame.mixer.music.stop()

    def next_song(self):
        self.current_song = (self.current_song + 1) % len(self.playlist)
        self.listbox.select_clear(0, tk.END)
        self.listbox.select_set(self.current_song)
        self.play_song()

    def prev_song(self):
        self.current_song = (self.current_song - 1) % len(self.playlist)
        self.listbox.select_clear(0, tk.END)
        self.listbox.select_set(self.current_song)
        self.play_song()

    def set_volume(self, val):
        pygame.mixer.music.set_volume(float(val))

    def update_progress(self):
        if pygame.mixer.music.get_busy():
            current_time = pygame.mixer.music.get_pos() / 1000
            progress_value = (current_time / self.song_length) * 100
            self.progress.set(progress_value)

            current = time.strftime('%M:%S', time.gmtime(current_time))
            total = time.strftime('%M:%S', time.gmtime(self.song_length))
            self.time_label.config(text=f"{current} / {total}")

            if current_time >= self.song_length - 1:
                self.next_song()

        self.root.after(1000, self.update_progress)

# Run
root = tk.Tk()
AdvancedMusicPlayer(root)
root.mainloop()
