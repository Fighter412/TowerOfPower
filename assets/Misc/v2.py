import tkinter as tk
from tkVideoPlayer import TkinterVideo
from PIL import ImageTk, Image
import os
import pygame
import time

# CONSTANTS
audioPath = r"School\Assignments\Game\audio.mp3"
videoPath = r"School\Assignments\Game\Video.mp4"
bgImgPath = r"School\Assignments\Game\blacksmith.png"
start = time.time()

keys = []

def keyup(e):
    if  e.char in keys :
        keys.pop(keys.index(e.char))

def keydown(e):
    if not e.char in keys :
        keys.append(e.char)
    if time.time()-start < pygame.mixer.Sound(audioPath).get_length():
        pygame.mixer.music.stop()
        for widget in root.winfo_children():
            widget.destroy()
        init()
    else:
        init()

def init():
    img = ImageTk.PhotoImage(Image.open(bgImgPath))
    panel = tk.Label(root, image = img)
    panel.place(x=0, y=0)

root = tk.Tk()
#root.geometry("1920x1009+0+0")
root.attributes('-fullscreen', True)
root.bind("<KeyPress>", keydown)
root.bind("<KeyRelease>", keyup)

videoplayer = TkinterVideo(master=root, scaled=True)
videoplayer.load(videoPath)
videoplayer.pack(expand=True, fill="both")

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(audioPath)
videoplayer.play() # play the video
pygame.mixer.music.play()

root.mainloop()